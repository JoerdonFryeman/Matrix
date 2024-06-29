import os
from time import sleep
from random import randint
from platform import system
from colorama import Fore


class Neo:
    @staticmethod
    def get_system_command() -> str:
        system_name = system()
        if system_name == 'Linux':
            return 'clear'
        elif system_name == 'Windows':
            return 'cls'

    def wake_up_neo(self, sentences_list: list):
        """
        The function takes a list of words and return as a printed input
        :param sentences_list: list
        """
        counter_first = 0
        for text in sentences_list:
            counter_first += 1
            counter_second = 0
            sentence = [i for i in str(text)]
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
                os.system(self.get_system_command())
                print(f'{Fore.GREEN}'.join(sentence[0:counter_second]))
            sleep(float(4))
        os.system(self.get_system_command())
        print(f'{Fore.GREEN}Knock, knock, Neo.')
        sleep(4.2)
        os.system(self.get_system_command())
