import os,sys
try:
    import requests
except:
    print("requests not found, installing")
    os.system("sudo apt install python3-requests -y")
import requests
if len(sys.argv) < 3 and (sys.argv[1] != "init"):
    print("""usage:
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

options:
run     - run/download an os
delete  - delete an os
init    - do this if you just downloaded skycat

os:
ubu14
ade1b6""")
    exit(1)

if sys.argv[1] not in ["run","delete","init"]:
    print("""usage:
    skycat [option] [os]
    
    options:
    run     - run/download an os
    delete  - delete an os
    init    - do this if you just downloaded skycat
    
    os:
    ubu14
    ade1b6""")
    exit(1)

if sys.argv[1] in ["run","delete"] and (sys.argv[2] not in ["ubu14","ade1b6"]):
    print("available os:" \
    "ubu14")
    exit(1)

if sys.argv[1] == "init":
    print("initializing skycat")
    os.system("sudo apt install quickemu -y")
    print("skycat initialized. do not run unless new skycat instance has been installed")
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
        os.system(f"rm -rf {sys.argv[2]}")
