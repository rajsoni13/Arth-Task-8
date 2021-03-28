import  os                                                        
import getpass


os.system("tput setaf 8")
#LVM MENU
while True:
    os.system("clear")
    os.system("tput setaf 4")  
    print("""\n
    press 1 : to see disk status
    press 2 : to create physical volume
    press 3 : to see the status of pythical volume
    press 4 : to exit
    press 5 : to create virtual group of hadisk 
    press 6 : to see the status pf vistual group of hardisk
    press 7 : to create logical volume 
    press 8 : to see the status of logical volume
    press 9 : to format the particiam
    press 10 : to create a directory 
    press 11 : to mount the volume
    press 12 : to extend the volume size
    press 13 : to resize the volume
    """)
    r = input("where you want to run this menu ? local / remote : ")
    print(r)
    os.system("tput setaf 7")
    if r == "remote":
        user = input("enter the user name")
        ip = input("enter remote ip : ")
        print(ip)
        opt = input("enter ur choice: " )

        if int(opt) ==1 :
            os.system("ssh {}@{} fdisk -l".format(user,ip))
        
        elif int(opt) == 2:
            diskName = input("enter the disk name : ")
            os.system("ssh {}@{} pvcreate {}".format(user,ip,diskName))
        elif int(opt) == 3:
            diskName = input("enter the disk name : ")
            os.system(" ssh {}@{} pvdisplay {}".format(user,ip,diskName))

        elif int(opt) == 4:
            exit()

        elif int(opt) == 5:
            vgName = input(" name your volume group")
            disk1 = input(" enter your disk one name : ")
            disk2 = input(" enter your disk two name : ")
            os.system("ssh {}@{} vgcreate {}  {} {}".format(user,ip,vgName,disk1,disk2))
        
        elif int(opt) == 6:
            vgName = input(" enter your created your volume group name : ")
            os.system("ssh {}@{} vgdisplay {}".format(user,ip,vgName))

        elif int(opt) == 7:
            size = int(input("enter the size of logical volume : "))
            lvName = input(" give name your logical volume : ")
            vgName = input(" enter your virtual group name : ")
            os.system("ssh {}@{} lvcreate --size {} --name {}  {}".format(user,ip,size,lvName,vgName))

        elif int(opt) == 8:
            vgName = input(" enter your virtual group name : ")
            lvName = input(" enter  your logical volume name: ")
            os.system("ssh {}@{} lvdisplay {}/{}".format(user,ip,vgName,lvName))

        elif int(opt) == 9:
            disk = input("enter your disk name that you have to format : ")
            os.system("ssh {}@{} mkfs.ext4  {}".format(user,ip,disk))

        elif int(opt) == 10:
            fol = input("give name of directory")
            os.system("ssh {}@{} mkdir {}".format(user,ip,fol))

        elif int(opt) == 11:
            diskname = input("enter your disk name : ")
            fol = input("enter the mount path : ")
            os.system("ssh {}@{} mount {}   {} ".format(user,ip,diskname,fol))

        elif int(opt) == 12:
            size = int(input("enter size that you want to increase"))
            lvName = input("enter the name of logical volume name : ")
            os.system("ssh {}@{} lvextend --size {} {}".format(user,ip,size,lvName))

        elif int(opt) == 13:
            lvName = input("enter your logical volume name : ")
            os.system(" ssh {}@{}  resize2fs {}".format(user,ip,lvName))
        
        else:
            print("not supported this option")
    else:
        print("please enter valid name  local or remote:")






