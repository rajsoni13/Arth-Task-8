import os
import getpass


r = input("Where to want to run This menu ? (Local/Remote) : ")
print(r)

while True:
	
	os.system("clear")
	os.system("tput setaf 14")
	print("""
	\n\t\t\t
	-----------------------rhcl8 basic---------------------------
	\n
	Press 1 : To know current Date 
	Press 2 : To know time in 12Hour Formate
	Press 3 : To open Calender
	Press 4 : To check connectivity between you and Website/System	
	Press 5 : To open Firefox
	Press 6 : To Search something in browser
	Press 7 : To create New TextFile
	Press 8 : To create New Folder
	Press 9 : To remove existing Folder
	Press 10 : To check which account you are logged in
	Press 11 : To create new file
	Press 12 : To open existing file
	Press 13 : To remove existing file
	Press 14 : To list all file inside folder
	Press 15 : To know how many data we can store in folder
	Press 16 : To know how many space free in RAM
	Press 17 : To know how many CPU working now
	Press 18 : To print exactly as you type
	Press 19 : To know used command history
	Press 20 : To See manual of particular program or software
	Press 21 : To know path where we are located now
	Press 22 : To know software version
	Press 23 : To know current status of Network card/current ip 
	""")
	os.system("tput setaf 10")
	print("""
	\n\t\t\t
	---------------------------AWS CLI-------------------------------
	\n
	Press 24 : To Create Keypair
	Press 25 : To Create Security Group
	Press 26 : To Launch Instance
	Press 27 : To create new Volume
	Press 28 : To Attach Volume
	
	""")
	#os.system("tput setaf 19")

	print("""
	\n
	\t\t\t
	--------------------Web server Configuration------------------------
	\n
	Press 29 : To Configure WebServer
	Press 30 : To check webserver Status Active or Not..
	Press 0  : To Exit 
	""")
	

	ch = input("Enter Choice : ")
	print(ch)

	if r == "Local":
		if int(ch) == 1:
		    os.system("date")

		elif int(ch) == 2: 	
		    os.system("date +%r")

		elif int(ch) == 3: 	
		    os.system("cal")
	
		elif int(ch) == 4: 	
		    ping = input("Enter Website Name/System ip : ")
		    os.system("ping {}".format(ping))

		elif int(ch) == 5: 	
		    os.system("firefox")

		elif int(ch) == 6: 
		    search = input("Type here what do you want to search : ")	
		    os.system("firefox {}".format(search))

		elif int(ch) == 7: 
		    textEditor = input("Give name for text file: ")	
		    os.system("gedit {}".format(textEditor))

		elif int(ch) == 8: 
		    folname = input("Give name for new Folder: ")	
		    os.system("mkdir {}".format(folname))

		elif int(ch) == 9: 
		    rmfolname = input("Give name for remove Folder: ")	
		    os.system("rmdir {}".format(rmfolname))

		elif int(ch) == 10: 	
		    os.system("whoami")

		elif int(ch) == 11: 
		    filename = input("Give File name : ")	
		    os.system("vim {}".format(filename))

		elif int(ch) == 12: 
		    filename = input("Give File name to open: ")	
		    os.system("vi {}".format(filename))

		elif int(ch) == 13: 
		    rmfilename = input("Give File name to remove : ")	
		    os.system("unlink {}".format(rmfilename))

		elif int(ch) == 14: 
		    listn = input("Give Folder name to list all file included : ")	
		    os.system("ls {}".format(listn))

		elif int(ch) == 15: 
		    lisn = input("Give Folder name to know how many data we can store : ")	
		    os.system("df -h {}".format(lisn))

		elif int(ch) == 16: 
		    os.system("free -m ")

		elif int(ch) == 17: 
		    os.system("lscpu")

		elif int(ch) == 18: 
		    echo = input("Enter text which you want to print :")
		    os.system("echo {}".format(echo))

		elif int(ch) == 19: 
		    os.system("history")

		elif int(ch) == 20: 
		    man = input("Enter program name to see manual :")
		    os.system("man {}".format(man))

		elif int(ch) == 21: 
		    os.system("pwd")

		elif int(ch) == 22: 
		    ver = input("Enter program name to see version :")
		    os.system("{} --version".format(ver))

		elif int(ch) == 23: 
		    os.system("ifconfig")

		elif int(ch) == 24: 
		    keyname = input("Enter Keypair name: ")	
		    os.system("aws ec2 create-key-pair --key-name {}".format(keyname))

		elif int(ch) == 25: 
		    SecurityGroup = input("Enter SecurityGroup Name: ")	
		    os.system("aws ec2 create-security-group --group-name {} --description AllTraffic".format(SecurityGroup))

		elif int(ch) == 26: 	
		    os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --count 1 --instance-type t2.micro --key-name {} --subnet-id subnet-0b060f63".format(keyname))

		elif int(ch) == 27: 	
		    os.system("aws ec2 create-volume  --availability-zone ap-south-1a  --no-encrypted  --size 1  --volume-type gp2")

		elif int(ch) == 28: 	
		    os.system("aws ec2 attach-volume --volume-id vol-07dcfb6002d6c3142 --instance-id  i-0da134f120ca41640 --device /dev/sdf")

		elif int(ch) == 29: 
		    os.system("yum install httpd")
		    name=input("Enter your file name :")
		    inp=input("Eenter here your file content : ")
		    os.system("touch {}".format(name))
		    os.system("echo '{}' > /var/www/html/{}".format(inp,name))
		    os.system("systemctl start httpd")

  			#os.system("tput setaf 3")
 			#print("================== configuration done =======================")

		elif int(ch) == 30:
		    os.system("systemctl status httpd")


		elif int(ch) == 0:
		    exit()


		

		else:
			print("Your Choice  not Supported..\n Please enter choice from given list")
	
	else:
		print("Not supported to login")

	input("\nPlease enter to continue...")



	
