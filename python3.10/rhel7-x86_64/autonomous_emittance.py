from pydantic import BaseModel , model_validator, field_validator, ConfigDict
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
    magnet: Magnet 
    #scan_values: List[float] = None
    screen_name: str
    screen: Screen
    #beamsize_measurement: ScreenBeamProfileMeasurement = None
    #quad_scan: QuadScanEmittance = None
    #run_attempts: int --> these params need to get set else where.
    #run_wait_time_ms: int


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

    @field_validator("magnet", mode="after")
    def instantiate_magnet(cls, magnet, values):
        magnet = create_magnet(values.data['area'], values.data['magnet_name'])
        return magnet
    
    @field_validator("screen", mode="after")
    def instantiate_screen(cls, screen, values):
        screen = create_screen(values.data['area'], values.data['screen_name'])
        return screen
    
    @field_validator("scan_values", mode="after")
    def instantiate_scan_values(cls, scan_values, values):
        if values['magnet'] is None:
            raise ValueError('magnet is of type none, cannot validate quad scan values')
        else:
            scan_values = np.linspace(values.data['magnet'].magnet.bmin,values.data['magnet'].magnet.bmax,5)
        return scan_values
    
    @field_validator("beamsize_measurement", mode="after")
    def instantiate_beamsize_measurement(cls,beamsize_measurement, values):
        beamsize_measurement = ScreenBeamProfileMeasurement(device= values.data['screen'])
        return beamsize_measurement
    
    @field_validator("quad_scan", mode="after")
    def instantiate_quad_scan(cls,quad_scan, values):
        quad_scan = QuadScanEmittance(energy = values.data['energy'], scan_values=
                             values.data['scan_values'], magnet = values.data['magnet'], beamsize_measurement=
                             values.data['beamsize_measurement'])
        return quad_scan
    