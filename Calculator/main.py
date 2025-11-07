from tokenizer import Token

tok = Token()

tokens = []

while tok.kind != 'q':
    token = tok.get_token()
    tokens.append(tok)

