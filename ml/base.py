from pydantic import BaseModel, ConfigDict, Field, model_validator, field_validator
from abc import ABC, abstractmethod
from typing import Union, Optional, List, Dict, Type
from lcls_tools.common.measurements.emittance_measurement import QuadScanEmittance

#MODEL_REGISTRY = {'QuadScanEmittanceMeasure': QuadScanEmittance}


class ProgramFile(BaseModel):
    # can be a complete program or incomplete program
    model_config = ConfigDict(arbitrary_types_allowed=True)
    file_name: str # program filename
    contents: Optional[Dict] = None

    
class AutonomousProgramBase(ABC, BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    program_file: Union[ProgramFile, str]   #can be a file or string
    program: Union[QuadScanEmittance,str] #use singular autonomous emittance as an example, but, also consider autonomous minimization or aut multi 
    # or any other program. 
    @abstractmethod
    def validadate_program(self):
        ...
    @abstractmethod
    def revalidate_program(self):
        ...

    
