import streamlit as st
import speech_recognition as sr

option = st.selectbox(
    'Choisissez une API de reconnaissance faciale :',
    ('Google Speech Recognition', 'Pyaudio', 'Librosa')
)
st.write('Vous avez sélectionné:', option)


def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Parler maintenant ")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transciption ...")

        try:
            status = st.radio("Select Gender: ", ('Francais', 'Anglais', 'Espagnol'))
            if status == "Francais":
                text = r.recognize_google(audio_text, language="fr-FR")
                return text

            if status == "Anglais":
                text = r.recognize_google(audio_text, language="en-GB")
                return text

            if status == "Espagnol":
                text = r.recognize_google(audio_text, language="es-AR")
                return text

        except:
            return "Desole impossible à transcrire"

def main():
    st.title("reconnaissance vocale ")
    st.write("Clicker pour commencer à lire votre texte:")

    # add a button to trigger speech recognition
    if st.button("enregistrement"):
        text = transcribe_speech()
        st.write("Transcription: ", text)
if __name__ == "__main__":
    main()