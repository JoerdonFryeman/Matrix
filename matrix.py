from time import sleep
from random import randint, choice
from threading import Thread, Lock

from configuration import (
    Configuration, wrapper, error, curs_set, baudrate, init_pair, use_default_colors, color_pair, A_BOLD
)


class Matrix(Configuration):
    """
    The Matrix class is utilized for performing various symbol operations,
    such as generating random symbols, drawing symbols on the screen, and managing their display.
    """
    __slots__ = ('init_height', 'locker')

    def __init__(self):
        super().__init__()
        self.init_height = 0
        self.locker = Lock()

    @staticmethod
    def generate_symbol(*args: bool) -> str:
        """
        This method returns a random character from boolean lists.
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
        return choice(symbol_list)

    def get_color(self, current_height: int) -> int:
        """
        The method calculates and returns the color of the given symbol based on current height.
        :param current_height: int
        :return: int
        """
        use_default_colors(), init_pair(1, self.verify_color(), -1)
        symbol_color = color_pair(1)
        if current_height % randint(3, self.bold_symbols_rate) == 0:
            return symbol_color | A_BOLD
        return symbol_color

    def draw_symbol(self, stdscr, current_height: int, init_width: int, switch: int, *args: bool) -> object:
        """
        The method draws a random symbol on the screen at specified position.
        :param stdscr: curses window object
        :param current_height: int
        :param init_width: int
        :param switch: int
        :param args: bool
        :return: object of curses
        """
        curs_set(False)
        if switch == 0:
            return stdscr.addch(current_height, init_width, ' ')
        return stdscr.addch(current_height, init_width, self.generate_symbol(*args), self.get_color(current_height))

    def get_info(self, stdscr, init_speed: float, max_width: int, max_height: int) -> object:
        """
        The method displays information on the screen.
        :param stdscr: curses window object
        :param init_speed: float
        :param max_width: int
        :param max_height: int
        :return: object of curses
        """
        if self.info:
            return stdscr.addstr(
                0, 0,
                f'{baudrate()} | {self.threads_rate} | {init_speed} | {max_width}x{max_height} | '
                f'GitHub: https://github.com/JoerdonFryeman/Matrix'
            )
        return stdscr.addstr(0, 0, '')

    @staticmethod
    def make_drop_height_random(current_height: int, max_height: int):
        """
        The method determines if the drop height should be reset.
        :param current_height: int
        :param max_height: int
        """
        if current_height == randint(max_height // 3, max_height):
            raise error

    def move_droplet_of_symbols(self, stdscr, current_height: int):
        """
        The method moves the droplet of symbols down the screen.
        :param stdscr: curses window object
        :param current_height: int
        """
        init_width, switch = 1, randint(0, 1)
        init_speed = float(f'{0.}{randint(self.min_speed, self.max_speed)}')
        for _ in range(self.cycle_number):
            max_height, max_width = stdscr.getmaxyx()
            try:
                with self.locker:
                    self.make_drop_height_random(current_height, max_height)
                    stdscr.addstr(current_height, init_width, ' ' * randint(0, self.void_rate))
                    self.draw_symbol(
                        stdscr, current_height, init_width, switch, self.digits, self.symbols,
                        self.currencies, self.greek, self.latin, self.cyrillic, self.chinese
                    )
                    self.get_info(stdscr, init_speed, max_width, max_height)
                    stdscr.refresh()
                    current_height += 1
                sleep(init_speed)
            except error:
                current_height = self.init_height
                init_width = choice([i for i in range(1, max_width - 1, 2)])
                init_speed = float(f'{0.}{randint(self.min_speed, self.max_speed)}')

    def make_threads_of_droplets(self):
        """The method makes threads of droplets."""
        try:
            for _ in range(0, self.threads_rate):
                Thread(target=wrapper, args=(self.move_droplet_of_symbols, self.init_height)).start()
        except error:
            pass
