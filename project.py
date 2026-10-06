import speech_recognition as sr
import pyttsx3 
#text to audio library
from googletrans import Translator

def speak(text,language="en"):
    engine=pyttsx3.init()
    # initialise functions available in pyttsx3
    engine.setProperty('rate', 150)
    voices=engine.getProperty('voices')
    if language=='en':
        engine.setProperty('voice', voices[0], id)
    else:
        engine.setProperty('voice', voices[1], id)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recogniser=sr.Recognizer()
    with sr.Microphone as source:
        print("Speak in English now......")
        audio = recogniser.listen(source)
    try:
        print("Recognising speech...")
        text = recogniser.recognize_google(audio, language='en-US')
        print(f"You said: {text}")
        return text

    except sr.UnknownValueError:
        print("Couldn't understand audio! :(")
    except sr.RequestError as e:
        print(f"Request error: {e}")

    return ""

def translate_text(text, target_language='es'):
    translator=Translator()
    translation=translator.translate(text, dest=target_language)
    print(f"Translation:{translation.text}")

    return translation.text

def display_language_options():

    print("Available translation languages: ")

    print("1. Hindi (hi)")

    print("2. Tamil (ta)")

    print("3. Telugu (te)")

    print("4. Bengali (bn)")

    print("5. Marathi (mr)")

    print("6. Gujarati (gu)")

    print("7. Malayalam (ml)")

    print("8. Punjabi (pa)")



    # User selects language

    choice = input("Please select the target language number (1-8): ")

    language_dict = {

        "1": "hi",

        "2": "ta",

        "3": "te",

        "4": "bn",

        "5": "mr",

        "6": "gu",

        "7": "ml",

        "8": "pa"

    }



    return language_dict.get(choice, "es")  # Default to Spanish if invalid input



# Main function to combine all steps

def main():

    # Step 1: Display language options and get user's choice

    target_language = display_language_options()



    # Step 2: Speech-to-Text (recognizing English speech)

    original_text = speech_to_text()



    if original_text:

        # Step 3: Translate to selected target language

        translated_text = translate_text(original_text, target_language=target_language)



        # Step 4: Text-to-Speech (Translate output and speak it)

        speak(translated_text, language="en")  # Speak the translation in English

        print("✅ Translation spoken out!")



main()