import streamlit as st
from utils import get_phonetic_breakdown, get_syllables, generate_tts_audio

# Custom CSS for styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Chewy&display=swap');

        /* New Background */
        @property --g9-a{
            syntax: '<angle>';
            inherits: true;
            initial-value: 0deg;
        }
        @property --g9-p {
            syntax: '<percentage>';
            inherits: true;
            initial-value: 0%;
        }
        @property --g9-c1 {
            syntax: '<color>';
            inherits: true;
            initial-value: #000;
        }
        @property --g9-c2 {
            syntax: '<color>';
            inherits: true;
            initial-value: #000;
        }
        html {
            --s: 80px; /* control the size */
            --_g: #0000, var(--g9-c1) 2deg calc(var(--g9-a) - 2deg),#0000 var(--g9-a);
            background: 
                conic-gradient(from calc(-45deg  - var(--g9-a)/2) at top    var(--g9-p) left  var(--g9-p),var(--_g)),
                conic-gradient(from calc(-45deg  - var(--g9-a)/2) at top    var(--g9-p) left  var(--g9-p),var(--_g)),
                conic-gradient(from calc( 45deg  - var(--g9-a)/2) at top    var(--g9-p) right var(--g9-p),var(--_g)),
                conic-gradient(from calc( 45deg  - var(--g9-a)/2) at top    var(--g9-p) right var(--g9-p),var(--_g)),
                conic-gradient(from calc(-135deg - var(--g9-a)/2) at bottom var(--g9-p) left  var(--g9-p),var(--_g)),
                conic-gradient(from calc(-135deg - var(--g9-a)/2) at bottom var(--g9-p) left  var(--g9-p),var(--_g)),
                conic-gradient(from calc( 135deg - var(--g9-a)/2) at bottom var(--g9-p) right var(--g9-p),var(--_g)),
                conic-gradient(from calc( 135deg - var(--g9-a)/2) at bottom var(--g9-p) right var(--g9-p),var(--_g))
                var(--g9-c2);
            background-size: calc(2*var(--s)) calc(2*var(--s));
            animation: g9 2s infinite alternate linear;
        }

        @keyframes g9 {
            0%,15% {
                --g9-a: 135deg;
                --g9-p: 20%;
                --g9-c1: #3B8183;
                --g9-c2: #FAD089;
                background-position: 0 0,var(--s) var(--s);
            }
            45%,50% {
                --g9-a: 90deg;
                --g9-p: 25%;
                --g9-c1: #3B8183;
                --g9-c2: #FAD089;
                background-position: 0 0,var(--s) var(--s);
            }
            50.01%,55% {
                --g9-a: 90deg;
                --g9-p: 25%;
                --g9-c2: #3B8183;
                --g9-c1: #FAD089;
                background-position: var(--s) 0,0 var(--s);
            }
            85%,100% {
                --g9-a: 135deg;
                --g9-p: 20%;
                --g9-c2: #3B8183;
                --g9-c1: #FAD089;
                background-position: var(--s) 0,0 var(--s);
            }
        }

        /* Original Body Styling */
        body {
            opacity: 0.8;
        }   

        .home-title {
            font-family: "Chewy", system-ui;
            font-size: 100px;
            color: white;
            padding: 50px 10px;
            text-align: center;
            border-radius: 30px;
            margin-top: -20px;
            width: 100%; /* Adjusts the banner width */
            max-width: 1200px; /* Limits max width so it doesn't get too stretched */
            margin-left: auto;
            margin-right: auto;
            opacity: 1 !important;
        }
        .home-content {
            font-size: 18px;
            color: #555;
        }
        .title {
            font-family: "Chewy", system-ui;
            color: #ffffff;
            font-size: 32px;
            font-weight: bold;
        }
        .syllable {
            color: #FF5722;
        }

        /* New Section Styling */
        .container {
            display: flex;
            justify-content: space-between;
            font-family: "Chewy", system-ui;
            text-align: center;
            margin-top: 100px;
        }
        .box, .box2 {
            background-color: #04122f; /* Solid color */
            padding: 20px;
            border-radius: 10px;
            flex: 1;
            margin: 0 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0);
        }
        .box2 {
            margin-top: 70px;
            margin-bottom: 150px;
        }            
        .number {
            font-size: 28px;
            font-weight: bold;
            color: #1E88E5;
        }
        .text {
            font-size: 20px;
            font-family: "Roboto";
            color: #ffffff ;
        }
        .container-title, h1{
            margin-top: 100px;
            text-align: center;
            font-family: "Chewy", system-ui;
        }

    </style>
""", unsafe_allow_html=True)

# Navigation menu
menu = st.sidebar.selectbox("Select a page", ["Home", "Phonics Sound Generator"])

if menu == "Home":
    # Home page content
    st.markdown('<h1 class="home-title">WELCOME TO PHONIC FACTORY</h1>', unsafe_allow_html=True)

    # New Three-column section
    st.markdown("""
        <div class="container-title"><h1>Why literacy rates are declining:</h1></div>
        <div class="container">
            <div class="box">
                <div class="number">01</div>
                <div class="text">Schools have deemphasized the importance of sounding out words</div>
            </div>
            <div class="box">
                <div class="number">02</div>
                <div class="text">They’ve replaced it with a “balanced literacy approach” with emphasis on sight words</div>
            </div>
            <div class="box">
                <div class="number">03</div>
                <div class="text">Sight words leave students at the mercy of whether they’ve seen the word or not</div>
            </div>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
        <div class="container-title"><h1>What is Phonic factory?</h1>
            <div class="box2">
                <div class="text">Phonic Factory is a gamified web application that specializes in teaching those who want to improve their English reading skills. This is accomplished through teaching how each word can be sounded out in online texts or texts the user uploads.</div>
            </div>
        </div>
        
     """, unsafe_allow_html=True)
    

    # st.write("""
    #     This website helps you learn phonetic breakdowns of words, 
    #     syllable pronunciation, and whole word pronunciations.
    #     You can enter a word, and the tool will generate phonetic breakdowns 
    #     and provide audio pronunciations for each part of the word.
        
    #     ### Features:
    #     - Hear the full word pronunciation.
    #     - Break the word down into its phonetic components.
    #     - Listen to the word pronounced letter by letter.

    #     ### How to use:
    #     1. Go to the "Phonics Sound Generator" page.
    #     2. Enter any word you'd like to hear pronounced.
    #     3. Choose an option for hearing the word.
    # """)

    # Add an image
    st.image("https://t4.ftcdn.net/jpg/05/17/28/55/240_F_517285522_di6KZJGee8j0vfC07Kf8XTRF5hK9ohsS.jpg", caption="Learn Phonics!", width=700)

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
