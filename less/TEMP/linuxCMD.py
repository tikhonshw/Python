import os
import subprocess 
# for simple commands
# subprocess.run(["ls", "-l"])
# for complex commands, with many args, use string + `shell=True`:
# cmd = "sshpass -p otstoj111 ssh -p 10018 user@10.3.103.100 df / | grep / | awk '{ print $5}' | sed 's/%//g'"
# cmd_str = subprocess.run(cmd, shell=True).stdout
 
# command = "sshpass -p otstoj111 ssh -p 10018 user@10.3.103.100 df / | grep / | awk '{ print $5}' | sed 's/%//g'"
# p = subprocess.Popen(command)
# text = p.stdout.read()
# retcode = p.wait()

# print('result text: ', text)

# print('result: ', cmd_str)



# percent = os.popen("sshpass -p otstoj111 ssh -p 10018 user@10.3.103.100 df / | grep / | awk '{ print $5}' | sed 's/%//g'").read()
lastFile = os.popen("ls -Art /home/user/MySoft/###Liana/###Back-Up/ | tail -n 1").read()
lastFile = "/home/user/MySoft/###Liana/###Back-Up/" + lastFile
dateFile = os.popen("stat " + lastFile).read()
ls --full-time  /home/user/MySoft/###Liana/###Back-Up/ | tail -n 1 | awk '{ print $6 " " $9}'

print('result: ', lastFile, ' dateFile: ', lastFile , " - ", dateFile)


 