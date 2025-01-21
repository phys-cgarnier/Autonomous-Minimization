
from pydantic import BaseModel ,model_validator, field_validator, ConfigDict
from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance
from lcls_tools.common.devices.magnet import Magnet
from lcls_tools.common.devices.screen import Screen
from lcls_tools.common.devices.reader import create_magnet, create_screen
from lcls_tools.common.measurements.screen_profile import ScreenBeamProfileMeasurement
from typing import List, Dict, Any, Optional
import numpy as np
import yaml

def load_yaml(yaml_name):
    with open(yaml_name, 'r') as program_file:
        program_data = yaml.safe_load(program_file)
    return program_data

class AutonomousEmittanceScanMeasure(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    energy: float = .091
    area: str
    magnet_name: str
    magnet: Optional[Magnet] = None
    scan_values: Optional[List[float]] = None
    screen_name: str
    screen: Optional[Screen] = None
    beamsize_measurement: Optional[ScreenBeamProfileMeasurement] = None
    quad_scan: Optional[QuadScanEmittance] = None

    # Single 'before' validator for device creation
    @model_validator(mode='before')
    def create_devices(cls, values):
        try:
            if values.get('magnet') is None:
                values['magnet'] = create_magnet(values['area'], values['magnet_name'])
            
            if values.get('screen') is None:
                values['screen'] = create_screen(values['area'], values['screen_name'])
        except Exception as e:
            raise ValueError(f"Failed to create devices: {str(e)}")
        return values

    # Single 'after' validator for dependent calculations
    @model_validator(mode='after')
    def setup_measurements(self):
        if self.magnet is None:
            raise ValueError("Magnet must be initialized")
        if self.screen is None:
            raise ValueError("Screen must be initialized")

        try:
            # Set scan values
            if self.scan_values is None:
                self.scan_values = np.linspace(self.magnet.bmin, self.magnet.bmax, 5)

            # Create beam profile measurement
            if self.beamsize_measurement is None:
                self.beamsize_measurement = ScreenBeamProfileMeasurement(device=self.screen)

            # Create quad scan after all dependencies are ready
            if self.quad_scan is None:
                if any(v is None for v in [self.scan_values, self.beamsize_measurement]):
                    raise ValueError("Required dependencies not initialized")
                
                self.quad_scan = QuadScanEmittance(
                    energy=self.energy,
                    scan_values=self.scan_values,
                    magnet=self.magnet,
                    beamsize_measurement=self.beamsize_measurement
                )
        except Exception as e:
            raise ValueError(f"Failed to setup measurements: {str(e)}")

        return self
    
    
class EmittanceRunner:
    # multi threading when I have capacity --> look at examples in pydevsup source code
    def __init__(self, record_name, args):
        area, magnet_name, screen_name = args.split(' ', 2)
        self.yaml_name = record_name.info('program_yaml')
        program_data = load_yaml(self.yaml_name)
        print(program_data)
        self.auto_emittance_kwargs = {'area':area, 'magnet_name' :magnet_name, 'screen_name' : screen_name}
        self.auto_emittance = AutonomousEmittanceScanMeasure(**self.auto_emittance_kwargs)
        print(self.auto_emittance.__repr__)

    def detach(self,record_name):
        pass
    def allowScan(self, record_name):
        pass
    def process(self,record_name,args):
        print(self.auto_emittance.quad_scan.name)



#def build(record_name,args):
#    return EmittanceRunner(record_name,args)
build = EmittanceRunner
# why is the PV not visible from dev3 when the ioc is started? is it that I needa soft ioc? I don't understand
