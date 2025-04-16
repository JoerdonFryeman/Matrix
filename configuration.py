import os
from io import TextIOWrapper
from json import load, dump, JSONDecodeError

try:
    from curses import (
        wrapper, error, curs_set, baudrate, start_color, init_pair, use_default_colors, color_pair, A_BOLD,
        COLOR_BLACK, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN, COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW
    )
except ModuleNotFoundError:
    print('\nДля работы программы необходимо установить модуль curses!\n')

directories = ('config_files', 'icons')
for directory in directories:
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass


class Configuration:
    """The Configuration class is used for reading and managing configuration settings from a JSON file."""

    matrix_config = {
        "info": False, "color": "GREEN", "info_color": "MAGENTA", "neo": {
            "enable": True, "neo_color": "GREEN", "sentence_first": "Wake up, Neo...",
            "sentence_second": "The Matrix has you...", "sentence_third": "Follow the white rabbit.",
            "sentence_fourth": "Knock, knock, Neo."
        },
        "matrix": {
            "enable": True, "cycle_number": 10000000, "threads_rate": 35, "bold_symbols_rate": 8, "min_speed": 2,
            "max_speed": 6, "void_rate": 2, "digits": True, "symbols": True, "currencies": True, "greek": True,
            "latin": True, "cyrillic": True, "chinese": True
        }
    }

    @staticmethod
    def write_json_data(config_name: str, json_data: dict) -> None:
        """
        The method creates a new default configuration file if the specified JSON file does not exist.

        :param config_name: Name of the configuration file (without .json extension).
        :param json_data: The data to be written as a dictionary.
        """
        try:
            with open(f'config_files/{config_name}.json', 'x', encoding='UTF-8') as write_file:
                assert isinstance(write_file, TextIOWrapper)
                dump(json_data, write_file, ensure_ascii=False, indent=4)
        except FileExistsError:
            pass
        except OSError as e:
            print(f'\nFailed to create file "{config_name}.json" due to {e}')

    @staticmethod
    def get_json_data(config_name: str):
        """
        The method reads a JSON configuration file.
        :param config_name: Name of the configuration file (without .json extension).
        """
        with open(f'config_files/{config_name}.json', encoding='UTF-8') as read_file:
            data = load(read_file)
        return data

    def get_config_data(self, config_name: str) -> dict | None:
        """
        The method tries to read the configuration file and, if it fails, overwrites it.

        :param config_name: The name of the configuration file (no .json extension).
        :return dict: The configuration data loaded from the JSON file.
        """
        try:
            return self.get_json_data(config_name)
        except FileNotFoundError:
            print(f'\nFileNotFoundError! File {config_name}.json not found!')
            self.write_json_data(config_name, self.matrix_config)
            return self.matrix_config
        except JSONDecodeError:
            print(f'\nJSONDecodeError! File "{config_name}.json" is corrupted or not a valid JSON!')
        except OSError as e:
            print(f'\nOSError! Failed to read file "{config_name}.json" due to {e}.')

    __slots__ = (
        'variables', 'info', 'color', 'info_color', 'neo', 'neo_enable', 'neo_color', 'sentence_first',
        'sentence_second', 'sentence_third', 'sentence_fourth', 'matrix', 'matrix_enable', 'cycle_number',
        'threads_rate', 'bold_symbols_rate', 'min_speed', 'max_speed', 'void_rate', 'digits', 'symbols',
        'currencies', 'greek', 'latin', 'cyrillic', 'chinese'
    )

    def __init__(self):
        self.variables = self.get_json_data('matrix_config')
        try:
            self.info = self.variables['info']
            self.color = self.variables['color']
            self.info_color = self.variables['info_color']
            self.neo = self.variables['neo']
            self.neo_enable = self.neo['enable']
            self.neo_color = self.neo['neo_color']
            self.sentence_first = self.neo['sentence_first']
            self.sentence_second = self.neo['sentence_second']
            self.sentence_third = self.neo['sentence_third']
            self.sentence_fourth = self.neo['sentence_fourth']
            self.matrix = self.variables['matrix']
            self.matrix_enable = self.matrix['enable']
            self.cycle_number = self.matrix['cycle_number']
            self.threads_rate = self.matrix['threads_rate']
            self.bold_symbols_rate = self.matrix['bold_symbols_rate']
            self.min_speed = self.matrix['min_speed']
            self.max_speed = self.matrix['max_speed']
            self.void_rate = self.matrix['void_rate']
            self.digits = self.matrix['digits']
            self.symbols = self.matrix['symbols']
            self.currencies = self.matrix['currencies']
            self.greek = self.matrix['greek']
            self.latin = self.matrix['latin']
            self.cyrillic = self.matrix['cyrillic']
            self.chinese = self.matrix['chinese']
        except TypeError:
            print('\nTypeError! Variables can\'t be initialized!')

    @staticmethod
    def verify_color(color):
        """
        The method checks the color setting from the configuration.
        :return: COLOR_*: The color constant corresponding to the color configuration.
        """
        color_map = {
            'BLACK': COLOR_BLACK, 'BLUE': COLOR_BLUE, 'CYAN': COLOR_CYAN, 'GREEN': COLOR_GREEN,
            'MAGENTA': COLOR_MAGENTA, 'RED': COLOR_RED, 'WHITE': COLOR_WHITE, 'YELLOW': COLOR_YELLOW,
        }
        return color_map.get(color, COLOR_WHITE)

    def paint(self, color: str, a_bold: bool) -> object:
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
