
import meme.names
from pathlib import Path
import os
import yaml
from pydantic import BaseModel, ConfigDict, model_validator, field_validator
from typing import List, Dict, Any
import epics
from collections import defaultdict
import pprint
#TODO: so for now we are just going to check pvs and extensions kind of one by one with hardcoded logic, but in the
# in the future maybe this work should be more of a sweet where strings have meta attached to them like whether they
# are pvs or extensions and the meta data is what subsystem cares about them.
MAPPING_DICT = {
                'magnet': ['BEND', 'BTRM', 'XCOR', 'YCOR', 'QUAD', 'LGPS', 'KICK'],
                'screen': ['OTRS'],
                'vacuum': ['VAC']
                }


class SystemChecks(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    yaml_file: Path
    config: Dict[str]
    devices: Dict[str,List[str]]
    #pv_list: List[epics.PV]

    @classmethod
    def from_yaml(cls, file_path: Path) -> "SystemChecks":
        """
        Factory method that dynamically loads a YAML file and instantiates the SystemChecks class.
        """

        if os.path.exists(file_path):
            try:
                with file_path.open("r", encoding="utf-8") as f:
                    config = yaml.safe_load(f)
            except Exception as exc:
                raise ValueError(f"Error reading YAML file: {exc}")

        else:
            # append to abs path the path to yaml folder
            search_path = Path('../../yaml/')
            found_path = next(search_path.rglob(file_path), None)
            try:
                with found_path.open("r", encoding="utf-8") as f:
                    config = yaml.safe_load(f)
            except Exception as exc:
                raise ValueError(f"Error reading YAML file: {exc}")

            if not isinstance(config, dict) or not config:
                raise ValueError("YAML file must contain a non-empty mapping.")
            
        areas = config.get('areas')
        device_dict = {area: cls.get_devices(area) for area in areas}
        device_defaults = cls.device_to_pv_mapping(device_list= device_dict['DIAG0'], mapping_dict = MAPPING_DICT)
        pprint.pprint(device_dict)
        pprint.pprint(device_defaults)
        pprint.pprint(MAPPING_DICT)

        return cls(yaml_file = file_path, config= config, device= device_dict)

    @staticmethod
    def get_devices(area: str):
        device_list = meme.names.list_devices(f"%{area}%", tag=area, sort_by="z")
        return device_list
    
    @staticmethod
    def device_to_pv_mapping(device_list: List[str], mapping_dict: Dict[str,List])-> List[epics.PV]:
        #device->TYPE:AREA:UNITNUM
        #if TYPE in key for in mapping_dict.keys()
        #Type = QUAD, key = magnet -> lookup config.key
        #[epics.PV()]
        device_defaults = defaultdict(list)
        [device_defaults[d.split(":")[0]].append(d) for d in device_list]
        #for key, val in device_defaults.items():
            #for config_key, config_val in 
        # this is a headache it the most software engineery thing in the whole app it needs to be properly with the best 
        # time complexity possible because it will be ran many many times. possibly.....
        # need a list of pvs for each device in and devices per value in config[device_type] but device_type has many sub
        # device types 
        return device_defaults
    
    def checks_pv_statuses(self):
        pass 
    
    def revalidate(self):
        pass

    def report_invalid_pv_statuses(self):
        pass

    def invalid_pv_status_callback(self):
        #TODO: force program to revalidate or pull device from run
        # if device is in the program
        pass

    def build_program_devices_ok_list(self):
        #if program fails to validate make new program -> maybe move to different code. that acts an intermediary that 
        # is called by systemChecksSupport and programSupport
        pass

