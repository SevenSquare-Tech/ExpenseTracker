"""
This type stub file was generated by pyright.
"""

import enum
from google.generativeai.notebook.lib import model as model_lib

"""Maintains set of LLM models that can be instantiated by name."""
class ModelName(enum.Enum):
    ECHO_MODEL = ...
    TEXT_MODEL = ...


class ModelRegistry:
    """Registry that instantiates and caches models."""
    DEFAULT_MODEL = ...
    def __init__(self) -> None:
        ...
    
    def get_model(self, model_name: ModelName) -> model_lib.AbstractModel:
        """Given `model_name`, return the corresponding Model instance.

        Model instances are cached and reused for the same `model_name`.

        Args:
          model_name: The name of the model.

        Returns:
          The corresponding model instance for `model_name`.
        """
        ...
    


