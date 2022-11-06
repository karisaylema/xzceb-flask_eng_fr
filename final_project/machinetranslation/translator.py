"""Module providingFunction ibm watson."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
MODEL_ID_1 = 'en-fr'
MODEL_ID_2 = 'fr-en'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """Function translate english to french."""
    try:
        french_text = language_translator.translate(
        text=english_text,
        model_id=MODEL_ID_1).get_result()
        texto= french_text['translations'][0]['translation']
    except:
        texto=None
    return texto

def french_to_english(french_text):
    """Function translate french to english."""
    try: 
        english_text=language_translator.translate(
        text=french_text,
        model_id=MODEL_ID_2).get_result()
        texto= english_text['translations'][0]['translation']
    except:
        texto=None
    return texto