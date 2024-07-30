# Imports
from tflite_support.task import vision
from tflite_support.task import core
from tflite_support.task import processor
import os

script_dir = os.path.dirname(__file__)

def model():
    model_path = os.path.join(script_dir, "./../model/ssd_mobilenet_v1.tflite")

    base_options = core.BaseOptions(file_name=model_path)
    detection_options = processor.DetectionOptions(max_results=2)
    options = vision.ObjectDetectorOptions(base_options=base_options, detection_options=detection_options)

    detector = vision.ObjectDetector.create_from_options(options)

    return detector

def objectDetectionModel(image):
    image = vision.TensorImage.create_from_buffer(image)

    detector = model()

    detection_result = detector.detect(image)

    detections_list = []
    for detection in detection_result.detections:
        bounding_box = {
            "origin_x": detection.bounding_box.origin_x,
            "origin_y": detection.bounding_box.origin_y,
            "width": detection.bounding_box.width,
            "height": detection.bounding_box.height
        }
        category = {
            "index": detection.categories[0].index,
            "score": detection.categories[0].score,
            "display_name": detection.categories[0].display_name,
            "category_name": detection.categories[0].category_name
        }
        detection_dict = {
            "bounding_box": bounding_box,
            "categories": [category]
        }
        detections_list.append(detection_dict)

    return detections_list