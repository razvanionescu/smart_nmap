import sys
import os
import argparse
from commands import *

#python smart_nmap.py nmap.log IP
#Author: Razvan-Costin IONESCU

parser=argparse.ArgumentParser(
    description='''Smart Nmap. It checks for all open ports and afterwards run 'nmap -v -A' only on the opened ports, saves the output in xml and html format. It requires xsltproc tool to be installed ''',
    epilog=""" Enjoy! """)
parser.add_argument('log', type=str, help='output log file')
parser.add_argument('ip', type=str, help='IP to be scanned')
args=parser.parse_args()

if (len(str(getoutput("which xsltproc")))>0):
   pass
else:
   print "xsltproc needs to be installed on the system\n"
   os.system("sudo apt-get install xsltproc")

os.system("nmap -sS -p1-65535 -oN "+str(sys.argv[1])+" "+str(sys.argv[2]))

with open(sys.argv[1], 'r') as f:
   read_data = f.readlines()

ports = []
for line in read_data:
   if "/tcp" in line:
      ports.append(line.split("/")[0])

print "nmap -v -A -p"+','.join(map(str,ports))+" "+sys.argv[2]

os.system("nmap -v -A -p"+','.join(map(str,ports))+" -oX "+str(sys.argv[1])+".xml "+sys.argv[2])
os.system("xsltproc "+str(sys.argv[1])+".xml -o "+str(sys.argv[1])+".html")

print "JOB DONE!"
