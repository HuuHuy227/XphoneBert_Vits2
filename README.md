# VITS2 extended with XPhoneBERT encoder

## Credits
- This repo based on the great work of [VITS2 repo](https://github.com/p0p4k/vits2_pytorch) and [XPhoneBERT](https://github.com/VinAIResearch/XPhoneBERT).

## Prerequisites
1. Python >= 3.10
2. Tested on Pytorch version 1.13.1 with Google Colab and LambdaLabs cloud.
3. Clone this repository
4. Install python requirements. Please refer [requirements.txt](requirements.txt)
5. Download datasets
    1. Download and extract the LJ Speech dataset, then rename or create a link to the dataset folder: `ln -s /path/to/LJSpeech-1.1/wavs DUMMY`
    2. Note: This repo do not supported training multi-speaker dataset
6. Move/copy your .txt training, validation and test files to the filelists directory, and then run the preprocess.py file (similar to as run for the LJSpeech dataset), for example:
   - Please refer to [XPhoneBERT](https://github.com/VinAIResearch/XPhoneBERT) for more information. They using `text2phonemesequence` for converting raw text to phoneme sequence.
	-	Initializing `text2phonemesequence` for each language requires its corresponding ISO 639-3 code. The ISO 639-3 codes of supported languages are available at [HERE](https://github.com/VinAIResearch/XPhoneBERT/blob/main/LanguageISO639-3Codes.md).
	
	- `text2phonemesequence` takes a word-segmented sequence as input. And users might also perform text normalization on the word-segmented sequence before feeding into `text2phonemesequence`.
 - **Note:** For languages such as Chinese, Korean, Japanese (CJK languages) and some southeast Asian languages, words are not separated by spaces. An external tokenizers must be used before feeding words into this model.
   In this case, write a script to normalize and segment your input before feeding to  `text2phonemesequence` (vie_preprocess.py is in my case)

   ```sh
    # In Case languages, words are not separated by spaces such as Vietnamese.
   python vie_preprocess.py --out_extension cleaned --filelists filelists/train.txt filelists/val.txt
   python preprocess.py --input_file filelists/train.txt.cleaned --output_file filelists/train.list --language vie-n --batch_size 64 --cuda
   python preprocess.py --input_file filelists/val.txt.cleaned --output_file filelists/val.list --language vie-n --batch_size 64 --cuda

   # In Case languages English.
   python preprocess.py --input_file filelists/train.txt.cleaned --output_file filelists/train.list --language eng-us --batch_size 64 --cuda
   python preprocess.py --input_file filelists/val.txt.cleaned --output_file filelists/val.list --language eng-us --batch_size 64 --cuda
    ```
7. Build Monotonic Alignment Search and run preprocessing if you use your own datasets.

```sh
# Cython-version Monotonoic Alignment Search
cd monotonic_align
python setup.py build_ext --inplace
```

## Training Example
More info about config refer to `configs/config.json`
```sh
# LJ Speech
python train.py -c configs/config.json -m ljs_base 

```
