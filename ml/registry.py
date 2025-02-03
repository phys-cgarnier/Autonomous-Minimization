
from typing import Type, Dict, Any

MODEL_REGISTRY: Dict[str, Type[Any]] = {}

def register_model(key: str):
    """
    Decorator that registers a Pydantic model class with the given key.
    This key is expected to match the top-level key in the YAML.
    """
    def decorator(cls: Type["Any"]) -> Type["Any"]:
        MODEL_REGISTRY[key] = cls
        return cls
    return decorator