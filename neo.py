from time import sleep
from random import randint

try:
    from curses import init_pair, COLOR_GREEN, COLOR_BLACK, color_pair, wrapper
except ModuleNotFoundError:
    print('To use the neo.py module, you must create a virtual environment and install the requirements.txt file!')


class Neo:
    @staticmethod
    def wake_up_neo(stdscr):
        """
        The function takes a list of words and return as a printed input
        :param stdscr: initscr
        """
        init_pair(1, COLOR_GREEN, COLOR_BLACK)
        green_on_black = color_pair(1)
        counter_first = 0
        for text in ('Wake up, Neo...', 'The Matrix has you...', 'Follow the white rabbit.'):
            counter_first += 1
            counter_second = 0
            sentence = [i for i in text]
            for i in range(len(sentence)):
                counter_second += 1
                if counter_first == 1:
                    sleep(float(f'0.{randint(1, 3)}'))
                elif counter_first == 2:
                    sleep(float(f'0.{randint(2, 4)}'))
                elif counter_first == 3:
                    sleep(float(f'0.{randint(1, 3)}'))
                else:
                    sleep(float(f'0.{randint(randint(1, 2), randint(3, 4))}'))
                stdscr.clear()
                stdscr.addstr(2, 3, ''.join(sentence[0:counter_second]), green_on_black)
                stdscr.refresh()
            sleep(float(4))
        stdscr.clear()
        stdscr.addstr(2, 3, 'Knock, knock, Neo.', green_on_black)
        stdscr.refresh()
        sleep(4.2)
        stdscr.clear()

    def get_neo_wrapper(self):
        return wrapper(self.wake_up_neo)

# if __name__ == '__main__':
#     neo = Neo()
#     neo.get_neo_wrapper()
