
from ml.registry import PROGRAM_REGISTRY
from ml.base import AutonomousProgramBaseClass

class AutonomousProgram(AutonomousProgramBaseClass):

    def validate_program(self):
        pass
    def run_program(self):
        print(self.program_key)

    def get_pvs_from_program_key(self, parent_key = ""):
        for key,val in self.raw_data.items():
            pass
    #TODO: iterate through dictionary,
    #TODO: get all device control names and tree path to the device, idea is if its a bad device pull it from the run