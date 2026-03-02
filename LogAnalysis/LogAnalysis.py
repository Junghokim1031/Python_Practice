from sys import argv
import datetime
import time
import random
import pandas as pd

servers = ["Server A", "Server B", "Server C"]
#actions = ["Log in", "Log Out", "Action A", "Action B", "Action C"]
#errrors = ["Error A", "Error B", "Error C"]
#warnings = ["Warning A", "Warning B", "Warning C"]



#with open("Logfile.txt", "a") as file:
#    for x in range(1000):
#        server = random.choice(servers)
#        action = random.choice(actions)
#        error = random.choice(errrors)
#        warning = random.choice(warnings)
#        timestamp = datetime.datetime.now()
#        file.write("%s: %s: %s: %s: %s\n" %(server, action, error, warning,timestamp))
#    print("End of Log")

with open("Server_Log.csv", "w") as file:
    file.write("Timestamp, Server, CPU Usage, Memory Usage, Disk Usage\n")
    for x in range(10000):
        server = random.choice(servers)
        timestamp = datetime.datetime.now()
        cpu = random.randint(0,100)
        memory = random.randint(2,16)*256
        disk = random.randint(0,100)
        file.write("%s, %s, %3d%%, %4d MB, %3d GB\n" %(timestamp, server, cpu, memory, disk))
        time.sleep(0.001)
    print("End of Log")