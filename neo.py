from os import system
from bext import goto
from time import sleep
from colorama import Fore
from random import randint


class Neo:
    wake_up = (
        'W', 'Wa', 'Wak', 'Wake', 'Wake ', 'Wake u', 'Wake up', 'Wake up,', 'Wake up, ', 'Wake up, N',
        'Wake up, Ne', 'Wake up, Neo', 'Wake up, Neo.', 'Wake up, Neo..', 'Wake up, Neo...'
    )

    the_matrix = (
        'T', 'Th', 'The', 'The ', 'The M', 'The Ma', 'The Mat', 'The Matr', 'The Matri', 'The Matrix', 'The Matrix ',
        'The Matrix h', 'The Matrix ha', 'The Matrix has', 'The Matrix has ', 'The Matrix has y', 'The Matrix has yo',
        'The Matrix has you', 'The Matrix has you.', 'The Matrix has you..', 'The Matrix has you...'
    )

    follow = (
        'F', 'Fo', 'Fol', 'Foll', 'Follo', 'Follow', 'Follow ', 'Follow t', 'Follow th', 'Follow the', 'Follow the ',
        'Follow the w', 'Follow the wh', 'Follow the whi', 'Follow the whit', 'Follow the white', 'Follow the white ',
        'Follow the white r', 'Follow the white ra', 'Follow the white rab', 'Follow the white rabb',
        'Follow the white rabbi', 'Follow the white rabbit', 'Follow the white rabbit.'
    )

    @staticmethod
    def generate_text(word, pause_first, pause_second, speed_first, speed_second) -> None:
        """
        The function takes a tuple of words and prints them at a certain speed
        :param word: str
        :param pause_first: float
        :param pause_second: float
        :param speed_first: int
        :param speed_second: int
        :return: None
        """
        count = 0
        system('cls')

        for i in range(len(word)):
            count += 1
            sleep(float(f'0.{randint(int(speed_first), int(speed_second))}'))
            goto(4, 2)
            print(f'{Fore.GREEN}{word[count - 1]}')

        sleep(float(pause_first))
        goto(4, 2)
        print(24 * ' ')
        sleep(float(pause_second))

    def run_text(self) -> None:
        """
        The function calls the text generating function
        :return: None
        """
        self.generate_text(self.wake_up, 4.4, 1.2, 1, 2)
        self.generate_text(self.the_matrix, 4.2, 0.7, 2, 4)
        self.generate_text(self.follow, 4, 0.2, 1, 3)
        goto(4, 2)
        print(f'{Fore.GREEN}Knock, knock, Neo.')
        sleep(4.2)
        system('cls')
