import base64
import io
from PIL import Image
import numpy as np

def decode_frame(data):
    data = data.replace('data:image/jpeg;base64,', '')
    img_bytes = base64.b64decode(data)
    img = Image.open(io.BytesIO(img_bytes))
    frame = np.array(img)
    return frame
