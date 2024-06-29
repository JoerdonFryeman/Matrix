from neo import Neo
from time import sleep
from random import randint
from threading import Thread
from bext import title, height, hide_cursor
from matrix import Matrix
from keyboard import press, press_and_release, release

neo = Neo()
mx = Matrix()


def get_consistency() -> None:
    """Consistency and full screen mode function"""
    press_and_release('alt+enter')
    sleep(0.1)
    press('ctrl+shift')
    for i in range(2):
        press_and_release('-')
    release('ctrl+shift')
    sleep(0.1)
    hide_cursor()


def main() -> None:
    """Entry point"""
    title("Matrix, version 1.2")
    get_consistency()
    neo.wake_up_neo(['Wake up, Neo...', 'The Matrix has you...', 'Follow the white rabbit.'])
    mx.get_matrix_move(-1, height() - 2, float(f'{0.0}{randint(3, 6)}'))
    Thread(target=mx.break_function).start()


if __name__ == '__main__':
    main()
