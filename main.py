from core.neo import Neo
from core.matrix import Matrix

neo = Neo()
matrix = Matrix()


def main() -> None:
    """Entry point function."""
    try:
        if neo.neo_enable:
            neo.get_neo_wrapper()
        if matrix.matrix_enable:
            matrix.make_threads_of_droplets()
        if not neo.neo_enable and not matrix.matrix_enable:
            print('\nNeo and matrix modules are disabled, what else do you want to see here?\n')
    except AttributeError:
        print('\nAttributeError! You need to restart the program!\n')
    except Exception as error:
        print(f'The check came back with an error: {error}')


if __name__ == '__main__':
    main()
