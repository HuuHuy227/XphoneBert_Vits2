from vinorm import TTSnorm
import py_vncorenlp
import os

path = os.path.join(os.getcwd(),"py_vncorenlp") #Get current path
rdrsegmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir=path)

def seg_sentence(text):
    "Segment a sentence"
    seg_text = rdrsegmenter.word_segment(text) 
    return seg_text[0]

def seg_sentences(text):
    "Segment sentences"
    seg_text = rdrsegmenter.word_segment(text) 
    return seg_text

def clean_text(text):
    norm_text = TTSnorm(text).strip() 
    seg_text = seg_sentence(norm_text) 
    return seg_text

if __name__ == "__main__":
    pass
