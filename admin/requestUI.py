class RequestUI:
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