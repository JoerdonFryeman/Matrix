import os
import platform
from logging import config, getLogger
from json import load, dump, JSONDecodeError


class Base:
    __slots__ = (
        'logger', 'config', 'variables', 'language', 'neo', 'neo_enable', 'neo_color', 'sentence_first',
        'sentence_second', 'sentence_third', 'sentence_fourth', 'matrix', 'matrix_enable', 'matrix_color',
        'threads_rate', 'bold_symbols_rate', 'min_speed', 'max_speed', 'digits', 'symbols',
        'currencies', 'greek', 'latin', 'cyrillic', 'chinese'
    )

    def __init__(self):
        self.logger = getLogger()
        self.config = {
            "language": "ru",
            "neo": {
                "enable": False, "neo_color": "GREEN", "sentence_first": "Wake up, Neo...",
                "sentence_second": "The Matrix has you...", "sentence_third": "Follow the white rabbit.",
                "sentence_fourth": "Knock, knock, Neo."
            },
            "matrix": {
                "enable": True, "matrix_color": "GREEN", "threads_rate": 25, "bold_symbols_rate": 0.007,
                "min_speed": 2, "max_speed": 8, "digits": True, "symbols": True, "currencies": True,
                "greek": True, "latin": True, "cyrillic": True, "chinese": True
            }
        }
        self.variables = self.get_config_data('config')
        try:
            self.language = self.variables['language']
            self.neo = self.variables['neo']
            self.neo_enable = self.neo['enable']
            self.neo_color = self.neo['neo_color']
            self.sentence_first = self.neo['sentence_first']
            self.sentence_second = self.neo['sentence_second']
            self.sentence_third = self.neo['sentence_third']
            self.sentence_fourth = self.neo['sentence_fourth']
            self.matrix = self.variables['matrix']
            self.matrix_enable = self.matrix['enable']
            self.matrix_color = self.matrix['matrix_color']
            self.threads_rate = self.matrix['threads_rate']
            self.bold_symbols_rate = self.matrix['bold_symbols_rate']
            self.min_speed = self.matrix['min_speed']
            self.max_speed = self.matrix['max_speed']
            self.digits = self.matrix['digits']
            self.symbols = self.matrix['symbols']
            self.currencies = self.matrix['currencies']
            self.greek = self.matrix['greek']
            self.latin = self.matrix['latin']
            self.cyrillic = self.matrix['cyrillic']
            self.chinese = self.matrix['chinese']
        except TypeError:
            print('\nTypeError! Переменные не могут быть инициализированы!')

    @staticmethod
    def create_directories() -> None:
        """Создаёт каталоги, игнорируя уже существующие."""
        directories: tuple[str, str, str] = ('config_files', 'config_files/logs', 'icons')
        for directory in directories:
            try:
                os.mkdir(directory)
            except FileExistsError:
                pass

    @staticmethod
    def verify_language(language: str) -> str:
        """Метод проверяет язык и возвращает 'ru', если язык не поддерживается."""
        if language not in ['ru', 'en']:
            language: str = 'ru'
        return language

    @staticmethod
    def verify_os() -> str | None:
        """Метод проверяет на какой ОС запускается программа."""
        system: str = platform.system()
        if system == 'Linux':
            return 'Linux'
        if system == 'Darwin':
            return 'macOS'
        if system == 'Windows':
            return 'Windows'
        return None

    @staticmethod
    def get_json_data(directory: str, name: str) -> dict:
        """Возвращает данные в формате json из указанного файла."""
        file_path: str = os.path.join(directory, f'{name}.json')
        try:
            with open(file_path, encoding='UTF-8') as json_file:
                data: dict = load(json_file)
            return data
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
        """Сохраняет файл json."""
        file_path: str = os.path.join(directory, f'{name}.json')
        try:
            with open(file_path, 'w', encoding='UTF-8') as json_file:
                dump(data, json_file, ensure_ascii=False, indent=4)
        except PermissionError:
            raise PermissionError(f'Нет доступа для записи в файл: {file_path}')
        except IOError as e:
            raise IOError(f'Ошибка записи в файл: {file_path}. Причина: {str(e)}')
        except Exception as e:
            raise Exception(f'Произошла ошибка: {str(e)}')

    def get_config_data(self, config_name: str):
        """Метод пробует прочитать файл конфигурации и, если это не удаётся, перезаписывает его."""
        try:
            return self.get_json_data('config_files', config_name)
        except FileNotFoundError:
            self.save_json_data('config_files', config_name, self.config)
            return self.config
        except JSONDecodeError:
            print(f'\nJSONDecodeError! Файл «{config_name}.json» поврежден или не является корректным JSON!')
            return None
        except OSError as e:
            print(f'\nOSError! Не удалось прочитать файл «{config_name}.json» из-за {e}')
            return None

    def get_logging_data(self) -> None:
        """Загружает и применяет конфигурацию логирования из JSON-файла."""
        config.dictConfig(self.get_json_data('config_files/logs', 'logging'))

    def log_app_release(self, name: str, version: str, year: int) -> None:
        """Логирует заголовок приложения в один info-вызов."""
        self.logger.info(
            '| ЭЛЕКТРОНИКА 54 | %s (version %s) | '
            'https://github.com/JoerdonFryeman/%s | '
            'MIT License, (c) %d Joerdon Fryeman |',
            name, version, name, year
        )
