from pydantic import BaseModel, ConfigDict, Field, model_validator, field_validator
from abc import ABC, abstractmethod
from typing import Union, List

class ProgramFile(BaseModel):
    # can be a complete program or incomplete program
    model_config = ConfigDict(arbitrary_types_allowed=True)
    file_name: str # program filename
    
class ProgramBase(ABC, BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    program_file: Union[ProgramFile, str]   #can be a file or string
    program: Union[...] #use singular autonomous emittance as an example, but, also consider autonomous minimization or aut multi 
    # or any other program. 
    required_program_fields: List[str] = Field()