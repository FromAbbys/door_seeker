from scapy import *
from scapy.all import *
import argparse
from warnings import filterwarnings
import socket





def banner():
    print("====== ORACLE ======")
    print("\nAutor: Abyss\n")
    print("====================\n")


parser = argparse.ArgumentParser(
        prog = 'Oracle',
        description = 'PortScanner',
        epilog = 'Searchs for open ports in target system',
        usage='python oracle.py [OPTIONS]'
        )

parser.add_argument('-s', '--scan', help='SYN = SYN SCAN (SEND ONLY A SYN PACKET). TCP = TCP CONNECTION. DEFAULT = SYN', required=True)
parser.add_argument('-p','--ports_range', action='append',nargs='+', help='A limit range to scan. DEFAULT = 1-1024')
parser.add_argument('-t', '--target', action='append', help='Specif the target of the scan', required=True)
parser.add_argument('-b', '--banner_grabing', help = 'Try or NOT do a banner grabbing in the service.')

args = parser.parse_args()



#defining the OBJECTS

target = args.target
port_range = args.ports_range
scan_type = args.scan.upper()
banner_grab = args.banner_grabing 







class PortScanner:

    def __init__(self, target,scan_type,banner_grab,port_range=1025):
        self.target = target
        self.port_range = port_range
        self.scan_type = scan_type
        self.banner_grab = banner_grab
        

    def PortScanner(self):

        
    

            alvo = target[0]

            if scan_type == 'SYN':
               
                print("Starting scan....")

                print('\nPORT ------- STATUS --------- BANNER')
                for X in range(1025):

                    my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

                    scan = my_socket.connect_ex((alvo, X))

                    if scan == 0:

                        if banner_grab[0] == 'S' or banner_grab[0] == 's':
                            
                            banner = my_socket.recv(1024)

                            print(f"{X}            OPEN              {banner.decode()}  ")
                        else:

                            print(f"{X}     OPEN")
                    
                    my_socket.close()

            elif scan_type == 'TCP':
                print("TCP CONNECT SCAN")
            else:
                print("Scan invalido. Use somente SYN/TCP como argumento.")



banner()
initt = PortScanner(target, port_range, scan_type)
initt.PortScanner()
