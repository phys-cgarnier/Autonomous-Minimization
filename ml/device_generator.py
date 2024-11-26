import os
#import devsup
import meme
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from pydantic import BaseModel, ConfigDict
#get env variable that says what the beam line is, this is set in the ioc st.cmd file

'''
class meme_service():
    #Meme Service Wrapper to get all devices on beamline
    def __init__(self):
        #self.beamline = os.getenv('BEAMLINE')
       #self.memey = meme
        self.service = meme
        #self.devices = self.get_devices(meme=self.memey,tag=self.beamline)

    def get_devices(self, tag: str):
        device_list = self.service.names.list_devices('%', tag)
        return device_list
'''


class Generator(ABC,BaseModel):
    #filename:str
    #_device_list: List[str] = None
    model_config = ConfigDict(arbitrary_types_allowed=True)
    beamline: str

    #substitutions: List[str] = None
    #config: Dict[str,str] = None
    
    @property
    def device_list(self):
        device_list = meme.names.list_devices('%',tag=self.beamline)
        return device_list
    
    def dump_to_file(self):
        ...

    def dump_message(self):
        return f'This is an automatically generated file.'
    
    @abstractmethod
    def config_contents(self):
        ...
    
    
#file bpmTmitStatDest.template
#{
#{DEV=$(DEV), DEST="SCD", SUFFIX="SCD1H",
#        RATE="TPG:SYS0:1:DST01:RATE", 
#        FACMODE="$(DEV):FACMODE",
#        NC_CALC="4", 
#        SC_CALC="C>A&&B>0?0:C>A&&B=0?1:4"
#}
#{DEV=$(DEV), DEST="SCB", SUFFIX="SCB1H", 
#        RATE="TPG:SYS0:1:DST02:RATE", 
#        FACMODE="$(DEV):FACMODE",
#        NC_CALC="4",
#        SC_CALC=0
#}


# Common AFE database (macros defined in bpmAfe.template)
#file bpmAfe.template {
#	pattern {       dbfile,             dbfilemode, suffix,      propomsl,       attomsl,         chrgL,            actlL       ,            attoL,     claoL     , autosave, calal}
#	        { bpmAfe.db, "a -- Use VME IOC PVs",    "L", "closed_loop", "supervisory", "$(chrg) CPP", "$(dev):ACCESS.RVAL CP", "$(dev):ATTO CP", "$(dev):CLAO CP" , ""      , "$(calal\=6)"}
#}


# maybe do meme service on a different thread I have no idea at this moment.
# in python a set can be given by {some value}