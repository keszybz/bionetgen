# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:11:35 2013

@author: proto
"""

import pexpect
import subprocess

def bngl2xml(bnglFile,timeout=60):
    try:
        bngconsole = pexpect.spawn('bngdev --console',timeout=timeout)
        bngconsole.expect('BNG>')
        bngconsole.sendline('load {0}'.format(bnglFile))
        bngconsole.expect('BNG>')
        bngconsole.sendline('action writeXML()')
        bngconsole.expect('BNG>')
        bngconsole.close() 
    except pexpect.TIMEOUT:
        subprocess.call(['killall','bngdev'])        
    
def correctness(bnglFile):
    bngconsole = pexpect.spawn('bngdev --console')
    bngconsole.expect('BNG>')
    bngconsole.sendline('load {0}'.format(bnglFile))
    bngconsole.expect('BNG>')
    output= bngconsole.before
    bngconsole.close()
    if 'ERROR' in output  in output:
        return False
    return True

    
def writeNetwork(bnglFile):
    bngconsole = pexpect.spawn('bngdev --console')
    bngconsole.expect('BNG>')
    bngconsole.sendline('load {0}'.format(bnglFile))
    bngconsole.expect('BNG>')
    bngconsole.sendline('action generate_network()')
    bngconsole.expect('BNG>')
    bngconsole.close() 
    
if __name__ == "__main__":      
    print bngl2xml('complex/output61.bngl')