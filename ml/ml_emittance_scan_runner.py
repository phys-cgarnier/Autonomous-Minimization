
from pydantic import BaseModel ,model_validator, field_validator, ConfigDict
from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance
from lcls_tools.common.devices.magnet import Magnet
from lcls_tools.common.devices.screen import Screen
from lcls_tools.common.devices.reader import create_magnet, create_screen
from lcls_tools.common.measurements.screen_profile import ScreenBeamProfileMeasurement
from typing import List, Dict, Any, Optional
import numpy as np


    
class AutonomousEmittanceScanMeasure(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True) 
    energy: float = .091 #arbitrary right now until we can get energy value
    area: str
    magnet_name: str
    magnet: Optional[Magnet] = None 
    scan_values: Optional[List[float]] = None
    screen_name: str
    screen: Optional[Screen] = None
    beamsize_measurement: Optional[ScreenBeamProfileMeasurement] = None
    quad_scan: Optional[QuadScanEmittance] = None
    #run_attempts: int --> these params need to get set else where.
    #run_wait_time_ms: int

    #TODO: add energy getter method PV instead of passing energy

    @model_validator(mode='before')
    def initialize_devices(cls, values):
        print("Model validator called with values:", values)
        
        # Initialize magnet
        if values.get('magnet') is None:
            print("Creating magnet")
            values['magnet'] = create_magnet(values['area'], values['magnet_name'])
        
        # Initialize screen
        if values.get('screen') is None:
            print("Creating screen")
            values['screen'] = create_screen(values['area'], values['screen_name'])
        
        # Initialize scan values
        if values.get('scan_values') is None and values.get('magnet') is not None:
            print("Creating scan values")
            values['scan_values'] = np.linspace(
                values['magnet'].magnet.bmin,
                values['magnet'].magnet.bmax,
                5
            ).tolist()  # Convert to list for Pydantic
        
        # Initialize beamsize measurement
        if values.get('beamsize_measurement') is None and values.get('screen') is not None:
            print("Creating beamsize measurement")
            values['beamsize_measurement'] = ScreenBeamProfileMeasurement(
                device=values['screen']
            )
        
        # Initialize quad scan
        if (values.get('quad_scan') is None and 
            all(values.get(k) is not None for k in ['magnet', 'scan_values', 'beamsize_measurement'])):
            print("Creating quad scan")
            values['quad_scan'] = QuadScanEmittance(
                energy=values['energy'],
                scan_values=values['scan_values'],
                magnet=values['magnet'],
                beamsize_measurement=values['beamsize_measurement']
            )
        
        return values

    
    
class EmittanceRunner:
    # multi threading when I have capacity --> look at examples in pydevsup source code
    def __init__(self, record_name, area, magnet_name, screen_name):
        self.auto_emittance_kwargs = {'area':area, 'magnet_name' :magnet_name, 'screen_name' : screen_name}
        self.auto_emittance = AutonomousEmittanceScanMeasure(**self.auto_emittance_kwargs)
        print(self.auto_emittance.__repr__)
    def detach(self,rec):
        pass

    def process(self,record_name,args):

        ### what is the smartest wa to do this..... I dont know???
        ### make a pydanic class that can run emittance the ????? I dont KNOW!~

        record_name = f'Process {record_name} was a success'
        print(self.auto_emittance.quad_scan.name)
        print('hello world')


def build(record,args):
    print(f'build {args}')
    largs = args.split(' ',2)
    largs = [l.strip() for l in largs ]
    return EmittanceRunner(record,*largs)

# why is the PV not visible from dev3 when the ioc is started? is it that I needa soft ioc? I don't understand
