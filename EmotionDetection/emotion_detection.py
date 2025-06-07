import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url=url, json=input_json, headers=headers)
    response_dict = response.json()
    emotion_predict_dict = response_dict['emotionPredictions'][0]['emotion']
    max_emotion_predict_value = max(emotion_predict_dict.values())
    for i in emotion_predict_dict.keys():
        if emotion_predict_dict[i] == max_emotion_predict_value:
            dominant_emotion = i
    emotion_predict_dict["dominant_emotion"] = dominant_emotion
    return emotion_predict_dict
