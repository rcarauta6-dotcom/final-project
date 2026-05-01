"""
This module implements a Flask web server for the Emotion Detection application.
It provides routes to render the main page and to process text for emotion analysis.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Renders the main index.html page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """
    Processes the text input from the user, passes it to the emotion_detector,
    and returns the formatted response or an error message if the text is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    