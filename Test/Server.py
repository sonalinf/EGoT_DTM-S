# Python Program to Get IP Address
##########################
#Enter the following command to run the script
#python 11_1_local_machine_info.py
#
##########################
# function to print machine information
import socket
def print_machine_info():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    print("Your Computer Name is: %s" + hostname)
    print("Your Computer IP Address is: %s" + IPAddr)

if __name__ == '__main__':
    print_machine_info()