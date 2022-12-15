import sys
import re
import pandas as pd
lines = sys.stdin.readline()
abbr = ['etc.', 'e.g.', 'i.e.']
def tokeniser(line, abbr):
    line = re.sub(r'([\(\)”?:!;])', r' \g<1> ', line)
    line = re.sub(r'([^0-9]),', r'\g<1> ,', line)
    line = re.sub(r',([^0-9])', r', \g<1>', line)
    line = re.sub(r'([0-9]), ', r'\g<1> ,', line)
    line = re.sub(r'  +', ' ', line)
    output = []
    for token in line.split(' '):
        if token == '':
            continue
        if token[-1] == '.' and token not in abbr:
            token = token[:-1] + ' .'
        output.append(token)
    return output
def PrintTokenizer(i, line, abbr):
    form = tokeniser(line, abbr)
    df = pd.DataFrame({'Form' : form})
    df['LEMMA'] = '-'
    df['UPOS'] = '-'
    df['XPOS'] = '-'
    df['FEATS'] = '-'
    df['HEAD'] = '-'
    df['DEPREL'] = '-'
    df['DEPS'] = '-'
    df['MISC'] = '-'
    print('# sent_id = ', i)
    print('# text = ', line)
    print(df)    
i = 1
while lines:
    lines = PrintTokenizer(i, lines, abbr)
    i += 1
    sys.stdout.write(lines)
    lines = sys.stdin.readline()

 
