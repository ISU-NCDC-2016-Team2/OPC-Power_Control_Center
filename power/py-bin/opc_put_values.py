#!/usr/bin/env python
import sys
from PyOPC.OPCContainers import *
from PyOPC.XDAClient import XDAClient
from config import paths

def print_options((ilist,options)):
    print ilist; print options; print

var = sys.argv[1]
value = sys.argv[2]

print >> sys.stderr, "PUT VALUES: ", sys.argv

relay1=paths['relay1']
relay2=paths['relay2']
gen1=paths['gen1']
gen2=paths['gen2']

xda_relay1 = XDAClient(OPCServerAddress=relay1,ReturnErrorText=False)
xda_relay2 = XDAClient(OPCServerAddress=relay2,ReturnErrorText=False)
xda_gen1 = XDAClient(OPCServerAddress=gen1,ReturnErrorText=False)
xda_gen2 = XDAClient(OPCServerAddress=gen2,ReturnErrorText=False)

if "relay1" in var:
	xda_relay1.Write([ItemContainer(ItemName=var, Value=value)],LocaleID='en-us')
if "relay2" in var:
	xda_relay2.Write([ItemContainer(ItemName=var, Value=value)],LocaleID='en-us')
if "gen1" in var:
	xda_gen1.Write([ItemContainer(ItemName=var, Value=value)],LocaleID='en-us')
if "gen2" in var:
	xda_gen2.Write([ItemContainer(ItemName=var, Value=value)],LocaleID='en-us')
