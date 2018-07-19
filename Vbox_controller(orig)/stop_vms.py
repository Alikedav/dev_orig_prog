#!/usr/bin/env python
import argparse
import re
import os
import subprocess

try:
    import json
except ImportError:
    import simplejson as json



def poweroff_vm(vmid):
    """
    Issues a 'poweroff' command to VirtualBox for the given VM.
    """   
    #vm_id = stopbtn
    print ("Powering off VM: %s..." % vmid)
    output = subprocess.Popen(['VBoxManage', 'controlvm', vmid, 'poweroff'])


