import logging
logger = logging.getLogger(__name__)

class DeviceSupport:
    def __init__(self,rec,link):
        self.rec = rec
        self.link = link
    def detach(self,rec):
        pass
    def process(self,rec,reason):
        print(f'rec: {self.rec}, reason: {reason}, link : {self.link}')
        rec.VAL  = rec.VAL + 1

def build(rec,link):
    return DeviceSupport(rec,link)