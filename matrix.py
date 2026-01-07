from time import sleep
from random import randint, choice
from threading import Thread, Lock

from base import Base
from configuration import wrapper, error, curs_set, baudrate


class Matrix(Base):
    """The Matrix class is utilized for performing various symbol operations,"""

    __slots__ = ('init_height', 'locker')

    def __init__(self):
        super().__init__()
        self.init_height: int = 0
        self.locker = Lock()
        self.running: bool = True

    @staticmethod
    def generate_symbol(*args: bool) -> str:
        """
        This method returns a random character from boolean lists.

        :param args: bool
        :return: symbol
        """
        generated_symbol = (
            *(i for i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') if args[0]),
            *(i for i in ('!', '@', '#', '%', '&', '§', '№', '~', '/', '?') if args[1]),
            *(i for i in ('₿', '₽', '€', '$', '₩', 'ƒ', '¥', '₹', '₫', '£') if args[2]),
            *(i for i in ('π', 'λ', 'β', 'γ', 'Ω', 'θ', 'Σ', 'Ψ', 'ξ', 'ω') if args[3]),
            *(i for i in ('X', 'Y', 'Z', 'x', 'y', 'z', 'r', 'd', 'f', 'l') if args[4]),
            *(i for i in ('Ё', 'ё', 'Э', 'э', 'Ф', 'ф', 'Ъ', 'ъ', 'Я', 'я') if args[5]),
            *(i for i in ('小', '凡', '体', '人', '里', '是', '永', '甲', '字', '书') if args[6])
        )
        return choice(generated_symbol)

    def draw_symbol(self, stdscr, current_height: int, init_width: int, switch: int, *args: bool) -> object:
        """
        The method draws a random symbol on the screen at specified position.

        :param stdscr: initscr
        :param current_height: current height of the symbol
        :param init_width: initial width of the symbol
        :param switch: switching between the drop and the void
        :param args: bool

        :return: object of curses
        """
        curs_set(False)
        if switch == 0:
            return stdscr.addch(current_height, init_width, ' ')
        verify_a_bold = lambda: True if current_height % randint(3, self.bold_symbols_rate) == 0 else False
        return stdscr.addch(
            current_height, init_width, self.generate_symbol(*args),
            self.paint(self.matrix_color, verify_a_bold())
        )

    def display_info(self, stdscr, init_speed: float, max_height: int, max_width: int) -> object:
        """
        The method displays information on the screen.

        :param stdscr: initscr
        :param init_speed: initial width of the drop
        :param max_width: width of the screen
        :param max_height: height of the screen

        :return: object of curses
        """
        if self.info_enable:
            try:
                info_color = self.paint(self.info_color, False)
                br, tr, isp, mh, mw = baudrate(), self.threads_rate, init_speed, max_height, max_width
                link = 'https://github.com/JoerdonFryeman/Matrix'
                stdscr.addstr(10, 34, f'{" " * 47}')
                stdscr.addstr(11, 34, f'{" " * 4}{br} | {tr} | {isp} | {mh}x{mw}{" " * 17}', info_color)
                stdscr.addstr(12, 34, f'{" " * 4}Matrix (version 1.1.0) | ЭЛЕКТРОНИКА 54{" " * 4}', info_color)
                stdscr.addstr(13, 34, f'{" " * 4}MIT License, (c) 2026 JoerdonFryeman{" " * 7}', info_color)
                stdscr.addstr(14, 34, f'{" " * 4}{link}{" " * 3}', info_color)
                stdscr.addstr(15, 34, f'{" " * 47}')
            except error:
                pass
        stdscr.addstr(0, 0, '')

    @staticmethod
    def make_drop_height_random(current_height: int, max_height: int) -> None:
        """
        The method determines if the drop height should be reset.

        :param current_height: current height of the symbol
        :param max_height: height of the screen

        :raises error: If the drop height should be reset.
        """
        if current_height == randint(max_height // 3, max_height):
            raise error

    def move_droplet_of_symbols(self, stdscr, current_height: int) -> None:
        """
        The method moves the droplet of symbols down the screen.

        :param stdscr: curses window object
        :param current_height: current height of the symbol
        """
        init_width, switch = 1, randint(0, 1)
        init_speed = float(f'{0.}{randint(self.min_speed, self.max_speed)}')
        while self.running:
            height, width = stdscr.getmaxyx()
            try:
                with self.locker:
                    self.make_drop_height_random(current_height, height)
                    stdscr.addstr(current_height, init_width, ' ' * randint(0, self.void_rate))
                    self.draw_symbol(
                        stdscr, current_height, init_width, switch, self.digits, self.symbols,
                        self.currencies, self.greek, self.latin, self.cyrillic, self.chinese
                    )
                    if width >= 78:
                        self.display_info(stdscr, init_speed, height, width)
                    stdscr.refresh()
                    current_height += 1
                sleep(init_speed)
            except error:
                current_height = self.init_height
                init_width = choice([i for i in range(1, width - 1, 2)])
                init_speed = float(f'{0.}{randint(self.min_speed, self.max_speed)}')

    def _wait_for_enter(self, stdscr) -> None:
        """Block on a curses window until a key is pressed, then stop the animation."""
        stdscr.nodelay(False)
        stdscr.getch()
        self.running: bool = False
        stdscr.clear()

    def _safe_wrapper_wait(self):
        """Run _wait_for_enter under curses.wrapper and ignore curses errors."""
        try:
            wrapper(self._wait_for_enter)
        except error:
            pass

    def _safe_wrapper_move(self, init_h: int):
        """
        Run move_droplet_of_symbols under curses.wrapper and ignore curses errors.
        :param init_h: initial height to pass to move_droplet_of_symbols.
        """
        try:
            wrapper(self.move_droplet_of_symbols, init_h)
        except error:
            pass

    def make_threads_of_droplets(self) -> None:
        """The method makes threads of droplets."""
        Thread(target=self._safe_wrapper_wait).start()
        for _ in range(self.threads_rate):
            Thread(target=self._safe_wrapper_move, args=(self.init_height,)).start()
