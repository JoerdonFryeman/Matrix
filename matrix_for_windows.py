import bext
import threading
from time import sleep
from colorama import Fore
from random import randint
from threading import Thread
from keyboard import press_and_release


class MatrixForWindows:
    v = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    w = ('Ω', 'λ', 'β', 'γ', 'θ', 'π', 'Σ', 'Ψ', '¥', 'ω')
    x = ('@', '№', '#', '%', '&', '§', '?', '₽', '€', '$')
    y = ('j', 'S', 'X', 'Y', 'Z', 'W', 'd', 'x', 'y', 'z')
    z = ('Ё', 'У', 'р', 'Ф', 'q', 'ё', 'R', 'й', 'Ь', 'ю')
    o = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

    locker = threading.Lock()
    main_counter = 0
    stop = False
    horizontal_coord_counter = 1  # counter and initial horizontal coordinate

    @staticmethod
    def get_title() -> str:
        """
        Title
        :return: str
        """
        return bext.title("Matrix, version 1.0")

    @staticmethod
    def get_full_screen() -> object:
        """
        Full screen mode
        :return: object
        """
        return press_and_release('alt+enter')

    @classmethod
    def break_function(cls) -> True:
        """
        Switch function
        :return: bool
        """
        input()
        cls.stop = True

    def get_matrix_symbol(self) -> str:
        """
        Forming a random symbol from the map function
        :return: str
        """
        f = (
            self.v[(randint(0, 9))],
            self.w[(randint(0, 9))],
            self.x[(randint(0, 9))],
            self.y[(randint(0, 9))],
            self.z[(randint(0, 9))],
            self.o[(randint(0, 9))]
        )
        return f[randint(0, 5)]

    def get_matrix_void(self) -> str:
        """
        Forming a void function
        :return: str
        """
        f = (self.o[(randint(0, 9))], self.o[(randint(0, 9))])
        return f[randint(0, 1)]

    def get_matrix_drop(self, drop_height, horizontal_coord, coord_of_the_drop_beginning) -> None:
        """
        Drop shaping function
        :param drop_height: final drop coordinate
        :param horizontal_coord: horizontal drop coordinate
        :param coord_of_the_drop_beginning: drop beginning coordinate
        :return: None
        """
        while not self.stop:  # overall process cycle
            for b in range(6):  # drop life cycle
                vertical_coord_counter = coord_of_the_drop_beginning
                self.main_counter += 1  # main cycle counter
                for c in range(randint(0, drop_height)):  # random coordinate of the final drop height
                    vertical_coord_counter += 1  # in each new cycle the drop height is multiplied by 1
                    with self.locker:
                        bext.goto(horizontal_coord, vertical_coord_counter)  # coordinates of drop width and drop height
                        if self.main_counter % 3 == 0:  # if the number of the main loop is divisible by 0
                            print(f'{Fore.GREEN}{self.get_matrix_void()}')  # a void is output
                        else:
                            print(f'{Fore.GREEN}{self.get_matrix_symbol()}')  # otherwise a droplet is generated
                    sleep(float(f'{0.0}{randint(3, 6)}'))
            self.main_counter = 0

    def get_matrix_move(self, coord_of_the_drop_beginning, drop_height) -> None:
        """
        Shaping droplet streams function
        :param coord_of_the_drop_beginning: drop beginning coordinate
        :param drop_height: final drop coordinate
        :return: None
        """
        bext.hide()
        for q in range(bext.width() // 2):
            Thread(target=MatrixForWindows().get_matrix_drop,
                   args=(drop_height, self.horizontal_coord_counter, coord_of_the_drop_beginning)).start()
            self.horizontal_coord_counter += 2  # pitch between droplet streams
