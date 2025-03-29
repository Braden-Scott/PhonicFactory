import pronouncing
import syllapy
from gtts import gTTS
import os

def get_phonetic_breakdown(word):
    """Get a cleaned phonetic breakdown of the word."""
    phonemes = pronouncing.phones_for_word(word)
    if phonemes:
        cleaned_phonemes = ''.join([c for c in phonemes[0] if not c.isdigit()])
        return cleaned_phonemes.split()
    return ["No phonetic breakdown found"]

def get_syllables(word):
    """Get syllable-based breakdown of the word."""
    return ["-".join([word])] * syllapy.count(word)  # ✅ Correct


def generate_tts_audio(text, filename):
    """Generate speech audio for a given text and save as MP3."""
    tts = gTTS(text=text, lang="en")
    audio_path = os.path.join("audio", filename)
    os.makedirs("audio", exist_ok=True)
    tts.save(audio_path)
    return audio_path
