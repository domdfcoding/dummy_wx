from wx import PyEventBinder

# Based on wxPython
# Copyright: (c) 2018 by Total Control Software
# License:   wxWindows License


def dummy_function(*args, **kwargs):
	return 0


ID_RICHTEXT_PROPERTIES1 = 6000
ID_RICHTEXT_PROPERTIES2 = 6001
ID_RICHTEXT_PROPERTIES3 = 6002
RE_CENTER_CARET = 32768
RE_CENTRE_CARET = 32768
RE_MULTILINE = 32
RE_READONLY = 16
RICHTEXT_ALL = (-2, -2)
RICHTEXT_ALT_DOWN = 4
RICHTEXT_CACHE_SIZE = 4
RICHTEXT_CHANGE_ATTRIBUTES = 2
RICHTEXT_CHANGE_OBJECT = 5
RICHTEXT_CHANGE_STYLE = 3
RICHTEXT_CTRL_DOWN = 2
RICHTEXT_DELETE = 1
RICHTEXT_DRAW_GUIDELINES = 8
RICHTEXT_DRAW_IGNORE_CACHE = 1
RICHTEXT_DRAW_PRINT = 4
RICHTEXT_DRAW_SELECTED = 2
RICHTEXT_EX_NO_GUIDELINES = 256
RICHTEXT_FIXED_HEIGHT = 2
RICHTEXT_FIXED_WIDTH = 1
RICHTEXT_FORMATTED = 1
RICHTEXT_FORMAT_BULLETS = 8
RICHTEXT_FORMAT_FONT = 2
RICHTEXT_FORMAT_INDENTS_SPACING = 16
RICHTEXT_FORMAT_STYLE_EDITOR = 1
RICHTEXT_FORMAT_TABS = 4
RICHTEXT_HANDLER_CONVERT_FACENAMES = 256
RICHTEXT_HANDLER_INCLUDE_STYLESHEET = 1
RICHTEXT_HANDLER_NO_HEADER_FOOTER = 128
RICHTEXT_HANDLER_SAVE_IMAGES_TO_BASE64 = 64
RICHTEXT_HANDLER_SAVE_IMAGES_TO_FILES = 32
RICHTEXT_HANDLER_SAVE_IMAGES_TO_MEMORY = 16
RICHTEXT_HEIGHT_ONLY = 8
RICHTEXT_HITTEST_AFTER = 4
RICHTEXT_HITTEST_BEFORE = 2
RICHTEXT_HITTEST_HONOUR_ATOMIC = 128
RICHTEXT_HITTEST_NONE = 1
RICHTEXT_HITTEST_NO_FLOATING_OBJECTS = 64
RICHTEXT_HITTEST_NO_NESTED_OBJECTS = 32
RICHTEXT_HITTEST_ON = 8
RICHTEXT_HITTEST_OUTSIDE = 16
RICHTEXT_INSERT = 0
RICHTEXT_INSERT_INTERACTIVE = 2
RICHTEXT_INSERT_NONE = 0
RICHTEXT_INSERT_WITH_PREVIOUS_PARAGRAPH_STYLE = 1
RICHTEXT_LAYOUT_SPECIFIED_RECT = 16
RICHTEXT_NONE = (-1, -1)
RICHTEXT_NO_SELECTION = (-2, -2)
RICHTEXT_ORGANISER_APPLY_STYLES = 4
RICHTEXT_ORGANISER_BROWSE = 4128
RICHTEXT_ORGANISER_BROWSE_NUMBERING = 1120
RICHTEXT_ORGANISER_CREATE_STYLES = 2
RICHTEXT_ORGANISER_DELETE_STYLES = 1
RICHTEXT_ORGANISER_EDIT_STYLES = 8
RICHTEXT_ORGANISER_OK_CANCEL = 32
RICHTEXT_ORGANISER_ORGANISE = 4127
RICHTEXT_ORGANISER_RENAME_STYLES = 16
RICHTEXT_ORGANISER_RENUMBER = 64
RICHTEXT_ORGANISER_SHOW_ALL = 4096
RICHTEXT_ORGANISER_SHOW_BOX = 2048
RICHTEXT_ORGANISER_SHOW_CHARACTER = 256
RICHTEXT_ORGANISER_SHOW_LIST = 1024
RICHTEXT_ORGANISER_SHOW_PARAGRAPH = 512
RICHTEXT_PAGE_ALL = 2
RICHTEXT_PAGE_CENTRE = 1
RICHTEXT_PAGE_EVEN = 1
RICHTEXT_PAGE_LEFT = 0
RICHTEXT_PAGE_ODD = 0
RICHTEXT_PAGE_RIGHT = 2
RICHTEXT_SETPROPERTIES_CHARACTERS_ONLY = 4
RICHTEXT_SETPROPERTIES_NONE = 0
RICHTEXT_SETPROPERTIES_PARAGRAPHS_ONLY = 2
RICHTEXT_SETPROPERTIES_REMOVE = 16
RICHTEXT_SETPROPERTIES_RESET = 8
RICHTEXT_SETPROPERTIES_WITH_UNDO = 1
RICHTEXT_SETSTYLE_CHARACTERS_ONLY = 8
RICHTEXT_SETSTYLE_NONE = 0
RICHTEXT_SETSTYLE_OPTIMIZE = 2
RICHTEXT_SETSTYLE_PARAGRAPHS_ONLY = 4
RICHTEXT_SETSTYLE_REMOVE = 128
RICHTEXT_SETSTYLE_RENUMBER = 16
RICHTEXT_SETSTYLE_RESET = 64
RICHTEXT_SETSTYLE_SPECIFY_LEVEL = 32
RICHTEXT_SETSTYLE_WITH_UNDO = 1
RICHTEXT_SHIFT_DOWN = 1
RICHTEXT_TYPE_ANY = 0
RICHTEXT_TYPE_HTML = 3
RICHTEXT_TYPE_PDF = 5
RICHTEXT_TYPE_RTF = 4
RICHTEXT_TYPE_TEXT = 1
RICHTEXT_TYPE_XML = 2
RICHTEXT_UNFORMATTED = 2
RICHTEXT_VARIABLE_HEIGHT = 8
RICHTEXT_VARIABLE_WIDTH = 4
class RichTextAction: ...
class RichTextActionList: ...
class RichTextActionList_iterator: ...
RichTextApplyStyle = dummy_function
class RichTextAttr: ...
class RichTextAttrArray: ...
RichTextBitlistsEqPartial = dummy_function
class RichTextBox: ...
class RichTextBuffer: ...
class RichTextBufferDataObject: ...
class RichTextCell: ...
class RichTextCharacterStyleDefinition: ...
RichTextCombineBitlists = dummy_function
class RichTextCommand: ...
class RichTextCommandId: ...
class RichTextCompositeObject: ...
class RichTextContextMenuPropertiesInfo: ...
class RichTextCtrl: ...
class RichTextCtrlSelectionState: ...
RichTextCtrlSelectionState_CommonAncestor = 1
RichTextCtrlSelectionState_Normal = 0
RichTextDecimalToRoman = dummy_function
class RichTextDrawingContext: ...
class RichTextDrawingHandler: ...
class RichTextDrawingHandlerList: ...
class RichTextDrawingHandlerList_iterator: ...
class RichTextEvent: ...
class RichTextField: ...
class RichTextFieldType: ...
class RichTextFieldTypeStandard: ...
class RichTextFileHandler: ...
class RichTextFileHandlerList: ...
class RichTextFileHandlerList_iterator: ...
class RichTextFileType: ...
class RichTextFloatCollector: ...
class RichTextFontTable: ...
class RichTextFormattingDialog: ...
class RichTextFormattingDialogFactory: ...
class RichTextHTMLHandler: ...
RichTextHasStyle = dummy_function
class RichTextHeaderFooterData: ...
class RichTextHitTestFlags: ...
class RichTextImage: ...
class RichTextImageBlock: ...
class RichTextLine: ...
RichTextLineBreakChar = '\x1d'
class RichTextLineList: ...
class RichTextLineList_iterator: ...
class RichTextListStyleDefinition: ...
RichTextModuleInit = dummy_function
class RichTextObject: ...
class RichTextObjectAddress: ...
class RichTextObjectList: ...
class RichTextObjectList_: ...
class RichTextObjectList__iterator: ...
class RichTextObjectList_iterator: ...
class RichTextObjectPtrArray: ...
class RichTextObjectPtrArrayArray: ...
class RichTextOddEvenPage: ...
class RichTextPageLocation: ...
class RichTextParagraph: ...
class RichTextParagraphLayoutBox: ...
class RichTextParagraphStyleDefinition: ...
class RichTextPlainText: ...
class RichTextPlainTextHandler: ...
class RichTextPrinting: ...
class RichTextPrintout: ...
class RichTextProperties: ...
class RichTextRange: ...
class RichTextRangeArray: ...
RichTextRemoveStyle = dummy_function
class RichTextRenderer: ...
class RichTextSelection: ...
RichTextSplitParaCharStyles = dummy_function
class RichTextStdRenderer: ...
class RichTextStyleComboCtrl: ...
class RichTextStyleDefinition: ...
class RichTextStyleListBox: ...
class RichTextStyleListCtrl: ...
class RichTextStyleOrganiserDialog: ...
class RichTextStyleSheet: ...
class RichTextTable: ...
RichTextTabsEq = dummy_function
class RichTextVariantArray: ...
class RichTextXMLHandler: ...
SCRIPT_MUL_FACTOR = 1.5
class SymbolPickerDialog: ...
TEXT_ATTR_KEEP_FIRST_PARA_STYLE = 536870912
TEXT_ATTR_UNITS_HUNDREDTHS_POINT = 256
TEXT_ATTR_UNITS_MASK = 271
TEXT_ATTR_UNITS_PERCENTAGE = 4
TEXT_ATTR_UNITS_PIXELS = 2
TEXT_ATTR_UNITS_POINTS = 8
TEXT_ATTR_UNITS_TENTHS_MM = 1
TEXT_ATTR_VALUE_VALID = 4096
TEXT_ATTR_VALUE_VALID_MASK = 4096
TEXT_BOX_ATTR_BORDER_COLOUR = 2
TEXT_BOX_ATTR_BORDER_DASHED = 3
TEXT_BOX_ATTR_BORDER_DOTTED = 2
TEXT_BOX_ATTR_BORDER_DOUBLE = 4
TEXT_BOX_ATTR_BORDER_GROOVE = 5
TEXT_BOX_ATTR_BORDER_INSET = 7
TEXT_BOX_ATTR_BORDER_MEDIUM = -2
TEXT_BOX_ATTR_BORDER_NONE = 0
TEXT_BOX_ATTR_BORDER_OUTSET = 8
TEXT_BOX_ATTR_BORDER_RIDGE = 6
TEXT_BOX_ATTR_BORDER_SOLID = 1
TEXT_BOX_ATTR_BORDER_STYLE = 1
TEXT_BOX_ATTR_BORDER_THICK = -3
TEXT_BOX_ATTR_BORDER_THIN = -1
TEXT_BOX_ATTR_BOX_STYLE_NAME = 16
TEXT_BOX_ATTR_CLEAR = 2
TEXT_BOX_ATTR_CLEAR_BOTH = 3
TEXT_BOX_ATTR_CLEAR_LEFT = 1
TEXT_BOX_ATTR_CLEAR_NONE = 0
TEXT_BOX_ATTR_CLEAR_RIGHT = 2
TEXT_BOX_ATTR_COLLAPSE_BORDERS = 4
TEXT_BOX_ATTR_COLLAPSE_FULL = 1
TEXT_BOX_ATTR_COLLAPSE_NONE = 0
TEXT_BOX_ATTR_CORNER_RADIUS = 64
TEXT_BOX_ATTR_FLOAT = 1
TEXT_BOX_ATTR_FLOAT_LEFT = 1
TEXT_BOX_ATTR_FLOAT_NONE = 0
TEXT_BOX_ATTR_FLOAT_RIGHT = 2
TEXT_BOX_ATTR_POSITION_ABSOLUTE = 32
TEXT_BOX_ATTR_POSITION_FIXED = 64
TEXT_BOX_ATTR_POSITION_MASK = 240
TEXT_BOX_ATTR_POSITION_RELATIVE = 16
TEXT_BOX_ATTR_POSITION_STATIC = 0
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT = 8
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_BOTTOM = 3
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_CENTRE = 2
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_NONE = 0
TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_TOP = 1
TEXT_BOX_ATTR_WHITESPACE = 32
TEXT_BOX_ATTR_WHITESPACE_NONE = 0
TEXT_BOX_ATTR_WHITESPACE_NORMAL = 1
TEXT_BOX_ATTR_WHITESPACE_NO_WRAP = 2
TEXT_BOX_ATTR_WHITESPACE_PREFORMATTED = 3
TEXT_BOX_ATTR_WHITESPACE_PREFORMATTED_LINE = 4
TEXT_BOX_ATTR_WHITESPACE_PREFORMATTED_WRAP = 5
class TextAttrBorder: ...
class TextAttrBorderFlags: ...
class TextAttrBorderStyle: ...
class TextAttrBorderWidth: ...
class TextAttrBorders: ...
TextAttrCollectCommonAttributes = dummy_function
class TextAttrDimension: ...
class TextAttrDimensionConverter: ...
class TextAttrDimensions: ...
TextAttrEq = dummy_function
class TextAttrShadow: ...
class TextAttrSize: ...
class TextAttrUnits: ...
class TextAttrValueFlags: ...
class TextBoxAttr: ...
class TextBoxAttrClearStyle: ...
class TextBoxAttrCollapseMode: ...
class TextBoxAttrFlags: ...
class TextBoxAttrFloatStyle: ...
class TextBoxAttrPosition: ...
class TextBoxAttrVerticalAlignment: ...
class TextBoxAttrWhitespaceMode: ...
class _im_RichTextRange: ...
wxEVT_RICHTEXT_BUFFER_RESET = 10507
wxEVT_RICHTEXT_CHARACTER = 10495
wxEVT_RICHTEXT_CONSUMING_CHARACTER = 10496
wxEVT_RICHTEXT_CONTENT_DELETED = 10503
wxEVT_RICHTEXT_CONTENT_INSERTED = 10502
wxEVT_RICHTEXT_DELETE = 10497
wxEVT_RICHTEXT_FOCUS_OBJECT_CHANGED = 10508
wxEVT_RICHTEXT_LEFT_CLICK = 10490
wxEVT_RICHTEXT_LEFT_DCLICK = 10493
wxEVT_RICHTEXT_MIDDLE_CLICK = 10491
wxEVT_RICHTEXT_PROPERTIES_CHANGED = 10505
wxEVT_RICHTEXT_RETURN = 10494
wxEVT_RICHTEXT_RIGHT_CLICK = 10492
wxEVT_RICHTEXT_SELECTION_CHANGED = 10506
wxEVT_RICHTEXT_STYLESHEET_CHANGED = 10501
wxEVT_RICHTEXT_STYLESHEET_CHANGING = 10500
wxEVT_RICHTEXT_STYLESHEET_REPLACED = 10499
wxEVT_RICHTEXT_STYLESHEET_REPLACING = 10498
wxEVT_RICHTEXT_STYLE_CHANGED = 10504
EVT_RICHTEXT_BUFFER_RESET = PyEventBinder()
EVT_RICHTEXT_CHARACTER = PyEventBinder()
EVT_RICHTEXT_CONTENT_DELETED = PyEventBinder()
EVT_RICHTEXT_CONTENT_INSERTED = PyEventBinder()
EVT_RICHTEXT_DELETE = PyEventBinder()
EVT_RICHTEXT_FOCUS_OBJECT_CHANGED = PyEventBinder()
EVT_RICHTEXT_LEFT_CLICK = PyEventBinder()
EVT_RICHTEXT_LEFT_DCLICK = PyEventBinder()
EVT_RICHTEXT_MIDDLE_CLICK = PyEventBinder()
EVT_RICHTEXT_RETURN = PyEventBinder()
EVT_RICHTEXT_RIGHT_CLICK = PyEventBinder()
EVT_RICHTEXT_SELECTION_CHANGED = PyEventBinder()
EVT_RICHTEXT_STYLESHEET_CHANGED = PyEventBinder()
EVT_RICHTEXT_STYLESHEET_CHANGING = PyEventBinder()
EVT_RICHTEXT_STYLESHEET_REPLACED = PyEventBinder()
EVT_RICHTEXT_STYLESHEET_REPLACING = PyEventBinder()
EVT_RICHTEXT_STYLE_CHANGED = PyEventBinder()
