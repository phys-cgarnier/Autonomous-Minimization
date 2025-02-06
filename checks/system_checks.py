
import meme.names
from pathlib import Path
import os
import yaml
from pydantic import BaseModel, ConfigDict, model_validator, field_validator
from typing import List, Dict, Any
class SystemChecks(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    yaml_file: Path
    config: Dict[str]
    devices: List[str]

    @field_validator("yaml_file")
    @classmethod
    def validate(cls, value):
        pass


    '''
    def __init__(self, yaml_file : Path, device_list : list = None, **kwargs):
        self.yaml = Path(f"../../yaml/{yaml_file}")
        try:
            with self.yaml.open("r", encoding="utf-8") as f:
                self.config = yaml.safe_load(f)
        except Exception as exc:
            raise ValueError(f"Error reading YAML file: {exc}")
        if self.config.ge
    '''