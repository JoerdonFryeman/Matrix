# ЭЛЕКТРОНИКА 54 (Matrix)

Your personal green rain of code in a Linux or Windows console!

![Matrix](https://github.com/user-attachments/assets/7ce3e61b-2871-4c82-a97f-83d22d86b06b)

## Startup
- Download [latest release](https://github.com/JoerdonFryeman/Matrix/releases/tag/Matrix_v1.0.8).
- In Linux, run ```Matrix_v1.0.8.app``` in the terminal or with the command:
```console
cd /home/your_directories.../Matrix_v1.0.8/Linux/ && ./Matrix_v1.0.8.app
```
- In Windows, run ```Matrix_v1.0.8.exe```

## Project structure

- `main.py`: The main module to run the program.
- `matrix.py`: Matrix symbol generation and animation module.
- `neo.py`: The module of generation and animation of symbols of the program “Neo”.
- `base`: Base module for all modules.
- `configuration.py`: Module for loading program configuration data.
- `matrix_config.json`: Program settings and configuration file.

## Requirements

- Python 3.13
- windows-curses 2.4.1a1 (for Windows)
- The application was developed for Arch Linux with the KDE Plasma desktop environment, but should work in other distributions as well as with limitations in Windows.

## Installation

Download the project

``` console
git clone https://github.com/JoerdonFryeman/Matrix
cd Matrix
```

### For Linux

Just run the script
``` console
python3 main.py
```

### For Windows

Create and activate a virtual environment

``` console
python -m venv venv
venv\Scripts\activate
```

Install the requirements and run the script

``` console
python.exe -m pip install --upgrade pip
pip install -r requirements_for_windows.txt
python main.py
```

## Startup

You can start the project in your console
``` console
python3 main.py
```

## Settings

Some program settings can be specified in the matrix_config.json file.

![matrix_colors](https://github.com/user-attachments/assets/6da55b9c-defb-41be-891d-7165047a3b04)

- Change the color of symbols: BLACK, BLUE, CYAN, GREEN, MAGENTA, RED, WHITE, YELLOW.
- Enable or disable info mode, matrix or neo modules.
- Write your own sentences for example: "Fall asleep, Neo...".
- You can also choose the rate of threads, voids or symbols and speed of rain.
- With true or false you may enable and disable some kinds of symbols.

The default settings can be restored by deleting the matrix_config.json file and restarting the program.

## License

This project is being developed under the MIT license.

## Support with Bitcoin

bc1qewfgtrrg2gqgtvzl5d2pr9pte685pp5n3g6scy
