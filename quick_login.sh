#!/bin/bash

#use this code to make it so that you never have to enter your password into poseidon again 
# this code only works on unix based systems (i.e. Linux or MacOS)

username=anthony.meza #define username

ssh-keygen #generate private keys 

ssh-copy-id $username@ilko.whoi.edu #copy keys to remote server
