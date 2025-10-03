"""
AI-based Web application
    
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes the emotional sentiment of the input text.
        
    Returns:
        dict: A dictionary with emotion scores 
        (e.g., {'anger': 0.1, 'joy': 0.8}) and 'dominant_emotion'.
    
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
     # Extract emotions and values (excluding dominant_emotion)
    emotions = {k: v for k, v in response.items() if k != "dominant_emotion"}
    dominant = response["dominant_emotion"]
    # Format the string by joining emotions with commas and 'and' before the last one
    emotion_parts = [f"'{k}': {v}" for k, v in emotions.items()]
    emotion_list = ", ".join(emotion_parts[:-1]) + " and " + emotion_parts[-1]

    # Construct the full output string
    if dominant is None:
        return "Invalid text! Please try again!"

    prefix = "For the given statement, the system response is"
    suffix = "The dominant emotion is"
    return f"{prefix} {emotion_list}. {suffix} {dominant}."


@app.route("/")
def render_index_page():
    """
    Render index page.
        
    Returns:
        page index.html.
    
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
