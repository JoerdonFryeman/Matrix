from json import load, dump

try:
    from curses import (
        wrapper, error, cbreak, curs_set, baudrate, start_color, init_pair, use_default_colors, color_pair, A_BOLD,
        COLOR_BLACK, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN, COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW
    )
except ModuleNotFoundError:
    print('\nFor Windows you must install the requirements_for_windows.txt file!\n')


class Configuration:
    json_data = {
        "info": False, "color": "GREEN", "neo": {
            "enable": True, "sentence_first": "Wake up, Neo...", "sentence_second": "The Matrix has you...",
            "sentence_third": "Follow the white rabbit.", "sentence_fourth": "Knock, knock, Neo."
        },
        "matrix": {
            "enable": True, "threads_rate": 73, "bold_symbols_rate": 9, "min_speed": 2, "max_speed": 8,
            "void_rate": 3, "digits": True, "symbols": True, "currencies": True, "greek": True,
            "latin": True, "cyrillic": True, "chinese": True}
    }

    def get_json_data(self, config_name: str) -> dict:
        try:
            with open(f'{config_name}.json') as file:
                data = load(file)
            return data
        except FileNotFoundError:
            print(f'\nFileNotFoundError! File {config_name}.json not found!')
            with open(f'{config_name}.json', 'w', encoding='UTF-8') as file:
                dump(self.json_data, file)
            print(f'\nThe file {config_name}.json was successfully created!')

    def __init__(self):
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
        dictionary = {
            'BLACK': lambda: COLOR_BLACK, 'BLUE': lambda: COLOR_BLUE,
            'CYAN': lambda: COLOR_CYAN, 'GREEN': lambda: COLOR_GREEN,
            'MAGENTA': lambda: COLOR_MAGENTA, 'RED': lambda: COLOR_RED,
            'WHITE': lambda: COLOR_WHITE, 'YELLOW': lambda: COLOR_YELLOW,
        }[self.color]
        return dictionary()
