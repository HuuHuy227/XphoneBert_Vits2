from text import vietnamese, cleaned_text_to_sequence

def clean_text(text):
    norm_text = vietnamese.text_normalize(text) 
    phones, tones = vietnamese.g2p(norm_text)
    return phones, tones

def text_to_sequence(text):
    phones, tones = clean_text(text)
    return cleaned_text_to_sequence(phones, tones)

if __name__ == "__main__":
    pass
