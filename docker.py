import os
import subprocess as sb
from time import sleep
import webbrowser

def install():
  res=sb.getstatusoutput("rpm -q docker-ce")
  if res[0]==1:
    sleep(1)
    sb.getstatusoutput("wget https://download.docker.com/linux/centos/7/x86_64/stable/")
    out=sb.getstatusoutput("yum install docker-ce  --nobest")
    os.system("tput setaf 3")
    if out[0] == "1":
        print("Succesfully installed!!")
    else:
        os.system("tput seta4 4")
        print("Failed!!")
    
      
   
   
  print("""
       -----------------------------------
       Press 1.Install docker
       Press 2:To start docker
       Press 3:To stop docker
       Press 4:To check docker info
       Press 5:To check docker help
       Press 6:To pull docker image
       Press 7:To check list of all os images
       Press 8:To run docker os
       Press 9:To run docker os in background
       Press 10:To run a single command in the docker
       Press 11:To check current running os
       Press 12:To check all running os
       Press 13:To configure webserver
       Press 14:To exit
       -------------------------------------
       """)
       
       
ch = input("Enter what  u want to do : ")
                if int(ch) == 1:
                install()
                time.sleep(5)
                
            if int(ch) == 2:
                sb.getstatusoutput("systemctl start docker")
                time.sleep(5)

            elif int(ch) == 3:
                sb.getstatusoutput("systemctl stop docker")
                time.sleep(5)

            elif int(ch) == 4:
                sb.getoutput("docker info",shell=True)
                time.sleep(5)

            elif int(ch) == 5:
                sb.getoutput("docker --help",shell=True)
                time.sleep(5)
                
            elif int(ch) == 6:
                print("""
                image example 
                1. Centos 
                2. Fedora
                3. Ubuntu
                ...etc..
                     """)
                image = input("Enter the name of image ")
                p=sb.getstatusoutput("docker pull {}".format(image))
                if p[0] == "1":
                  print("Succesfully installed the image of OS")
                else:
                  print("Failed")
                  
            elif int(ch) == 7:
                sb.getoutput("docker images",shell=True)
                time.sleep(5)
                
            elif int(ch) == 8:
                name = input("Enter the name of os")
                img = input("Enter the name of img")
                sb.call("docker run -it --name {} {}".format(name, img),shell=True)
                
            elif int(ch) == 9:
                name = input("Enter the name of os")
                img = input("Enter the name of image")
                sb.call("docker run -dit --name {} {}".format(name, img),shell=True)
                
            elif int(ch) == 11:
                sb.getoutput("docker ps",shell=True)
                time.sleep(5)
                
            elif int(ch) == 12:
                sb.getoutput("docker ps -a",shell=True)
                time.sleep(5)
            
            elif int(ch) == 13:
            
                
            elif int(ch) == 14:
                exit()
            else:
                print("Not supported ")
                
       
                
                         
