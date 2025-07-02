import numpy as np
from PIL import Image


def mask_finder(path_to_combined_mask):
    rgb_mask = np.array(Image.open(path_to_combined_mask))
    unique_colors = np.unique(rgb_mask.reshape(-1, 3), axis=0)
    color_to_class = {tuple(color): idx for idx, color in enumerate(unique_colors)}

    for color, class_id in color_to_class.items():
        color_np = np.array(color)

    H, W, _ = rgb_mask.shape
    class_mask = np.zeros((H, W), dtype=np.uint8)
    for color, class_id in color_to_class.items():
        matches = np.all(rgb_mask == color, axis=-1)
        class_mask[matches] = class_id
    
    masks=[]
    for color, class_id in color_to_class.items():
        target_color=np.array(color)
        binary_mask = np.all(rgb_mask == target_color, axis=-1).astype(np.uint8)
        masks.append(binary_mask)
    return masks