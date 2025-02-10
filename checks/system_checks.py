
import meme.names
from pathlib import Path
import os
import yaml
from pydantic import BaseModel, ConfigDict, model_validator, field_validator
from typing import List, Dict, Any
import epics
from collections import defaultdict
import pprint
from itertools import product
#TODO: so for now we are just going to check pvs and extensions kind of one by one with hardcoded logic, but in the
# in the future maybe this work should be more of a sweet where strings have meta attached to them like whether they
# are pvs or extensions and the meta data is what subsystem cares about them.
MAPPING_DICT = {
                'magnet': ['KICK','BEND', 'BTRM', 'XCOR', 'YCOR', 'QUAD', 'LGPS'],
                'screen': ['OTRS'],
                #'vacuum': ['VVPG'] #maybe I don't need this could be something take care of by MPS
                }


class SystemChecks(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    yaml_file: Path
    config: Dict
    devices: Dict[str,List[str]]
    pv_list: Dict[str,List[epics.PV]]

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
            # append to abs path the path to yaml folder --- will need to check this while testing the ioc 
            # returns posix error if yaml is not found?
            search_path = Path('../../yaml/')
            found_path = next(search_path.rglob(file_path), None)
            print(found_path)

            try:
                with found_path.open("r", encoding="utf-8") as f:
                    config = yaml.safe_load(f)
            except Exception as exc:
                raise ValueError(f"Error reading YAML file: {exc}")

            if not isinstance(config, dict) or not config:
                raise ValueError("YAML file must contain a non-empty mapping.")
            
        areas = config.get('areas')
        device_dict = {area: cls.get_devices(area) for area in areas}
        #pvs = cls.device_to_pv_mapping(device_list= device_dict['DIAG0'], 
        #                                           mapping_dict = MAPPING_DICT, 
        #                                           extensions =config.get('extensions'))
        #print(pvs)
        #pprint.pprint(device_dict)
        #pprint.pprint(device_defaults)
        #pprint.pprint(MAPPING_DICT)
        #pprint.pprint(config)
        return  cls(yaml_file = file_path, config= config, devices= device_dict) #, pv_list=pvs)

    @staticmethod
    def get_devices(area: str):
        device_list = meme.names.list_devices(f"%{area}%", tag=area, sort_by="z")
        return device_list
    
    @staticmethod
    def device_to_pv_mapping(device_list: List[str], mapping_dict: Dict[str,List], extensions: Dict[str,list])-> List[epics.PV]:
        #maybe dont even need this..... 
        
        
        #device->TYPE:AREA:UNITNUM
        #if TYPE in key for in mapping_dict.keys()
        #Type = QUAD, key = magnet -> lookup config.key
        #[epics.PV()]

        #TODO: one day when you have time make this faster time complexity..... this is a triple or quadruple for loop
        #TODO: spend some time learning how.
        device_defaults = defaultdict(list)
        [device_defaults[d.split(":")[0]].append(d) for d in device_list]
        mapped_dict = {}
        for key,val_list in mapping_dict.items():
            for val in val_list:
                devices = device_defaults[val]
                pv_ext = extensions[key]
                #print(devices)
                #print(pv_ext)
                pvs = [epics.PV(dev +':'+ ext) for dev, ext in product(devices,pv_ext)]
                #print(pvs)
                if mapped_dict.get(key):
                    mapped_dict[key] += pvs
                else:
                    mapped_dict[key] = pvs
                #print(mapped_dict)
        return mapped_dict
    
    def perform_checks(self,program_pvs):
        pass

    def check_magnet_pv_severity(self):
        pass

    def check_screen_pv_severity(self):
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

