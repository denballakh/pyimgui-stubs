import typing as t
from typing import Any

Vec2 = tuple[float, float]
Vec4 = tuple[float, float, float, float]
# ==== Condition enum redefines ====
NONE: int
ALWAYS: int
ONCE: int
FIRST_USE_EVER: int
APPEARING: int

# ==== Style var enum redefines ====
STYLE_ALPHA: float
STYLE_WINDOW_PADDING: Vec2
STYLE_WINDOW_ROUNDING: float
STYLE_WINDOW_BORDERSIZE: float
STYLE_WINDOW_MIN_SIZE: Vec2
STYLE_WINDOW_TITLE_ALIGN: Vec2
STYLE_CHILD_ROUNDING: float
STYLE_CHILD_BORDERSIZE: float
STYLE_POPUP_ROUNDING: float
STYLE_POPUP_BORDERSIZE: float
STYLE_FRAME_PADDING: Vec2
STYLE_FRAME_ROUNDING: float
STYLE_FRAME_BORDERSIZE: float
STYLE_ITEM_SPACING: Vec2
STYLE_ITEM_INNER_SPACING: Vec2
STYLE_INDENT_SPACING: float
STYLE_CELL_PADDING: int
STYLE_SCROLLBAR_SIZE: float
STYLE_SCROLLBAR_ROUNDING: float
STYLE_GRAB_MIN_SIZE: float
STYLE_GRAB_ROUNDING: float
STYLE_TAB_ROUNDING: float
STYLE_BUTTON_TEXT_ALIGN: Vec2
STYLE_SELECTABLE_TEXT_ALIGN: Vec2

# ==== Button Flags ====
BUTTON_NONE: int
BUTTON_MOUSE_BUTTON_LEFT: int
BUTTON_MOUSE_BUTTON_RIGHT: int
BUTTON_MOUSE_BUTTON_MIDDLE: int

# ==== Key map enum redefines ====
KEY_TAB: int
KEY_LEFT_ARROW: int
KEY_RIGHT_ARROW: int
KEY_UP_ARROW: int
KEY_DOWN_ARROW: int
KEY_PAGE_UP: int
KEY_PAGE_DOWN: int
KEY_HOME: int
KEY_END: int
KEY_INSERT: int
KEY_DELETE: int
KEY_BACKSPACE: int
KEY_SPACE: int
KEY_ENTER: int
KEY_ESCAPE: int
KEY_PAD_ENTER: int
KEY_A: int
KEY_C: int
KEY_V: int
KEY_X: int
KEY_Y: int
KEY_Z: int

# ==== Key Mod Flags ====
KEY_MOD_NONE: int
KEY_MOD_CTRL: int
KEY_MOD_SHIFT: int
KEY_MOD_ALT: int
KEY_MOD_SUPER: int

# ==== Nav Input ====
NAV_INPUT_ACTIVATE: int
NAV_INPUT_CANCEL: int
NAV_INPUT_INPUT: int
NAV_INPUT_MENU: int
NAV_INPUT_DPAD_LEFT: int
NAV_INPUT_DPAD_RIGHT: int
NAV_INPUT_DPAD_UP: int
NAV_INPUT_DPAD_DOWN: int
NAV_INPUT_L_STICK_LEFT: int
NAV_INPUT_L_STICK_RIGHT: int
NAV_INPUT_L_STICK_UP: int
NAV_INPUT_L_STICK_DOWN: int
NAV_INPUT_FOCUS_PREV: int
NAV_INPUT_FOCUS_NEXT: int
NAV_INPUT_TWEAK_SLOW: int
NAV_INPUT_TWEAK_FAST: int
NAV_INPUT_COUNT: int

# ==== Window flags enum redefines ====
WINDOW_NONE: int
WINDOW_NO_TITLE_BAR: int
WINDOW_NO_RESIZE: int
WINDOW_NO_MOVE: int
WINDOW_NO_SCROLLBAR: int
WINDOW_NO_SCROLL_WITH_MOUSE: int
WINDOW_NO_COLLAPSE: int
WINDOW_ALWAYS_AUTO_RESIZE: int
WINDOW_NO_BACKGROUND: int
WINDOW_NO_SAVED_SETTINGS: int
WINDOW_NO_MOUSE_INPUTS: int
WINDOW_MENU_BAR: int
WINDOW_HORIZONTAL_SCROLLING_BAR: int
WINDOW_NO_FOCUS_ON_APPEARING: int
WINDOW_NO_BRING_TO_FRONT_ON_FOCUS: int
WINDOW_ALWAYS_VERTICAL_SCROLLBAR: int
WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR: int
WINDOW_ALWAYS_USE_WINDOW_PADDING: int
WINDOW_NO_NAV_INPUTS: int
WINDOW_NO_NAV_FOCUS: int
WINDOW_UNSAVED_DOCUMENT: int
WINDOW_NO_NAV: int
WINDOW_NO_DECORATION: int
WINDOW_NO_INPUTS: int

# ==== Color Edit Flags ====
COLOR_EDIT_NONE: int
COLOR_EDIT_NO_ALPHA: int
COLOR_EDIT_NO_PICKER: int
COLOR_EDIT_NO_OPTIONS: int
COLOR_EDIT_NO_SMALL_PREVIEW: int
COLOR_EDIT_NO_INPUTS: int
COLOR_EDIT_NO_TOOLTIP: int
COLOR_EDIT_NO_LABEL: int
COLOR_EDIT_NO_SIDE_PREVIEW: int
COLOR_EDIT_NO_DRAG_DROP: int
COLOR_EDIT_NO_BORDER: int

COLOR_EDIT_ALPHA_BAR: int
COLOR_EDIT_ALPHA_PREVIEW: int
COLOR_EDIT_ALPHA_PREVIEW_HALF: int
COLOR_EDIT_HDR: int
COLOR_EDIT_DISPLAY_RGB: int
COLOR_EDIT_DISPLAY_HSV: int
COLOR_EDIT_DISPLAY_HEX: int
COLOR_EDIT_UINT8: int
COLOR_EDIT_FLOAT: int
COLOR_EDIT_PICKER_HUE_BAR: int
COLOR_EDIT_PICKER_HUE_WHEEL: int
COLOR_EDIT_INPUT_RGB: int
COLOR_EDIT_INPUT_HSV: int

COLOR_EDIT_DEFAULT_OPTIONS: int

# ==== TreeNode flags enum redefines ====
TREE_NODE_NONE: int
TREE_NODE_SELECTED: int
TREE_NODE_FRAMED: int
TREE_NODE_ALLOW_ITEM_OVERLAP: int
TREE_NODE_NO_TREE_PUSH_ON_OPEN: int
TREE_NODE_NO_AUTO_OPEN_ON_LOG: int
TREE_NODE_DEFAULT_OPEN: int
TREE_NODE_OPEN_ON_DOUBLE_CLICK: int
TREE_NODE_OPEN_ON_ARROW: int
TREE_NODE_LEAF: int
TREE_NODE_BULLET: int
TREE_NODE_FRAME_PADDING: int
TREE_NODE_SPAN_AVAILABLE_WIDTH: int
TREE_NODE_SPAN_FULL_WIDTH: int
TREE_NODE_NAV_LEFT_JUPS_BACK_HERE: int
TREE_NODE_COLLAPSING_HEADER: int

# ==== Popup Flags ====
POPUP_NONE: int
POPUP_MOUSE_BUTTON_LEFT: int
POPUP_MOUSE_BUTTON_RIGHT: int
POPUP_MOUSE_BUTTON_MIDDLE: int
POPUP_MOUSE_BUTTON_MASK: int
POPUP_MOUSE_BUTTON_DEFAULT: int
POPUP_NO_OPEN_OVER_EXISTING_POPUP: int
POPUP_NO_OPEN_OVER_ITEMS: int
POPUP_ANY_POPUP_ID: int
POPUP_ANY_POPUP_LEVEL: int
POPUP_ANY_POPUP: int

# ==== Selectable flags enum redefines ====
SELECTABLE_NONE: int
SELECTABLE_DONT_CLOSE_POPUPS: int
SELECTABLE_SPAN_ALL_COLUMNS: int
SELECTABLE_ALLOW_DOUBLE_CLICK: int
SELECTABLE_DISABLED: int
SELECTABLE_ALLOW_ITEM_OVERLAP: int

# ==== Combo flags enum redefines ====
COMBO_NONE: int
COMBO_POPUP_ALIGN_LEFT: int
COMBO_HEIGHT_SMALL: int
COMBO_HEIGHT_REGULAR: int
COMBO_HEIGHT_LARGE: int
COMBO_HEIGHT_LARGEST: int
COMBO_NO_ARROW_BUTTON: int
COMBO_NO_PREVIEW: int
COMBO_HEIGHT_MASK: int

# ==== Tab Bar Flags ====
TAB_BAR_NONE: int
TAB_BAR_REORDERABLE: int
TAB_BAR_AUTO_SELECT_NEW_TABS: int
TAB_BAR_TAB_LIST_POPUP_BUTTON: int
TAB_BAR_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON: int
TAB_BAR_NO_TAB_LIST_SCROLLING_BUTTONS: int
TAB_BAR_NO_TOOLTIP: int
TAB_BAR_FITTING_POLICY_RESIZE_DOWN: int
TAB_BAR_FITTING_POLICY_SCROLL: int
TAB_BAR_FITTING_POLICY_MASK: int
TAB_BAR_FITTING_POLICY_DEFAULT: int

# ==== Tab Item Flags ====
TAB_ITEM_NONE: int
TAB_ITEM_UNSAVED_DOCUMENT: int
TAB_ITEM_SET_SELECTED: int
TAB_ITEM_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON: int
TAB_ITEM_NO_PUSH_ID: int
TAB_ITEM_NO_TOOLTIP: int
TAB_ITEM_NO_REORDER: int
TAB_ITEM_LEADING: int
TAB_ITEM_TRAILING: int

# === Table Flags ===
# Features
TABLE_NONE: int
TABLE_RESIZABLE: int
TABLE_REORDERABLE: int
TABLE_HIDEABLE: int
TABLE_SORTABLE: int
TABLE_NO_SAVED_SETTINGS: int
TABLE_CONTEXT_MENU_IN_BODY: int
# Decorations
TABLE_ROW_BACKGROUND: int
TABLE_BORDERS_INNER_HORIZONTAL: int
TABLE_BORDERS_OUTER_HORIZONTAL: int
TABLE_BORDERS_INNER_VERTICAL: int
TABLE_BORDERS_OUTER_VERTICAL: int
TABLE_BORDERS_HORIZONTAL: int
TABLE_BORDERS_VERTICAL: int
TABLE_BORDERS_INNER: int
TABLE_BORDERS_OUTER: int
TABLE_BORDERS: int
TABLE_NO_BORDERS_IN_BODY: int
TABLE_NO_BORDERS_IN_BODY_UTIL_RESIZE: int
# Sizing Policy (read above for defaults)
TABLE_SIZING_FIXED_FIT: int
TABLE_SIZING_FIXED_SAME: int
TABLE_SIZING_STRETCH_PROP: int
TABLE_SIZING_STRETCH_SAME: int
# Sizing Extra Options
TABLE_NO_HOST_EXTEND_X: int
TABLE_NO_HOST_EXTEND_Y: int
TABLE_NO_KEEP_COLUMNS_VISIBLE: int
TABLE_PRECISE_WIDTHS: int
# Clipping
TABLE_NO_CLIP: int
# Padding
TABLE_PAD_OUTER_X: int
TABLE_NO_PAD_OUTER_X: int
TABLE_NO_PAD_INNER_X: int
# Scrolling
TABLE_SCROLL_X: int
TABLE_SCROLL_Y: int
# Sorting
TABLE_SORT_MULTI: int
TABLE_SORT_TRISTATE: int

# === Table Column Flags ===
# Input configuration flags
TABLE_COLUMN_NONE: int
TABLE_COLUMN_DEFAULT_HIDE: int
TABLE_COLUMN_DEFAULT_SORT: int
TABLE_COLUMN_WIDTH_STRETCH: int
TABLE_COLUMN_WIDTH_FIXED: int
TABLE_COLUMN_NO_RESIZE: int
TABLE_COLUMN_NO_REORDER: int
TABLE_COLUMN_NO_HIDE: int
TABLE_COLUMN_NO_CLIP: int
TABLE_COLUMN_NO_SORT: int
TABLE_COLUMN_NO_SORT_ASCENDING: int
TABLE_COLUMN_NO_SORT_DESCENDING: int
TABLE_COLUMN_NO_HEADER_WIDTH: int
TABLE_COLUMN_PREFER_SORT_ASCENDING: int
TABLE_COLUMN_PREFER_SORT_DESCENDING: int
TABLE_COLUMN_INDENT_ENABLE: int
TABLE_COLUMN_INDENT_DISABLE: int
# Output status flags, read-only via TableGetColumnFlags()
TABLE_COLUMN_IS_ENABLED: int
TABLE_COLUMN_IS_VISIBLE: int
TABLE_COLUMN_IS_SORTED: int
TABLE_COLUMN_IS_HOVERED: int

# === Table Row Flags ===
TABLE_ROW_NONE: int
TABLE_ROW_HEADERS: int

# === Table Background Target ===
TABLE_BACKGROUND_TARGET_NONE: int
TABLE_BACKGROUND_TARGET_ROW_BG0: int
TABLE_BACKGROUND_TARGET_ROW_BG1: int
TABLE_BACKGROUND_TARGET_CELL_BG: int

# === Focus flag enum redefines ====
# TODO: Change to FOCUSED_ ?
FOCUS_NONE: int
FOCUS_CHILD_WINDOWS: int
FOCUS_ROOT_WINDOW: int
FOCUS_ANY_WINDOW: int
FOCUS_ROOT_AND_CHILD_WINDOWS: int

# === Hovered flag enum redefines ====
HOVERED_NONE: int
HOVERED_CHILD_WINDOWS: int
HOVERED_ROOT_WINDOW: int
HOVERED_ANY_WINDOW: int
HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP: int
HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM: int
HOVERED_ALLOW_WHEN_OVERLAPPED: int
HOVERED_ALLOW_WHEN_DISABLED: int
HOVERED_RECT_ONLY: int
HOVERED_ROOT_AND_CHILD_WINDOWS: int

# === Drag Drop flag enum redefines ====
DRAG_DROP_NONE: int
DRAG_DROP_SOURCE_NO_PREVIEW_TOOLTIP: int
DRAG_DROP_SOURCE_NO_DISABLE_HOVER: int
DRAG_DROP_SOURCE_NO_HOLD_TO_OPEN_OTHERS: int
DRAG_DROP_SOURCE_ALLOW_NULL_ID: int
DRAG_DROP_SOURCE_EXTERN: int
DRAG_DROP_SOURCE_AUTO_EXPIRE_PAYLOAD: int

# === Accept Drag Drop Payload flag enum redefines ====
DRAG_DROP_ACCEPT_BEFORE_DELIVERY: int
DRAG_DROP_ACCEPT_NO_DRAW_DEFAULT_RECT: int
DRAG_DROP_ACCEPT_NO_PREVIEW_TOOLTIP: int
DRAG_DROP_ACCEPT_PEEK_ONLY: int

# === Cardinal Direction enum redefines ====
DIRECTION_NONE: int
DIRECTION_LEFT: int
DIRECTION_RIGHT: int
DIRECTION_UP: int
DIRECTION_DOWN: int

# === Sorting Direction ===
SORT_DIRECTION_NONE: int
SORT_DIRECTION_ASCENDING: int
SORT_DIRECTION_DESCENDING: int

# ==== Mouse Cursors ====
MOUSE_CURSOR_NONE: int
MOUSE_CURSOR_ARROW: int
MOUSE_CURSOR_TEXT_INPUT: int
MOUSE_CURSOR_RESIZE_ALL: int
MOUSE_CURSOR_RESIZE_NS: int
MOUSE_CURSOR_RESIZE_EW: int
MOUSE_CURSOR_RESIZE_NESW: int
MOUSE_CURSOR_RESIZE_NWSE: int
MOUSE_CURSOR_HAND: int
MOUSE_CURSOR_NOT_ALLOWED: int

# ==== Color identifiers for styling ====
COLOR_TEXT: int
COLOR_TEXT_DISABLED: int
COLOR_WINDOW_BACKGROUND: int
COLOR_CHILD_BACKGROUND: int
COLOR_POPUP_BACKGROUND: int
COLOR_BORDER: int
COLOR_BORDER_SHADOW: int
COLOR_FRAME_BACKGROUND: int
COLOR_FRAME_BACKGROUND_HOVERED: int
COLOR_FRAME_BACKGROUND_ACTIVE: int
COLOR_TITLE_BACKGROUND: int
COLOR_TITLE_BACKGROUND_ACTIVE: int
COLOR_TITLE_BACKGROUND_COLLAPSED: int
COLOR_MENUBAR_BACKGROUND: int
COLOR_SCROLLBAR_BACKGROUND: int
COLOR_SCROLLBAR_GRAB: int
COLOR_SCROLLBAR_GRAB_HOVERED: int
COLOR_SCROLLBAR_GRAB_ACTIVE: int
COLOR_CHECK_MARK: int
COLOR_SLIDER_GRAB: int
COLOR_SLIDER_GRAB_ACTIVE: int
COLOR_BUTTON: int
COLOR_BUTTON_HOVERED: int
COLOR_BUTTON_ACTIVE: int
COLOR_HEADER: int
COLOR_HEADER_HOVERED: int
COLOR_HEADER_ACTIVE: int
COLOR_SEPARATOR: int
COLOR_SEPARATOR_HOVERED: int
COLOR_SEPARATOR_ACTIVE: int
COLOR_RESIZE_GRIP: int
COLOR_RESIZE_GRIP_HOVERED: int
COLOR_RESIZE_GRIP_ACTIVE: int
COLOR_TAB: int
COLOR_TAB_HOVERED: int
COLOR_TAB_ACTIVE: int
COLOR_TAB_UNFOCUSED: int
COLOR_TAB_UNFOCUSED_ACTIVE: int
COLOR_PLOT_LINES: int
COLOR_PLOT_LINES_HOVERED: int
COLOR_PLOT_HISTOGRAM: int
COLOR_PLOT_HISTOGRAM_HOVERED: int
COLOR_TABLE_HEADER_BACKGROUND: int
COLOR_TABLE_BORDER_STRONG: int
COLOR_TABLE_BORDER_LIGHT: int
COLOR_TABLE_ROW_BACKGROUND: int
COLOR_TABLE_ROW_BACKGROUND_ALT: int
COLOR_TEXT_SELECTED_BACKGROUND: int
COLOR_DRAG_DROP_TARGET: int
COLOR_NAV_HIGHLIGHT: int
COLOR_NAV_WINDOWING_HIGHLIGHT: int
COLOR_NAV_WINDOWING_DIM_BACKGROUND: int
COLOR_MODAL_WINDOW_DIM_BACKGROUND: int
COLOR_COUNT: int

# ==== Data Type ====
DATA_TYPE_S8: int
DATA_TYPE_U8: int
DATA_TYPE_S16: int
DATA_TYPE_U16: int
DATA_TYPE_S32: int
DATA_TYPE_U32: int
DATA_TYPE_S64: int
DATA_TYPE_U64: int
DATA_TYPE_FLOAT: int
DATA_TYPE_DOUBLE: int

# ==== Text input flags ====
INPUT_TEXT_NONE: int
INPUT_TEXT_CHARS_DECIMAL: int
INPUT_TEXT_CHARS_HEXADECIMAL: int
INPUT_TEXT_CHARS_UPPERCASE: int
INPUT_TEXT_CHARS_NO_BLANK: int
INPUT_TEXT_AUTO_SELECT_ALL: int
INPUT_TEXT_ENTER_RETURNS_TRUE: int
INPUT_TEXT_CALLBACK_COMPLETION: int
INPUT_TEXT_CALLBACK_HISTORY: int
INPUT_TEXT_CALLBACK_ALWAYS: int
INPUT_TEXT_CALLBACK_CHAR_FILTER: int
INPUT_TEXT_ALLOW_TAB_INPUT: int
INPUT_TEXT_CTRL_ENTER_FOR_NEW_LINE: int
INPUT_TEXT_NO_HORIZONTAL_SCROLL: int
INPUT_TEXT_ALWAYS_OVERWRITE: int
INPUT_TEXT_ALWAYS_INSERT_MODE: int
INPUT_TEXT_READ_ONLY: int
INPUT_TEXT_PASSWORD: int
INPUT_TEXT_NO_UNDO_REDO: int
INPUT_TEXT_CHARS_SCIENTIFIC: int
INPUT_TEXT_CALLBACK_RESIZE: int
INPUT_TEXT_CALLBACK_EDIT: int

# ==== Draw Corner Flags ===
# OBSOLETED in 1.82 (from Mars 2021), use ImDrawFlags_xxx
DRAW_CORNER_NONE: int
DRAW_CORNER_TOP_LEFT: int
DRAW_CORNER_TOP_RIGHT: int
DRAW_CORNER_BOTTOM_LEFT: int
DRAW_CORNER_BOTTOM_RIGHT: int
DRAW_CORNER_TOP: int
DRAW_CORNER_BOTTOM: int
DRAW_CORNER_LEFT: int
DRAW_CORNER_RIGHT: int
DRAW_CORNER_ALL: int

# ==== Draw Flags ====
DRAW_NONE: int
DRAW_CLOSED: int
DRAW_ROUND_CORNERS_TOP_LEFT: int
DRAW_ROUND_CORNERS_TOP_RIGHT: int
DRAW_ROUND_CORNERS_BOTTOM_LEFT: int
DRAW_ROUND_CORNERS_BOTTOM_RIGHT: int
DRAW_ROUND_CORNERS_NONE: int
DRAW_ROUND_CORNERS_TOP: int
DRAW_ROUND_CORNERS_BOTTOM: int
DRAW_ROUND_CORNERS_LEFT: int
DRAW_ROUND_CORNERS_RIGHT: int
DRAW_ROUND_CORNERS_ALL: int

# ==== Draw List Flags ====
DRAW_LIST_NONE: int
DRAW_LIST_ANTI_ALIASED_LINES: int
DRAW_LIST_ANTI_ALIASED_LINES_USE_TEX: int
DRAW_LIST_ANTI_ALIASED_FILL: int
DRAW_LIST_ALLOW_VTX_OFFSET: int

# ==== Font Atlas Flags ====
FONT_ATLAS_NONE: int
FONT_ATLAS_NO_POWER_OF_TWO_HEIGHT: int
FONT_ATLAS_NO_MOUSE_CURSOR: int
FONT_ATLAS_NO_BAKED_LINES: int

# ==== Config Flags ====
CONFIG_NONE: int
CONFIG_NAV_ENABLE_KEYBOARD: int
CONFIG_NAV_ENABLE_GAMEPAD: int
CONFIG_NAV_ENABLE_SET_MOUSE_POS: int
CONFIG_NAV_NO_CAPTURE_KEYBOARD: int
CONFIG_NO_MOUSE: int
CONFIG_NO_MOUSE_CURSOR_CHANGE: int
CONFIG_IS_RGB: int
CONFIG_IS_TOUCH_SCREEN: int

# ==== Backend Flags ====
BACKEND_NONE: int
BACKEND_HAS_GAMEPAD: int
BACKEND_HAS_MOUSE_CURSORS: int
BACKEND_HAS_SET_MOUSE_POS: int
BACKEND_RENDERER_HAS_VTX_OFFSET: int

# ==== Slider Flags ====
SLIDER_FLAGS_NONE: int
SLIDER_FLAGS_ALWAYS_CLAMP: int
SLIDER_FLAGS_LOGARITHMIC: int
SLIDER_FLAGS_NO_ROUND_TO_FORMAT: int
SLIDER_FLAGS_NO_INPUT: int

# ==== Mouse Button ====
MOUSE_BUTTON_LEFT: int
MOUSE_BUTTON_RIGHT: int
MOUSE_BUTTON_MIDDLE: int

# ==== Viewport Flags ====
VIEWPORT_FLAGS_NONE: int
VIEWPORT_FLAGS_IS_PLATFORM_WINDOW: int
VIEWPORT_FLAGS_IS_PLATFORM_MONITOR: int
VIEWPORT_FLAGS_OWNED_BY_APP: int

def get_io() -> _IO: ...
def new_frame() -> Any: ...
def render() -> Any: ...
def get_version() -> Any: ...
def style_colors_classic(dst: Any = None) -> Any: ...
def show_style_editor(style: Any = None) -> Any: ...
def show_font_selector(label: str) -> Any: ...
def begin(label: str, closable: Any = False, flags: Any = 0) -> _BeginEnd: ...
def get_draw_data() -> Any: ...
def begin_child(
    label: Any, width: float = 0, height: float = 0, border: bool = False, flags: Any = 0
) -> _BeginEndChild: ...
def end_child() -> Any: ...
def get_content_region_available() -> Any: ...
def get_window_content_region_min() -> Any: ...
def get_window_content_region_width() -> Any: ...
def set_window_focus_labeled(label: str) -> Any: ...
def set_window_size_named(
    label: str, width: float, height: float, condition: int = ONCE
) -> Any: ...
def get_scroll_y() -> Any: ...
def get_scroll_max_y() -> Any: ...
def set_scroll_y(scroll_y: float) -> Any: ...
def set_next_window_collapsed(collapsed: bool, condition: int = ALWAYS) -> Any: ...
def set_next_window_bg_alpha(alpha: float) -> Any: ...
def get_overlay_draw_list() -> Any: ...
def get_window_size() -> Any: ...
def get_window_height() -> Any: ...
def set_next_window_size(width: float, height: float, condition: int = ALWAYS) -> Any: ...
def set_next_window_content_size(width: float, height: float) -> Any: ...
def set_window_position_labeled(
    label: str, x: float, y: float, condition: int = ALWAYS
) -> Any: ...
def set_window_collapsed_labeled(label: str, collapsed: bool, condition: int = ALWAYS) -> Any: ...
def is_window_appearing() -> Any: ...
def tree_pop() -> Any: ...
def collapsing_header(text: str, visible: Any = None, flags: int = 0) -> Any: ...
def selectable(
    label: str, selected: Any = False, flags: int = 0, width: int = 0, height: int = 0
) -> Any: ...
def begin_list_box(label: str, width: int = 0, height: int = 0) -> _BeginEndListBox: ...
def end_list_box() -> Any: ...
def end_tooltip() -> Any: ...
def end_main_menu_bar() -> Any: ...
def end_menu_bar() -> Any: ...
def end_menu() -> Any: ...
def open_popup(label: str, flags: Any = 0) -> Any: ...
def open_popup_on_item_click(label: str | None = None, popup_flags: Any = 1) -> Any: ...
def begin_popup_context_item(
    label: str | None = None, mouse_button: Any = 1
) -> _BeginEndPopup: ...
def begin_popup_context_window(
    label: str | None = None, popup_flags: Any = 1
) -> _BeginEndPopup: ...
def begin_popup_context_void(label: str | None = None, popup_flags: Any = 1) -> _BeginEndPopup: ...
def end_popup() -> Any: ...
def begin_table(
    label: str,
    column: int,
    flags: Any = 0,
    outer_size_width: float = 0.0,
    outer_size_height: float = 0.0,
    inner_width: float = 0.0,
) -> _BeginEndTable: ...
def end_table() -> Any: ...
def table_next_column() -> Any: ...
def table_next_row(flags: int=0, min_row_height: int=0) -> Any: ...
def table_setup_column(
    label: str, flags: Any = 0, init_width_or_weight: float = 0.0, user_id: int = 0
) -> Any: ...
def table_setup_scroll_freeze(cols: int, rows: int) -> Any: ...
def table_header(label: str) -> Any: ...
def table_get_column_count() -> Any: ...
def table_get_row_index() -> Any: ...
def table_get_column_flags(column_n: int = -1) -> Any: ...
def text(text: str) -> Any: ...
def text_ansi(text: str) -> Any: ...
def text_ansi_colored(text: str, r: float, g: float, b: float, a: float = 1.0) -> Any: ...
def text_disabled(text: str) -> Any: ...
def label_text(label: str, text: str) -> Any: ...
def bullet() -> Any: ...
def bullet_text(text: str) -> Any: ...
def small_button(label: str) -> Any: ...
def invisible_button(identifier: str, width: float, height: float, flags: Any = 0) -> Any: ...
def image_button(
    texture_id,
    width: float,
    height: float,
    uv0: Any = (0, 0),
    uv1: Any = (1, 1),
    tint_color: Any = (1, 1, 1, 1),
    border_color: Any = (0, 0, 0, 0),
    frame_padding: int = -1,
) -> Any: ...
def checkbox(label: str, state: bool) -> Any: ...
def radio_button(label: str, active: bool) -> Any: ...
def begin_combo(label: str, preview_value: str, flags: Any = 0) -> _BeginEndCombo: ...
def end_combo() -> Any: ...
def color_edit3(label: str, r: float, g: float, b: float, flags: Any = 0) -> Any: ...
def drag_float(
    label: str,
    value: float,
    change_speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    flags: Any = 0,
) -> Any: ...
def drag_float3(
    label: str,
    value0: float,
    value1: float,
    value2: float,
    change_speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    flags: Any = 0,
) -> Any: ...
def drag_float_range2(
    label: str,
    current_min: float,
    current_max: float,
    speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    format_max: str | None = None,
    flags: Any = 0,
) -> Any: ...
def drag_int(
    label: str,
    value: int,
    change_speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    flags: Any = 0,
) -> Any: ...
def drag_int3(
    label: str,
    value0: int,
    value1: int,
    value2: int,
    change_speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    flags: Any = 0,
) -> Any: ...
def drag_int4(
    label: str,
    value0: int,
    value1: int,
    value2: int,
    value3: int,
    change_speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    flags: Any = 0,
) -> Any: ...
def drag_int_range2(
    label: str,
    current_min: int,
    current_max: int,
    speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    format_max: str | None = None,
    flags: Any = 0,
) -> Any: ...
def drag_scalar(
    label: str,
    data_type: Any,
    data: Any,
    change_speed: float,
    min_value: Any = None,
    max_value: Any = None,
    format: str | None = None,
    flags: Any = 0,
) -> Any: ...
def input_text(
    label: str,
    value: str,
    buffer_length: int = -1,
    flags: Any = 0,
    callback: Any = None,
    user_data: Any = None,
) -> tuple[bool, str]: ...
def input_text_with_hint(
    label: str,
    hint: str,
    value: str,
    buffer_length: int = -1,
    flags: Any = 0,
    callback: Any = None,
    user_data: Any = None,
) -> Any: ...
def input_float(
    label: str,
    value: float,
    step: float = 0.0,
    step_fast: float = 0.0,
    format: str = "%.3f",
    flags: Any = 0,
) -> Any: ...
def input_float3(
    label: str, value0: float, value1: float, value2: float, format: str = "%.3f", flags: Any = 0
) -> Any: ...
def input_int(
    label: str, value: int, step: int = 1, step_fast: int = 100, flags: Any = 0
) -> Any: ...
def input_int3(label: str, value0: int, value1: int, value2: int, flags: Any = 0) -> Any: ...
def input_int4(
    label: str, value0: int, value1: int, value2: int, value3: int, flags: Any = 0
) -> Any: ...
def input_double(
    label: str,
    value: float,
    step: float = 0.0,
    step_fast: float = 0.0,
    format: str = "%.6f",
    flags: Any = 0,
) -> Any: ...
def input_scalar(
    label: str,
    data_type: Any,
    data: Any,
    step: Any = None,
    step_fast: Any = None,
    format: str | None = None,
    flags: Any = 0,
) -> Any: ...
def slider_float(
    label: str,
    value: float,
    min_value: float,
    max_value: float,
    format: str = "%.3f",
    flags: Any = 0,
) -> Any: ...
def slider_float3(
    label: str,
    value0: float,
    value1: float,
    value2: float,
    min_value: float,
    max_value: float,
    format: str = "%.3f",
    flags: Any = 0,
) -> Any: ...
def slider_float4(
    label: str,
    value0: float,
    value1: float,
    value2: float,
    value3: float,
    min_value: float,
    max_value: float,
    format: str = "%.3f",
    flags: Any = 0,
) -> Any: ...
def slider_angle(
    label: str,
    rad_value: float,
    value_degrees_min: float = -360.0,
    value_degrees_max: float = 360,
    deg: Any = ...,
    flags: Any = 0,
) -> Any: ...
def slider_int(
    label: str, value: int, min_value: int, max_value: int, format: str = "%.f", flags: Any = 0
) -> Any: ...
def slider_int3(
    label: str,
    value0: int,
    value1: int,
    value2: int,
    min_value: int,
    max_value: int,
    format: str = "%.f",
    flags: Any = 0,
) -> Any: ...
def slider_int4(
    label: str,
    value0: int,
    value1: int,
    value2: int,
    value3: int,
    min_value: int,
    max_value: int,
    format: str = "%.f",
    flags: Any = 0,
) -> Any: ...
def slider_scalar(
    label: str,
    data_type: Any,
    data: Any,
    min_value: Any,
    max_value: Any,
    format: str = '',
    flags: Any = 0,
) -> Any: ...
def v_slider_float(
    label: str,
    width: float,
    height: float,
    value: float,
    min_value: float,
    max_value: float,
    format: str = "%.f",
    flags: Any = 0,
) -> Any: ...
def v_slider_scalar(
    label: str,
    width: float,
    height: float,
    data_type: Any,
    data: Any,
    min_value: Any,
    max_value: Any,
    format: str | None = None,
    flags: Any = 0,
) -> Any: ...
def progress_bar(fraction: float, size: Any = (-FLOAT_MIN, 0), overlay: str = "") -> Any: ...
def set_keyboard_focus_here(offset: int = 0) -> Any: ...
def is_item_focused() -> Any: ...
def is_item_clicked(mouse_button: Any = 0) -> Any: ...
def is_item_edited() -> Any: ...
def is_item_deactivated() -> Any: ...
def is_item_toggled_open() -> Any: ...
def is_any_item_active() -> Any: ...
def get_item_rect_min() -> Any: ...
def get_item_rect_size() -> Any: ...
def get_main_viewport() -> Any: ...
def is_window_focused(flags: Any = 0) -> Any: ...
def is_rect_visible(size_width: float, size_height: float) -> Any: ...
def get_time() -> Any: ...
def get_foreground_draw_list() -> Any: ...
def is_key_pressed(key_index: int, repeat: bool = False) -> Any: ...
def is_mouse_hovering_rect(
    r_min_x: float, r_min_y: float, r_max_x: float, r_max_y: float, clip: bool = True
) -> Any: ...
def is_mouse_clicked(button: int = 0, repeat: bool = False) -> Any: ...
def is_mouse_released(button: int = 0) -> Any: ...
def is_mouse_dragging(button: int, lock_threshold: float = -1.0) -> Any: ...
def get_mouse_pos() -> Any: ...
def get_mouse_cursor() -> Any: ...
def capture_mouse_from_app(want_capture_mouse_value: bool = True) -> Any: ...
def load_ini_settings_from_disk(ini_file_name: str) -> Any: ...
def save_ini_settings_to_disk(ini_file_name: str) -> Any: ...
def set_clipboard_text(text: str) -> Any: ...
def set_scroll_here_x(center_x_ratio: float = 0.5) -> Any: ...
def set_scroll_from_pos_x(local_x: float, center_x_ratio: float = 0.5) -> Any: ...
def push_font(font: Any) -> Any: ...
def color_convert_u32_to_float4(in_: int) -> Any: ...
def color_convert_rgb_to_hsv(r: float, g: float, b: float) -> Any: ...
def separator() -> Any: ...
def new_line() -> Any: ...
def dummy(width, height) -> Any: ...
def unindent(width: float = 0.0) -> Any: ...
def next_column() -> Any: ...
def get_column_offset(column_index: int = -1) -> Any: ...
def get_column_width(column_index: int = -1) -> Any: ...
def get_columns_count() -> Any: ...
def end_tab_bar() -> Any: ...
def begin_tab_item(label: str, opened: Any = None, flags: Any = 0) -> _BeginEndCombo: ...
def end_tab_item() -> Any: ...
def set_tab_item_closed(tab_or_docked_window_label: str) -> Any: ...
def begin_drag_drop_source(flags: Any = 0) -> _BeginEndDragDropSource: ...
def set_drag_drop_payload(type: str, data: Any, condition: int = 0) -> Any: ...
def begin_drag_drop_target() -> _BeginEndDragDropTarget: ...
def end_drag_drop_target() -> Any: ...
def push_clip_rect(
    clip_rect_min_x: float,
    clip_rect_min_y: float,
    clip_rect_max_x: float,
    clip_rect_max_y: float,
    intersect_with_current_clip_rect: bool = False,
) -> Any: ...
def pop_clip_rect() -> Any: ...
def begin_group() -> _BeginEndGroup: ...
def end_group() -> Any: ...
def get_cursor_pos_x() -> Any: ...
def set_cursor_pos_y(y: float) -> Any: ...
def get_cursor_screen_pos() -> Any: ...
def align_text_to_frame_padding() -> Any: ...
def get_text_line_height_with_spacing() -> Any: ...
def get_frame_height_with_spacing() -> Any: ...
def destroy_context(ctx: Any = None) -> Any: ...
def set_current_context(ctx: Any) -> Any: ...
def pop_id() -> Any: ...
def _ansifeed_text_ansi_colored(
    text: str, r: float, g: float, b: float, a: float = 1.0
) -> Any: ...
def _py_styled(variable: Any, value) -> Any: ...
def _py_scoped(str_id: str) -> Any: ...
def _py_vertex_buffer_vertex_uv_offset() -> Any: ...
def _py_vertex_buffer_vertex_size() -> Any: ...
def get_style() -> GuiStyle: ...
def end_frame() -> Any: ...
def show_user_guide() -> Any: ...
def style_colors_dark(dst: Any = None) -> Any: ...
def style_colors_light(dst: Any = None) -> Any: ...
def show_test_window() -> Any: ...
def show_metrics_window() -> Any: ...
def show_style_selector(label: str) -> Any: ...
def end() -> Any: ...
def get_content_region_max() -> Any: ...
def get_content_region_available_width() -> Any: ...
def get_window_content_region_max() -> Any: ...
def set_window_focus() -> Any: ...
def get_scroll_x() -> Any: ...
def get_scroll_max_x() -> Any: ...
def set_scroll_x(scroll_x: float) -> Any: ...
def set_window_font_scale(scale: float) -> Any: ...
def set_next_window_focus() -> Any: ...
def get_window_draw_list() -> Any: ...
def get_window_position() -> Any: ...
def get_window_width() -> Any: ...
def set_next_window_position(
    x: float, y: float, condition: int = ALWAYS, pivot_x: float = 0, pivot_y: float = 0
) -> Any: ...
def set_window_position(x: float, y: float, condition: int = ALWAYS) -> Any: ...
def set_window_collapsed(collapsed: bool, condition: int = ALWAYS) -> Any: ...
def is_window_collapsed() -> Any: ...
def tree_node(text: str, flags: int = 0) -> Any: ...
def get_tree_node_to_label_spacing() -> Any: ...
def set_next_item_open(is_open: bool, condition: int = 0) -> Any: ...
def listbox(label: str, current: int, items: Any, height_in_items: int = -1) -> Any: ...
def listbox_footer() -> Any: ...
def set_tooltip(text: str) -> Any: ...
def begin_tooltip() -> _BeginEndTooltip: ...
def begin_main_menu_bar() -> _BeginEndMainMenuBar: ...
def begin_menu_bar() -> _BeginEndMenuBar: ...
def begin_menu(label: str, enabled: Any = True) -> _BeginEndMenu: ...
def menu_item(
    label: str, shortcut: str | None = None, selected: bool = False, enabled: Any = True
) -> Any: ...
def begin_popup(label: str, flags: Any = 0) -> _BeginEndPopup: ...
def begin_popup_modal(title: str, visible: Any = None, flags: Any = 0) -> _BeginEndPopupModal: ...
def is_popup_open(label: str, flags: Any = 0) -> Any: ...
def close_current_popup() -> Any: ...
def table_set_column_index(column_n: int) -> Any: ...
def table_headers_row() -> Any: ...
def table_get_sort_specs() -> Any: ...
def table_get_column_index() -> Any: ...
def table_get_column_name(column_n: int = -1) -> Any: ...
def text_colored(text: str, r: float, g: float, b: float, a: float = 1.0) -> Any: ...
def text_wrapped(text: str) -> Any: ...
def text_unformatted(text: str) -> Any: ...
def button(label: str, width: int = 0, height: int = 0) -> Any: ...
def arrow_button(label: str, direction: Any = DIRECTION_NONE) -> Any: ...
def color_button(
    desc_id: str,
    r: float,
    g: float,
    b: float,
    a: Any = 1.0,
    flags: int = 0,
    width: float = 0,
    height: float = 0,
) -> Any: ...
def image(
    texture_id,
    width: float,
    height: float,
    uv0: Any = (0, 0),
    uv1: Any = (1, 1),
    tint_color: Any = (1, 1, 1, 1),
    border_color: Any = (0, 0, 0, 0),
) -> Any: ...
def checkbox_flags(label: str, flags: int, flags_value: int) -> Any: ...
def combo(label: str, current: int, items: Any, height_in_items: int = -1) -> Any: ...
def color_edit4(label: str, r: float, g: float, b: float, a: float, flags: Any = 0) -> Any: ...
def drag_float2(
    label: str,
    value0: float,
    value1: float,
    change_speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    flags: Any = 0,
) -> Any: ...
def drag_float4(
    label: str,
    value0: float,
    value1: float,
    value2: float,
    value3: float,
    change_speed: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 0.0,
    format: str = "%.3f",
    flags: Any = 0,
) -> Any: ...
def drag_int2(
    label: str,
    value0: int,
    value1: int,
    change_speed: float = 1.0,
    min_value: int = 0,
    max_value: int = 0,
    format: str = "%d",
    flags: Any = 0,
) -> Any: ...
def input_text_multiline(
    label: str,
    value: str,
    buffer_length: int = -1,
    width: float = 0,
    height: float = 0,
    flags: Any = 0,
    callback: Any = None,
    user_data: Any = None,
) -> Any: ...
def input_float2(
    label: str, value0: float, value1: float, format: str = "%.3f", flags: Any = 0
) -> Any: ...
def v_slider_int(
    label: str,
    width: float,
    height: float,
    value: int,
    min_value: int,
    max_value: int,
    format: str = "%d",
    flags: Any = 0,
) -> Any: ...
def set_item_default_focus() -> Any: ...
def is_item_active() -> Any: ...
def is_item_visible() -> Any: ...
def is_item_hovered() -> Any: ...
def is_item_activated() -> Any: ...
def is_item_deactivated_after_edit() -> Any: ...
def is_any_item_hovered() -> Any: ...
def is_any_item_focused() -> Any: ...
def get_item_rect_max() -> Any: ...
def set_item_allow_overlap() -> Any: ...
def get_style_color_name(index: int) -> Any: ...
def get_background_draw_list() -> Any: ...
def get_key_index(key: int) -> Any: ...
def is_key_down(key_index: int) -> Any: ...
def is_mouse_double_clicked(button: int = 0) -> Any: ...
def is_mouse_down(button: int = 0) -> Any: ...
def get_mouse_drag_delta(button: int = 0, lock_threshold: float = -1.0) -> Any: ...
def reset_mouse_drag_delta(button: int = 0) -> Any: ...
def set_mouse_cursor(mouse_cursor_type: Any) -> Any: ...
def get_clipboard_text() -> Any: ...
def load_ini_settings_from_memory(ini_data: str) -> Any: ...
def save_ini_settings_to_memory() -> Any: ...
def set_scroll_here_y(center_y_ratio: float = 0.5) -> Any: ...
def set_scroll_from_pos_y(local_y: float, center_y_ratio: float = 0.5) -> Any: ...
def pop_font() -> Any: ...
def calc_text_size(
    text: str, hide_text_after_double_hash: bool = False, wrap_width: float = -1.0
) -> Any: ...
def color_convert_float4_to_u32(r: float, g: float, b: float, a: float) -> Any: ...
def color_convert_hsv_to_rgb(h: float, s: float, v: float) -> Any: ...
def push_style_var(variable: Any, value) -> Any: ...
def push_style_color(variable: Any, r: float, g: float, b: float, a: float = 1.0) -> Any: ...
def pop_style_var(count: int = 1) -> Any: ...
def get_font_size() -> Any: ...
def get_style_color_vec_4(idx: Any) -> Any: ...
def get_font_tex_uv_white_pixel() -> Any: ...
def get_color_u32_idx(idx: Any, alpha_mul: float = 1.0) -> Any: ...
def get_color_u32_rgba(r: float, g: float, b: float, a: float) -> Any: ...
def get_color_u32(col: int) -> Any: ...
def push_item_width(item_width: float) -> Any: ...
def pop_item_width() -> Any: ...
def set_next_item_width(item_width: float) -> Any: ...
def calculate_item_width() -> Any: ...
def push_text_wrap_pos(wrap_pos_x: float = 0.0) -> Any: ...
def pop_text_wrap_pos() -> Any: ...
def push_allow_keyboard_focus(allow_focus: bool) -> Any: ...
def pop_allow_keyboard_focus() -> Any: ...
def push_button_repeat(repeat: bool) -> Any: ...
def pop_button_repeat() -> Any: ...
def pop_style_color(count: int = 1) -> Any: ...
def same_line(position: float = 0.0, spacing: float = -1.0) -> Any: ...
def spacing() -> Any: ...
def indent(width: float = 0.0) -> Any: ...
def columns(count: int = 1, identifier: str | None = None, border: bool = True) -> Any: ...
def get_column_index() -> Any: ...
def set_column_offset(column_index: int, offset_x: float) -> Any: ...
def set_column_width(column_index: int, width: float) -> Any: ...
def begin_tab_bar(identifier: str, flags: Any = 0) -> _BeginEndTabBar: ...
def tab_item_button(label: str, flags: Any = 0) -> Any: ...
def end_drag_drop_source() -> Any: ...
def accept_drag_drop_payload(type: str, flags: Any = 0) -> Any: ...
def get_drag_drop_payload() -> Any: ...
def get_cursor_pos() -> Any: ...
def get_cursor_pos_y() -> Any: ...
def set_cursor_pos_x(x: float) -> Any: ...
def get_cursor_start_pos() -> Any: ...
def get_text_line_height() -> Any: ...
def get_frame_height() -> Any: ...
def create_context(shared_font_atlas: Any = None) -> Any: ...
def get_current_context() -> Any: ...
def push_id(str_id: str) -> Any: ...
def _ansifeed_text_ansi(text: str) -> Any: ...
def _py_font(font: Any) -> Any: ...
def _py_vertex_buffer_vertex_pos_offset() -> Any: ...
def _py_vertex_buffer_vertex_col_offset() -> Any: ...
def _py_index_buffer_index_size() -> Any: ...
def plot_lines(
    label: str,
    values: Any,  # supports buffer interface
    overlay_text: str = '',
    scale_min: float = FLOAT_MAX,
    scale_max: float = FLOAT_MAX,
    graph_size: tuple[float, float] = (0, 0),
    # low-level
    values_count: int = -1,
    values_offset: int = 0,
    stride: int = ...,
): ...

class GlyphRanges:
    pass

class GuiStyle:
    @staticmethod
    def create() -> GuiStyle: ...

    alpha: Any
    window_padding: Any
    window_min_size: Any
    window_rounding: Any
    window_border_size: Any
    child_rounding: Any
    child_border_size: Any
    popup_rounding: Any
    popup_border_size: Any
    window_title_align: Any
    window_menu_button_position: Any
    frame_padding: Any
    frame_rounding: Any
    frame_border_size: Any
    item_spacing: Any
    item_inner_spacing: Any
    cell_padding: Any
    touch_extra_padding: Any
    indent_spacing: Any
    columns_min_spacing: Any
    scrollbar_size: Any
    scrollbar_rounding: Any
    grab_min_size: Any
    grab_rounding: Any
    log_slider_deadzone: Any
    tab_rounding: Any
    tab_border_size: Any
    tab_min_width_for_close_button: Any
    color_button_position: Any
    button_text_align: Any
    selectable_text_align: Any
    display_window_padding: Any
    display_safe_area_padding: Any
    mouse_cursor_scale: Any
    anti_aliased_lines: Any
    anti_aliased_line_use_tex: Any
    anti_aliased_fill: Any
    curve_tessellation_tolerance: Any
    circle_tessellation_max_error: Any
    colors: _Colors

class _CM:
    def __enter__(self) -> t.Self: ...
    def __exit__(self, *_) -> bool: ...

class _BeginEnd(_CM):
    @property
    def expanded(self) -> bool: ...
    @property
    def opened(self) -> bool: ...

class _BeginEndChild(_CM):
    @property
    def visible(self) -> bool: ...

class _BeginEndCombo(_CM):
    @property
    def opened(self) -> bool: ...

class _BeginEndDragDropSource(_CM):
    @property
    def dragging(self) -> bool: ...

class _BeginEndDragDropTarget(_CM):
    @property
    def hovered(self) -> bool: ...

class _BeginEndGroup(_CM):
    pass

class _BeginEndListBox(_CM):
    @property
    def opened(self) -> bool: ...

class _BeginEndMainMenuBar(_CM):
    @property
    def opened(self) -> bool: ...

class _BeginEndMenu(_CM):
    @property
    def opened(self) -> bool: ...

class _BeginEndMenuBar(_CM):
    @property
    def opened(self) -> bool: ...

class _BeginEndPopup(_CM):
    @property
    def opened(self) -> bool: ...

class _BeginEndPopupModal(_CM):
    @property
    def opened(self) -> bool: ...
    @property
    def visible(self) -> bool: ...

class _BeginEndTabBar(_CM):
    @property
    def opened(self) -> bool: ...

class _BeginEndTabItem(_CM):
    @property
    def selected(self) -> bool: ...
    @property
    def opened(self) -> bool: ...

class _BeginEndTable(_CM):
    @property
    def opened(self) -> bool: ...

class _BeginEndTooltip(_CM):
    pass

class _Colors:
    def __getitem__(self, index: int) -> Vec4: ...
    def __setitem__(self, index: int, value: Vec4) -> None: ...

class _DrawCmd:
    def texture_id(self) -> Any: ...
    def elem_count(self) -> Any: ...
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    def clip_rect(self) -> Any: ...

class _DrawData:
    def _require_pointer(self) -> Any: ...
    def deindex_all_buffers(self) -> Any: ...
    def valid(self) -> Any: ...
    def total_vtx_count(self) -> Any: ...
    def display_size(self) -> Any: ...
    def total_idx_count(self) -> Any: ...
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    def scale_clip_rects(self, width, height) -> Any: ...
    def cmd_count(self) -> Any: ...
    def display_pos(self) -> Any: ...
    def frame_buffer_scale(self) -> Any: ...
    def commands_lists(self) -> Any: ...

class _DrawList:
    def cmd_buffer_size(self) -> Any: ...
    def vtx_buffer_size(self) -> Any: ...
    def idx_buffer_size(self) -> Any: ...
    def flags(self) -> Any: ...
    def push_clip_rect(
        self,
        clip_rect_min_x: float,
        clip_rect_min_y: float,
        clip_rect_max_x: float,
        clip_rect_max_y: float,
        intersect_with_current_clip_rect: bool = False,
    ) -> Any: ...
    def push_clip_rect_full_screen(self) -> Any: ...
    def push_texture_id(self, texture_id) -> Any: ...
    def get_clip_rect_min(self) -> Any: ...
    def add_line(
        self,
        start_x: float,
        start_y: float,
        end_x: float,
        end_y: float,
        col: int,
        thickness: float = 1.0,
    ) -> Any: ...
    def add_rect(
        self,
        upper_left_x: float,
        upper_left_y: float,
        lower_right_x: float,
        lower_right_y: float,
        col: int,
        rounding: float = 0.0,
        flags: Any = 0,
        thickness: float = 1.0,
    ) -> Any: ...
    def add_rect_filled(
        self,
        upper_left_x: float,
        upper_left_y: float,
        lower_right_x: float,
        lower_right_y: float,
        col: int,
        rounding: float = 0.0,
        flags: Any = 0,
    ) -> Any: ...
    def add_rect_filled_multicolor(
        self,
        upper_left_x: float,
        upper_left_y: float,
        lower_right_x: float,
        lower_right_y: float,
        col_upr_left: int,
        col_upr_right: int,
        col_bot_right: int,
        col_bot_left: int,
    ) -> Any: ...
    def add_quad(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        point4_x: float,
        point4_y: float,
        col: int,
        thickness: float = 1.0,
    ) -> Any: ...
    def add_quad_filled(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        point4_x: float,
        point4_y: float,
        col: int,
    ) -> Any: ...
    def add_triangle(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        col: int,
        thickness: float = 1.0,
    ) -> Any: ...
    def add_triangle_filled(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        col: int,
    ) -> Any: ...
    def add_bezier_cubic(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        point4_x: float,
        point4_y: float,
        col: int,
        thickness: float,
        num_segments: int = 0,
    ) -> Any: ...
    def add_bezier_quadratic(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        point3_x: float,
        point3_y: float,
        col: int,
        thickness: float,
        num_segments: int = 0,
    ) -> Any: ...
    def add_circle(
        self,
        centre_x: float,
        centre_y: float,
        radius: float,
        col: int,
        num_segments: int = 0,
        thickness: float = 1.0,
    ) -> Any: ...
    def add_circle_filled(
        self, centre_x: float, centre_y: float, radius: float, col: int, num_segments: int = 0
    ) -> Any: ...
    def add_ngon(
        self,
        centre_x: float,
        centre_y: float,
        radius: float,
        col: int,
        num_segments: int,
        thickness: float = 1.0,
    ) -> Any: ...
    def add_ngon_filled(
        self, centre_x: float, centre_y: float, radius: float, col: int, num_segments: int
    ) -> Any: ...
    def add_text(self, pos_x: float, pos_y: float, col: int, text: str) -> Any: ...
    def add_image(
        self,
        texture_id,
        a: Any,
        b: Any,
        uv_a: Any = (0, 0),
        uv_b: Any = (1, 1),
        col: int = 0xFFFFFFFF,
    ) -> Any: ...
    def add_image_rounded(
        self,
        texture_id,
        a: Any,
        b: Any,
        uv_a: Any = (0, 0),
        uv_b: Any = (1, 1),
        col: int = 0xFFFFFFFF,
        rounding: float = 0.0,
        flags: Any = 0,
    ) -> Any: ...
    def add_polyline(
        self, points: Any, col: int, flags: Any = 0, thickness: float = 1.0
    ) -> Any: ...
    def path_clear(self) -> Any: ...
    def path_arc_to(
        self,
        center_x: float,
        center_y: float,
        radius: float,
        a_min: float,
        a_max: float,
        num_segments: int = 0,
    ) -> Any: ...
    def path_arc_to_fast(
        self,
        center_x: float,
        center_y: float,
        radius: float,
        a_min_of_12: int,
        a_max_of_12: int,
    ) -> Any: ...
    def path_rect(
        self,
        point1_x: float,
        point1_y: float,
        point2_x: float,
        point2_y: float,
        rounding: float = 0.0,
        flags: Any = 0,
    ) -> Any: ...
    def path_fill_convex(self, col: int) -> Any: ...
    def channels_split(self, channels_count: int) -> Any: ...
    def channels_merge(self) -> Any: ...
    def prim_unreserve(self, idx_count: int, vtx_count: int) -> Any: ...
    def prim_write_vtx(
        self, pos_x: float, pos_y: float, u: float, v: float, color: int = 0xFFFFFFFF
    ) -> Any: ...
    def prim_vtx(
        self, pos_x: float, pos_y: float, u: float, v: float, color: int = 0xFFFFFFFF
    ) -> Any: ...
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    def cmd_buffer_data(self) -> Any: ...
    def vtx_buffer_data(self) -> Any: ...
    def idx_buffer_data(self) -> Any: ...
    def pop_texture_id(self) -> Any: ...
    def get_clip_rect_max(self) -> Any: ...
    def path_line_to(self, x: float, y: float) -> Any: ...
    def channels_set_current(self, idx: int) -> Any: ...
    def prim_reserve(self, idx_count: int, vtx_count: int) -> Any: ...
    def prim_rect(
        self, a_x: float, a_y: float, b_x: float, b_y: float, color: int = 0xFFFFFFFF
    ) -> Any: ...
    def prim_write_idx(self, idx: Any) -> Any: ...
    def commands(self) -> Any: ...

class _Font: ...

class _FontAtlas:
    def _require_pointer(self) -> Any: ...
    def add_font_from_file_ttf(
        self, filename: str, size_pixels: float, font_config: Any = None, glyph_ranges: Any = None
    ) -> _Font: ...
    def clear_tex_data(self) -> Any: ...
    def clear_fonts(self) -> Any: ...
    def get_glyph_ranges_default(self) -> Any: ...
    def get_glyph_ranges_japanese(self) -> Any: ...
    def get_glyph_ranges_chinese(self) -> Any: ...
    def get_glyph_ranges_thai(self) -> Any: ...
    def get_glyph_ranges_latin(self) -> Any: ...
    def get_tex_data_as_rgba32(self) -> Any: ...

    texture_id: int  # usually an integer
    texture_width: int
    texture_desired_width: int
    texture_height: int

    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    def add_font_default(self) -> Any: ...
    def clear_input_data(self) -> Any: ...
    def clear(self) -> Any: ...
    def get_glyph_ranges_korean(self) -> Any: ...
    def get_glyph_ranges_chinese_full(self) -> Any: ...
    def get_glyph_ranges_cyrillic(self) -> Any: ...
    def get_glyph_ranges_vietnamese(self) -> Any: ...
    def get_tex_data_as_alpha8(self) -> Any: ...

class _IO:
    backend_flags: int
    config_cursor_blink: bool
    config_drag_click_to_input_text: bool
    config_flags: int
    config_mac_osx_behaviors: bool
    config_memory_compact_timer: float
    config_windows_move_from_title_bar_only: bool
    config_windows_resize_from_edges: bool
    delta_time: float
    display_fb_scale: Vec2
    display_size: Vec2
    font_allow_user_scaling: bool
    font_global_scale: float
    fonts: _FontAtlas
    framerate: float
    ini_file_name: str
    ini_saving_rate: float
    key_alt: bool
    key_ctrl: bool
    key_repeat_delay: float
    key_repeat_rate: float
    key_shift: bool
    key_super: bool
    keys_down: Any
    log_file_name: str
    metrics_active_allocations: int
    metrics_active_windows: int
    metrics_render_indices: int
    metrics_render_vertices: int
    metrics_render_windows: int
    mouse_delta: Vec2
    mouse_double_click_max_distance: float
    mouse_double_click_time: float
    mouse_down: bool
    mouse_drag_threshold: float
    mouse_draw_cursor: Any
    mouse_pos: Vec2
    mouse_wheel: float
    mouse_wheel_horizontal: float
    nav_active: bool
    nav_inputs: Any
    nav_visible: bool
    want_capture_keyboard: bool
    want_capture_mouse: bool
    want_save_ini_settings: bool
    want_set_mouse_pos: bool
    want_text_input: bool
    def add_input_character(self, c: int) -> Any: ...
    def add_input_character_utf16(self, utf16_chars: str) -> Any: ...
    def add_input_characters_utf8(self, utf8_chars: str) -> Any: ...
    def clear_input_characters(self) -> int: ...
    def get_clipboard_text_fn(self) -> Any: ...
    def key_map(self) -> Any: ...
    def populate(self, callback_fn, user_data) -> Any: ...
    def set_clipboard_text_fn(self) -> Any: ...
    def set_text_input_buffer(
        self, text_input_buffer: Any, text_input_buffer_size: int
    ) -> Any: ...

class _ImGuiContext:
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...

class _ImGuiInputTextCallbackData:
    def _require_pointer(self) -> Any: ...
    def flags(self) -> Any: ...
    def event_char(self) -> Any: ...
    def event_key(self) -> Any: ...
    def buffer(self, buffer: str) -> Any: ...
    def buffer_size(self) -> Any: ...
    def buffer_dirty(self, dirty: bool) -> Any: ...
    def cursor_pos(self, pos: int) -> Any: ...
    def selection_start(self, start: int) -> Any: ...
    def selection_end(self, end: int) -> Any: ...
    def insert_chars(self, pos: int, text: str) -> Any: ...
    def clear_selection(self) -> Any: ...
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    def event_flag(self) -> Any: ...
    def user_data(self) -> Any: ...
    def buffer_text_length(self) -> Any: ...
    def delete_chars(self, pos: int, bytes_count: int) -> Any: ...
    def select_all(self) -> Any: ...
    def has_selection(self) -> Any: ...

class _ImGuiSizeCallbackData:
    def _require_pointer(self) -> Any: ...
    def pos(self) -> Any: ...
    def desired_size(self) -> Any: ...
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    def user_data(self) -> Any: ...
    def current_size(self) -> Any: ...

class _ImGuiTableColumnSortSpecs:
    def column_user_id(self) -> Any: ...
    def column_index(self) -> Any: ...
    def sort_order(self) -> Any: ...
    def sort_direction(self) -> Any: ...
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    def _get_item(self, idx: Any) -> Any: ...

class _ImGuiTableColumnSortSpecs_array:
    pass

class _ImGuiTableSortSpecs:
    def specs(self) -> Any: ...
    def specs_dirty(self) -> Any: ...
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    def specs_count(self) -> Any: ...

class _ImGuiViewport:
    def flags(self) -> Any: ...
    def size(self) -> Any: ...
    def work_size(self) -> Any: ...
    def get_work_center(self) -> Any: ...
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...
    def work_pos(self) -> Any: ...
    def get_center(self) -> Any: ...

class _InputTextSharedBuffer:
    def reserve_memory(self, buffer_size: int) -> Any: ...
    def free_memory(self) -> Any: ...

class _StaticGlyphRanges:
    @classmethod
    def from_ptr(cls, ptr: Any) -> t.Self: ...

class _callback_user_info:
    pass

class FontConfig:
    def __init__(
        self,
        font_no=None,
        size_pixels=None,
        oversample_h=None,
        oversample_v=None,
        pixel_snap_h=None,
        glyph_extra_spacing_x=None,
        glyph_extra_spacing_y=None,
        glyph_offset_x=None,
        glyph_offset_y=None,
        glyph_min_advance_x=None,
        glyph_max_advance_x=None,
        merge_mode=None,
        font_builder_flags=None,
        rasterizer_multiply=None,
        ellipsis_char=None,
    ): ...
