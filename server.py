# Import Flask, render_template, request from the flask framework package 
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector
# Initiate the flask app
app = Flask("Emotion Analyzer")
@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    #check if the dominant_emotion is none
    if dominant_emotion is None:
        return "Invalid text! try again"
    # Extract the anger, digust, fear, joy, sadness and dominant_emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    return f"'Anger': {anger}, 'disgust:' {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}, The dominant emotion is {dominant_emotion} "

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # To be completed
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000'''
    # To be completed
    app.run(host="0.0.0.0", port=5000)
