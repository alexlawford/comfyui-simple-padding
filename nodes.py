#  Package Modules
import os
from typing import Union, BinaryIO, Dict, List, Tuple, Optional
import time

#  ComfyUI Modules
import folder_paths
from comfy.utils import ProgressBar

#  Your Modules
from .modules.calculator import CalculatorModel

#  Basic practice to get paths from ComfyUI
custom_nodes_script_dir = os.path.dirname(os.path.abspath(__file__))
custom_nodes_model_dir = os.path.join(folder_paths.models_dir, "my-custom-nodes")
custom_nodes_output_dir = os.path.join(folder_paths.get_output_directory(), "my-custom-nodes")

#  Simple Padding Node
class SimplePadding:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "X1": ("INT", {"default": 0}),
                "Y1": ("INT", {"default": 0}),
                "X2": ("INT", {"default": 0}),
                "Y2": ("INT", {"default": 0}),
                "max_X": ("INT", {"default": 0}),
                "max_Y": ("INT", {"default": 0}),
                "padding": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT")
    RETURN_NAMES = ("X1", "Y1", "X2", "Y2")
    FUNCTION = "pad"
    CATEGORY = "CustomNodesTemplate"

    def pad(self,
             X1: int,
             Y1: int,
             X2: int,
             Y2: int,
             max_X: int,
             max_Y: int,
             padding: int,
             ) -> Tuple[int]:
       
        x1b = X1 - padding if X1 - padding > 0 else 0
        x2b = X2 + padding if X2 + padding < max_X else max_X
        y1b = Y1 - padding if Y1 - padding > 0 else 0
        y2b = Y2 + padding if Y2 + padding < max_Y else max_Y

        return (x1b, y1b, x2b, y2b)