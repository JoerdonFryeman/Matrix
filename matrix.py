from time import sleep
from random import randint, choice
from threading import Thread, Lock
from configuration import (
    Configuration, wrapper, error, cbreak, curs_set, baudrate, init_pair, use_default_colors, color_pair, A_BOLD
)


class Matrix(Configuration):
    __slots__ = ('_init_height', 'locker')

    def __init__(self):
        super().__init__()
        self._init_height = 0
        self.locker = Lock()

    @staticmethod
    def generate_symbol(*args: bool) -> str:
        """
        This function returns a random character from boolean lists
        :param args: bool
        :return: symbol
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
        return symbol_list[randint(0, len(symbol_list) - 1)]

    def get_color(self, current_height: int) -> int:
        """
        The function returns color of the random symbol
        :param current_height: current height of the symbol
        :return: value of color
        """
        use_default_colors(), init_pair(1, self.verify_color(), -1)
        symbol_color = color_pair(1)
        if current_height % randint(3, self.bold_symbols_rate) == 0:
            return symbol_color | A_BOLD
        return symbol_color

    def draw_symbol(self, stdscr, current_height: int, init_width: int, switch: int, *args: bool) -> object:
        """
        The function returns the random symbol in the wrapper of the screen
        :param stdscr: initscr
        :param current_height: current height of the symbol
        :param init_width: initial width of the symbol
        :param switch: switching between the drop and the void
        :param args: bool
        :return: object of curses
        """
        cbreak(), curs_set(False)
        if switch == 0:
            return stdscr.addch(current_height, init_width, ' ')
        return stdscr.addch(current_height, init_width, self.generate_symbol(*args), self.get_color(current_height))

    def get_info(self, stdscr, init_speed: float, max_width: int, max_height: int) -> object:
        """
        The function gives info
        :param stdscr: initscr
        :param init_speed: initial width of the drop
        :param max_width: width of the screen
        :param max_height: height of the screen
        :return: object of curses
        """
        match self.info:
            case True:
                return stdscr.addstr(
                    0, 0, f'{baudrate()} | {self.threads_rate} | {init_speed} | {max_width}x{max_height}'
                )
            case False:
                return stdscr.addstr(0, 0, '')

    @staticmethod
    def make_drop_height_random(current_height: int, max_height: int):
        """
        The function raises error
        :param current_height: current height of the symbol
        :param max_height: height of the screen
        """
        if current_height == randint(max_height // 3, max_height):
            raise error

    def move_droplet_of_symbols(self, stdscr, _current_height: int):
        """
        The function moves the droplet of symbols down
        :param stdscr: initscr
        :param _current_height: current height of the symbol
        """
        _init_width, _switch = 1, randint(0, 1)
        init_speed = float(f'{0.}{randint(self.min_speed, self.max_speed)}')
        while True:
            max_height, max_width = stdscr.getmaxyx()
            try:
                with self.locker:
                    self.make_drop_height_random(_current_height, max_height)
                    stdscr.addstr(_current_height, _init_width, ' ' * randint(0, self.void_rate))
                    self.draw_symbol(
                        stdscr, _current_height, _init_width, _switch, self.digits, self.symbols,
                        self.currencies, self.greek, self.latin, self.cyrillic, self.chinese
                    )
                    self.get_info(stdscr, init_speed, max_width, max_height)
                    stdscr.refresh()
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
