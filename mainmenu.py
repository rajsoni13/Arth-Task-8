from getpass import getpass
from os import system

passwd = "redhat"

while True:
    system("tput setaf 6")
    pass1=getpass("\n\t To Continue, enter your password:  ")
    if pass1 == passwd: 
        system("tput setaf 3")
        print("\n\t User authenticated! ...")
        system("sleep 1")
        break
    else:
        system("tput setaf 1")
        print("\t your password is incorrect \n")

while True:
    while True:
        system("clear")
        system("tput setaf 2")
        print("\n\t"+55*"-")
        print("\t\t ARTH Team 18 automation Menu")
        print("\n\t"+55*"-")
        system("tput setaf 3")
        print("\n Note: To get best output of this program , please ensure that your yum is configured with local packages")
        system("tput setaf 7")
        print("\n\tPlease select an option: \n")
        system("tput setaf 5")
        print("\t\t1 : system command")
        print("\t\t2 : Docker")
        print("\t\t3 : Hadoop")
        print("\t\t4 : Create Partision")
        print("\t\t5 : exit")
        system("tput setaf 6")
        opt = int(input("\n\tOption selected: "))

        if opt == 1:
            import systemcmd
            system("clear")
            systemcmd.menu()

        elif opt == 2:
            import docker
            system("clear")
            docker.menu()

        elif opt == 3:
            import hadoop
            system("clear")
            hadoop.menu()

        elif  opt == 4:
            import lvm
            system("clear")
            lvm.menu()

        elif opt == 5:
            exit()

        else:
            pass

