import json
from argparse import ArgumentParser
from infer_image import infer_image

# pass args
parser = ArgumentParser()
parser.add_argument('--img', type =str, default = "00002.png")
args = parser.parse_args()

# retrive image result
infer_image(args.img)



