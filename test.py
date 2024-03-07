from text import _symbol_to_id, cleaned_text_to_sequence
print(_symbol_to_id)
from text.vietnamese import g2p

p, t = g2p("Xin chào, tên của tôi là Huy")
print(p)
print(t)
print(cleaned_text_to_sequence(p, t))