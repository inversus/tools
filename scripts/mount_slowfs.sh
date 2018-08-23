#!/bin/bash

#sudo umount -l /mnt

#sshfs -o debug -o IdentityFile=/home/vrio/.ssh/id_rsa rio@de02dwemt156:/slowfs/de02dwt2p082/ /mnt/slowfs/
sshfs -o IdentityFile=/home/vrio/.ssh/id_rsa rio@de02dwia024:/slowfs/de02dwt2p082/ /mnt/slowfs/
sshfs -o IdentityFile=/home/vrio/.ssh/id_rsa rio@de02dwia024:/SCRATCH/ /mnt/scratch

