from enum import Enum
from typing import Literal, Self

from .constant import LIB_FILE_PATH
from .loader import load_lib
from .logger import _logger


class FontSize(Enum):
    """
    All supported font size enum
    """

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
    """
    All supported color display on the led/lcd
    """

    @staticmethod
    def new_color(r: int, g: int, b: int) -> int:
        """
        Generates a new color value based on the specified red, green, and blue components.

        Parameters:
        r (int): The red component of the color, between 0 and 255.
        g (int): The green component of the color, between 0 and 255.
        b (int): The blue component of the color, between 0 and 255.

        Returns:
        int: A 24-bit color value, with 8 bits for each red, green, and blue component.

        Raises:
        ValueError: If any color component is outside the range of 0 to 255.
        """
        # Validate that each color component is within the acceptable range
        if any([c < 0 or c > 255 for c in (r, g, b)]):
            raise ValueError("Color value must be between 0 and 255")

        # Combine the red, green, and blue components into a single 24-bit color value
        return (r << 16) + (g << 8) + b

    WHITE = new_color(255, 255, 255)
    GRAY = new_color(128, 128, 128)
    BLACK = new_color(0, 0, 0)

    RED = new_color(255, 0, 0)
    GREEN = new_color(0, 255, 0)
    BLUE = new_color(0, 0, 255)

    B_RED = new_color(255, 0, 128)
    G_RED = new_color(255, 128, 0)

    G_BLUE = new_color(0, 128, 255)
    R_BLUE = new_color(128, 0, 255)

    R_GREEN = new_color(128, 255, 0)
    B_GREEN = new_color(0, 255, 128)

    YELLOW = new_color(255, 255, 0)
    MAGENTA = new_color(255, 0, 255)
    CYAN = new_color(0, 255, 255)

    ORANGE = new_color(128, 128, 0)
    PURPLE = new_color(128, 0, 128)
    BLUEGREEN = new_color(0, 128, 128)

    DARKBLUE = new_color(0, 0, 139)
    DARKGREEN = new_color(0, 139, 0)
    DARKRED = new_color(139, 0, 0)


class Screen:
    """
    Screen module

    This class represents an LCD screen and provides methods to manipulate it.
    Each method returns self to enable chainable calls.
    """

    lib = load_lib(LIB_FILE_PATH)

    def __init__(self, screen_dir: Literal[1, 2] | int = None):
        """
        Initializes the Screen class.

        Parameters:
            screen_dir (Literal[1, 2], optional): The direction to open the screen in. Defaults to None.

        Returns:
            None
        """

        if screen_dir is not None:
            self.open(direction=screen_dir).fill_screen(Color.BLACK).refresh()

    def open(self, direction: Literal[1, 2] | int = 2) -> Self:
        """
        Open the LCD and set the displaying direction.

        Args:
          direction (Literal[1, 2]): Display direction; 1 for vertical, 2 for horizontal.

        Returns:
          Self for chainable calls.
        """

        _logger.info(f"Open LCD with direction: {direction}")
        self.lib.lcd_open(direction)
        return self

    def close(self) -> Self:
        """
        Close the LCD.

        Returns:
          Self for chainable calls.
        """
        _logger.info("Closing LCD")
        self.lib.lcd_close()
        return self

    def refresh(self) -> Self:
        """
        Refresh the screen, printing the display data from the cache onto the screen.

        Returns:
          Self for chainable calls.
        """
        self.lib.LCD_Refresh()
        return self

    def set_font_size(self, font_size: FontSize) -> Self:
        """
        Set the font size.

        Args:
          font_size (FontSize): The desired font size.

        Returns:
          Self for chainable calls.
        """
        self.lib.LCD_SetFont(font_size.value)
        return self

    def set_fore_color(self, color: Color) -> Self:
        """
        Set the foreground color.

        Args:
          color (Color): The desired foreground color.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_SetForecolor(color)
        return self

    def set_back_color(self, color: Color) -> Self:
        """
        Set the background color of the LCD.

        Args:
          color (Color): The desired background color.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_SetBackcolor(color)
        return self

    def set_led_color(self, index: Literal[0, 1] | int, color: Color) -> Self:
        """
        Set the LED color at a specific index.

        Parameters:
            index (Literal[0, 1]): The index of the LED to set the color for.
            color (Color): The color to set for the LED.

        Returns:
            Self: The instance of the class to allow for method chaining.
        """
        self.lib.adc_led_set(index, color.value)
        return self

    def set_led_0(self, color: Color) -> Self:
        self.lib.adc_led_set(0, color.value)
        return self

    def set_led_1(self, color: Color) -> Self:
        self.lib.adc_led_set(1, color.value)
        return self

    def set_led_hex(self, index: int, color: int) -> Self:
        self.lib.adc_led_set(index, color)
        return self

    def fill_screen(self, color: Color) -> Self:
        """
        Fill the entire screen with the specified color.

        Args:
          color (Color): The color to fill the screen with.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_FillScreen(color.value)
        return self

    def put_string(self, x: int, y: int, display_string: str) -> Self:
        """
        Place a string at specific coordinates on the LCD.

        Args:
          x (int): X coordinate (in pixels).
          y (int): Y coordinate (in pixels).
          display_string (str): The string to display on the LCD.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_PutString(x, y, display_string)
        return self

    def fill_frame(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> Self:
        """
        Fill a rectangular frame with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          color (Color): The color to fill the frame with.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_FillFrame(x1, y1, x2, y2, color.value)
        return self

    def fill_round_frame(
        self, x1: int, y1: int, x2: int, y2: int, r: int, color: Color
    ) -> Self:
        """
        Fill a rounded rectangular frame with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          r (int): The radius of the corners.
          color (Color): The color to fill the round frame with.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_FillRoundFrame(x1, y1, x2, y2, r, color.value)
        return self

    def fill_circle(self, x0: int, y0: int, r: int, color: Color) -> Self:
        """
        Fill a circle with the specified color.

        Args:
          x0 (int): The X coordinate of the circle center.
          y0 (int): The Y coordinate of the circle center.
          r (int): The radius of the circle.
          color (Color): The color to fill the circle with.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_FillCircle(x0, y0, r, color.value)
        return self

    def draw_mesh(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> Self:
        """
        Draw a mesh pattern within a rectangle with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          color (Color): The color of the mesh lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawMesh(x1, y1, x2, y2, color.value)
        return self

    def draw_frame(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> Self:
        """
        Draw an empty rectangular frame with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          color (Color): The color of the frame lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawFrame(x1, y1, x2, y2, color.value)
        return self

    def draw_round_frame(
        self, x1: int, y1: int, x2: int, y2: int, r: int, color: Color
    ) -> Self:
        """
        Draw an empty rounded rectangular frame with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          r (int): The radius of the corners.
          color (Color): The color of the frame lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawRoundFrame(x1, y1, x2, y2, r, color.value)
        return self

    def draw_pixel(self, x0: int, y0: int, color: Color) -> Self:
        """
        Draw a single pixel at the specified coordinates with the specified color.

        Args:
          x0 (int): The X coordinate of the pixel.
          y0 (int): The Y coordinate of the pixel.
          color (Color): The color of the pixel.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawPixel(x0, y0, color.value)
        return self

    def draw_circle(self, x0: int, y0: int, r: int, color: Color) -> Self:
        """
        Draw an empty circle with the specified color.

        Args:
          x0 (int): The X coordinate of the circle center.
          y0 (int): The Y coordinate of the circle center.
          r (int): The radius of the circle.
          color (Color): The color of the circle lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawCircle(x0, y0, r, color.value)
        return self

    def draw_arc(self, x0: int, y0: int, r: int, s: int, color: Color) -> Self:
        """
        Draw an arc with the specified color.

        Args:
          x0 (int): The X coordinate of the circle center.
          y0 (int): The Y coordinate of the circle center.
          r (int): The radius of the arc circle.
          s (int): The starting angle of the arc.
          color (Color): The color of the arc lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawArc(x0, y0, r, s, color.value)
        return self

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> Self:
        """
        Draw a line between two points with the specified color.

        Args:
          x1 (int): The X coordinate of the first point.
          y1 (int): The Y coordinate of the first point.
          x2 (int): The X coordinate of the second point.
          y2 (int): The Y coordinate of the second point.
          color (Color): The color of the line.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawLine(x1, y1, x2, y2, color.value)
        return self


if __name__ == "__main__":
    pass
