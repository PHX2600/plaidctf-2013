#!/bin/bash

qemu-system-x86_64 \
    -m 64M \
    -nographic \
    -kernel bzImage \
    -append 'console=ttyS0 loglevel=3 oops=panic panic=1' \
    -initrd initramfs.img \
    -net nic,model=e1000 \
    -net user
