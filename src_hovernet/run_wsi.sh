python src_hovernet/run_infer.py \
--gpu='0' \
--nr_types=7 \
--type_info_path=src_hovernet/type_info.json \
--batch_size=48 \
--model_mode=fast \
--model_path=model_bin/NucSegAI_NSCLC.tar \
--nr_inference_workers=0 \
--nr_post_proc_workers=0 \
wsi \
--input_dir=/scratch/st-kenfield-1/repo_data/NucSegAI/std_output \
--output_dir=/scratch/st-kenfield-1/repo_data/NucSegAI/pred \
--input_mask_dir=mask \
--save_thumb \
--save_mask