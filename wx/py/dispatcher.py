"""Provides global signal dispatching services."""

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"

import types
import weakref


class DispatcherError(Exception):
    def __init__(self, args=None):
        self.args = args


class Parameter:
    """Used to represent default parameter values."""
    def __repr__(self):
        return self.__class__.__name__

class Any(Parameter): pass
Any = Any()

class Anonymous(Parameter): pass
Anonymous = Anonymous()


connections = {}
senders = {}
_boundMethods = weakref.WeakKeyDictionary()


def connect(receiver, signal=Any, sender=Any, weak=True):
    """
    Connect receiver to sender for signal.

    * If sender is Any, receiver will receive signal from any sender.
    * If signal is Any, receiver will receive any signal from sender.
    * If sender is None, receiver will receive signal from Anonymous.
    * If signal is Any and sender is None, receiver will receive any
      signal from Anonymous.
    * If signal is Any and sender is Any, receiver will receive any
      signal from any sender.
    * If weak is true, weak references will be used.
    """
    if signal is None:
        raise DispatcherError('signal cannot be None')
    if weak:
        receiver = safeRef(receiver)
    senderkey = id(sender)
    signals = {}
    if senderkey in connections:
        signals = connections[senderkey]
    else:
        connections[senderkey] = signals
        # Keep track of senders for cleanup.
        if sender not in (None, Any):
            def remove(object, senderkey=senderkey):
                _removeSender(senderkey=senderkey)
            # Skip objects that can not be weakly referenced, which means
            # they won't be automatically cleaned up, but that's too bad.
            try:
                weakSender = weakref.ref(sender, remove)
                senders[senderkey] = weakSender
            except:
                pass
    receivers = []
    if signal in signals:
        receivers = signals[signal]
    else:
        signals[signal] = receivers
    try:
        receivers.remove(receiver)
    except ValueError:
        pass
    receivers.append(receiver)

def disconnect(receiver, signal=Any, sender=Any, weak=True):
    """Disconnect receiver from sender for signal.

    Disconnecting is not required. The use of disconnect is the same as for
    connect, only in reverse. Think of it as undoing a previous connection."""
    if signal is None:
        raise DispatcherError('signal cannot be None')
    if weak:
        receiver = safeRef(receiver)
    senderkey = id(sender)
    try:
        receivers = connections[senderkey][signal]
    except KeyError:
        raise DispatcherError(f'No receivers for signal {signal!r} from sender {sender}')
    try:
        receivers.remove(receiver)
    except ValueError:
        raise DispatcherError(f'No connection to receiver {receiver} for signal {signal!r} from sender {sender}')
    _cleanupConnections(senderkey, signal)

def send(signal, sender=Anonymous, **kwds):
    """Send signal from sender to all connected receivers.

    Return a list of tuple pairs [(receiver, response), ... ].
    If sender is not specified, signal is sent anonymously."""
    senderkey = id(sender)
    anykey = id(Any)
    # Get receivers that receive *this* signal from *this* sender.
    receivers = []
    try:
        receivers.extend(connections[senderkey][signal])
    except KeyError:
        pass
    # Add receivers that receive *any* signal from *this* sender.
    anyreceivers = []
    try:
        anyreceivers = connections[senderkey][Any]
    except KeyError:
        pass
    for receiver in anyreceivers:
        if receivers.count(receiver) == 0:
            receivers.append(receiver)
    # Add receivers that receive *this* signal from *any* sender.
    anyreceivers = []
    try:
        anyreceivers = connections[anykey][signal]
    except KeyError:
        pass
    for receiver in anyreceivers:
        if receivers.count(receiver) == 0:
            receivers.append(receiver)
    # Add receivers that receive *any* signal from *any* sender.
    anyreceivers = []
    try:
        anyreceivers = connections[anykey][Any]
    except KeyError:
        pass
    for receiver in anyreceivers:
        if receivers.count(receiver) == 0:
            receivers.append(receiver)
    # Call each receiver with whatever arguments it can accept.
    # Return a list of tuple pairs [(receiver, response), ... ].
    responses = []
    for receiver in receivers:
        if type(receiver) is weakref.ReferenceType \
        or isinstance(receiver, BoundMethodWeakref):
            # Dereference the weak reference.
            receiver = receiver()
            if receiver is None:
                # This receiver is dead, so skip it.
                continue
        response = _call(receiver, signal=signal, sender=sender, **kwds)
        responses += [(receiver, response)]
    return responses

def _call(receiver, **kwds):
    """Call receiver with only arguments it can accept."""
##    if type(receiver) is types.InstanceType:
    if hasattr(receiver, '__call__') and \
       (hasattr(receiver.__call__, '__func__') or hasattr(receiver.__call__, '__code__')):
        # receiver is a class instance; assume it is callable.
        # Reassign receiver to the actual method that will be called.
        receiver = receiver.__call__
    if hasattr(receiver, '__func__'):
        # receiver is a method. Drop the first argument, usually 'self'.
        fc = receiver.__func__.__code__
        acceptable = fc.co_varnames[1:fc.co_argcount]
    elif hasattr(receiver, '__code__'):
        # receiver is a function.
        fc = receiver.__code__
        acceptable = fc.co_varnames[0:fc.co_argcount]
    else:
        raise DispatcherError(f'Unknown receiver {receiver} of type {type(receiver)}')
    if not (fc.co_flags & 8):
        # fc does not have a **kwds type parameter, therefore
        # remove unacceptable arguments.

        for arg in list(kwds):
            if arg not in acceptable:
                del kwds[arg]
    return receiver(**kwds)


def safeRef(object):
    """Return a *safe* weak reference to a callable object."""
    if hasattr(object, '__self__'):
        if object.__self__ is not None:
            # Turn a bound method into a BoundMethodWeakref instance.
            # Keep track of these instances for lookup by disconnect().
            selfkey = object.__self__
            funckey = object.__func__
            if selfkey not in _boundMethods:
                _boundMethods[selfkey] = weakref.WeakKeyDictionary()
            if funckey not in _boundMethods[selfkey]:
                _boundMethods[selfkey][funckey] = \
                BoundMethodWeakref(boundMethod=object)
            return _boundMethods[selfkey][funckey]
    return weakref.ref(object, _removeReceiver)


class BoundMethodWeakref:
    """BoundMethodWeakref class."""

    def __init__(self, boundMethod):
        """Return a weak-reference-like instance for a bound method."""
        self.isDead = 0
        def remove(object, self=self):
            """Set self.isDead to true when method or instance is destroyed."""
            self.isDead = 1
            _removeReceiver(receiver=self)
        self.weakSelf = weakref.ref(boundMethod.__self__, remove)
        self.weakFunc = weakref.ref(boundMethod.__func__, remove)

    def __repr__(self):
        """Return the closest representation."""
        return f'<bound method weakref for {self.weakSelf}.{self.weakFunc}>'

    def __call__(self):
        """Return a strong reference to the bound method."""
        if self.isDead:
            return None
        else:
            object = self.weakSelf()
            method = self.weakFunc().__name__
            try:  # wxPython hack to handle wxDead objects.
                return getattr(object, method)
            except AttributeError:
##                 _removeReceiver(receiver=self)
                return None


def _removeReceiver(receiver):
    """Remove receiver from connections."""
    list_keys = [(senderkey, signal)
                 for senderkey in connections
                 for signal in connections[senderkey]]

    for senderkey, signal in list_keys:
        try:
            connections[senderkey][signal].remove(receiver)
        except:
            pass
        _cleanupConnections(senderkey, signal)

def _cleanupConnections(senderkey, signal):
    """Delete any empty signals for senderkey. Delete senderkey if empty."""
    receivers = connections[senderkey][signal]
    if not receivers:
        # No more connected receivers. Therefore, remove the signal.
        signals = connections[senderkey]
        del signals[signal]
        if not signals:
            # No more signal connections. Therefore, remove the sender.
            _removeSender(senderkey)

def _removeSender(senderkey):
    """Remove senderkey from connections."""
    del connections[senderkey]
    # Senderkey will only be in senders dictionary if sender
    # could be weakly referenced.
    try:
        del senders[senderkey]
    except:
        pass
