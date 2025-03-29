import streamlit as st
from utils import get_phonetic_breakdown, get_syllables, generate_tts_audio

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-ser if;
        }
        .home-title {
            font-size: 36px;
            color: #4CAF50;
        }
        .home-content {
            font-size: 18px;
            color: #555;
        }
        .button {
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
        }
        .title {
            color: #1E88E5;
            font-size: 32px;
            font-weight: bold;
        }
        .syllable {
            color: #FF5722;
        }
    </style>
    """, unsafe_allow_html=True)

# Navigation menu
menu = st.sidebar.selectbox("Select a page", ["Home", "Phonics Sound Generator"])

if menu == "Home":
    # Home page content
    st.markdown('<h1 class="home-title">Welcome to the Phonics Sound Generator!</h1>', unsafe_allow_html=True)
    
    st.write("""
        This website helps you learn phonetic breakdowns of words, 
        syllable pronunciation, and whole word pronunciations.
        You can enter a word, and the tool will generate phonetic breakdowns 
        and provide audio pronunciations for each part of the word.
        
        ### Features:
        - Hear the full word pronunciation.
        - Break the word down into its phonetic components.
        - Listen to the word pronounced letter by letter.

        ### How to use:
        1. Go to the "Phonics Sound Generator" page.
        2. Enter any word you'd like to hear pronounced.
        3. Choose an option for hearing the word.
    """)

    # Add an image
    st.image("https://www.example.com/phonics_image.jpg", caption="Learn Phonics!", width=700)

elif menu == "Phonics Sound Generator":
    # Phonics sound generator page
    st.markdown('<h1 class="title">Phonics Sound Generator</h1>', unsafe_allow_html=True)

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
