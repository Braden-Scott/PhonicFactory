import streamlit as st
from utils import get_phonetic_breakdown, get_syllables, generate_tts_audio

st.title("Phonics Sound Generator")

word = st.text_input("Enter a word:")

option = st.radio(
    "Choose how you want to hear the word:",
    ("Whole Word Pronunciation", "Phonetic Breakdown", "Letter by Letter Pronunciation")
)

if word:
    if option == "Whole Word Pronunciation":
        audio_path = generate_tts_audio(word, f"{word}_whole.mp3")
        st.audio(audio_path)

    elif option == "Phonetic Breakdown":
        syllables = get_syllables(word)
        phonemes = get_phonetic_breakdown(word)

        st.write(f"**Syllables:** {' - '.join(syllables)}")
        st.write(f"**Phonetic Breakdown:** {' '.join(phonemes)}")

        audio_path = generate_tts_audio(" ".join(phonemes), f"{word}_phonetic.mp3")
        st.audio(audio_path)

    elif option == "Letter by Letter Pronunciation":
        for letter in word:
            if st.button(f"Play {letter.upper()}"):
                audio_path = generate_tts_audio(letter, f"{letter}.mp3")
                st.audio(audio_path)
