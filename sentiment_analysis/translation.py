"""
import environ
from google.cloud import translate_v2 as translate

target = 'en'


def translation(text):
    translate_client = translate.Client()
    result = translate_client.translate(
        text,
        target_language=target
    )
    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))


translation('Hello world')
"""
from googletrans import Translator

def translate(text):
    translator = Translator()
    translation = translator.translate(text)
    return translation.text

print(translate("hola amigo"))