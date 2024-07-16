from platform import system
from matrix import Neo, Matrix

neo = Neo()
matrix = Matrix()


def verify_os_for_requirements():
    """This function creates a requirements.txt file depending on the operating system"""
    system_name = system()
    if system_name == 'Linux':
        return True
    elif system_name == 'Windows':
        try:
            with open('requirements.txt', 'w') as file:  # Your requirements.txt file is here...
                file.write('windows-curses==2.3.3')
        except FileExistsError:
            pass
        return True
    else:
        print('This program is currently for Linux or Windows only!')
        return False


def main():
    """Entry point"""
    if verify_os_for_requirements():
        try:
            neo.get_neo_wrapper()
            matrix.make_threads_of_droplets()
        except NameError:
            print('You must install the requirements.txt file!')


if __name__ == '__main__':
    main()
