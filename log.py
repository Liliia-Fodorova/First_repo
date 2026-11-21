from colorama import Fore

def log_info(message):
    print(f"{Fore.BLUE} [INFO] {Fore.RESET} {message}")

def log_warning(message):
    print(f"{Fore.YELLOW} [WARNING] {Fore.RESET} {message}")

def log_error(message):
    print(f"{Fore.RED} [ERROR] {Fore.RESET} {message}")


log_info("Программа запущена")
log_warning("Внимание!")
log_error("Произошла ошибка")    
