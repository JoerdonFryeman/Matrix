from time import sleep
from random import randint, choice
from threading import Thread, Lock
from curses import wrapper, curs_set, start_color, init_pair, COLOR_GREEN, COLOR_BLACK, color_pair, A_BOLD, error


class Matrix:
    def __init__(self):
        self.locker = Lock()
        self.init_height = 0

    @staticmethod
    def generate_symbol(*args: int | bool) -> str:
        """
        This function generates a random character from boolean lists
        :param args: int | bool
        """
        symbol_list = [
            *[' ' for _ in range(0, args[0])],
            *[i for i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') if args[1]],
            *[i for i in ('!', '@', '#', '%', '&', '§', '№', '~', '/', '?') if args[2]],
            *[i for i in ('₿', '₽', '€', '$', '₩', 'ƒ', '¥', '₹', '₫', '£') if args[3]],
            *[i for i in ('π', 'λ', 'β', 'γ', 'Ω', 'θ', 'Σ', 'Ψ', 'ξ', 'ω') if args[4]],
            *[i for i in ('X', 'Y', 'Z', 'x', 'y', 'z', 'r', 'd', 'f', 'l') if args[5]],
            *[i for i in ('Ё', 'ё', 'Э', 'э', 'Ф', 'ф', 'Ъ', 'ъ', 'Я', 'я') if args[6]],
            *[i for i in ('小', '西', '体', '人', '里', '是', '永', '甲', '字', '书') if args[7]]
        ]
        if args[8]:
            symbol_list.clear()
            symbol_list.append(' ')
        return choice(symbol_list[randint(0, len(symbol_list) - 1)])

    @staticmethod
    def get_color(current_height: int) -> object:
        """
        The function returns color of the random symbol
        :param current_height: int
        """
        curs_set(False)
        start_color()
        init_pair(1, COLOR_GREEN, COLOR_BLACK)
        green_on_black = color_pair(1)
        if current_height % randint(3, 9) == 0:
            return green_on_black | A_BOLD
        return green_on_black

    def draw_symbol(self, stdscr, current_height: int, init_width: int, switch: int, *args: int | bool) -> object:
        """
        The function returns the random symbol on the screen
        :param stdscr: initscr
        :param current_height: int
        :param init_width: int
        :param switch: int
        :param args: int | bool
        """
        if switch == 0:
            return stdscr.addstr(current_height, init_width, ' ', self.get_color(current_height))
        return stdscr.addstr(current_height, init_width, self.generate_symbol(*args), self.get_color(current_height))

    def move_droplet_of_symbols(self, stdscr, current_height: int):
        """
        The function moves the droplet of symbols down
        :param stdscr: initscr
        :param current_height: int
        """
        init_width = 1
        switch = randint(0, 1)
        min_speed, max_speed, step = 2, 8, 2
        init_speed = float(f'{0}.{0}{randint(min_speed, max_speed)}')
        while True:
            max_height, max_width = stdscr.getmaxyx()
            void_rate = 5
            num, sym, cur, gre, lat, cyr, chi, clear = True, True, True, True, True, True, True, False
            try:
                with self.locker:
                    stdscr.refresh()
                    if current_height == randint(max_height // 3, max_height):
                        raise error
                    args = void_rate, num, sym, cur, gre, lat, cyr, chi, clear
                    self.draw_symbol(stdscr, current_height, init_width, switch, *args)
                    current_height += 1
                sleep(init_speed)
            except error:
                if switch == 0:
                    sleep(float(f'{0}.{0}{randint(min_speed, max_speed)}'))
                current_height = self.init_height
                init_width = choice([i for i in range(1, max_width - 1, 2)])
                init_speed = float(f'{0}.{0}{randint(min_speed, max_speed)}')

    def make_threads_of_droplets(self):
        """The function makes 73 threads of droplets"""
        try:
            for i in range(0, 73):  # self.max_width // 2
                Thread(target=wrapper, args=(self.move_droplet_of_symbols, self.init_height)).start()
        except error:
            pass

# if __name__ == '__main__':
#     matrix = Matrix()
#     matrix.make_threads_of_droplets()
