from neo import Neo
from time import sleep
from threading import Thread
from bext import title, height, hide
from matrix_for_windows import MatrixForWindows
from keyboard import press, press_and_release, release

neo = Neo()
matrix_windows = MatrixForWindows()


def get_consistency() -> None:
    """Consistency and full screen mode function"""
    press_and_release('alt+enter')
    sleep(0.1)
    press('ctrl+shift')
    for i in range(2):
        press_and_release('-')
    release('ctrl+shift')
    sleep(0.1)
    hide()


def main() -> None:
    """Entry point"""
    title("Matrix, version 1.1")
    get_consistency()
    neo.run_text()
    matrix_windows.get_matrix_move(-1, height() - 2)
    Thread(target=matrix_windows.break_function()).start()


if __name__ == '__main__':
    main()
