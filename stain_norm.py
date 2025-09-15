# Test stain normalization using stain tools
import staintools
import pandas as pd
import os
import pdb
import numpy as np
import random
from PIL import Image
import matplotlib.pyplot as plt

random.seed(0)
np.random.seed(0)

plot_thumnail = True # whether to plot a thumbnail for the original and normalized images

# Path to original images need to be normalized
patch_path ="./sample_images"
original_images = os.listdir(patch_path)

# Target image for normalization
target_image_path = "./ref_image/ref_image.tiff"
target = staintools.read_image(os.path.join(target_image_path))
target = staintools.LuminosityStandardizer.standardize(target) # Standardize brightness (optional, can improve the tissue mask calculation)
normalizer = staintools.StainNormalizer(method='vahadane')
normalizer.fit(target)

save_path = "./std_output"
os.makedirs(save_path, exist_ok = True)
if plot_thumnail:
    thumb_path = os.path.join(save_path, "./norm_thumbnails")
    os.makedirs(thumb_path, exist_ok = True)
   
for image in original_images:
    print(f"Processing {image}")
    if not os.path.exists(os.path.join(patch_path, image)):
        print(f"Missing {image}")
        continue
    if os.path.exists(os.path.join(save_path, image)):
        print(f"{image} has been processed, skipping")
        continue
    try:
        original = staintools.read_image(os.path.join(patch_path, image))
        br_standard = staintools.LuminosityStandardizer.standardize(original)
        transformed = normalizer.transform(br_standard)
        save_im = Image.fromarray(transformed)
        save_im.save(os.path.join(save_path, image))

        # Save a thumbnail to compare original versus transformed images
        if plot_thumnail:
            f, ax = plt.subplots(1, 2)
            ax[0].imshow(original)
            ax[0].set_title("Original")
            ax[0].tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)  # Hide the ticks

            ax[1].imshow(transformed)
            ax[1].set_title("Normalized")
            ax[1].tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)  # Hide the ticks
            plt.savefig(os.path.join(thumb_path, image), dpi=400)
            plt.close()
    except Exception as e:
        print(image)
        print(e)