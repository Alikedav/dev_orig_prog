#!/usr/bin/env python
import argparse
import re
import os
import subprocess

try:
    import json
except ImportError:
    import simplejson as json


def get_running_vms():

    """
    Returns the list of ids for the VMs currently running in VirtualBox.
    """
    output = subprocess.Popen(['VBoxManage', 'list', 'runningvms'], stdout=subprocess.PIPE).communicate()[0]
    vms = []
    if output is not None:
        lines = output.split('\n')
        for line in lines:
            pattern = re.compile(r'.*{(.*)}')
            match = pattern.match(line)
            print(match)
            if match:
		#print("got a match: " + match.group(0))
                vms.append(line)
    return vms


