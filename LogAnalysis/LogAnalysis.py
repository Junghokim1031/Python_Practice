import datetime
import time
import random
import pandas as pd

servers = ["Server A", "Server B", "Server C"]

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