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
                "x": ("INT", {"default": 0}),
                "y": ("INT", {"default": 0}),
                "width": ("INT", {"default": 0}),
                "height": ("INT", {"default": 0}),
                "padding": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT")
    RETURN_NAMES = ("x", "y", "width", "height")
    FUNCTION = "pad"
    CATEGORY = "CustomNodesTemplate"

    def pad(self,
             X1: int,
             Y1: int,
             width: int,
             height: int,
             padding: int,
             ) -> Tuple[int]:
       
        x1b = X1 - padding if X1 - padding > 0 else 0
        y1b = Y1 - padding if Y1 - padding > 0 else 0
        width = width + padding
        height = height + padding

        return (x1b, y1b, width, height)