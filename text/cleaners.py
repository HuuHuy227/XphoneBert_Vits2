from vinorm import TTSnorm
import py_vncorenlp
import os

path = os.path.join(os.getcwd(),"py_vncorenlp") #Get current path
rdrsegmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir=path)

def clean_text(text):
    norm_text = TTSnorm(text).strip() 
    seg_text = rdrsegmenter.word_segment(norm_text) 
    return seg_text

if __name__ == "__main__":
    pass
