#!/bin/bash
conda activate /share/pre_envs/icamp3_lmdeploy
lmdeploy serve gradio /share/new_models/Shanghai_AI_Laboratory/internlm2-chat-1_8b  --cache-max-entry-count 0.1
