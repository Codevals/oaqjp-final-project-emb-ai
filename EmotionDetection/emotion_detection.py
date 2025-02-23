import requests, json

def emotion_detector(text_to_analyze):
    # url of the API emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Custom header specifying the model ID for emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Sending the POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    #if the response status code is 200, extract label and score
    if response.status_code == 200:
        # Extracting emotion charactersitics from the response
        formatted_response = formatted_response['emotionPredictions'][0]['emotion']
        #extracting emotion anger, fear, joy, sadness, and dominant_emotion from the response
        data = {
            'anger': formatted_response['anger'],
            'disgust': formatted_response['disgust'],
            'fear': formatted_response['fear'],
            'joy': formatted_response['joy'],
            'sadness': formatted_response['sadness']
        }
        dominant_emotion = max(data, key=data.get)
        #return response json from API
        return {
            'anger': formatted_response['anger'],
            'disgust': formatted_response['disgust'],
            'fear': formatted_response['fear'],
            'joy': formatted_response['joy'],
            'sadness': formatted_response['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        return {
            'anger': "",
            'disgust': "",
            'fear': "",
            'joy': "",
            'sadness': "",
            'dominant_emotion': None
        }