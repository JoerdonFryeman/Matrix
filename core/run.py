from time import sleep
from curses import error
from threading import Thread, Lock
from random import random, randint

from .neo import Neo
from .visualisation import Visualisation


class Additionally(Neo, Visualisation):
    message = {
        "ru": "\nМодули часов и информации деактивированы, что ещё ты хочешь здесь увидеть?",
        "en": "\nClock and info modules are disabled, what else do you want to see here?"
    }

    class NoThreadsError(Exception):

        def __init__(self, message: dict[str, str], key: str):
            super().__init__(message[key])

    def renew(self):
        """Обновляет необходимые атрибуты."""
        self.variables = self.get_config_data('config')
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
        self.rainbow_mode = self.matrix['rainbow_mode']
        self.lego_mode = self.matrix['lego_mode']
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


class RunProgram(Additionally):
    __slots__ = ('locker', 'running', 'init_height', 'init_width')

    def __init__(self):
        super().__init__()
        self.locker = Lock()
        self.running = True
        self.init_height = 0
        self.init_width = 1

    def wait_for_enter(self, stdscr) -> None:
        """Ждёт нажатия клавиши и устанавливает флаг остановки."""
        stdscr.getch()
        self.running: bool = False

    def create_main_loop(self, stdscr, current_height, init_width) -> None:
        """Запускает все модули программы в цикле."""
        counter = 0
        switch, rainbow = randint(0, 1), randint(1, 8)
        init_speed = randint(self.min_speed, self.max_speed) / 100.0
        while self.running:
            height, width = stdscr.getmaxyx()
            try:
                with self.locker:
                    if counter % 5 == 0:
                        self.renew()
                    if current_height == randint(height // 3, height):
                        raise error
                    stdscr.addstr(current_height, init_width, '  ')
                    if switch == 0:
                        stdscr.addch(current_height, init_width, ' ')
                    else:
                        bold = random() < max(0.02, min(0.9, self.bold_symbols_rate / init_speed))
                        stdscr.addch(
                            current_height, init_width, self.generate_symbol(
                                self.digits, self.symbols, self.currencies, self.greek,
                                self.latin, self.cyrillic, self.chinese
                            ), self.paint(rainbow, self.matrix_color, bold)
                        )
                    stdscr.refresh()
                    current_height += 1
                sleep(init_speed)
            except error:
                init_width = 1 + 2 * randint(0, max(0, (width - 3) // 2))
                current_height = self.init_height
                init_speed = randint(self.min_speed, self.max_speed) / 100.0
            counter = (counter + 1) % 100

    def create_wrapped_threads(self) -> None:
        """Запускает потоки для выполнения модулей в зависимости от наличия системной информации."""
        self.safe_wrapper(self.init_curses, None)
        Thread(target=self.safe_wrapper, args=(self.wait_for_enter, None)).start()
        if self.neo_enable:
            self.safe_wrapper(self.wake_up_neo, None)
        if self.matrix_enable:
            for _ in range(self.threads_rate):
                Thread(
                    target=self.safe_wrapper,
                    args=(self.create_main_loop, self.init_height, self.init_width)
                ).start()
        if not self.neo_enable and not self.matrix_enable:
            raise self.NoThreadsError(self.message, self.verify_language(self.language))
