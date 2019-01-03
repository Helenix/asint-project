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

                if building_type == 'CAMPUS' or building_type == 'BUILDING': 
                   
                    building_name = input("Name: ")
                    try:
                        input_holder = input("Building ID: ")
                        building_id = int(input_holder)
                        if building_type == 'BUILDING':
                            input_holder = input("Top level space ID: ")
                            building_top_level_id = int(input_holder)
                    except ValueError:
                        print("ID's must be integers!\n")
                        continue

                    if building_type == 'BUILDING':
                        try:
                            input_holder = input("Bottom latitude: ")
                            building_botLat = float(input_holder)
                            input_holder = input("Left longitude: ")
                            building_leftLng = float(input_holder)
                            input_holder = input("Top latitude: ")
                            building_topLat = float(input_holder)
                            input_holder = input("Right longitude: ")
                            building_rightLng = float(input_holder)
                        except ValueError:
                            print("Latitudes and longitudes must be floats!\n")
                            continue
                    
                    building_info = {
                        'type': building_type,
                        'id': building_id,
                        'name': building_name
                    }
                    if building_type == 'BUILDING':
                        building_info['topLevelId'] = building_top_level_id
                        building_info['botLat'] = building_botLat
                        building_info['leftLng'] = building_leftLng
                        building_info['topLat'] = building_topLat
                        building_info['rightLng'] = building_rightLng

                    url = "http://127.0.0.1:5000/api/admin"

                    response = requests.post(url + "/building", json = building_info)
                    print(response.json())

                    
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

