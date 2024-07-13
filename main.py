from neo import Neo
from matrix import Matrix

neo = Neo()
matrix = Matrix()


def main():
    """Entry point"""
    neo.get_neo_wrapper()
    matrix.make_threads_of_droplets()


if __name__ == '__main__':
    main()
