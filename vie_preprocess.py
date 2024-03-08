import argparse
from tqdm import tqdm
import os
from vinorm import TTSnorm
import py_vncorenlp

path = os.path.join(os.getcwd(),"py_vncorenlp") # Get current path. Pycorenlp requires absolute path.
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
    norm_text = TTSnorm(text, punc=False, unknown=True, rule=False).strip() # Normalize before segmenting word
    seg_text = seg_sentence(norm_text) 
    return seg_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_extension", default="cleaned")
    parser.add_argument("--audio_path", type=str)
    parser.add_argument(
        "--filelists",
        nargs="+",
        default=[
            "filelists/train.txt",
            "filelists/val.txt",
        ],
    )

    args = parser.parse_args()
    
    for filelist in args.filelists:
        print("START:", filelist)
        
        print("-----------Normalizing Text And Segmented On Raw Text-------------")
        with open(filelist + "." + args.out_extension, "w", encoding="utf-8") as out_file:
                with open(filelist, "r", encoding="utf-8") as trans_file:
                    lines = trans_file.readlines()
                    if len(lines) != 0:
                        for line in tqdm(lines):
                            try: 
                                utt, text = line.strip().split("|")
                                norm_seg_text = clean_text(text)
                                out_file.write(
                                    "{}|{}\n".format(
                                        utt,
                                        norm_seg_text
                                    )
                                )
                            except Exception as e:
                                print(line)
                                print(f"Error while preprocess data:\n{e}")

        if args.audio_path is not None:
            #Check Audio Files is exists
            with open(filelist, "r", encoding="utf-8") as f:
                audioPaths = set()
                countSame = 0
                countNotFound = 0
                for line in f.readlines():
                    utt, phones = line.strip().split("|")
                    if utt in audioPaths:
                        print(f"Duplicate：{line}")
                        countSame += 1
                        continue
                    if not os.path.isfile(os.path.join(args.audio_path,utt)):
                        print(f"Not found audio respectively：{utt}")
                        countNotFound += 1
                        continue
                    audioPaths.add(utt)
                print(f"Total duplicate audio：{countSame}，Total not found audio:{countNotFound}")
        
    print("Done！")
