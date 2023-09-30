import bext
from time import sleep
from threading import Thread
from matrix_for_windows import MatrixForWindows

matrix_windows = MatrixForWindows()


def main() -> None:
    matrix_windows.get_title()
    matrix_windows.get_full_screen()
    sleep(0.1)
    matrix_windows.get_matrix_move(-1, bext.height() - 2)
    Thread(target=matrix_windows.break_function()).start()


if __name__ == '__main__':
    main()
