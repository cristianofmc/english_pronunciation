import speech_recognition as sr

class Voice:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()

    def speaker(self):
        with sr.Microphone() as source:
            print("Please talk\n")
            audio_text = self.recognizer.listen(source)
            print("Recorded!")
            print("Processing...")
            try:
                text = self.recognizer.recognize_google(audio_text, language="en-US").lower()
            except:
                print("Sorry, unable to process audio, please try again.")
        return text
