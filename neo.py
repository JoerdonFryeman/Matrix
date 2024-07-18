from time import sleep
from random import randint
from configuration import init_pair, COLOR_BLACK, color_pair, wrapper, Configuration


class Neo(Configuration):
    def wake_up_neo(self, stdscr):
        """
        The function takes a list of words and return as a printed input
        :param stdscr: initscr
        """
        init_pair(1, self.verify_color(), COLOR_BLACK)
        green_on_black = color_pair(1)
        _counter_first = 0
        for text in (self.sentence_first, self.sentence_second, self.sentence_third):
            _counter_first += 1
            _counter_second = 0
            sentence = [i for i in text]
            for i in range(len(sentence)):
                _counter_second += 1
                if _counter_first == 1:
                    sleep(float(f'0.{randint(1, 3)}'))
                elif _counter_first == 2:
                    sleep(float(f'0.{randint(2, 4)}'))
                elif _counter_first == 3:
                    sleep(float(f'0.{randint(1, 3)}'))
                else:
                    sleep(float(f'0.{randint(randint(1, 2), randint(3, 4))}'))
                stdscr.clear()
                stdscr.addstr(2, 3, ''.join(sentence[0:_counter_second]), green_on_black)
                stdscr.refresh()
            sleep(float(4))
        stdscr.clear()
        stdscr.addstr(2, 3, self.sentence_fourth, green_on_black)
        stdscr.refresh()
        sleep(4.2)
        stdscr.clear()

    def get_neo_wrapper(self):
        return wrapper(self.wake_up_neo)
