import socket
from tabulate import tabulate

print("""
               
___________.__                 __                  ________                     .__                                       __   
\_   _____/|  | _____    ____ |  | __ ___________  \______ \   _______  __ ____ |  |   ____ ______   _____   ____   _____/  |_ 
 |    __)  |  | \__  \  /    \|  |/ // __ \_  __ \  |    |  \_/ __ \  \/ // __ \|  |  /  _ \\____ \ /     \_/ __ \ /    \   __\
 |     \   |  |__/ __ \|   |  \    <\  ___/|  | \/  |    `   \  ___/\   /\  ___/|  |_(  <_> )  |_> >  Y Y  \  ___/|   |  \  |  
 \___  /   |____(____  /___|  /__|_ \\___  >__|    /_______  /\___  >\_/  \___  >____/\____/|   __/|__|_|  /\___  >___|  /__|  
     \/              \/     \/     \/    \/                \/     \/          \/            |__|         \/     \/     \/      
                      __________                                      __                                                       
                      \______   \_______   ____   ______ ____   _____/  |_  ______                                             
                       |     ___/\_  __ \_/ __ \ /  ___// __ \ /    \   __\/  ___/                                             
                       |    |     |  | \/\  ___/ \___ \\  ___/|   |  \  |  \___ \                                              
                       |____|     |__|    \___  >____  >\___  >___|  /__| /____  >                                             
                                              \/     \/     \/     \/          \/                                              
     
""")

host_name_input = input("Write the host name: ")

class Ip_Host(object):
    def __init__(self, url=host_name_input):
        self.url = url
        self.host_name = socket.gethostname()
        self.ip_adress = socket.gethostbyname(self.host_name)
        self.remote_ip = self.remote_info()

    def __repr__(self):
        data = {"Host Name:": [self.host_name],
                "Ip Adress:": [self.ip_adress],
                f"{self.url}:": [self.remote_ip]}
        table = tabulate(data, headers="keys", tablefmt="pretty")
        return table
    
    def remote_info(self):
        try:
            return socket.gethostbyname(self.url)
        except socket.error as err_msg:
            return err_msg
        
if __name__ == "__main__":
    print(Ip_Host())