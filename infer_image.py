import json
from paddleocr import PaddleOCR

# Applying OCR with PAOCR-v3
ocr = PaddleOCR(use_angle_cls=True) # need to run only once to download and load model into memory

# function to infer image
def infer_image(image):
    # Pass image name as a str 
    image_name = image[:-4]
    image_path = "result/" + image_name + ".json"

    # Inference from OCR
    infer = ocr.ocr(image)
    result = [line[1][0] for line in infer[0]]

    # Dump image in jsonl file
    with open(image_path, 'w') as json_file:
        json.dump(result, json_file)
