import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { "grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock" }
    input = { "raw_document" : { "text" : text_to_analyze } }
    response = requests.post(url, json = input, headers=headers)

    response_obj = json.loads(response.text)
    emotions = response_obj['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    dominant_score = 0
    dominant_emotion_index = 0

    for i, emotion in enumerate(list(emotions.values())):
        if dominant_score < emotion:
            dominant_score = emotion
            dominant_emotion_index = i


    dominant_emotion = list(emotions.keys())[dominant_emotion_index]


    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
