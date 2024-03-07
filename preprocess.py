import argparse
from utils import load_filepaths_and_text
from text.cleaners import clean_text
from tqdm import tqdm
import os

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

    # for filelist in args.filelists:
    #     print("START:", filelist)
    #     filepaths_and_text = load_filepaths_and_text(filelist)
    #     for i in tqdm(range(len(filepaths_and_text))):
    #         original_text = filepaths_and_text[i][args.text_index]
    #         cleaned_text, tone = clean_text(original_text)
    #         filepaths_and_text[i].append(tone)
    #         filepaths_and_text[i][args.text_index] = " ".join(cleaned_text)

    #     new_filelist = filelist + "." + args.out_extension
    #     with open(new_filelist, "w", encoding="utf-8") as f:
    #         f.writelines(["|".join(x) + "\n" for x in filepaths_and_text])

    for filelist in args.filelists:
        print("START:", filelist)

        with open(filelist + "." + args.out_extension, "w", encoding="utf-8") as out_file:
            with open(filelist, "r", encoding="utf-8") as trans_file:
                lines = trans_file.readlines()
                # print(lines, ' ', len(lines))
                if len(lines) != 0:
                    for line in tqdm(lines):
                        try:
                            utt, text = line.strip().split("|")
                            phones, tones = clean_text(text)
                            out_file.write(
                                "{}|{}|{}\n".format(
                                    utt,
                                    " ".join(phones),
                                    " ".join([str(i) for i in tones])
                                )
                            )
                        except Exception as e:
                            print(line)
                            print(f"Error while preprocess data:\n{e}")

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
