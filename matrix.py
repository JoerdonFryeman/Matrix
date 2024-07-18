from time import sleep
from random import randint, choice
from threading import Thread, Lock
from configuration import (
    noecho, cbreak, curs_set, start_color, init_pair,
    COLOR_BLACK, color_pair, A_BOLD, error, wrapper, Configuration
)


class Matrix(Configuration):
    __slots__ = ('_init_height', 'threads_rate', 'locker')

    def __init__(self):
        super().__init__()
        self._init_height = 0
        self.threads_rate = 60
        self.locker = Lock()

    @staticmethod
    def generate_symbol(*args: bool) -> str:
        """
        This function generates a random character from boolean lists
        :param args: bool
        """
        symbol_list = [
            *[i for i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') if args[0]],
            *[i for i in ('!', '@', '#', '%', '&', '§', '№', '~', '/', '?') if args[1]],
            *[i for i in ('₿', '₽', '€', '$', '₩', 'ƒ', '¥', '₹', '₫', '£') if args[2]],
            *[i for i in ('π', 'λ', 'β', 'γ', 'Ω', 'θ', 'Σ', 'Ψ', 'ξ', 'ω') if args[3]],
            *[i for i in ('X', 'Y', 'Z', 'x', 'y', 'z', 'r', 'd', 'f', 'l') if args[4]],
            *[i for i in ('Ё', 'ё', 'Э', 'э', 'Ф', 'ф', 'Ъ', 'ъ', 'Я', 'я') if args[5]],
            *[i for i in ('小', '西', '体', '人', '里', '是', '永', '甲', '字', '书') if args[6]],
        ]
        list_size = len(symbol_list) - 1
        return symbol_list[randint(0, list_size)]

    def get_color(self, current_height: int) -> object:
        """
        The function returns color of the random symbol
        :param current_height: int
        """
        start_color()
        init_pair(1, self.verify_color(), COLOR_BLACK)
        green_on_black = color_pair(1)
        if current_height % randint(3, self.bold_symbols_rate) == 0:
            return green_on_black | A_BOLD
        return green_on_black

    def draw_symbol(self, stdscr, current_height: int, init_width: int, switch: int, *args: bool) -> object:
        """
        The function returns the random symbol on the screen
        :param stdscr: initscr
        :param current_height: int
        :param init_width: int
        :param switch: int
        :param args: bool
        """
        noecho()  # disabling the display of input characters
        cbreak()  # disabling the character reading delay
        curs_set(False)
        if switch == 0:
            return stdscr.addstr(current_height, init_width, ' ')
        return stdscr.addstr(current_height, init_width, self.generate_symbol(*args), self.get_color(current_height))

    def move_droplet_of_symbols(self, stdscr, _current_height: int):
        """
        The function moves the droplet of symbols down
        :param stdscr: initscr
        :param _current_height: int
        """
        _init_width = 1
        _switch = randint(0, 1)
        init_speed = float(f'{0.}{randint(self.min_speed, self.max_speed)}')
        while True:
            max_height, max_width = stdscr.getmaxyx()
            try:
                with self.locker:
                    stdscr.refresh()
                    if _current_height == randint(max_height // 3, max_height):
                        raise error
                    stdscr.addstr(_current_height, _init_width, ' ' * randint(0, self.void_rate))
                    self.draw_symbol(
                        stdscr, _current_height, _init_width, _switch, self.digits, self.symbols,
                        self.currencies, self.greek, self.latin, self.cyrillic, self.chinese
                    )
                    stdscr.addstr(0, 0, '')
                    _current_height += 1
                sleep(init_speed)
            except error:
                _current_height = self._init_height
                _init_width = choice([i for i in range(1, max_width - 1, 2)])
                init_speed = float(f'{0.}{randint(self.min_speed, self.max_speed)}')

    def make_threads_of_droplets(self):
        """The function makes threads of droplets"""
        try:
            for i in range(0, self.threads_rate):
                Thread(target=wrapper, args=(self.move_droplet_of_symbols, self._init_height)).start()
        except error:
            pass
