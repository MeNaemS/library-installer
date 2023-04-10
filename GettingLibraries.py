def installing_libraries(libraries: list) -> None:  # Installing libraries and displaying an error, if any.
    try:
        getting_libraries(libraries)
    except ImportError:
        from subprocess import run
        
        print('Colorama module not found. Installing the colorama module... ')
        colorama = run(['pip', 'install', 'colorama'])
        if colorama.returncode != 0:
            print(f'Failed to install colorama module, please try to install it manually.\n {colorama.stderr.decode("utf-8")}')
        else:
            from colorama import Fore

            print(Fore.GREEN + f'The colorama has been installed. Restart the program.')


def getting_libraries(libraries: list) -> None:  # The subroutine takes as input a list that includes modules, libraries that need to be installed, returns nothing.
    from threading import Thread
    from colorama import init as init_colorama, Fore

    def letter_animation(text: str) -> None:  # The local function that takes the text to animate the ellipsis returns nothing.
        from itertools import cycle
        from time import sleep

        it, words = cycle(['.'] * 3 + ['\b \b'] * 3), text
        print(words, end='')
        while processes[0].is_alive():
            print(next(it), end='', flush=True)
            sleep(.3)

    def subprocess_output(command: str) -> None:  # A local function that takes a cmd command and then installs the necessary modules, libraries, returns nothing.
        from subprocess import check_output, run

        modules = check_output(command.split(), encoding='cp866').split('\n')
        print(Fore.GREEN + '\nInstalled modules received.')
        modules = [module.split('=')[0] for module in modules]
        for library in libraries:
            if library not in modules:
                print(f'{library} module not found. Module installation in progress...')
                output = run(['pip', 'install', library])
                if output.returncode != 0:
                    print(Fore.RED + f'Error installing {library}\n {output.stderr.decode("utf-8")}')
                    continue
            print(Fore.GREEN + f'The {library} has been installed')

    init_colorama(autoreset=True)
    processes = []
    for index in range(2):
        processes.append(Thread(target=subprocess_output, args=('pip freeze',))) if index == 0 else processes.append(Thread(target=letter_animation, args=('Please wait, checking installed modules',)))
        processes[index].start()
    for process in processes:
        process.join()
