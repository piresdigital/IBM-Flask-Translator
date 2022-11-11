"""
This module translates between english and portuguese
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['APIKEY']
URL = os.environ['URL']

authenticator = IAMAuthenticator(API_KEY)

language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(URL)

def english_to_portuguese(english_text = ''):
    """
    Take english text and translate to portuguese.
    Return '' if no text is provided.
    """
    if english_text == '':
        return english_text
    translation = language_translator.translate(
        text = english_text,
        model_id = 'en-pt'
    ).get_result()

    portuguese_text = translation['translations'][0]['translation']

    return portuguese_text

def french_to_english(portuguese_text = ''):
    """
    Take portuguese text and translate to english.
    Return '' if no text is provided.
    """
    if portuguese_text == '':
        return portuguese_text
    translation = language_translator.translate(
        text = portuguese_text,
        model_id = 'pt-en'
    ).get_result()

    english_text = translation['translations'][0]['translation']

    return english_text
