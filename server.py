from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract emotions and values (excluding dominant_emotion)
    emotions = {k: v for k, v in emotion_data.items() if k != "dominant_emotion"}
    dominant = emotion_data["dominant_emotion"]

    # Format the string by joining emotions with commas and 'and' before the last one
    emotion_parts = [f"'{k}': {v}" for k, v in emotions.items()]
    emotion_list = ", ".join(emotion_parts[:-1]) + " and " + emotion_parts[-1]

    # Return a formatted string 
    return f"For the given statement, the system response is {emotion_list}. The dominant emotion is {dominant}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)