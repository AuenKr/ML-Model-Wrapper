from modal.utils import count_cattle
from utils.decodeFrame import decode_frame
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('video_stream')
def handle_video_stream(data):
    frame = decode_frame(data)
    cattle_count, boxes_scores = count_cattle(frame)
    
    # Convert boxes_scores to a list of lists with native float objects
    boxes_scores_list = [[float(x) for x in box_score[:4]] + [float(score)] for box_score, score in boxes_scores]

    emit('cattle_count', {'count': cattle_count, 'boxes_scores': boxes_scores_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    socketio.run(app)
