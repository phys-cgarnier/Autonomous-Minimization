
from pydantic import BaseModel ,model_validator, field_validator, ConfigDict
from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance
from lcls_tools.common.devices.magnet import Magnet
from lcls_tools.common.devices.screen import Screen
from lcls_tools.common.devices.reader import create_magnet, create_screen
from lcls_tools.common.measurements.screen_profile import ScreenBeamProfileMeasurement
from typing import List, Dict, Any, Optional
import numpy as np
import yaml
import os

def load_yaml(yaml_name):
    filepath = '../../yaml/' + yaml_name
    if os.path.exists(filepath):
        with open(filepath, 'r') as program_file:
            program_data = yaml.safe_load(program_file)
    else:
        program_data = 'This is a blank string'
    return program_data


    
class EmittanceRunner:
    # multi threading when I have capacity --> look at examples in pydevsup source code
    def __init__(self, record_name, args):
        area, magnet_name, screen_name = args.split(' ', 2)
        self.yaml_name = record_name.info('program_yaml')
        print(self.yaml_name)
        program_data = load_yaml(self.yaml_name)
        #print(program_data)
        self.model = QuadScanEmittance.model_validate(program_data)
        print(self.model.scan_values)

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
