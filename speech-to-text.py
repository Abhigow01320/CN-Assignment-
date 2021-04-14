from scipy.io import wavfile
import numpy as np
def audio_file_to_text(audio_file):
    import speech_recognition as sr
    import pyttsx3
    r = sr.Recognizer()



    with sr.AudioFile(audio_file) as source:
        audio_text = r.listen(source)
        try:
            data = r.recognize_google(audio_text)
            print(data)
        except:
            print('Sorry.. run again...')


# audio_file_to_text("male.wav")

def quick_speech_to_text():
    import speech_recognition as sr
    r = sr.Recognizer()
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            print("Text: "+r.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")


# quick_speech_to_text()
def convertAudioFiletoText():
    """
    Accepts only audio files with .WAV extension 
    """
    import speech_recognition as sr
    from os import path                                                       
    # AUDIO_FILE = "cysec.wav"
    AUDIO_FILE = "hello-world.wav"

    # use the audio file as the audio source                                        
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)  # read the entire audio file                  
            print("Transcription: ", r.recognize_google(audio, language = 'en-IN' ))
            # print("Transcription: ", r.recognize_google(audio, language = 'en-US' ))
convertAudioFiletoText()

def readAudioFile():
    import wave
    obj = wave.open('cysec.wav','r')
    print( "Number of channels",obj.getnchannels())
    print ( "Sample width",obj.getsampwidth())
    print ( "Frame rate.",obj.getframerate())
    print ("Number of frames",obj.getnframes())
    print ( "parameters:",obj.getparams())
    obj.close()            
# readAudioFile()    