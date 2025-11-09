letter = '''Dear <|NAME|>,
You are selected!
<|DATE|> '''
print(letter.replace("<|NAME|>", "Harry").replace("<|DATE|>", "24 September 2050"))