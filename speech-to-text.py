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
