
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
    def instantiate_magnet(cls,values):
        if 'magnet' not in values:
            values['magnet'] = create_magnet(values['area'],values['magnet_name'],)
        return values

    @model_validator(mode='before')
    def instantiate_screen(cls,values):
        if 'screen' not in values:
            values['screen'] = create_screen(values['area'],values['screen_name'],)
        return values

    @model_validator(mode='after')
    def instantiate_scan_values(cls,instance):
        instance.scan_values = np.linspace(instance.magnet.bmin,instance.magnet.bmax,5)
        return instance

    @model_validator(mode='after')
    def instantiate_screen_measurement(cls,instance):
        instance.beamsize_measurement = ScreenBeamProfileMeasurement(device=instance.screen)
        return instance

    @model_validator(mode='after')
    def instantiate_quad_scan(cls,instance):
        instance.quad_scan = QuadScanEmittance(energy = instance.energy, scan_values=
                             instance.scan_values, magnet = instance.magnet, beamsize_measurement=
                             instance.beamsize_measurement)
        return instance

    
    
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
