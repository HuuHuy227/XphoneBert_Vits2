from text.symbols import *

_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}

def cleaned_text_to_sequence(cleaned_text, tones):
    """Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
    """
    # phones = [_symbol_to_id[symbol] for symbol in cleaned_text]
    sequence = []
    for symbol in cleaned_text:
        if symbol in _symbol_to_id.keys():
            symbol_id = _symbol_to_id[symbol]
            sequence += [symbol_id]
        else:
            continue
    return sequence, tones

def sequence_to_text(sequence):
    """Converts a sequence of IDs back to a string"""
    result = ""
    for symbol_id in sequence:
        s = _id_to_symbol[symbol_id]
        result += s
    return result
