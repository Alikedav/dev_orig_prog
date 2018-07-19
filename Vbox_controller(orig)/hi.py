#!/usr/bin/env python
import argparse
import re
import os
import subprocess

try:
    import json
except ImportError:
    import simplejson as json



def poweron_vm(vm_id):
    """
    Issues a 'poweron' command to VirtualBox for the given VM.
    """
    print ("Powering on VM: %s..." % vm_id)
    output = subprocess.Popen(['VBoxManage', 'controlvm', vm_id, 'poweron'])

vm_id = str(input("Enter machine ID: "))

results = poweron_vm(vm_id)
print(results)
