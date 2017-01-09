import socket
import _thread
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Core(object):
    ipurl=0
    mode=1024
    menu1=False
    f=None
    network_speed="LAN"
    menu2=False
    def GetData(self, url):
        self.url = url
        try:
            self.ipurl = socket.gethostbyname(self.url)
        except Exception as e:
            print ("Invalid URL or IP")
            exit(0)
        Core.ipurl=self.ipurl
        print (60*"-")
        print (22*" ",bcolors.FAIL,"Port Scanner v1",bcolors.ENDC)
        print (60*"-")
        while Core.menu1 is not True:
            choice = input("\n1 - simple \n2 - extended\n")
            if choice == "1":
                Core.mode=1024
                menu=True
                break
            elif choice == "2":
                Core.mode=64000
                menu = True
                break
            else:
                print("Incorrect answer, choose 1 or 2")
        while Core.menu2 is not True:
            choice = input("\n1 - LAN \n2 - Global Network\n")
            if choice == "1":
                Core.network_speed=0.05
                menu2=True
                break
            elif choice == "2":
                Core.network_speed=0.3
                menu2 = True
                break
            else:
                print("Incorrect answer, choose 1 or 2")

    def Start_Scan(self, port_start, port_end):
        Core.f = open(Core.ipurl, "a")
        try:
            for x in range(port_start,port_end):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = sock.connect_ex((Core.ipurl,x))
                if res is 0:
                    tmp="Port",x,"is open", socket.getservbyport(x)
                    tmp1=str(tmp[0])+" "+str(tmp[1])+" "+str(tmp[2])+" "+str(tmp[3])
                    print(bcolors.OKGREEN,tmp1)
                    Core.f.write(str(tmp)+"\n")
            Core.f.close()
        except Exception as e:
            print (e)
try:
    scan = Core()
    scan.GetData(input("Type IP or address\n"))
    print(bcolors.WARNING,"Range:",Core.mode,"\n Target:",Core.ipurl,"\n Scanning speed:",Core.network_speed,bcolors.ENDC)
    print(bcolors.BOLD,"Please wait...",bcolors.ENDC)
    for count in range(0,Core.mode):
        #print (Core.mode)
        time.sleep(Core.network_speed)
        _thread.start_new_thread(scan.Start_Scan, (count,count+1))
        if count > Core.mode:
            exit(0)
except Exception as e:
    print (e)
