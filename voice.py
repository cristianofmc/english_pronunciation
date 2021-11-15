import speech_recognition as sr

class Voice:
    def __init__(self) -> None:

        self.recognizer = sr.Recognizer()

    def speaker(self):
        with sr.Microphone() as source:
            print("Talk\n")
            audio_text = self.recognizer.listen(source)
            print('Recorded!')
            print("Processing...")
            try:
                text = self.recognizer.recognize_google(audio_text, language='en-US').lower()
            except:
                print("Sorry, I did not get that")
        return text
