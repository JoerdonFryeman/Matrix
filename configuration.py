from json import load

try:
    from curses import (
        noecho, cbreak, curs_set, start_color, init_pair, COLOR_BLACK, COLOR_BLUE, COLOR_CYAN,
        COLOR_GREEN, COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW, color_pair, A_BOLD, error, wrapper
    )
except ModuleNotFoundError:
    print('The windows-curses module must be installed for the Windows operating system!')


class Configuration:
    @staticmethod
    def get_json_data() -> dict:
        try:
            with open('matrix_config.json') as file:
                data = load(file)
            return data
        except FileNotFoundError:
            print('File "matrix_config.json" not found!')

    def __init__(self):
        self.variables = self.get_json_data()
        self.color = self.variables['color']
        self.neo = self.variables['neo']
        self.neo_enable = self.neo['enable']
        self.sentence_first = self.neo['sentence_first']
        self.sentence_second = self.neo['sentence_second']
        self.sentence_third = self.neo['sentence_third']
        self.sentence_fourth = self.neo['sentence_fourth']
        self.matrix = self.variables['matrix']
        self.matrix_enable = self.matrix['enable']
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

    def verify_color(self):
        dictionary = {
            'BLACK': lambda: COLOR_BLACK, 'BLUE': lambda: COLOR_BLUE,
            'CYAN': lambda: COLOR_CYAN, 'GREEN': lambda: COLOR_GREEN,
            'MAGENTA': lambda: COLOR_MAGENTA, 'RED': lambda: COLOR_RED,
            'WHITE': lambda: COLOR_WHITE, 'YELLOW': lambda: COLOR_YELLOW,
        }[self.color]
        return dictionary()
