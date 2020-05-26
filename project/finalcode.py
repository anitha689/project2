import json
from os.path import join, dirname
from ibm_watson import TextToSpeechV1, AssistantV2, SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

authenticator = IAMAuthenticator('4wkdjQhdPLJHesobhZvWNHKlkdJDFnszT6tDnUjOg6Oq')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/f3299ed8-6a49-48c8-afe2-3add5fdb08f8')

authenticator = IAMAuthenticator('7dv4U-FsuSOt_CrJyQETorUdhTH_24TlnoIuFOUszrRa')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/d6125149-3261-4c24-b78a-485be8f1d69e')


def speech2text(file):
    with open(join(dirname(__file__), './.', file),
               'rb') as audio_file:
        results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
        
    ).get_result()
    a=results['results'][0]['alternatives'][0]['transcript']
    return a

def chatbot_123(text):
    authenticator = IAMAuthenticator('7KJRLPXL_21oNMXWNxubBGuHzAQkRrqXepWmDjThYB-R')
    assistant = AssistantV2(
        version='2020-04-01',
        authenticator = authenticator
    )

    assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/9c900750-5d1e-4049-ad1b-16b9d02c3124')
    aid='9fcbfad5-528f-42f8-968d-89afdad4b8c8'
    response = assistant.create_session(
        assistant_id=aid
    ).get_result()

    a=response['session_id']
    response = assistant.message(
        assistant_id=aid,
        session_id=a,
        input={
            'message_type': 'text',
            'text': text
        }
    ).get_result()
    a=response['output']['generic'][0]['text']
    print(a)
    return a

def text2speech(text):
    with open('sample.mp3', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                text,
                voice='en-US_AllisonVoice',
                accept='audio/mp3'        
            ).get_result().content)
    playsound('sample.mp3')

playsound('welcome.mp3')
a="hum.mp3"
b=speech2text(a)
c=chatbot_123(b)
playsound(a)
text2speech(c)
