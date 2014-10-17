cyberpunk
========

## Building and uploading AVR firmware
The commands for building and uploading firmware images are straight-forward CMake:

```
mkdir build
cd build
cmake ..
make
make cyberpunk-upload # Assuming cyberpunk is used in generate\_arduino\_firmware()
```

