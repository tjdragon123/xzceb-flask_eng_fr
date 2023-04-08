'''
translates from french to english or vice versa
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('n8XMcJWr8gLtwnEXh77SJW8_wXyy7mDmk_uDqAyMXOvm')
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')


def english_to_french(english_text):
    '''translates from english to french'''
    if english_text != '':
        french_text = translator.translate(
        text=english_text,
        model_id='en-fr').get_result()['translations'][0]['translation']
    else: french_text = ''
    return french_text

def french_to_english(french_text):
    '''translates from french to english'''
    if french_text != '':
        english_text = translator.translate(
            text=french_text,
            model_id='fr-en').get_result()['translations'][0]['translation']
    else: english_text = ''
    return english_text
