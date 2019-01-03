import requests
import json

class CommandUI:
    def __init__(self):
        exited = False
        while not exited:
            print("Valid commands:")
            print("->'1' to define a build and their locations (latitude, longitude)")
            print("->'2' to list all users that are logged-in into the system")
            print("->'3' to list all users that are inside a certaint building")
            print("->'4' to list the history of all the users movements and exchanged messages")
            print("->'5' to exit\n")

            cmd = input("> ")

            if cmd == '1':
                building_type = input("Type (campus, building): ")
                
                if building_type.lower() == 'campus':
                    pass
                elif building_type.lower() == 'building':
                    pass
                else:
                    print("Wrong building type!\n")

            elif cmd == '2':
                print("")
            elif cmd == '3':
                print("")
            elif cmd == '4':
                print("")
            elif cmd == '5':
                exited = True
            else:
                print("Invalid command!\n")