import os
from json import load, dump, JSONDecodeError

try:
    from curses import (
        wrapper, error, curs_set, baudrate, start_color, init_pair, use_default_colors, color_pair, A_BOLD,
        COLOR_BLACK, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN, COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW
    )
except ModuleNotFoundError:
    print('\nFor the program to work, you need to install the curses module!\n')

directories: tuple[str, str] = ('config_files', 'icons')
for d in directories:
    try:
        os.mkdir(d)
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
            "enable": True, "matrix_color": "GREEN", "threads_rate": 35,
            "bold_symbols_rate": 8, "min_speed": 2, "max_speed": 6, "void_rate": 2, "digits": True,
            "symbols": True, "currencies": True, "greek": True, "latin": True, "cyrillic": True, "chinese": True
        },
        "info": {
            "enable": False, "info_color": "MAGENTA"
        }
    }

    @staticmethod
    def get_json_data(directory: str, name: str) -> dict | None:
        """
        The method reads a JSON configuration file.

        :param directory: directory of the configuration file.
        :param name: Name of the configuration file (without .json extension).
        """
        file_path = os.path.join(directory, f'{name}.json')
        try:
            with open(file_path, encoding='UTF-8') as json_file:
                data = load(json_file)
            return data
        except FileExistsError:
            pass
        except FileNotFoundError:
            raise FileNotFoundError(f'Файл не найден: {file_path}')
        except JSONDecodeError:
            raise ValueError(f'Ошибка декодирования JSON в файле: {file_path}')
        except PermissionError:
            raise PermissionError(f'Нет доступа к файлу: {file_path}')
        except Exception as e:
            raise Exception(f'Произошла ошибка: {str(e)}')

    @staticmethod
    def save_json_data(directory: str, name: str, data: list | dict) -> None:
        """
        The method creates a new default configuration file if the specified JSON file does not exist.

        :param directory: directory of the configuration file.
        :param name: Name of the configuration file (without .json extension).
        :param data: The data to be written as a dictionary.
        """
        file_path = os.path.join(directory, f'{name}.json')
        try:
            with open(file_path, 'w', encoding='UTF-8') as json_file:
                dump(data, json_file, ensure_ascii=False, indent=4)
        except PermissionError:
            raise PermissionError(f'Нет доступа для записи в файл: {file_path}')
        except IOError as e:
            raise IOError(f'Ошибка записи в файл: {file_path}. Причина: {str(e)}')
        except Exception as e:
            raise Exception(f'Произошла ошибка: {str(e)}')

    def get_config_data(self, config_name: str) -> dict[str, dict[str, str | bool | int]] | None:
        """
        The method tries to read the configuration file and, if it fails, overwrites it.

        :param config_name: The name of the configuration file (no .json extension).
        :return dict: The configuration data loaded from the JSON file.
        """
        try:
            return self.get_json_data('config_files', config_name)
        except FileNotFoundError:
            self.save_json_data('config_files', config_name, self.matrix_config)
            return self.matrix_config
        except JSONDecodeError:
            print(f'\nJSONDecodeError! File "{config_name}.json" is corrupted or not a valid JSON!')
            return None
        except OSError as e:
            print(f'\nOSError! Failed to read file "{config_name}.json" due to {e}.')
            return None

    __slots__ = (
        'variables', 'neo', 'neo_enable', 'neo_color', 'sentence_first', 'sentence_second', 'sentence_third',
        'sentence_fourth', 'matrix', 'matrix_enable', 'matrix_color', 'threads_rate',
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
