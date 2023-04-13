# write firmware
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin 

# clear chip
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

# access repl
screen /dev/ttyUSB0 115200
to exit the repl press ctrl+a -> k -> y

# view files
rshell --buffer-size=30 -p /dev/ttyUSB0 -a
ls /pyboard to list files
type repl to enter repl

# sync files form current dir to the esp32
rsync . /pyboard