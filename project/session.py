import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

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
        'text': 'what is todays temperature'
    }
).get_result()
a=response['output']['generic'][0]['text']
print(a)
