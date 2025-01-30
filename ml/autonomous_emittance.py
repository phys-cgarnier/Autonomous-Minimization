from pydantic import BaseModel , model_validator, field_validator, ConfigDict, computed_field
from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance
from lcls_tools.common.devices.magnet import Magnet
from lcls_tools.common.devices.screen import Screen
from lcls_tools.common.devices.reader import create_magnet, create_screen
from lcls_tools.common.measurements.screen_profile import ScreenBeamProfileMeasurement
from typing import List, Dict, Any, Optional
import numpy as np


class AutonomousEmittanceScanMeasure(BaseModel):
    area: str
    magnet_name: str
    combo: Optional[str] = None

    @model_validator(mode = 'after')
    def verify(self):
        self.combo = self.area+self.magnet_name
        return self


'''   
class AutonomousEmittanceScanMeasure():
    def __init__(self,**kwargs):
        self.area = kwargs['area']
        self.magnet_name = kwargs['magnet_name']
        self.screen_name = kwargs['screen_name']
        #self.magnet = create_magnet(self.area, self.magnet_name)
    def print_attr(self):
        print('magnet name: f"{self.magnet_name}" + screen_name: f"{screen_name}"')
'''

