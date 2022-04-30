import six
import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"D:\HACKATHONS\env\creatica-server-keys.json"
def translation(text,target):
    translate_client=translate.Client()
    # text="Good"
    # target='hi'

    result= translate_client.translate(
        text,
        target_language=target
    )
    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))



text = input("Enter the message:")
str = input('Language:')
translation(text,str)
