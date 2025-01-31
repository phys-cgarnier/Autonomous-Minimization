
from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance
from ml.autonomous_emittance import AutonomousEmittanceScanMeasure
import numpy as np
import yaml
import os

def load_yaml(yaml_name):
    fp = os.getcwd()
    #with open(yaml_name, 'r') as program_file:
        #program_data = yaml.safe_load(program_file)
    return fp
    #return program_data


    
class EmittanceRunner:
    # multi threading when I have capacity --> look at examples in pydevsup source code
    def __init__(self, record_name, args):
        area, magnet_name, screen_name = args.split(' ', 2)
        self.yaml_name = record_name.info('program_yaml')
        program_data = load_yaml(self.yaml_name)
        print(program_data)
        self.auto_emittance_kwargs = {'area':area, 'magnet_name' :magnet_name, 'screen_name' : screen_name}
        self.auto_emittance = AutonomousEmittanceScanMeasure(**self.auto_emittance_kwargs)

    def detach(self,record_name):
        pass
    def allowScan(self, record_name):
        pass
    def process(self,record_name,args):
        print(self.auto_emittance.quad_scan.scan_values)
        pass



#def build(record_name,args):
#    return EmittanceRunner(record_name,args)
build = EmittanceRunner
# why is the PV not visible from dev3 when the ioc is started? is it that I needa soft ioc? I don't understand
