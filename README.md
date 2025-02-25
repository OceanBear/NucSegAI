# NucSegAI

## Introduction

NucSegAI is a deep learning model for automated nuclear segmentation and classification in H&E-stained histology images. NucSegAI is based on the HoverNet backbone, and is trained on H&E-stained images with paired multiplex immunofluorescence imaging data. The current model is optimized for non-small-cell lung cancer images. 

## Environment setup

1. Create a new conda environment: `conda create -n nucsegai python=3.9`
2. Activate the environment: `conda activate nucsegai`
3. Install the library requirements for HoverNet: `pip install src_hovernet/requirements.txt`
4. Install the stain-tools: `pip install staintools`

## Image preparation

1. Images can be either patches/tiles in `.tiff` or whole-slide images (WSI) in `.svs`. 

2. Images are assumed to be captured at 40X magnification, with a resolution of 0.25 um/pixel. Improper resolution will generate suboptimal results. 

2. During model development, we found staining normalization is critical for generating accurate and consistent results. It is highly recommended to normalize the H&E staining before applying the model:

- `python3 stain_norm.py`

## Inference

1. Download the model weights ("NucSegAI_torch.tar") from the [HuggingFace](https://huggingface.co/OGevaertLab/NucSegAI/). 

2. Place it into a `model_bin/` folder under the same directory with this repo. 

3. Run `src_hovernet/run_tile.sh` for tile inference or `src_hovernet/run_wsi.sh` for WSI inference. 

## Relevant repositories: 

- StainTools: https://github.com/Peter554/StainTools 
- HoverNet: https://github.com/vqdang/hover_net



































