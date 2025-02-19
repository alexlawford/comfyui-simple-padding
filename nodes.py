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

#  Second Node
class SimplePadding:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "X1": ("INT", {"default": 0}),
                "Y1": ("INT", {"default": 0}),
                "X2": ("INT", {"default": 0}),
                "Y1": ("INT", {"default": 0}),
                "Max X": ("INT", {"default": 0}),
                "Max Y": ("INT", {"default": 0}),
                "Padding": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT")
    RETURN_NAMES = ("X1", "Y1", "X2", "Y2")
    FUNCTION = "pad"
    CATEGORY = "CustomNodesTemplate"

    def pad(self,
             x1: int,
             y1: int,
             x2: int,
             y2: int,
             max_x: int,
             max_y: int,
             padding: int,
             ) -> Tuple[int]:
       
        x1b = x1 - padding if x1 - padding > 0 else 0
        x2b = x2 + padding if x2 + padding < max_x else max_x
        y1b = y1 - padding if y1 - padding > 0 else 0
        y2b = y2 + padding if y2 + padding < max_y else max_y

        return (x1b, y1b, x2b, y2b)