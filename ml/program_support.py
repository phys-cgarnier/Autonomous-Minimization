
from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance
from programs import AutonomousProgram
import numpy as np



### want jsut one thing that takes care off all progs
class AutonomousProgramSupport:
    # multi threading when I have capacity --> look at examples in pydevsup source code
    def __init__(self, record_name, args):
        area, magnet_name, screen_name = args.split(' ', 2)
        self.yaml_name = record_name.info('program_yaml')
        self.auto_program= AutonomousProgram.from_yaml(self.yaml_name)

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
