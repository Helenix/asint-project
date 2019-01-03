import getpass
import requests
import json

if __name__ == "__main__":
    logged = False
    while not logged:
        name = input('Login name: ')
        password = getpass.getpass('Password: ')

        login_info = {
            'name': name,
            'password': password
        }

        url = "http://127.0.0.1:5000/api/admin"

        response = requests.get(url + "/login", json = login_info)

        response_json = response.json()

        try:
            token = response_json['token'] 
            logged = True
            print('Login successfull!\n')

        except:
            print('Error in login!\n')
           
    # Start requests
    exited = False
    while not exited:
        print("Valid commands:")
        print("->'1' for ")
        print("->'2' for ")
        print("->'3' for ")
        print("->'4' for ")
        print("->'5' for exit\n")

        cmd = input("> ")

        if cmd is '1':
            print("")
        elif cmd is '2':
            print("")
        elif cmd is '3':
            print("")
        elif cmd is '4':
            print("")
        elif cmd is '5':
            exited = True
        else:
            print("Invalid command!\n")