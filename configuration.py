from io import TextIOWrapper
from json import load, dump
from typing import Dict

try:
    from curses import (
        wrapper, error, curs_set, baudrate, start_color, init_pair, use_default_colors, color_pair, A_BOLD,
        COLOR_BLACK, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN, COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW
    )
except ModuleNotFoundError:
    print('\nFor Windows you must install the requirements_for_windows.txt file!\n')


class Configuration:
    """
    The Configuration class is used for reading and managing configuration settings from a JSON file.
    It sets various properties such as color, matrix parameters, and Neo-related sentences to be displayed.
    """
    json_data = {
        "info": False, "color": "GREEN", "neo": {
            "enable": True, "sentence_first": "Wake up, Neo...", "sentence_second": "The Matrix has you...",
            "sentence_third": "Follow the white rabbit.", "sentence_fourth": "Knock, knock, Neo."
        },
        "matrix": {
            "enable": True, "cycle_number": 10000000, "threads_rate": 60, "bold_symbols_rate": 9, "min_speed": 2,
            "max_speed": 8, "void_rate": 3, "digits": True, "symbols": True, "currencies": True, "greek": True,
            "latin": True, "cyrillic": True, "chinese": True}
    }

    @classmethod
    def get_json_data(cls, config_name: str) -> Dict:
        """
        The method reads the JSON configuration file.
        If the specified JSON file does not exist, it creates a new file with default configurations.
        :param config_name: The name of the configuration file (without the .json extension).
        :return Dict: The configuration data loaded from the JSON file.
        """
        try:
            with open(f'{config_name}.json') as read_file:
                data = load(read_file)
            return data
        except FileNotFoundError:
            print(f'\nFileNotFoundError! File {config_name}.json not found!')
            try:
                with open(f'{config_name}.json', 'w', encoding='UTF-8') as write_file:
                    if isinstance(write_file, TextIOWrapper):
                        dump(cls.json_data, write_file)
                    else:
                        raise TypeError("Expected TextIOWrapper for the file type")
                print(f'\nThe file {config_name}.json was successfully created!')
            except OSError as e:
                print(f'\nFailed to create file {config_name}.json due to {e}')
            return cls.json_data

    __slots__ = (
        'variables', 'info', 'color', 'neo', 'neo_enable', 'sentence_first', 'sentence_second', 'sentence_third',
        'sentence_fourth', 'matrix', 'matrix_enable', 'cycle_number', 'threads_rate', 'bold_symbols_rate', 'min_speed',
        'max_speed', 'void_rate', 'digits', 'symbols', 'currencies', 'greek', 'latin', 'cyrillic', 'chinese'
    )

    def __init__(self):
        """
        Initializes the Configuration object.
        Loads the configuration from the JSON file and sets the instance variables accordingly.
        """
        self.variables = self.get_json_data('matrix_config')
        try:
            self.info = self.variables['info']
            self.color = self.variables['color']
            self.neo = self.variables['neo']
            self.neo_enable = self.neo['enable']
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

    def verify_color(self):
        """
        Verifies the color setting from the configuration.
        :return: COLOR_*: The color constant that matches the color configuration.
        """
        dictionary = {
            'BLACK': lambda: COLOR_BLACK, 'BLUE': lambda: COLOR_BLUE,
            'CYAN': lambda: COLOR_CYAN, 'GREEN': lambda: COLOR_GREEN,
            'MAGENTA': lambda: COLOR_MAGENTA, 'RED': lambda: COLOR_RED,
            'WHITE': lambda: COLOR_WHITE, 'YELLOW': lambda: COLOR_YELLOW,
        }[self.color]
        return dictionary()
