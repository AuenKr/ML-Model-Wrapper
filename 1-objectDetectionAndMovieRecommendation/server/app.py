from flask import Flask, request, jsonify
from utils.movie import get_recommendations
from utils.objectDetection import objectDetectionModel

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        'msg': "Server running fine"
    })

@app.route('/movies', methods=['POST'])
def predict():
    try:
        data = request.json
        count = data['count']

        prediction = get_recommendations(data['movie_title'], count)
    
        return jsonify({'movies': prediction})
    except:
        return jsonify({
            'msg': "Internal server error"
        }), 500

@app.route('/object', methods=['POST'])
def objectDetection():
    try:
        received_image = request.files['image']
        image = received_image.stream.read()
        result = objectDetectionModel(image)
        return jsonify({
            'result': result
        })
    except:
        return jsonify({
            'msg': "Internal server error"
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
