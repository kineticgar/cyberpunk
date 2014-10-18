cyberpunk
========

## Fixing permission errors writing firmware
When writing firmware, avrdude may fail with the following message
```
avrdude: ser_open(): can't open device "/dev/ttyACM0": Permission denied
```

Further inspection reveals that permission to open the device is granted to the `dialout` or `tty` group
```
$ ls -al /dev/ttyACM*
crw-rw---- 1 root dialout 166, 0 Oct 17 13:22 /dev/ttyACM0
crw-rw---- 1 root dialout 166, 1 Oct 17 16:09 /dev/ttyACM1
```

To fix this, add yourself to the appropriate group
```
$ sudo usermod -a -G dialout <username>
```

## Building and uploading AVR firmware
The commands for building and uploading firmware images are straight-forward CMake:

```
mkdir build
cd build
cmake ..
make
make cyberpunk-upload # Assuming cyberpunk is used in generate_arduino_firmware()
```

