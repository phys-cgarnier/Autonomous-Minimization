
from ml.autonomous_emittance import AutonomousEmittanceScanMeasure
from typing import List, Dict, Any, Optional
import numpy as np
import yaml
import os
import epics
import threading
print('hello world')



 
class EmittanceRunner:
    # multi threading when I have capacity --> look at examples in pydevsup source code
    def __init__(self, record_name, args):
        area, magnet_name, screen_name = args.split(' ', 2)
        kwargs = {'area' :area, 'magnet_name': magnet_name}
        self.auto_emit = AutonomousEmittanceScanMeasure(**kwargs)
        #self.auto_emit.print_attr()
        self.mag_pv = epics.PV('QUAD:DIAG0:390:BACT')
        #print(self.mag_pv)
        #print(self.auto_emit.combo)
    def detach(self,record_name):
        pass
    def allowScan(self, record_name):
        pass
    def process(self,record_name,args):
        print('processing')
        pass



#def build(record_name,args):
#    return EmittanceRunner(record_name,args)
build = EmittanceRunner
# why is the PV not visible from dev3 when the ioc is started? is it that I needa soft ioc? I don't understand
