#TODO: add logging
#import logging
#logger = logging.getLogger(__name__)
import ast
import runpy
import os
import devsup.db as db

class AutonomousProgramSupport:
    #TODO: maybe make this a killable thread? that way we can abort the program with a callback.
    # attributes of class are .fields of pv?
    def __init__(self, ctrl: str = None, prog_file: str = None, home_dir : str = None ):
        #TODO: separate this into another class and use error handling?
        self.ctrl= db.getRecord(ctrl)
        self.prog_file = db.getRecord(prog_file)
        self.home_dir = db.getRecord(home_dir)

    def detach(self, record):
        pass

    def process(self,record, *args):
        fn = str(self.home_dir.VAL) + '/' + str(self.prog_file.VAL)
        print(fn)
        #TODO: set call back to val field of this record to running? or a status pv - this is after tests
        try:
            if os.path.exists(fn):
                print('running')
                runpy.run_path(fn)
        except Exception as e:
            print(e)
        print(f"I processed")

def build(rec,args):
    try:
        kwargs = ast.literal_eval(args)
        #print(kwargs)
    except Exception as e:
        print(f'got an error {e}')
        kwargs = {}

    return AutonomousProgramSupport(**kwargs)
