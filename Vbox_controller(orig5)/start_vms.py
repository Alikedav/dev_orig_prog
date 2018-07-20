#!/usr/bin/env python
import argparse
import re
import os
import subprocess

try:
    import json
except ImportError:
    import simplejson as json



def poweron_vm(vmid):
    """
    Issues a 'poweron' command to VirtualBox for the given VM.
    """
    print ("Powering on VM: %s..." % vmid)
    #output = subprocess.call(['ls -a'])
    #print(output)
    output = subprocess.call(['VBoxManage', 'startvm', vmid, '--type','headless'])







