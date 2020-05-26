import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('7dv4U-FsuSOt_CrJyQETorUdhTH_24TlnoIuFOUszrRa')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/d6125149-3261-4c24-b78a-485be8f1d69e')

with open(join(dirname(__file__), './.', 'sample.mp3'),
               'rb') as audio_file:
    results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
        
    ).get_result()
a=results['results'][0]['alternatives'][0]['transcript']
print(a)
