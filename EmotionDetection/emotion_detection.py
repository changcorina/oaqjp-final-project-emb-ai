import requests  
import json

def emotion_detector(text_to_analyse): 
     # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header) 

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extract emotions and their scores
    if response.status_code == 200:
        emotions_data = formatted_response["emotionPredictions"][0]["emotion"]
        emotions = {
            "anger": emotions_data["anger"],
            "disgust": emotions_data["disgust"],
            "fear": emotions_data["fear"],
            "joy": emotions_data["joy"],
            "sadness": emotions_data["sadness"],
            "dominant_emotion": max(["anger", "disgust", "fear", "joy", "sadness"],
                                key=lambda x: emotions_data[x])
        }
    elif response.status_code == 400:
        emotions = {
            "anger": None, "disgust": None, "fear": None, "joy": None,
            "sadness": None, "dominant_emotion": None
        }
    return emotions