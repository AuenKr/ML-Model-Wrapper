import cv2
import numpy as np
import onnxruntime as rt
import os

script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, './best.onnx')

ort_session = rt.InferenceSession(model_path)

def preprocess(image):
    input_size = (640, 640)
    image_resized = cv2.resize(image, input_size)
    image_resized = image_resized.astype(np.float32) / 255.0
    image_transposed = np.transpose(image_resized, (2, 0, 1))
    input_tensor = np.expand_dims(image_transposed, axis=0)
    return input_tensor

def postprocess(outputs, confidence_threshold=0.15, iou_threshold=0.1):
    # Assuming 'outputs' is a list of numpy arrays containing predictions
    predictions = outputs[0]  # Modify this based on your model's output structure
    # Perform Non-Maximum Suppression (NMS) and filter out low confidence boxes
    boxes, scores, class_ids = [], [], []
    for prediction in predictions:
        if prediction[4] > confidence_threshold:  # Assuming the confidence score is at index 4
            boxes.append(prediction[:4])
            scores.append(prediction[4])
            class_ids.append(np.argmax(prediction[5:]))  # Assuming class scores start at index 5

    # Apply NMS
    indices = cv2.dnn.NMSBoxes(boxes, scores, confidence_threshold, iou_threshold)
    if len(indices) == 0:
        return []
    return [(boxes[i], scores[i], class_ids[i]) for i in indices.flatten()]

def count_cattle(frame):
    input_tensor = preprocess(frame)
    outputs = ort_session.run(None, {ort_session.get_inputs()[0].name: input_tensor})
    predictions = postprocess(outputs[0])
    cattle_count = len(predictions)
    boxes_scores = [(box, score) for (box, score, _) in predictions]
    return cattle_count, boxes_scores
