from time import sleep
from random import randint

from .visualisation import Visualisation


class Neo(Visualisation):

    @staticmethod
    def get_click_speed(counter_first: int) -> float:
        """The method returns a random float value from 0.1 to 0.3"""
        dictionary = {
            1: lambda: float(f'0.{randint(1, 3)}'),
            2: lambda: float(f'0.{randint(2, 4)}'),
            3: lambda: float(f'0.{randint(1, 3)}')
        }[counter_first]
        return dictionary()

    def print_sentence(
            self, stdscr, sentence: list, counter_second: int, counter_first: int, symbol_color: object
    ) -> None:
        """The method prints the sentence in the wrapper of the screen."""
        for i in range(len(sentence)):
            counter_second += 1
            sleep(self.get_click_speed(counter_first))
            stdscr.clear()
            stdscr.addstr(2, 3, ''.join(sentence[0:counter_second]), symbol_color)
            stdscr.refresh()

    def get_split_sentence(self, stdscr, counter_first: int, symbol_color: object) -> None:
        """The method splits separate sentences into a list of letters."""
        for text in (self.sentence_first, self.sentence_second, self.sentence_third):
            counter_first += 1
            counter_second = 0
            self.print_sentence(stdscr, [i for i in text], counter_second, counter_first, symbol_color)
            sleep(float(4))

    def wake_up_neo(self, stdscr) -> None:
        """The method takes a list of words and return as a printed input."""
        symbol_color = self.paint(self.neo_color, False)
        counter_first = 0
        self.get_split_sentence(stdscr, counter_first, symbol_color)
        stdscr.clear()
        stdscr.addstr(2, 3, self.sentence_fourth, symbol_color)
        stdscr.refresh()
        sleep(4.2)
        stdscr.clear()
