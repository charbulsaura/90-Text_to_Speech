#Assignment: Convert PDF to Audiobook
"""
Write a Python script that takes a PDF file and converts it into speech.
"""
"""
Too tired to read? Build a python script that takes a PDF file, identifies the text and converts the text to speech. 
Effectively creating a free audiobook.
AI text-to-speech has come so far. They can sound more lifelike than a real audiobook.

Using what you've learnt about HTTP requests, APIs and Python scripting, 
create a program that can convert PDF files to speech.

You right want to choose your own Text-To-Speech (TTS) API. But here are some you can consider:
http://www.ispeech.org/api/#introduction
https://cloud.google.com/text-to-speech/docs/basics
https://aws.amazon.com/polly/
"""
#Tasks
"""
1. (done) Connect Google API
2. (done) Load text file (PDF) --- Open PDF as text file python? How to store/convert text from PDF?
3. (done) Convert to audio 
"""
"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
import os
os.environ.__setitem__("GOOGLE_APPLICATION_CREDENTIALS", "text-to-speech-354423-b36ed9bdec52.json")
GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
print(GOOGLE_APPLICATION_CREDENTIALS)

#OPENS ANY PDF FILE OF CHOICE
import PyPDF2
INPUT_FILE_NAME = "#Syllabus+for+100+Days+of+Python"
# TEXT = "HELLO WORLD I AM HERE!"

pdf_file = open(f"{INPUT_FILE_NAME}.pdf","rb")
pdf_read = PyPDF2.PdfFileReader(pdf_file)
pdf_page = pdf_read.getPage(0)
TEXT = pdf_page.extractText()
print(TEXT)


from google.cloud import texttospeech
# Instantiates a client
client = texttospeech.TextToSpeechClient()
# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=TEXT)
# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)
# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)
# The response's audio_content is binary.
with open(f"output-{INPUT_FILE_NAME}.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print(f'Audio content written to file "output-{INPUT_FILE_NAME}.mp3"')
