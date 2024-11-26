import os
import devsup
import meme
from abc import ABC, abstractmethod
from typing import List, Dict, Any
#get env variable that says what the beam line is, this is set in the ioc st.cmd file

class meme_service():
    '''Meme Service Wrapper to get all devices on beamline'''
    def __init__(self):
        self.beamline = os.getenv('BEAMLINE')
        self.memey = meme
        print(self.beamline)
        self.device= self.get_devices(meme=self.memey,tag=self.beamline)
        print(self.device)
    def get_devices(self,meme: meme,tag: str):
        device_list = meme.names.list_devices('%', tag)
        return device_list



class Generator(ABC):
    filename:str
    master_device_list: List[str]
    






# maybe do meme service on a different thread I have no idea at this moment.