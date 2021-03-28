import  os
import getpass

os.system("tput setaf 6")
print("to use this automation feature you first need to install hadoop and this automation will setup your hadoop cluster in 1 click")

os.system("tput setaf 8")

#Hadoop MENU
while True:
    os.system("clear")
    os.system("tput setaf 4")
    print("""
    \n
    press 1 : setup hadoop namenode
    press 2 : setup hadoop datanode
    press 3 : setup hadoop client
    press 4 : to exit 
    """)
    r = input("where you want to run this menu ? local / remote : ")
    print(r)
    os.system("tput setaf 7")
    if r == "remote":
        user = input("enter the user name")
        ip = input("enter remote ip: ")
        print(ip)
        opt = input("enter ur choice : ")
        
        if int(opt) == 1:
            #hdfs file
            os.system("ssh {}@{} echo '<?xml version='1.0'?>' > /etc/hadoop/hdfs-site.xml".format(user,ip))

            os.system(" ssh {}@{} echo '<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))

            os.system("ssh {}@{} echo '<configuration>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))

            os.system("ssh {}@{} echo '<property>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))

            os.system("ssh {}@{} echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))

            folder = input("enter the path of folder that you want to mount")

            os.system("ssh {}@{} echo '<value>{}</value> ' >> /etc/hadoop/hdfs-site.xml".format(user,ip,folder))

            os.system("ssh {}@{} echo '<property>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))

            os.system("ssh {}@{} echo '<configuration>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))
        #core site file


            os.system("ssh {}@{} echo '<?xml version='1.0'?>' > /etc/hadoop/core-site.xml".format(user,ip))

            os.system(" ssh  {}@{} echo '<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>' >> /etc/hadoop/core-site.xml".format(user,ip))

            os.system("ssh {}@{} echo '<configuration>' >> /etc/hadoop/core-site.xml".format(user,ip))

            os.system("ssh {}@{} echo '<property>' >> /etc/hadoop/core-site.xml".format(user,ip))
            os.system("ssh {}@{} echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml".format(user,ip))
            masterip = input("enter the master ip")
            portno = input("enter the port no")

            os.system("ssh {}@{} echo '<value>hdfs://{}:{}</value> ' >> /etc/hadoop/core-site.xml".format(user,ip,masterip,portno))

            os.system("ssh {}@{} echo '<property>' >> /etc/hadoop/core-site.xml".format(user,ip))

            os.system("ssh {}@{} echo '<configuration>' >> /etc/hadoop/core-site.xml".format(user,ip))
            
            os.system("ssh {}@{} hadoop namenode -format".format(user,ip))
            os.system("ssh {}@{} hadoop-daemon.sh start namenode".format(user,ip))
            os.system("ssh {}@{} jps".format(user,ip))
        elif int(opt) == 2:
            os.system("ssh {}@{} echo '<?xml version='1.0'?>' > /etc/hadoop/hdfs-site.xml".format(user,ip))

            os.system(" ssh  {}@{} echo '<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))

            os.system("ssh {}@{} echo '<configuration>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))
            os.system("ssh {}@{} echo '<property>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))
            os.system("ssh {}@{} echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))

            folder = input("enter the path of folder that you want to mount")
            
            os.system("ssh {}@{} echo '<value>{}</value> ' >> /etc/hadoop/hdfs-site.xml".format(user,ip,folder))
            os.system("ssh {}@{} echo '<property>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))

            os.system("ssh {}@{} echo '<configuration>' >> /etc/hadoop/hdfs-site.xml".format(user,ip))

        elif int(opt)==4:
            exit()

        else:
            print("not supported")



    


