import argparse
from text2phonemesequence import Text2PhonemeSequence
from text.cleaners import clean_text
from tqdm import tqdm
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_extension", default="cleaned")
    parser.add_argument("--audio_path", type=str)
    parser.add_argument("--raw_text", type=bool, default=True)
    parser.add_argument("--language", default="vie-n")
    parser.add_argument("--cuda", type=bool, default=False)
    parser.add_argument("--pretrained_g2p_model", default="charsiu/g2p_multilingual_byT5_small_100")
    parser.add_argument("--tokenizer", default="google/byt5-small")
    parser.add_argument("--batch_size", default=64)

    parser.add_argument(
        "--filelists",
        nargs="+",
        default=[
            "filelists/train.txt",
            "filelists/val.txt",
        ],
    )

    args = parser.parse_args()
    
    # Load Text2PhonemeSequence
    model = Text2PhonemeSequence(pretrained_g2p_model=args.pretrained_g2p_model, tokenizer=args.tokenizer, language=args.language, is_cuda=args.cuda)
    
    for filelist in args.filelists:
        print("START:", filelist)
        
        #print("-----------Normalizing Text And Segmented On Raw Text-------------")
        with open(filelist + "." + args.out_extension, "w", encoding="utf-8") as out_file:
                with open(filelist, "r", encoding="utf-8") as trans_file:
                    lines = trans_file.readlines()
                    # print(lines, ' ', len(lines))
                    if len(lines) != 0:
                        for line in tqdm(lines):
                            try:
                                utt, text = line.strip().split("|")
                                if args.raw_text:
                                    norm_seg_text = clean_text(text)
                                    seq = model.infer_sentence(norm_seg_text)
                                else:
                                    seq = model.infer_sentence(text)
                                out_file.write(
                                    "{}|{}\n".format(
                                        utt,
                                        seq 
                                    )
                                )
                            except Exception as e:
                                print(line)
                                print(f"Error while preprocess data:\n{e}")
            # print("----------- Phonemezing On Normalized Segmented-Word -------------")
            # Processing data
        #     model.infer_dataset(input_file = filelist + "." + args.out_extension, 
        #                         output_file=filelist + "." + args.out_extension + ".phonemed", 
        #                         batch_size=args.batch_size)
            
        # else:
        #     print("----------- Phonemezing On Normalized Segmented-Word -------------")
        #     # Processing data
        #     model.infer_dataset(input_file = filelist , 
        #                         output_file=filelist  + ".phonemed", 
        #                         batch_size=args.batch_size)

        # Check Audio Files is exists
        # with open(filelist, "r", encoding="utf-8") as f:
        #     audioPaths = set()
        #     countSame = 0
        #     countNotFound = 0
        #     for line in f.readlines():
        #         utt, phones = line.strip().split("|")
        #         if utt in audioPaths:
        #             print(f"Duplicate：{line}")
        #             countSame += 1
        #             continue
        #         if not os.path.isfile(os.path.join(args.audio_path,utt)):
        #             print(f"Not found audio respectively：{utt}")
        #             countNotFound += 1
        #             continue
        #         audioPaths.add(utt)
        #     print(f"Total duplicate audio：{countSame}，Total not found audio:{countNotFound}")
        
    print("Done！")
