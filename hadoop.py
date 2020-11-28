import os
import getpass
import time
import webbrowser

def file(fp, ip, n):
	file = open("{}".format(fp), 'r')
	contents = file.readlines()
	file.close()

	initial = contents.index('<configuration>\n')
	final = contents.index('</configuration>\n')

	del contents[initial+1:final]
	if fp == '/etc/hadoop/hdfs-site.xml':
		contents.insert(initial + 1, "<property>\n")
		if n == 1:
			contents.insert(initial + 2, "<name>dfs.name.dir</name>\n")
		else:
			contents.insert(initial + 2, "<name>dfs.data.dir</name>\n")
		contents.insert(initial + 3, "<value>/nn</value>\n")
		contents.insert(initial + 4, "</property>\n")
	elif fp == '/etc/hadoop/core-site.xml':
		contents.insert(initial + 1, "<property>\n")
		contents.insert(initial + 2, "<name>fs.default.name</name>\n")
		contents.insert(initial + 3, "<value>hdfs://{}:9001</value>\n".format(ip))
		contents.insert(initial + 4, "</property>\n")
	else:
		sb.call('echo "configuration file not found"', shell=True)

	file = open("{}".format(fp), "w")
	new_content = "".join(contents)
	file.write(new_content)
	file.close()

def namenode( ) :
	os.system("echo 'NAMENODE:'")
	ip=input("Enter the ip address of namenode: \n")
	os.system("echo 'Configuring hdfs-site.xml...'")
	file('/etc/hadoop/hdfs-site.xml',ip,1)
	time.sleep(1)
	os.system("echo 'Configuring core-site.xml...'")
	file('/etc/hadoop/core-site.xml',ip,1)
	time.sleep(1)
	os.system("rm -rf /nn")
	os.system("mkdir /nn")
	o=os.system("echo 'Y' | hadoop namenode -format")
	if o[0] == 0:
		os.system(" echo 'Succesfully formatted Namenode'")
	else:
		print("Error ")
	os.system("echo 3 > /proc/sys/vm/drop_caches")
	os.system("hadoop-daemon.sh start namenode")
	os.system("jps")

def datanode( ):
	os.system("echo 'DATANODE:'")
	ip = input("Enter the ip address of namenode: \n")
	os.system("echo 'Configuring hdfs-site.xml...'")
	file('/etc/hadoop/hdfs-site.xml', ip, 0)
	time.sleep(1)
	os.system("echo 'Configuring core-site.xml...'")
	file('/etc/hadoop/core-site.xml', ip, 0)
	time.sleep(1)
	os.system("rm -rf /nn")
	os.system("mkdir /nn")
	os.system("systemctl stop firewalld")
	os.system("echo 3 > /proc/sys/vm/drop_caches")
	os.system("hadoop-daemon.sh start datanode")
	os.system("jps")

def clientnode( ):
	os.system("echo 'CLIENTNODE:'")
	ip=input("Enter the ip address of namenode: \n")
	file('/etc/hadoop/core-site.xml',ip,1)
	time.sleep(1)
	os.system("echo 'Configured client'")



os.system("tput setaf 4")
print("--------------------------------------------------------------------")
os.system("tput setaf 11")
print("\t\t\tWelcome to World Automation")
os.system("tput setaf 4")
print("--------------------------------------------------------------------")

password = getpass.getpass("Enter ur password : \n")

os.system("tput setaf 1")
if password != "password":
    print("password is incorrect!! ")
    exit()
    
    
print("""
         Press 1:Configure master node/name node
         Press 2:Configure slave node/data node
         Press 3:Configure client
         Press 4:To upload file from client 
         Press 5:To read the existing files in the hadoop
         Press 6:To delete a file 
         Press 7:To check the hdfs report
         Press 8:To see the report in WebUI
         Press 9:To start name node
         Press 10:To start data node
         Press 11:To stop namenode
         Press 12:To stop datanode
         Press 13:To exit
         """)
	        ch=input("Enter what you want to do : ")


            #configure namenode
	        if int(ch) == 1:
		        namenode()
		        os.system("hadoop dfsadmin -report")

            #configure datanode
	        elif int(ch)==2:
		        datanode()
		        os.system("hadoop dfsadmin -report")

            #configure clientnode
	        elif int(ch) ==3:
                clientnode()
                
            # uplaoding the contents of file
	        elif int(ch) == 4:
                p = os.chdir('/')
		        fname = input('Enter the file name:')

		        f = open(fname, "w+")
		        data = input("Enter the contents of file:\n")
		        f.write(data)
		        f.close()

		        os.system('cd')
		        size = input("Enter the block size(Default block size=64MB):\n")
		        os.system('hadoop fs -Ddfs.block.size={} -put {} {}'.format(size, fname, p))
		        os.chdir('/')
		        p = os.system('ls')

        # reading the contents of the file
	    elif int(ch) == 5:
		        a = os.chdir('/')
		        print("List of existing files:\n")
		        p = os.system('ls')
		        i = input("Which file do you want to open?")
		        print("The contents of the file are:")
		        f = open(i, "r")

		        if f.mode == "r":
			        contents = f.read()
			        print(contents)

       # deleting files
	   elif int(ch) == 6:
		        os.chdir('/')
		        p = os.system('ls')
		        d = input("Which file do you want to delete?")
		        os.system('rm {}'.format(d))
		        print("File Removed\n")
		        r = os.system('ls')

      # to see the report
	   elif int(ch) == 7:
		        rep = os.system('hadoop dfsadmin -report')

      # to see report in webui
	  elif int(ch) == 8:
		        ipa = input("Enter the ip address of master node:")
		        webbrowser.open('http://{}:50070'.format(ipa))

      # to start namenode
	  elif int(ch) == 9:
		        os.system('hadoop namenode -format')
		        os.system('echo 3 > /proc/sys/vm/drop_caches')
		        os.system('hadoop-daemon.sh start namenode')
		        res = os.system('jps')

     # to start datanode
	 elif int(ch) == 10:
		        os.system('systemctl stop firewalld')
		        os.system('echo 3 > /proc/sys/vm/drop_caches')
		        os.system('hadoop-daemon.sh start datanode')
		        res = os.system('jps')

     # to stop namenode
	 elif int(ch) == 11:
		        os.system('hadoop-daemon.sh stop namenode')
     # to stop datanode
	 elif int(ch) == 12:
		        os.system('hadoop-daemon.sh stop datanode')

     # to exit
	  elif int(ch) == 13:
		        exit()

	  else:
		        print("Not Supported\n")
		        exit()
  
       

