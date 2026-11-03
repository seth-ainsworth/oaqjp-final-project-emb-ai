from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def send_index():
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == 'None':
        return 'Invalid text! Please try again!'


    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

if __name__ == "__main__":
    app.run()