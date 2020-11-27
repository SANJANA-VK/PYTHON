import os
import time
import subprocess as sb
from keyboard import press


//FUNCTIONS    
def Lvm():                            //Creates lvm partition
    ch=input("Do you want to know the hard disk information:[Y/N]\n")
    if ch=="Y" or ch=="y":
        sb.call("fdisk -l",shell=True)
        time.sleep(2)

    hdname=input("\nEnter the hard disk name: \n")
    sb.call("pvcreate {}".format(hdname),shell=True)

    ch1=input("Do you want to see the physical volume info:[Y/N]\n")
    if ch1=="Y" or ch1=="y":
        sb.call("pvdisplay {}".format(hdname),shell=True)
        time.sleep(2)

    vname=input("Enter the vg name: \n")
    sb.call("vgcreate {} {}".format(vname,hdname),shell=True)

    ch2 = input("Do you want to see the volume group info:[Y/N]\n")
    if ch2 == "Y" or ch2 == "y":
        sb.call("vgdisplay {}".format(vname), shell=True)
        time.sleep(2)

    lv=input("Enter the name of lv: \n")
    size=input("Enter the size of lv: \n")
    sb.call("lvcreate --size {} --name {} {}".format(size,lv,vname),shell=True)

    ch3 = input("Do you want to see the lvm info:[Y/N]\n")
    if ch3 == "Y" or ch3 == "y":
        sb.call("lvdisplay {}/{}".format(vname,lv), shell=True)
        time.sleep(2)

    sb.getoutput("mkfs.ext4 /dev/{}/{}".format(vname,lv))

    dir=input("Enter the directory name: \n")
    sb.call("mkdir /{}".format(dir),shell=True)
    sb.call("mount /dev/{}/{}  /{}".format(vname,lv,dir),shell=True)
    time.sleep(1)

    ch4 = input("Do you want to see the hard disk info:[Y/N]\n")
    if ch4 == "Y" or ch4 == "y":
        sb.call("df -h", shell=True)

def increase():
    path=input("Enter the path of lv: \n")
    size1=input("Enter the size: \n")
    sb.call("lvextend --size +{} /dev/{}".format(size1,path),shell=True)
    sb.call("resize2fs {}".format(path),shell=True)
    sb.call("df -h",shell =True)

def decrease():
    m=input("Enter the mount point: \n")
    sb.call("umount {}".format(m),shell=True)
    vname=input("Enter the vg name:\n")
    lv=input("Enter the name of lv: \n")
    sb.call("e2fsck -f /dev/mapper/{}-{}".format(vname,lv),shell=True)
    sb.call("resize2fs /dev/mapper/{}-{}".format(vname,lv),shell=True)
    size2=input("Enter the size to be reduced: \n")
    sb.call("lvreduce --size -{} /dev/mapper/{}-{}".format(size2,vname,lv),shell=True)
    sb.call("mount /dev/{}/{}".format(vname,m),shell=True)
   
   
def partition():
    ch=input("Do you want to know the hard disk information:[Y/N]\n")
    if ch=="Y" or ch=="y":
        sb.call("fdisk -l",shell=True)
        time.sleep(2)
    
    hd=input("Enter the hard disk you want to use for partition: \n")
    s=input("Enter the size of the partition: \n")
    mount=input("Folder name/Mount Point: \n")
    sb.getoutput("fdisk {}".format(hd),shell=True)
    time.sleep(2)
    os.system("echo p")
    press('enter')
    time.sleep(2)
    os.system("echo n")
    press('enter')
    time.sleep(2)
    press('enter')
    time.sleep(2)
    os.system("echo $s")
    press('enter')
    time.sleep(2)
    os.system("echo w")
    press('enter')
    sb.getoutput("udevadm settle",shell=True)
    sb.getoutput("mkfs.ext4  {}".format(hd),shell=True)
    sb.getoutput("mkdir /{}".format(mount))
    sb.getoutput("mount {}/{}".format(hd,mount),shell=True)
    sb.getoutput("df -h",shell=True)
    
def change_permission():
    dir=input("Enter the path of the file: /n")
    sb.getoutput("ls  -l {}".format(dir),shell=True)
    person=input("Whose permission you want to change? 
                    -To chnage owner permission PRESS o\n
                    -To change user permission PRESS u\n
                    -To change group permission PRESS g\n
                    ")
    permissions=input("List of permissions:\n  r(read) \n  w(write) \n x(execute)\n")
    sign=input("To remove permission press '-'\n To add permission press '+'\n")
    sb.call("chmod {}{}{}".format(person,sign,permissions,shell=True)
    
def change_owner():
    owner=input("Enter the new owner name: \n")
    file=input("Enter the file name: \n")
    sb.call("chown {} {}".format(owner,file),shell=True)
  
    
    

print("""
    --------------------------------
        Press 1: File handling
        Press 2: Storage
        Press 3: Networking
        Press 4: Configure servers/Downloading softwares
        Press 5: User Adminstration
        Press 6: Exit 

   -------------------------------
   """)
    
    
  
ch = input("What would you want to do today?")


if int(ch)==1:                        //FILE HANDLING
  os.system("clear")
  
  print("""
      --------------------------------------
          Press 1:Create a directory
          Press 2:Remove the directory
          Press 3:Create file 
          Press 4:Delete the file
          Press 5:View the contents of file
          Press 6:To view list of files present in a directory
          Press 7:To view the permissions given to a directory or a file
          Press 8:To change the given permissions to file
          Press 9:To change the owner of file
          Press 10:To exit
      --------------------------------------
     """)
     
     ch1=input("What is your choice?\n")
     ch1=int(ch1)
     
    if ch1==1:
      dir=input("Enter the directory name: \n")
      sb.getstatusoutput("mkdir {}",format(dir))
      time.sleep(5)
      continue
      
    elif ch2==2:
      dir=input("Enter the name of the directory you want to delete: \n")
      sb.call("rmdir {}".format(dir))
      time.sleep(5)
      continue
      
    elif ch1==3:
      file=input("Enter the file name along with the path : \n")
      contents=input("Enter the contents of the file: \n")
      f= open("{}".format(file),"w+")
      f.write(contents)
      f.close()
      time.sleep(5)
      continue
      
    elif ch1==4:
      file=input("Enter the file name along with path : \n")
      sb.call("rm {}".format(file),shell=True)
      time.sleep(5)
      continue
      
    elif ch1==5:
      file=input("Enter the file name along with path : \n")
      sb.getoutput("cat {}",format(file),shell=True)
      time.sleep(5)
      continue
      
    elif ch1==6:
      dir=input("Enter the path of the directory: /n")
      sb.getoutput("ls {}".format(dir),shell=True)
      time.sleep(5)
      continue
      
    elif ch1==7:
      dir=input("Enter the path of the directory: /n")
      sb.getoutput("ls  -l {}".format(dir),shell=True)
      time.sleep(5)
      continue
      
    elif ch1==8:
      change_permission()
      time.sleep(5)
      continue
      
    elif ch1==9:
      change_owner()
      time.sleep(5)
      continue
      
    elif ch1==10:
      exit()
      
    else:
      print("Not Supported!!\n")
      exit()
      
elif int(ch)==2:                      //STORAGE
  os.system("clear")
  
  print("""
      --------------------------------------
          Press 1:To know the information of hard disk
          Press 2:To know the infromation of  ram
          Press 3:To delete cache memory
          Press 4:To create partition
          Press 5:To create lvm partition
          Press 6:To increase lvm partition
          Press 7:To decrease lvm partition
          Press 8:To exit
      --------------------------------------
     """)
   ch3=int(input("Enter your choice \n"))
   
   if ch3==1:
    sb.getoutput("df -h",shell=True)
    time.sleep(5)
    continue
    
  elif ch3==2:
    sb.getoutput("free -m",shell=True)
    time.sleep(5)
    continue
    
  elif ch3==3:
    sb.getoutput("echo 3 > /proc/sys/vm/drop_caches",shell=True)
    time.sleep(5)
    continue
    
  elif ch3==4:
    partition()
    time.sleep(5)
    continue
    
  elif ch3==5:
    lvm()
    time.sleep(5)
    continue
  
  elif ch3==6:
    increase()
    time.sleep(5)
    continue
    
  elif ch3==7:
    decrease()
    time.sleep(5)
    continue
    
  elif ch3==8:
    exit()
    
  else:
    print("Not Supported\n")
    exit()
    
    
elif int(ch)==3:                      //NETWORKING
  os.system("clear")
  
  print("""
      --------------------------------------
          Press 1:To know the ip address
          Press 2:To know the router name
          Press 3:To change ip address
          Press 4:To connect a remote server
          Press 5:To connect to a remote server to a particular user
          Press 6:To check the n/w connectivity
          Press 7:To enable selinux
          Press 8:To disable selinux
          Press 9:To run a command on diffrent server
          Press 10:To exit
      --------------------------------------
     """)
    
  ch4=int(input("Enter your choice: \n"))
  
  if ch4==1:
    os.system("ifconfig ")
    time.sleep(5)
    continue
    
  elif ch4==2:
    os.system("route -n")
    time.sleep(5)
    continue
    
  elif ch4==3:
    ip=input("Enter the ip address: \n")
    nm=input("Enter the netmask: \n")
    os.system("ifconfig enp0s3 {} netmask {}".format(ip,nm))
    time.sleep(5)
    continue
    
  elif ch4==4:
    ip=input("Enter the ip address: \n")
    os.system("ssh {}".format(ip))
    time.sleep(5)
    continue
    
  elif ch4==5:
    ip=input("Enter the ip address: \n")
    user=input("Enter the username: /n")
    os.system("ssh@{} {}",format(user,ip))
    time.sleep(5)
    continue
    
 elif ch4==6:
    url=input("Enter url  of the server: \n")
    os.system("nslookup {}".format(url))
    time.sleep(5)
    continue
    
 elif ch4==7:
  os.system("setenforce 0")
  time.sleep(5)
  continue
 
 elif ch4==8:
  os.system("setenforce 1")
  time.sleep(5)
  continue
  
 elif ch4==9:
  ip=input("Enter the ip address: \n")
  command=input("Enter the command: \n")
  user=input("Enter the user: \n")
  if user=="":
    os.system("ssh {} {}",format(ip,command))
  elif:
    os.system("ssh -t  -l {} {} sudo {}".format( user,ip,command))
  time.sleep(5)
  continue
  
 elif ch4==10:
  exit()
  
else:
  print("Not supported\n")
  exit()
  
  
elif int(ch)==5:                      //USER ADMINSTRATION
  os.system("clear")
  
  print("""
      --------------------------------------
          Press 1:To add user
          Press 2:To create a group
          Press 3:To add a user to group
          Press 4:To login to the user
          Press 5:To see the list of users
          Press 6:To see the list of groups
          Press 7:To change the permission
          Press 8:To change the owner
          Press 9:To know user id
          Press 10:To exit
      --------------------------------------
     """)
  ch5=int(input("Enter your choice:\n")
  
  if ch5==1:
    name=input("Enter the user name: \n")
    os.system("useradd {}".format(name))
    os.system("passwd {}".format(name))
    time.sleep(5)
    continue
    
  elif ch5==2:
    name=input("Enter the group name: \n")
    os.system("groupadd {}".format(name))
    time.sleep(5)
    continue
  
  elif ch==3:
    gname=input("Enter the group name: \n")
    name=input("Enter the user name: \n")
    os.system("groupadd -G {} {}".format(gname,name))
    time.sleep(5)
    continue
    
  elif ch==4:
    name=input("Enter the username: \n")
    os.system("su {}".format(user))
    
  elif ch==5:
    //under process
    
  elif ch==6:
    //under permissions
    
  elif ch==7:
    change_permission()
    time.sleep(2)
    continue
    
  elif ch==8:
    change_owner()
    time.sleep(2)
    continue
    
  elif ch==9:
    user=input("Enter the name of user:\n")
    os.system("id -u {}".format(user))
    time.sleep(4)
    continue
    
  elif ch==10:
    exit()
  
  else:
  print("Not Supported")
  exit()
  
  
  
  
else:
  print("Thank You\n")
  exit()
    
    
  
    
    
    

    
    
 
  
  
    
    
   
      
      
      
   
    
      
      
