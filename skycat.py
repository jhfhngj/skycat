import os,sys
usage = """usage:
skycat [option] [os]

default login credentials:
user: skycat
pass: skycat
also try:
user: skycat
pass: skycatss
or:
user: root
pass: skycatss
maybe:
user: root
pass: skycat

options:
run     - run/download an os
delete  - delete an os
init    - do this if you just downloaded skycat
conf    - configure an os

os:
ubu14
ade1b6

conf options:
ram       "(number)(K/M/G)"
disk_size "(number)(K/M/G)"
cpu_cores "(number)"
do not modify others or you may break your skycat vm"""
try:
    import requests
except:
    print("requests not found, installing")
    os.system("sudo apt install python3-requests -y")
import requests
if len(sys.argv) < 2: exit(1)
if (len(sys.argv) < 3 and (sys.argv[1] != "init")) or (len(sys.argv) > 5 and (sys.argv[1] != "conf")):
    print(usage)
    exit(1)

if sys.argv[1] not in ["run","delete","init","conf"]:
    print(usage)
    exit(1)

if sys.argv[1] in ["run","delete","conf"] and (sys.argv[2] not in ["ubu14","ade1b6"]):
    print(usage)
    exit(1)

if sys.argv[1] == "init":
    print("initializing skycat")
    os.system("sudo apt install quickemu -y")
    print("skycat initialized\ndo not run unless new skycat instance has been installed")
    exit(0)

if sys.argv[1] == "run":
    print("attempting to run",sys.argv[2])
    if sys.argv[2] in os.listdir("."):
        print("running",sys.argv[2])
        exit(os.system(f"quickemu --vm {sys.argv[2]}/ubuntu*.conf"))
    else:
        print("downloading",sys.argv[2])
        with open(f"{sys.argv[2]}.tar.xz","wb") as f: f.write(requests.get(f"https://github.com/jhfhngj/skycat-os/releases/download/{sys.argv[2]}/{sys.argv[2]}.tar.xz").content)
        os.system(f"tar -I 'xz -d -T0' -xf {sys.argv[2]}.tar.xz")
        print("re-run this command to run",sys.argv[2])\

if sys.argv[1] == "delete":
    if int(input("are you sure? (1/0)")):
        os.system(f"rm -rf {sys.argv[2]}*")

if sys.argv[1] == "conf":
    if int(input("are you sure? (1/0)")):
        ossel = sys.argv[2]
        skib = os.listdir(f"./{ossel}/")
        configuration = ""
        for item in skib:
            if item.endswith(".conf"):
                configuration = item
                break
        new = []
        modlines = []
        with open(f"./{ossel}/{configuration}")as f:
            for i,line in enumerate(f.readlines()):
                x = line.split("=")
                print(x)
                if x[0] == sys.argv[3]:
                    x[1] = sys.argv[4]
                    new.append(f"{x[0]}=\"{x[1]}\"\n")
                else:
                    new.append(line)
        with open(f"./{ossel}/{configuration}","w")as f:
            f.write("".join(new))
