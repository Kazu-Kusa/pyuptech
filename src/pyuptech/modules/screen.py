from enum import Enum
from typing import Literal

from .constant import LIB_FILE_PATH
from .loader import load_lib


class Font(Enum):
    FONT_4X6 = 0
    FONT_5X8 = 1
    FONT_5X12 = 2
    FONT_6X8 = 3
    FONT_6X10 = 4
    FONT_7X12 = 5
    FONT_8X8 = 6
    FONT_8X12 = 7
    FONT_8X14 = 8
    FONT_10X16 = 9
    FONT_12X16 = 10
    FONT_12X20 = 11
    FONT_16X26 = 12
    FONT_22X36 = 13
    FONT_24X40 = 14


class Color(Enum):
    COLOR_WHITE = 0xFFFF
    COLOR_BLACK = 0x0000
    COLOR_BLUE = 0x001F
    COLOR_BRED = 0xF81F
    COLOR_GRED = 0xFFE0
    COLOR_GBLUE = 0x07FF
    COLOR_RED = 0xF800
    COLOR_MAGENTA = 0xF81F
    COLOR_GREEN = 0x07E0
    COLOR_CYAN = 0x7FFF
    COLOR_YELLOW = 0xFFE0
    COLOR_BROWN = 0xBC40
    COLOR_BRRED = 0xFC07
    COLOR_GRAY = 0x8430
    COLOR_DARKBLUE = 0x01CF
    COLOR_LIGHTBLUE = 0x7D7C
    COLOR_GRAYBLUE = 0x5458
    COLOR_LIGHTGREEN = 0x841F
    COLOR_LGRAY = 0xC618
    COLOR_LGRAYBLUE = 0xA651
    COLOR_LBBLUE = 0x2B12


class Screen(object):
    """
    Screen module
    """

    lib = load_lib(LIB_FILE_PATH)

    def __init__(self, init_screen: bool = True):
        if init_screen:
            Screen.open()
            Screen.fill_screen(Color.COLOR_BLACK)
            Screen.refresh()

    @staticmethod
    def open(direction: Literal[1, 2] = 2):
        """
        open with lcd ,and set the LCD displaying direction

        1 for vertical, 2 for horizontal
        """

        return Screen.lib.lcd_open(direction)

    @staticmethod
    def refresh():
        """
        refresh the screen, print the display data in the cache on the screen
        """
        Screen.lib.LCD_Refresh()

    @staticmethod
    def set_font_size(font_size: Font):
        Screen.lib.LCD_SetFont(font_size.value)

    @staticmethod
    def set_fore_color(color: Color):
        """
        set the fore color
        """
        Screen.lib.UG_SetForecolor(color)

    @staticmethod
    def set_back_color(color: Color):
        """
        set the LCD background color
        """
        Screen.lib.UG_SetBackcolor(color)

    @staticmethod
    def set_led_color(index: int, color: Color):
        """
        set the color of the LED according to index and color
        """
        Screen.lib.adc_led_set(index, color.value)

    @staticmethod
    def fill_screen(color: Color):
        """
        fill the screen with the given color
        """
        Screen.lib.UG_FillScreen(color)

    @staticmethod
    def put_string(x: int, y: int, display_string: str):
        """
        x,y(unit:pixel) are the coordinates of where the string that will be displayed

        display_string is  string that will be displayed in the LCD

        """
        Screen.lib.UG_PutString(x, y, display_string.encode())

    @staticmethod
    def fill_frame(x1, y1, x2, y2, color: Color):
        Screen.lib.UG_FillFrame(x1, y1, x2, y2, color.value)

    @staticmethod
    def fill_round_frame(x1, y1, x2, y2, r, color: Color):
        Screen.lib.UG_FillRoundFrame(x1, y1, x2, y2, r, color.value)

    @staticmethod
    def fill_circle(x0, y0, r, color: Color):
        Screen.lib.UG_FillCircle(x0, y0, r, color.value)

    @staticmethod
    def draw_mesh(x1, y1, x2, y2, color: Color):
        Screen.lib.UG_DrawMesh(x1, y1, x2, y2, color.value)

    @staticmethod
    def draw_frame(x1, y1, x2, y2, color: Color):
        Screen.lib.UG_DrawFrame(x1, y1, x2, y2, color.value)

    @staticmethod
    def draw_round_frame(x1, y1, x2, y2, r, color: Color):
        Screen.lib.UG_DrawRoundFrame(x1, y1, x2, y2, r, color.value)

    @staticmethod
    def draw_pixel(x0, y0, color: Color):
        Screen.lib.UG_DrawPixel(x0, y0, color.value)

    @staticmethod
    def draw_circle(x0, y0, r, color: Color):
        Screen.lib.UG_DrawCircle(x0, y0, r, color.value)

    @staticmethod
    def draw_arc(x0: int, y0: int, r, s, color: Color):
        Screen.lib.UG_DrawArc(x0, y0, r, s, color.value)

    @staticmethod
    def draw_line(x1: int, y1: int, x2: int, y2: int, color: Color):
        Screen.lib.UG_DrawLine(x1, y1, x2, y2, color.value)


if __name__ == "__main__":
    pass
