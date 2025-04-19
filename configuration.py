import os
from io import TextIOWrapper
from json import load, dump, JSONDecodeError

try:
    from curses import (
        wrapper, error, curs_set, baudrate, start_color, init_pair, use_default_colors, color_pair, A_BOLD,
        COLOR_BLACK, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN, COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW
    )
except ModuleNotFoundError:
    print('\nFor the program to work, you need to install the curses module!\n')

directories: tuple[str, str] = ('config_files', 'icons')
for directory in directories:
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass


class Configuration:
    """The Configuration class is used for reading and managing configuration settings from a JSON file."""

    matrix_config: dict[str, dict[str, bool | str] | dict[str, bool | str | int]] = {
        "neo": {
            "enable": True, "neo_color": "GREEN", "sentence_first": "Wake up, Neo...",
            "sentence_second": "The Matrix has you...", "sentence_third": "Follow the white rabbit.",
            "sentence_fourth": "Knock, knock, Neo."
        },
        "matrix": {
            "enable": True, "matrix_color": "GREEN", "cycle_number": 10000000, "threads_rate": 35,
            "bold_symbols_rate": 8, "min_speed": 2, "max_speed": 6, "void_rate": 2, "digits": True,
            "symbols": True, "currencies": True, "greek": True, "latin": True, "cyrillic": True, "chinese": True
        },
        "info": {
            "enable": False, "info_color": "MAGENTA"
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
    def get_json_data(config_name: str) -> dict[str, dict[str, str | bool | int]]:
        """
        The method reads a JSON configuration file.
        :param config_name: Name of the configuration file (without .json extension).
        """
        with open(f'config_files/{config_name}.json', encoding='UTF-8') as read_file:
            data: dict[str, dict[str, str | bool | int]] = load(read_file)
        return data

    def get_config_data(self, config_name: str) -> dict[str, dict[str, str | bool | int]] | None:
        """
        The method tries to read the configuration file and, if it fails, overwrites it.

        :param config_name: The name of the configuration file (no .json extension).
        :return dict: The configuration data loaded from the JSON file.
        """
        try:
            return self.get_json_data(config_name)
        except FileNotFoundError:
            self.write_json_data(config_name, self.matrix_config)
            return self.matrix_config
        except JSONDecodeError:
            print(f'\nJSONDecodeError! File "{config_name}.json" is corrupted or not a valid JSON!')
            return None
        except OSError as e:
            print(f'\nOSError! Failed to read file "{config_name}.json" due to {e}.')
            return None

    __slots__ = (
        'variables', 'neo', 'neo_enable', 'neo_color', 'sentence_first', 'sentence_second', 'sentence_third',
        'sentence_fourth', 'matrix', 'matrix_enable', 'matrix_color', 'cycle_number', 'threads_rate',
        'bold_symbols_rate', 'min_speed', 'max_speed', 'void_rate', 'digits', 'symbols', 'currencies',
        'greek', 'latin', 'cyrillic', 'chinese', 'info', 'info_enable', 'info_color'
    )

    def __init__(self):
        self.variables: dict[str, dict[str, str | bool | int]] = self.get_config_data('matrix_config')
        try:
            self.neo: dict[str, str | bool | int] = self.variables['neo']
            self.neo_enable: str | bool | int = self.neo['enable']
            self.neo_color: str | bool | int = self.neo['neo_color']
            self.sentence_first: str | bool | int = self.neo['sentence_first']
            self.sentence_second: str | bool | int = self.neo['sentence_second']
            self.sentence_third: str | bool | int = self.neo['sentence_third']
            self.sentence_fourth: str | bool | int = self.neo['sentence_fourth']
            self.matrix: dict[str, str | bool | int] = self.variables['matrix']
            self.matrix_enable: str | bool | int = self.matrix['enable']
            self.matrix_color: str | bool | int = self.matrix['matrix_color']
            self.cycle_number: str | bool | int = self.matrix['cycle_number']
            self.threads_rate: str | bool | int = self.matrix['threads_rate']
            self.bold_symbols_rate: str | bool | int = self.matrix['bold_symbols_rate']
            self.min_speed: str | bool | int = self.matrix['min_speed']
            self.max_speed: str | bool | int = self.matrix['max_speed']
            self.void_rate: str | bool | int = self.matrix['void_rate']
            self.digits: str | bool | int = self.matrix['digits']
            self.symbols: str | bool | int = self.matrix['symbols']
            self.currencies: str | bool | int = self.matrix['currencies']
            self.greek: str | bool | int = self.matrix['greek']
            self.latin: str | bool | int = self.matrix['latin']
            self.cyrillic: str | bool | int = self.matrix['cyrillic']
            self.chinese: str | bool | int = self.matrix['chinese']
            self.info: dict[str, str | bool | int] = self.variables['info']
            self.info_enable: str | bool | int = self.info['enable']
            self.info_color: str | bool | int = self.info['info_color']
        except TypeError:
            print('\nTypeError! Variables can\'t be initialized!')
