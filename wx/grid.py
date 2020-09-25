from wx import PyEventBinder

# Based on wxPython
# Copyright: (c) 2018 by Total Control Software
# License:   wxWindows License


def dummy_function(*args, **kwargs):
	return 0


GRIDTABLE_NOTIFY_COLS_APPENDED = 2006
GRIDTABLE_NOTIFY_COLS_DELETED = 2007
GRIDTABLE_NOTIFY_COLS_INSERTED = 2005
GRIDTABLE_NOTIFY_ROWS_APPENDED = 2003
GRIDTABLE_NOTIFY_ROWS_DELETED = 2004
GRIDTABLE_NOTIFY_ROWS_INSERTED = 2002
GRIDTABLE_REQUEST_VIEW_GET_VALUES = 2000
GRIDTABLE_REQUEST_VIEW_SEND_VALUES = 2001
GRID_AUTOSIZE = -1
GRID_DRAW_BOX_RECT = 8
GRID_DRAW_CELL_LINES = 4
GRID_DRAW_COLS_HEADER = 2
GRID_DRAW_DEFAULT = 15
GRID_DRAW_ROWS_HEADER = 1
GRID_DRAW_SELECTION = 16
GRID_FLOAT_FORMAT_COMPACT = 64
GRID_FLOAT_FORMAT_DEFAULT = 16
GRID_FLOAT_FORMAT_FIXED = 16
GRID_FLOAT_FORMAT_SCIENTIFIC = 32
GRID_FLOAT_FORMAT_UPPER = 128
GRID_VALUE_BOOL = 'bool'
GRID_VALUE_CHOICE = 'choice'
GRID_VALUE_CHOICEINT = 'choiceint'
GRID_VALUE_DATE = 'date'
GRID_VALUE_DATETIME = 'datetime'
GRID_VALUE_FLOAT = 'double'
GRID_VALUE_LONG = 'long'
GRID_VALUE_NUMBER = 'long'
GRID_VALUE_STRING = 'string'
GRID_VALUE_TEXT = 'string'
class Grid: ...
class GridBlockCoords: ...
class GridBlockDiffResult: ...
class GridBlocks: ...
class GridCellAttr: ...
class GridCellAttrProvider: ...
class GridCellAttrPtr: ...
class GridCellAutoWrapStringEditor: ...
class GridCellAutoWrapStringRenderer: ...
class GridCellBoolEditor: ...
class GridCellBoolRenderer: ...
class GridCellChoiceEditor: ...
class GridCellCoords: ...
class GridCellCoordsArray: ...
class GridCellDateEditor: ...
class GridCellDateRenderer: ...
class GridCellDateTimeRenderer: ...
class GridCellEditor: ...
class GridCellEditorPtr: ...
class GridCellEnumEditor: ...
class GridCellEnumRenderer: ...
class GridCellFloatEditor: ...
class GridCellFloatFormat: ...
class GridCellFloatRenderer: ...
class GridCellNumberEditor: ...
class GridCellNumberRenderer: ...
class GridCellRenderer: ...
class GridCellRendererPtr: ...
class GridCellStringRenderer: ...
class GridCellTextEditor: ...
class GridColumnHeaderRenderer: ...
class GridColumnHeaderRendererDefault: ...
class GridCornerHeaderRenderer: ...
class GridCornerHeaderRendererDefault: ...
class GridEditorCreatedEvent: ...
class GridEvent: ...
class GridFitMode: ...
class GridHeaderLabelsRenderer: ...
GridNameStr = b'grid'
class GridRangeSelectEvent: ...
class GridRenderStyle: ...
class GridRowHeaderRenderer: ...
class GridRowHeaderRendererDefault: ...
class GridSizeEvent: ...
class GridSizesInfo: ...
class GridStringTable: ...
class GridTableBase: ...
class GridTableMessage: ...
class GridTableRequest: ...
class GridUpdateLocker: ...
class PyGridBlocksIterator: ...
class PyGridCellAttrProvider: ...
class PyGridCellEditor: ...
class PyGridCellRenderer: ...
class PyGridTableBase: ...
class _im_GridCellCoords: ...
wxEVT_GRID_CELL_BEGIN_DRAG = 10258
wxEVT_GRID_CELL_CHANGED = 10270
wxEVT_GRID_CELL_CHANGING = 10269
wxEVT_GRID_CELL_LEFT_CLICK = 10254
wxEVT_GRID_CELL_LEFT_DCLICK = 10256
wxEVT_GRID_CELL_RIGHT_CLICK = 10255
wxEVT_GRID_CELL_RIGHT_DCLICK = 10257
wxEVT_GRID_COL_AUTO_SIZE = 10265
wxEVT_GRID_COL_MOVE = 10266
wxEVT_GRID_COL_SIZE = 10264
wxEVT_GRID_COL_SORT = 10267
wxEVT_GRID_EDITOR_CREATED = 10274
wxEVT_GRID_EDITOR_HIDDEN = 10273
wxEVT_GRID_EDITOR_SHOWN = 10272
wxEVT_GRID_LABEL_LEFT_CLICK = 10259
wxEVT_GRID_LABEL_LEFT_DCLICK = 10261
wxEVT_GRID_LABEL_RIGHT_CLICK = 10260
wxEVT_GRID_LABEL_RIGHT_DCLICK = 10262
wxEVT_GRID_RANGE_SELECT = 10268
wxEVT_GRID_ROW_SIZE = 10263
wxEVT_GRID_SELECT_CELL = 10271
wxEVT_GRID_TABBING = 10275
EVT_GRID_CELL_BEGIN_DRAG = PyEventBinder()
EVT_GRID_CELL_CHANGED = PyEventBinder()
EVT_GRID_CELL_CHANGING = PyEventBinder()
EVT_GRID_CELL_LEFT_CLICK = PyEventBinder()
EVT_GRID_CELL_LEFT_DCLICK = PyEventBinder()
EVT_GRID_CELL_RIGHT_CLICK = PyEventBinder()
EVT_GRID_CELL_RIGHT_DCLICK = PyEventBinder()
EVT_GRID_CMD_CELL_BEGIN_DRAG = PyEventBinder()
EVT_GRID_CMD_CELL_CHANGED = PyEventBinder()
EVT_GRID_CMD_CELL_CHANGING = PyEventBinder()
EVT_GRID_CMD_CELL_LEFT_CLICK = PyEventBinder()
EVT_GRID_CMD_CELL_LEFT_DCLICK = PyEventBinder()
EVT_GRID_CMD_CELL_RIGHT_CLICK = PyEventBinder()
EVT_GRID_CMD_CELL_RIGHT_DCLICK = PyEventBinder()
EVT_GRID_CMD_COL_MOVE = PyEventBinder()
EVT_GRID_CMD_COL_SIZE = PyEventBinder()
EVT_GRID_CMD_COL_SORT = PyEventBinder()
EVT_GRID_CMD_EDITOR_CREATED = PyEventBinder()
EVT_GRID_CMD_EDITOR_HIDDEN = PyEventBinder()
EVT_GRID_CMD_EDITOR_SHOWN = PyEventBinder()
EVT_GRID_CMD_LABEL_LEFT_CLICK = PyEventBinder()
EVT_GRID_CMD_LABEL_LEFT_DCLICK = PyEventBinder()
EVT_GRID_CMD_LABEL_RIGHT_CLICK = PyEventBinder()
EVT_GRID_CMD_LABEL_RIGHT_DCLICK = PyEventBinder()
EVT_GRID_CMD_RANGE_SELECT = PyEventBinder()
EVT_GRID_CMD_ROW_SIZE = PyEventBinder()
EVT_GRID_CMD_SELECT_CELL = PyEventBinder()
EVT_GRID_CMD_TABBING = PyEventBinder()
EVT_GRID_COL_MOVE = PyEventBinder()
EVT_GRID_COL_SIZE = PyEventBinder()
EVT_GRID_COL_SORT = PyEventBinder()
EVT_GRID_EDITOR_CREATED = PyEventBinder()
EVT_GRID_EDITOR_HIDDEN = PyEventBinder()
EVT_GRID_EDITOR_SHOWN = PyEventBinder()
EVT_GRID_LABEL_LEFT_CLICK = PyEventBinder()
EVT_GRID_LABEL_LEFT_DCLICK = PyEventBinder()
EVT_GRID_LABEL_RIGHT_CLICK = PyEventBinder()
EVT_GRID_LABEL_RIGHT_DCLICK = PyEventBinder()
EVT_GRID_RANGE_SELECT = PyEventBinder()
EVT_GRID_ROW_SIZE = PyEventBinder()
EVT_GRID_SELECT_CELL = PyEventBinder()
EVT_GRID_TABBING = PyEventBinder()
