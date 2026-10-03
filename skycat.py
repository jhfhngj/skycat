import os,sys
if sys.argv < 3:
    print("""usage:
skycat [option] [os]

options:
run     - run/download an os
delete  - delete an os
init    - do this if you just downloaded skycat

os:
ubu14""")
    exit(1)

if sys.argv[1] not in ["run","delete","init"]:
    print("""usage:
    skycat [option] [os]
    
    options:
    run     - run/download an os
    delete  - delete an os
    init    - do this if you just downloaded skycat
    
    os:
    ubu14""")
    exit(1)

if sys.argv[2] != "ubu14":
    print("available os:" \
    "ubu14")

if sys.argv[1] == "init":
    print("initializing skycat")
    os.system("sudo apt install quickemu -y")