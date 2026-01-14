from .configuration import (
    Configuration, init_pair, use_default_colors, color_pair, A_BOLD, COLOR_BLACK,
    COLOR_BLUE, COLOR_CYAN, COLOR_GREEN, COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW
)


class Base(Configuration):
    @staticmethod
    def verify_color(color) -> object | int:
        """
        The method checks the color setting from the configuration.
        :return: COLOR_*: The color constant corresponding to the color configuration.
        """
        color_map: dict[str, int] = {
            'BLACK': COLOR_BLACK, 'BLUE': COLOR_BLUE, 'CYAN': COLOR_CYAN, 'GREEN': COLOR_GREEN,
            'MAGENTA': COLOR_MAGENTA, 'RED': COLOR_RED, 'WHITE': COLOR_WHITE, 'YELLOW': COLOR_YELLOW,
        }
        return color_map.get(color, COLOR_WHITE)

    def paint(self, color: str, a_bold: bool) -> int:
        """
        Method colors text or text image.

        :param color: The color of the image.
        :param a_bold: A bold symbol true or false

        :return: Color_pair object.
        :raises KeyError: If the specified color is not found in the color dictionary.
        """
        colors_dict: dict[str, int] = {
            'MAGENTA': 1, 'BLUE': 2, 'CYAN': 3, 'GREEN': 4,
            'YELLOW': 5, 'RED': 6, 'WHITE': 7, 'BLACK': 8
        }
        if color not in colors_dict:
            raise KeyError(f'Цвет "{color}" не найден в доступных цветах.')
        for i, color_name in enumerate(colors_dict.keys()):
            use_default_colors()
            init_pair(1 + i, self.verify_color(color_name), -1)
        if a_bold:
            return color_pair(colors_dict[color]) | A_BOLD
        return color_pair(colors_dict[color])
