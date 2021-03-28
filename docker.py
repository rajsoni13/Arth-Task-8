import  os
import getpass



os.system("tput setaf 8")

r = input("where you want to run this menu ? (local/remote) :")
print(r)

os.system("tput setaf 7")

#DOCKER MENU

while True:
    os.system("tput setaf 4")
    print("""
    \n
    press 1 : to pull images
    press 2 : to see the images
    press 3 : to see the status of container
    press 4 : to see all stop and running container
    press 5 : to see the container details
    press 6 : to see the history of image
    press 7 : to see network status
    press 8 : to see the volume status
    press 9 : to the docker version
    press 10 : to exit
    press 11 : to launch container
    press 12 : to launch conatiner with network
    press 13 : to launch conatiner with network and expose
    press 14 : to launch container and expose
    press 15 : to launch container with volume
    press 16 : to launch container with volume and expose 
    press 17 : to delete container
    press 18 : to start container
    press 19 : to stop container
    press 20 : to delete images
    press 21 : to rename images
    press 22 : to push image
    press 23 : create image by commit 
    """)
    os.system("tput setaf 2")
    ch = input("enter your choice : " )
    print(ch)
    os.system("tput setaf 7")

    if r == "local":
        if int(ch) == 1:
            image = input ("enter the image name")
            os.system("docker pull {}".format(image))
        elif int(ch) == 2:
            os.system("docker images")
        elif int(ch) == 3:
            os.system("docker ps")
        elif int(ch) == 4:
            os.system("docker ps -a")
        elif int(ch) == 5:
            conName = input("enter container name : ")
            os.system("docker inspect {} ". format(conName))
        elif int(ch) == 6:
            imgName == input("enter your image name : ")
            os.system("docker history {} ".format(imgName))
        elif int(ch) == 7:
            os.system("docker network ls")
        elif int(ch) == 8:
            os.system("docker volume ls")
        elif int(ch) == 9:
            os.system("docker version")
        elif int(ch) == 10:
            exit()
        elif int (ch) == 11:
            conName = input(" enter container name")
            imgName = input("enter image name with tag")
            os.system("docker run -dit --name {} {}".format(conName,imgName))
        elif int(ch) == 12:
            conName = input(" enter container name")
            imgName = input("enter image name with tag")
            networkname = input("enter network name")
            os.system("docker run -dit --network {}  --name {} {} ".format(networkname,conName,imgName))
        elif int(ch) == 13:
            conName = input(" enter container name")
            imgName = input("enter image name with tag")
            networkname = input("enter network name")
            os.system("docker run -dit --network {} -P --name {} {} ".format(networkname,conName,imgName))
        elif int(ch) == 14:
            conName = input("enter container name")
            imgName = input("enter image name with tag")
            os.system("docker run -dit -P  --name {} {} ".format(conName,imgName))
        elif int(ch) == 17:
            conName = input("enter container name")
            os.system("docker rm -f {} ".format(conName))
        elif int(ch) == 18:
            conName = input("enter container name")
            os.system("docker start {} ".format(conName))
        elif int(ch) == 19:
            conName = input("enter container name")
            os.system("docker stop {} ".format(conName))
        elif int(ch) == 20:
            imgName = input("enter image name with tag")
            os.system("docker rmi -f {} ".format(imgName))
        elif int(ch) == 21:
            oldname = input("enter the old name of image")
            newname = intput("enter new name of image")
            os.system("docker tag {} {} ".format(OldName,NewName))
        elif int(ch) == 22:
            imgName = input("enter image name with tag")
            os.system("docker push {} ".format(ImageName))
        elif int(ch) == 23:
            conName = input("enter container name")
            setimgname = input("enter your image name which you want to set")
            os.system("docker commit {} {} ".format(conName, setimgname))
        else:
            print("not supported")
