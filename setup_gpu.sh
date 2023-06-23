#!/bin/bash
#!/usr/bin/env bash -l

# conda create -n paocr python=3.10
python3 -m pip install pymupdf
python3 -m pip install "paddleocr>=2.0.1" # Recommend to use version 2.0.1+
pip3 install Pillow
python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
python3 -m pip install paddlepaddle-gpu
unset LD_LIBRARY_PATH