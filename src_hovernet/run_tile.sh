python src_hovernet/run_infer.py \
--gpu='0' \
--nr_types=7 \
--type_info_path=src_hovernet/type_info.json \
--batch_size=4 \
--model_mode=fast \
--model_path=model_bin/NucSegAI_NSCLC.tar \
--nr_inference_workers=0 \
--nr_post_proc_workers=0 \
tile \
--input_dir=std_output \
--output_dir=pred \
--mem_usage=0.2 \