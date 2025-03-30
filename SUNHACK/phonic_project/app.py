import streamlit as st
from utils import get_phonetic_breakdown, get_syllables, generate_tts_audio
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Vincent\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
# CSS Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Chewy&display=swap');

        /* New Background */
        .stApp {
    @property --g9-a {
        syntax: '<angle>';
        inherits: true;
        initial-value: 0deg;
    }
    @property --g9-p {
        syntax: '<percentage>';
        inherits: true;
        initial-value: 100%;
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
    --s: 80px; /* Control the size */
    --_g: #0000, var(--g9-c1) 2deg calc(var(--g9-a) - 2deg), #0000 var(--g9-a);
    background: 
        conic-gradient(from calc(-45deg  - var(--g9-a)/2) at top    var(--g9-p) left  var(--g9-p),var(--_g)),
        conic-gradient(from calc(-45deg  - var(--g9-a)/2) at top    var(--g9-p) left  var(--g9-p),var(--_g)),
        conic-gradient(from calc( 45deg  - var(--g9-a)/2) at top    var(--g9-p) right var(--g9-p),var(--_g)),
        conic-gradient(from calc( 45deg  - var(--g9-a)/2) at top    var(--g9-p) right var(--g9-p),var(--_g)),
        conic-gradient(from calc(-135deg - var(--g9-a)/2) at bottom var(--g9-p) left  var(--g9-p),var(--_g)),
        conic-gradient(from calc(-135deg - var(--g9-a)/2) at bottom var(--g9-p) left var(--g9-p),var(--_g)),
        conic-gradient(from calc( 135deg - var(--g9-a)/2) at bottom var(--g9-p) right var(--g9-p),var(--_g)),
        conic-gradient(from calc( 135deg - var(--g9-a)/2) at bottom var(--g9-p) right var(--g9-p),var(--_g))
        var(--g9-c2);
    background-size: calc(2 * var(--s)) calc(2 * var(--s));
    animation: g9 2s infinite alternate linear;
    z-index: -1; /* Ensure the background stays behind */
    position: fixed;
    width: 100%;
    height: 100%;
}

@keyframes g9 {
    0%,15% {
        --g9-a: 135deg;
        --g9-p: 10%;
        --g9-c1: #3B8183;
        --g9-c2: #FAD089;
        background-position: 0 0, var(--s) var(--s);
    }
    45%,50% {
        --g9-a: 90deg;
        --g9-p: 25%;
        --g9-c1: #3B8183;
        --g9-c2: #FAD089;
        background-position: 0 0, var(--s) var(--s);
    }
    50.01%,55% {
        --g9-a: 90deg;
        --g9-p: 25%;
        --g9-c2: #3B8183;
        --g9-c1: #FAD089;
        background-position: var(--s) 0, 0 var(--s);
    }
    85%,100% {
        --g9-a: 100deg;
        --g9-p: 20%;
        --g9-c2: #3B8183;
        --g9-c1: #FAD089;
        background-position: var(--s) 0, 0 var(--s);
    }
}

/* Ensure text is solid and readable without transparency */
h1, h2, h3, p, .stText, .stMarkdown {
    color: white !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7); /* Light text shadow for better contrast */
}

/* Fix body transparency */
body {
    margin: 0;
    padding: 0;
    background: none !important;
}

/* Make only the necessary boxes solid */
.stApp .box, 
.stApp .box2, 
.stApp .box3, 
.stApp .single-box {
    background-color: rgba(0, 0, 0, 0.8) !important; /* Dark solid background */
    padding: 20px;
    border-radius: 10px;
    color: white !important;
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);
}

/* Banner and title */
.home-title {
    font-family: "Chewy", system-ui;
    font-size: 100px;
    color: white !important;
    background: rgba(0, 0, 0, 0);
    padding: 50px 10px;
    text-align: center;
    border-radius: 30px;
    margin-top: -20px;
    width: 100%; /* Adjusts the banner width */
    max-width: 1200px; /* Limits max width so it doesn't get too stretched */
    margin-left: auto;
    margin-right: auto;
    z-index: 10; /* Ensure the text is above the background */
    position: relative; /* Position relative to stack above the background */
}
.home-content {
    font-size: 18px;
    color: #555;
    z-index: 10;
}
.title {
    font-family: "Chewy", system-ui;
    color: #ffffff;
    font-size: 100px;
    font-weight: bold;
    z-index: 10;
}
.syllable {
    color: #FF5722;
    z-index: 10;
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
    margin-top:5px;
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
    font-size: 70px;
}

    </style>
""", unsafe_allow_html=True)

# Navigation menu
menu = st.sidebar.selectbox("Select a page", ["Home", "Phonics Sound Generator", "Image to Text"])

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
    
    st.image("https://t4.ftcdn.net/jpg/05/17/28/55/240_F_517285522_di6KZJGee8j0vfC07Kf8XTRF5hK9ohsS.jpg", caption="Learn Phonics!", width=700)

elif menu == "Phonics Sound Generator":
    # Phonics sound generator page
    st.markdown('<h1 class="title">Phonics Sound Generator</h1>', unsafe_allow_html=True)

    st.markdown("""
    <style>
        .stTextInput label {
            font-family: 'Roboto', sans-serif;
            font-size: 28px;
            font-weight: bold;
        }
        .stTextInput input {
            font-family: 'Roboto', sans-serif;
            font-size: 24px;
            padding: 15px;
            border-radius: 10px;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

    word = st.text_input("Enter a word:", key="word")

    st.markdown("""
    <style>
        .stRadio label {
            font-family: 'Roboto', sans-serif;
            font-size: 28px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    option = st.radio(
        "Choose how you want to hear the word:",
        ("Whole Word Pronunciation", "Phonetic Breakdown", "Letter by Letter Pronunciation")
    )

    # Custom CSS to make text and button labels bigger
    st.markdown("""
    <style>
        .stWrite, .stText {
            font-family: 'Calibri', sans-serif;
            font-size: 40px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    # Putting the entire logic in a box
    if word:
        with st.container():
            st.markdown("""
            <style>
                .st-box {
                    padding: 20px;
                    border: 2px solid #000;
                    border-radius: 10px;
                    background-color: #f1f1f1;
                    font-family: 'Calibri', sans-serif;
                    font-size: 20px;
                }
            </style>
            """, unsafe_allow_html=True)

            if option == "Whole Word Pronunciation":
                audio_path = generate_tts_audio(word, f"{word}_whole.mp3")
                st.audio(audio_path)

            elif option == "Phonetic Breakdown":
                syllables = get_syllables(word)
                phonemes = get_phonetic_breakdown(word)

                # Displaying syllables and phonetic breakdown inside the box
                st.write(f"**Syllables:** {' - '.join(syllables)}")
                st.write(f"**Phonetic Breakdown:** {' '.join(phonemes)}")

                audio_path = generate_tts_audio(" ".join(phonemes), f"{word}_phonetic.mp3")
                st.audio(audio_path)

            elif option == "Letter by Letter Pronunciation":
                for letter in word:
                    if st.button(f"Play {letter.upper()}"):
                        audio_path = generate_tts_audio(letter, f"{letter}.mp3")
                        st.audio(audio_path)

elif menu == "Image to Text":
    # Image to text page
    st.markdown('<h1 class="title">Image to Text Converter</h1>', unsafe_allow_html=True)

    # File uploader for image
    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
    
    if uploaded_image is not None:
        # Open the uploaded image using PIL
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extract text from the image using pytesseract
        extracted_text = pytesseract.image_to_string(image)

        if extracted_text:
            st.subheader("Extracted Text:")
            st.write(extracted_text)
        else:
            st.write("No text could be extracted from this image.")
