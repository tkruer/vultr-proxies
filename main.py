import os
from os import environ
from src import tools

def main():
    if not os.path.exists('.env'):
        print('No .env file found')
        exit(1)
    else:
        choice = input('Do you want to create or destroy proxies? (enter "C" or "D") or write current proxies to text file(enter "W")?')
        if choice == 'C' or choice == 'c':
            tools.server_create()
        elif choice == 'D' or choice== 'd':
            tools.server_destroy()
        elif choice == 'W' or choice == 'w':
            tools.write_to_file()
        else:
            print('You entered your something incorrectly, please enter as specified.')
            main()

if __name__ == "__main__":
    main()
