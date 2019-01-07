from inputs_validator import InputsValidator
 
class CommandUI: 
    def __init__(self):
        validor = InputsValidator()

        exited = False 
        while not exited: 
            print("Valid commands:") 
            print("-'1' to define a build and their locations (latitude, longitude)") 
            print("-'2' to list all users that are logged-in into the system") 
            print("-'3' to list all users that are inside a certain building") 
            print("-'4' to list the history of all the users movements and exchanged messages") 
            print("-'exit' or 'q' to exit\n") 
 
            cmd = input("> ") 
 
            if cmd == '1':                 
                validor.checkBuilding()
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