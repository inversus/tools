#!/bin/bash

die () {
    echo >&2 "$@"
    exit 1
}
[ "$#" -eq 2 ] || die "usage: $0 <BUILDROOT> <SDCARD>"

# SDCard must have a 32bit partition

BUILDROOT=$1
SDCARD=$2

echo "buildroot: $BUILDROOT"
echo "sdcard: $SDCARD"

IMG="$BUILDROOT/output/images"

cp -v $IMG/boot.bin $SDCARD
cp -v $IMG/u-boot.img $SDCARD
cp -v $IMG/uImage $SDCARD
cp -v $IMG/rootfs.cpio.uboot $SDCARD/uramdisk.image.gz
cp -v $IMG/zynq-zed.dtb $SDCARD/devicetree.dtb

