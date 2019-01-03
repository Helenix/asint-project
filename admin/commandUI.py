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
            print("->'exit' or 'q' to exit\n") 
 
            cmd = input("> ") 
 
            if cmd == '1': 
                input_holder = input("Type (campus, building): ")

                building_type = input_holder.upper()

                if building_type == 'CAMPUS': 
                    # nao sei se vale a pena adicionar campus
                    ''' input_holder = input("ID: ")
                    input_holder = input("Name: ")
                    input_holder = input("Contained Spaces: ") '''
                    pass
                elif building_type == 'BUILDING': 
                    try:
                        input_holder = input("Building ID: ")
                        building_id = int(input_holder)
                        input_holder = input("Top level space ID: ")
                        building_id = int(input_holder)
                    except ValueError:
                        print("ID's must be integers!\n")
                        continue

                    building_name = input("Name: ")
                    
                    try:
                        input_holder = input("Bottom latitude: ")
                        botLat = float(input_holder)
                        input_holder = input("Left longitude: ")
                        leftLng = float(input_holder)
                        input_holder = input("Top latitude: ")
                        topLat = float(input_holder)
                        input_holder = input("Right longitude: ")
                        print("Left longitude must be a float!\n")
                    except ValueError:
                        print("Latitudes and longitudes must be floats!\n")
                        continue

                else: 
                    print("Wrong building type!\n")
 
            elif cmd == '2': 
                print("") 
            elif cmd == '3': 
                print("") 
            elif cmd == '4': 
                print("") 
            elif cmd.lower() == 'exit' or cmd.lower() == 'q': 
                exited = True 
            else: 
                print("Invalid command!\n")

def askCampus():
    print("Campus")

def askBuildind():
    print("Contained")

