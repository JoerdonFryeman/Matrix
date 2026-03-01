# ЭЛЕКТРОНИКА 54 (Matrix)

Your personal green rain of code in a Linux or Windows console!

![Matrix](https://github.com/user-attachments/assets/7ce3e61b-2871-4c82-a97f-83d22d86b06b)

## Startup
Download [latest release](https://github.com/JoerdonFryeman/Matrix/releases/tag/Matrix_v1.1.0).

In Linux, run ```Matrix_v1.1.0.app``` in the terminal or with the command:
```console
cd /home/your_directories.../Matrix_v1.1.0/Linux/ && ./Matrix_v1.1.0.app
```
In Windows, run ```Matrix_v1.1.0.exe```

## Docker

Image [latest release](https://hub.docker.com/r/joerdonfryeman/matrix).

Run with attached standard streams (interactive terminal):

```console
docker run -it joerdonfryeman/matrix:1.1.0
```

Same with automatic container removal after exit:

```console
docker run --rm -it joerdonfryeman/matrix:1.1.0
```

## Requirements

- Python: >= 3.11
- windows-curses: >= 2.4.1a1 (for Windows)
- The application was developed for Arch Linux with the KDE Plasma desktop environment, but should work in other distributions as well as with limitations in Windows.

## Installation

Download the project:

``` console
git clone https://github.com/JoerdonFryeman/Matrix
cd Matrix
```

### For Linux

Just run the script in your console:
``` console
python main.py
```

### For Windows

Create and activate a virtual environment:

``` console
python -m venv venv
venv\Scripts\activate
```

Install the requirements and run the script in your console:

``` console
python.exe -m pip install --upgrade pip
pip install -r requirements_for_windows.txt
python main.py
```

## Stop

Just press Enter or try any other key.

## Settings

Some program settings can be specified in the config.json file.

![matrix_colors](https://github.com/user-attachments/assets/6da55b9c-defb-41be-891d-7165047a3b04)

- Change the color of symbols: BLACK, BLUE, CYAN, GREEN, MAGENTA, RED, WHITE, YELLOW.
- Enable or disable matrix or neo modules.
- Write your own sentences for example: "Fall asleep, Neo...".
- You can also choose the rate of threads, bold symbols and speed of rain.
- With true or false you can enable or disable some kinds of symbols and the rainbow or lego color mode.

The default settings can be restored by deleting the config.json file and restarting the program.

## License

This project is being developed under the MIT license.

## Support with Bitcoin

bc1qewfgtrrg2gqgtvzl5d2pr9pte685pp5n3g6scy
