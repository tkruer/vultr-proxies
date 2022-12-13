import os
from os import environ
from src import tools
from dotenv import load_dotenv
import json

def main():
    load_dotenv()
    if not os.path.exists('.env'):
        print('No .env file found')
        exit(1)
    else:
        api_key = os.environ.get('API_KEY')
        # fix this here
        choice = input('Do you want to create or destroy proxies? (enter "C" or "D") or write current proxies to text file(enter "W")? or check account info(enter "I")? create script(enter "S")? ')
        if choice == 'I' or choice == 'i':
            accountInfo = tools.loadAccountInfo(key=api_key)
        elif choice == 'S' or choice == 's':
            script = tools.createStartupScript(key=api_key)
        elif choice == 'C' or choice == 'c':
            try:
                tools.createStartupScript(key=api_key)
                proxylocation = input('Enter where you want your proxies located [Miami, Dallas, Seattle, Atlanta, Chicago, LA, NY, Silicon Valley, Germany, France, UK, Amsterdam, Tokyo, Sydney]: ')
                numproxies = input('Enter number of proxies you want to create: ')
                #get json data from src/config.json
                with open('src/config.json') as f:
                    data = json.load(f)
                    scriptid = data['v2_id']
                    tools.create(key=api_key, location=proxylocation, proxies=numproxies, osid=scriptid)
            except:
                print('Error creating proxies')
                exit(1)
        elif choice == 'D' or choice == 'd':
            tools.server_destroy(key=api_key)
        elif choice == 'W' or choice == 'w':
            tools.write_to_file(key=api_key)
        else:
            print('You entered your something incorrectly, please enter as specified.')
            main()

if __name__ == "__main__":
    main()
