
from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance
from ml.autonomous_program import AutonomousProgram
import numpy as np
from pathlib import Path



### want jsut one thing that takes care off all progs
class AutonomousProgramSupport:
    # multi threading when I have capacity --> look at examples in pydevsup source code
    def __init__(self, record_name, args):
        area, magnet_name, screen_name = args.split(' ', 2)
        print(area, magnet_name, screen_name)
        self.yaml_name = record_name.info('program_yaml')
        path = Path(f"../../yaml/{self.yaml_name}")
        self.auto_program= AutonomousProgram.from_yaml(path)

    def detach(self,record_name):
        pass

    def allowScan(self, record_name):
        pass

    def process(self,record_name,args):
        self.auto_program.run_program()
        pass



#def build(record_name,args):
#    return EmittanceRunner(record_name,args)
build = AutonomousProgramSupport
# why is the PV not visible from dev3 when the ioc is started? is it that I needa soft ioc? I don't understand
