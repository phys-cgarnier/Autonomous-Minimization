from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance
from ml.registry import register_model
from ml.base import AutonomousProgramBase

@register_model("AutonomousEmittanceMeasurement")
class AutonomousEmittanceMeasurement(AutonomousProgramBase):
    program: QuadScanEmittance
    def validadate_program(self):
        # add logic for advanced validation
        return super().validadate_program()
    def revalidate_program(self):
        return super().revalidate_program()
    def run(self):
        return self.program.measure()
    
