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

text='what is the humidity'
def text2speech(text):
    with open('hum.mp3', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                text,
                voice='en-US_AllisonVoice',
                accept='audio/mp3'        
            ).get_result().content)
    playsound('hum.mp3')
text2speech(text)


