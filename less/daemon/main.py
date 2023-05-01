# import daemon
# import os
# import time
# from datetime import datetime 

# def run():
#     print(str(os.getpid()))
#     while True:
#         now = datetime.now() 
#         current_time = now.strftime("%H:%M:%S") 
#         file = open("/home/user/MySoft/Python/less/daemon/test.txt", "w")
#         file.write("hello world " + current_time)
#         file.close()
#         time.sleep(5)

# with daemon.DaemonContext():
#     run()


import os
import time
import daemon
from datetime import datetime 

pid_file = "/home/user/MySoft/Python/less/daemon/test11.pid"

def do_something():
    while True:
        now = datetime.now() 
        current_time = now.strftime("%H:%M:%S") 
        file = open("/home/user/MySoft/Python/less/daemon/test11.txt", "a")
        file.write("hello world " + current_time)
        file.close()
        time.sleep(5)

def run_daemon():
    with open(pid_file, "w") as f:
        f.write(str(os.getpid())) # write PID to file

    with daemon.DaemonContext():
        do_something()

if __name__ == "__main__":
    run_daemon()