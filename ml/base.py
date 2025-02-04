import yaml
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Type
from pydantic import BaseModel, ValidationError, Field, model_validator, field_validator, ConfigDict
from ml.registry import PROGRAM_REGISTRY


class AutonomousProgramBaseClass(BaseModel, ABC):
    """
    Abstract Pydantic base class for autonomous programs.
    Loads YAML, extracts first key as 'program', and validates its data.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)
    file_path: Path = Field(..., description="Path to the YAML program file")
    program_key: str = Field(..., description="Extracted program key from YAML")
    raw_data: Dict[str, Any] = Field(..., description="Raw YAML data under the program key")

    # This field holds the validated Pydantic model instance
    program: BaseModel = Field(..., description = 'Program to run')

    @abstractmethod
    def validate_program(self) -> BaseModel:
        """
        Abstract method to validate `raw_data` using a specific Pydantic model.
        Subclasses must implement this.
        """
        pass
        #maybe abstract?
    @classmethod
    def from_yaml(cls, file_path: Path) -> "AutonomousProgramBaseClass":
        """
        Factory method that dynamically loads a YAML file and instantiates the correct subclass.
        """
        try:
            with file_path.open("r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as exc:
            raise ValueError(f"Error reading YAML file: {exc}")

        if not isinstance(data, dict) or not data:
            raise ValueError("YAML file must contain a non-empty mapping.")

        # Extract the first key and associated value
        program_key, program_data = next(iter(data.items()))
        print('program key ', program_key)
        # Dynamically find the correct subclass from the registry
        try: 
            program = (PROGRAM_REGISTRY.get(program_key)).model_validate(program_data)
        except ValidationError as e:
            print('insufficient program data in yaml')
        
        return cls(file_path = file_path, program_key = program_key, raw_data = program_data, program = program)

        #return subclass(file_path=file_path, program_key=program_key, raw_data=program_data)
    @classmethod
    def from_system(cls, program_key: str, system_checks_dict: Dict[str,Any]):
        pass
    '''
    def revalidate(self) -> None:
        """
        Reload and revalidate the YAML file.
        """
        updated_instance = self.__class__.from_yaml(self.file_path)
        self.program_model = updated_instance.program_model
        self.raw_data = updated_instance.raw_data
    '''
