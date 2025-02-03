
from ml.registry import PROGRAM_REGISTRY
from ml.base import AutonomousProgramBaseClass

class AutonomousProgram(AutonomousProgramBaseClass):

    def validate_program(self):
        pass
    def run_program(self):
        print(self.program_key)