#!/system/bin/python
"""
#################################################
# WIPGrab - Web IP Grabber (15-09-2017 (19:50)) #
# Author  : DedSecTL                            #
# Team    : AndroSec1337 Cyber Team             #
# Github  : https://github.com/Gameye98         #
#################################################
"""
import os
import sys
import socket

#--- Color ---#
N = '\033[0m' # Normal
Y = '\033[33;1m' # Yellow

def banner():
   print "%s                               _              %s" % (Y, N)
   print "%s _ _ _  _  ___  ___  ___  ___ | |_            %s" % (Y, N)
   print "%s| | | || || . || . ||  _|| . || . |           %s" % (Y, N)
   print "%s|_____||_||  _||_  ||_|  |__.||___|v1.0       %s" % (Y, N)
   print "%s          |_|   _| | WEB IP GRABBER           %s" % (Y, N)
   print "%s               |___| ANDROSEC1337             %s" % (Y, N)

if len(sys.argv) != 2:
  banner()
  print
  print "%sUsage: python wipgrab.py http://www.example.com %s" % (Y, N)
  print "%s       python wipgrab.py www.example.com        %s" % (Y, N)
  sys.exit(1)

web=sys.argv[1].replace("http://","").rsplit("/",1)[0] 

banner()
print
print "%s[+] Target => http://%s%s" % (Y, web, N)
ip_address=socket.gethostbyname(web)
print "%s[+] IP     => %s%s" % (Y, ip_address, N)
sys.exit()