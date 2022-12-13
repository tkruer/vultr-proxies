import os
from os import environ
from src import tools
from dotenv import load_dotenv

def main():
    if not os.path.exists('.env'):
        print('No .env file found')
        exit(1)
    else:
        load_dotenv()
        api_key = os.environ.get('API_KEY')
        tools.loadscript(key=api_key)
        choice = input('Do you want to create or destroy proxies? (enter "C" or "D") or write current proxies to text file(enter "W")?')
        if choice == 'C' or choice == 'c':
            tools.server_create(key=api_key)
        elif choice == 'D' or choice== 'd':
            tools.server_destroy(key=api_key)
        elif choice == 'W' or choice == 'w':
            tools.write_to_file(key=api_key)
        else:
            print('You entered your something incorrectly, please enter as specified.')
            main()

if __name__ == "__main__":
    main()
