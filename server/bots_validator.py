class BotsValidator:
    def __init__(self):
        pass

    def checkBot(self, botDict):
        keys = list(botDict.keys())
        args_list = ['acc_name', 'acc_pass', 'acc_building_id']

        for value in args_list:
            if value in keys:
                pass
            else: 
                return False

        return True