import sys
import os.path
#checking wheater check a single IP address or a file conataning multiple ip address
def mainloop():
    q1= input("1-Enter a single IP address \n2-Enter a path to a file containing IP address \n")
    if int(q1)==1:
        ip_addr=input("please enter your IP address:\n")
        single_ip_addr_valid(ip_addr)
    elif int(q1)== 2:
        file_path= input("Please enter your IP address file path:\n")
        ip_file_valid(file_path)
    else:
        print("please enter a valid number")
        mainloop()
        
#checking octet 
def ip_addr_valid(list):
    for ip in list:
        ip =ip.rstrip("\n")
        octect_list = ip.split('.')
        if (len(octect_list)== 4) and (1<=int(octect_list[0]) <=223) and (int(octect_list[0])!= 127) and (int(octect_list[0])!=169 or int(octect_list[1])!=254) and (0<=int(octect_list[1])<=255 and 0<=int(octect_list[2])<=255 and 0<=int(octect_list[3])<=255):
            print("{} is valid\n".format(ip))
        else:
            print("\n there was an invalid ip address in the file: {}\n".format(ip))
            continue
            
            
def single_ip_addr_valid(ip):
        ip =ip.rstrip("\n")
        octect_list = ip.split('.')
        if (len(octect_list)== 4) and (1<=int(octect_list[0]) <=223) and (int(octect_list[0])!= 127) and (int(octect_list[0])!=169 or int(octect_list[1])!=254) and (0<=int(octect_list[1])<=255 and 0<=int(octect_list[2])<=255 and 0<=int(octect_list[3])<=255):
            print("Your Ip address is valid")
        else:
            print("\n Your IP address is invalid {} :(\n".format(ip))
            sys.exit()
            
def ip_file_valid(ip_file):
    #checking if the file exist
    if os.path.isfile(ip_file)==True:
        print("IP file path is valid\n")
    else:
        print("\n * file {} does not exist :( please check and try again.\n".format(ip_file))
        sys.exit()
    #open user selected file for reading 
    selected_ip_file=open(ip_file,'r')
    #Starting from the begining of the file 
    selected_ip_file.seek(0)
    #Reading each ip address (line) in the file 
    ip_list= selected_ip_file.readlines()
    #closing the file 
    selected_ip_file.close()
    ip_addr_valid(ip_list)
mainloop()