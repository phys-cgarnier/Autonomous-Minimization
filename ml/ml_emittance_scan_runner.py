
from pydantic import BaseModel , field_validator, ConfigDict
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


    @field_validator("magnet", mode="after")
    def instantiate_magnet(cls, magnet, values):
        magnet = create_magnet(values.data['area'], values.data['magnet_name'])
        return magnet
    
    @field_validator("screen", mode="after")
    def instantiate_screen(cls, screen, values):
        screen = create_screen(values.data['area'], values.data['screen_name'])
        return screen
    '''
    @field_validator("scan_values", mode="after")
    def instantiate_scan_values(cls, scan_values, values):
        if values['magnet'] is None:
            raise ValueError('magnet is of type none, cannot validate quad scan values')
        else:
            scan_values = np.linspace(values['magnet'].magnet.bmin,values['magnet'].magnet.bmax,5)
        return scan_values
    '''
class EmittanceRunner:
    # multi threading when I have capacity --> look at examples in pydevsup source code
    def __init__(self, record_name, area, magnet_name, screen_name):
        self.auto_emittance_kwargs = {'area':area, 'magnet_name' :magnet_name, 'screen_name' : screen_name}
        self.auto_emittance = AutonomousEmittanceScanMeasure(**self.auto_emittance_kwargs)

    def detach(self,rec):
        pass

    def process(self,record_name,args):

        ### what is the smartest wa to do this..... I dont know???
        ### make a pydanic class that can run emittance the ????? I dont KNOW!~

        record_name = f'Process {record_name} was a success'
        #print(self.auto_emittance.quad_scan.name)
        print('hello world')


def build(record,args):
    print(f'build {args}')
    largs = args.split(' ',2)
    largs = [l.strip() for l in largs ]
    return EmittanceRunner(record,*largs)

# why is the PV not visible from dev3 when the ioc is started? is it that I needa soft ioc? I don't understand
