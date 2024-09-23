#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import win32com.shell.shell as shell
import subprocess
ASADMIN = 'asadmin'

rep=input('DHCP=0 Statique=1 ?')
if rep==1:
    com1='netsh interface ipv4 set address "Ethernet" static 10.175.8.200 255.255.0.0 10.175.63.254 20'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+com1)
elif rep==0:
    com1='netsh interface ipv4 set address "Ethernet" source=dhcp'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+com1)
else:
    print "Ben alors..."
