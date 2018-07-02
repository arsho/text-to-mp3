import os
from gtts import gTTS

from utils.helpers import generate_short_timestamp, generate_current_timestamp


def text_file_to_mp3(filename = None):
    try:
        with open(filename) as fp:
            lines = fp.readlines()
            lines = " ".join(lines)
            tts = gTTS(text=lines, lang='en', slow=False)
            output_filename = filename+".mp3"
            tts.save(output_filename)
            return output_filename
    except:
        return None

def text_to_mp3(text = None, directory = None, output_filename = None):
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        filename = generate_current_timestamp()+".mp3"
        if output_filename and output_filename.strip()!='':
            filename = output_filename+generate_short_timestamp()+".mp3"
        filename = os.path.join(directory, filename)
        tts.save(filename)
        return filename
    except Exception as e:
        print(str(e))
        return None
