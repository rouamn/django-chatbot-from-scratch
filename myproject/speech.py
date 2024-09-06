import speech_recognition
import pyttsx3
recognizer=speech_recognition.Recognizer()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("Listening:")
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            audio=recognizer.listen(mic)
            print("Recognizing:")
            text=recognizer.recognize_google(audio)
            print(text)
    except speech_recognition.RequestError:
        print("Network error.")
    except speech_recognition.UnknownValueError:
        print("Unable to recognize speech.")
    except speech_recognition.WaitTimeoutError:
        pass
    except speech_recognition.WaitTimeoutError:
        pass
    except KeyboardInterrupt:
        break