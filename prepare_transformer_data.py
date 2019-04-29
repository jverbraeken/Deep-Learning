import json

escape_dict={'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
           '\t':r'\t',
           '\v':r'\v',
           '\'':r'\'',
           '\"':r'\"',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}

def raw(text):
    """Returns a raw string representation of text"""
    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    return new_string

with open('data/train.json', encoding='utf-8') as fh:
    train = json.load(fh)

with open('data/test.json', encoding='utf-8') as fh:
    test = json.load(fh)

with open('data/valid.json', encoding='utf-8') as fh:
    valid = json.load(fh)

with open('transformer_data/train/train.cd', 'w+') as fw:
    for item in train:
        fw.write(raw(item['code']) + '\n') 

with open('transformer_data/train/train.en', 'w+') as fw:
    for item in train:
        fw.write(raw(item['nl']) + '\n')

with open('transformer_data/test/test.cd', 'w+') as fw:
    for item in test:
        fw.write(raw(item['code']) + '\n') 

with open('transformer_data/test/test.en', 'w+') as fw:
    for item in test:
        fw.write(raw(item['nl']) + '\n')

with open('transformer_data/valid/valid.cd', 'w+') as fw:
    for item in valid:
        fw.write(raw(item['code']) + '\n') 

with open('transformer_data/valid/valid.en', 'w+') as fw:
    for item in valid:
        fw.write(raw(item['nl']) + '\n')
