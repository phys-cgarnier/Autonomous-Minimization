# This program takes in args and creates the work flow to do an emittance scan.
# note to self, need current lcls-tools to be in env, also need to update pydevsup to use python version from rhel_7_devel env
from pydantic import BaseModel, model_validator
from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance
from lcls_tools.common.devices.magnet import Magnet
from lcls_tools.common.devices.reader import create_magnet
from lcls_tools.common.measurements.measurement import Measurement

class AutonomousEmittanceScanMeasure(BaseModel):
    #what is everything I need to run an emittance scan
    #quad_scan: QuadScanEmittance 
    area: str
    magnet_name: str
    magnet: Magnet 

    @model_validator(mode='before')
    def instantiate_magnet(cls,values):
        if 'magnet' not in values:
            values['magnet'] = create_magnet(values['area'],values['manget_name'],)
        return values

class EmittanceRunner:
    # multi threading when I have capacity --> look at examples in pydevsup source code
    def __init__(self, record_name, *args):
        pass

    def process(self,record_name,args): 
        print(f'process: {args}')

def build(record,args):
    print(f'build {args}')
    return EmittanceRunner(args)


'''
class QuadScanEmittance(Measurement):
    """Use a quad and profile monitor/wire scanner to perform an emittance measurement
    ------------------------
    Arguments:
    energy: beam energy
    scan_values: BDES values of magnet to scan over
    magnet: Magnet object used to conduct scan
    beamsize_measurement: BeamsizeMeasurement object from profile monitor/wire scanner
    n_measurement_shots: number of beamsize measurements to make per individual quad
    strength
    ------------------------
    Methods:
    measure: does the quad scan, getting the beam sizes at each scan value,
    gets the rmat and twiss parameters, then computes and returns the emittance and BMAG
    measure_beamsize: take measurement from measurement device, store beam sizes
    """
    energy: float
    scan_values: list[float]
    magnet: Magnet
    beamsize_measurement: Measurement
    n_measurement_shots: PositiveInt = 1

    rmat: Optional[ndarray] = None  # 4 x 4 beam transport matrix
    design_twiss: Optional[dict] = None  # design twiss values
    beam_sizes: Optional[dict] = {}

    name: str = "quad_scan_emittance"
    model_config = ConfigDict(arbitrary_types_allowed=True)

'''

# can make the Measurement field in Quadscan have a default so that I don't have to create it here
