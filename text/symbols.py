""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.
"""

# Not using 
_pad = "_"
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = "nhtcgiuamđàovưrlábykpsôạếdóảêệấờộớốâìềểợơủqxịậầữíựúăắeứọụãởồặùòừổũỏửẽỉéẹẩýẫằẻễỗĩỡỹèẳõỳỷẵỵ"
_letters_ipa = "atːəɜ26ni̪ŋhɪy4omɲɗɡɔkɛuzʊvel5bɕʂʃwxfpsjcɣ1()æɹdɒɑʌʒ7ðɐʐ"

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# Special symbol ids
SPACE_ID = symbols.index(" ")
