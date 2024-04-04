from openai import OpenAI
from pydub import AudioSegment
import requests
from requests.auth import HTTPBasicAuth
client = OpenAI()
def open_ai_s2t(client, audio_file_path):
	with open(audio_file_path, "rb") as f:
	transcription = client.audio.transcriptions.create(
	  model="whisper-1", 
	  file=f
	)
	return(transcription.text)

def divide_audio(audio_file_path, from=0, to=10):
    audio = AudioSegment.from_mp3()
    lower = from * 60 * 1000 # PyDub handles time in milliseconds
    upper = to * 60 * 1000 # PyDub handles time in milliseconds
    first_10_minutes = song[lower:upper]
    first_10_minutes.export(audio_file_path, format="mp3")

## zamzar convert from a format to another
with open("zamzar_api_key.ini", "r") as f:
	api_key = f.read()

endpoint = "https://sandbox.zamzar.com/v1/jobs"
source_file = "/tmp/portrait.gif"
target_format = "png"

file_content = {'source_file': open(source_file, 'rb')}
data_content = {'target_format': target_format}
res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
print res.json()



file_id = 3
local_filename = '/tmp/portrait.png'
endpoint = f"https://sandbox.zamzar.com/v1/files/{file_id}/content"

response = requests.get(endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))

try:
  with open(local_filename, 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
      if chunk:
        f.write(chunk)
        f.flush()

    print "File downloaded"

except IOError:
  print "Error"