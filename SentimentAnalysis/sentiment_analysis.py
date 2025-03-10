# Task 3: Format the output of the application
# Task 4: Package the application
# Task 7: Incorporate Error handling

import requests
import json

def sentiment_analyzer(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}

# from sentiment_analysis import sentiment_analyzer
# sentiment_analyzer("I love this new technology.")
# export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "
# from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
# sentiment_analyzer("This is fun.")
# python3.11
# from . import sentiment_analysis
# from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
# sentiment_analyzer("This is fun.")