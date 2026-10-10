# SkyCat
```text
user@host:~$ python3 skycat.py --help
usage:
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
do not modify others or you may break your skycat vm

user@host:~$ whatis skycat
SkyCat is a frontend for QuickEMU that downloads and extracts prebuilt VMs.
Instead of waiting quite a bit to setup and download, just wait quite a miniscule bit to download! No setup. Easy.

user@host:~$ python3 skycat.py init

user@host:~$ time python3 skycat.py run ubu14 # Real tested performance metric, output is from actual command
attempting to run ubu14
downloading ubu14
re-run this command to run ubu14

real    1m40.103s
user    0m19.532s
sys     0m4.070s

user@host:~$ time python3 skycat.py delete ubu14 # Again
1are you sure? (1/0)

real    0m0.426s
user    0m0.138s
sys     0m0.223s
```