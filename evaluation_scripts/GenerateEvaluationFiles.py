import numpy as np

filenames = ['tim', 'jaapjan', 'chris', 'henk', 'joost']
commentsPer = 100
ranges = [x * commentsPer for x in range(1, len(filenames)+1)]

labs = np.random.choice(2, len(filenames) * commentsPer)

def writeComment(f, id, code, comment):
    f.write('id: ' + str(id) + '\n\n')
    f.write('Code snippet:\n```\n')
    codestring = ""
    for line in code.split(r'\n'):
        codestring += line
        codestring += '\n'
    f.write(codestring.strip())
    f.write('\n```\n')
    f.write('Comment:\n```\n')
    f.write(comment.strip())
    f.write('\n```')
    f.write('\n---\n')

with open('sampled.cd', 'r') as a, open('sampled.en', 'r') as b, open('sampled_model.en', 'r') as c:
    code = a.readlines()
    reference = b.readlines()
    generated = c.readlines()
    for i in range(0, len(filenames)):
        with open(filenames[i] + '.md', 'w') as out, open('labels.txt', 'a') as outlabels:
            if i == 0:
                start = 0
            else:
                start = ranges[i-1]

            for x in range(start, ranges[i]):
                if labs[x] == 0:
                    writeComment(out, x, code[x], reference[x])
                    outlabels.write(str(x) + ' original\n')
                else:
                    writeComment(out, x, code[x], generated[x])
                    outlabels.write(str(x) + ' generated\n')
    
    # Check if everything went well
    with open('labels.txt', 'r') as l:
        labels = l.readlines()

        for x in range(0, len(labels)):
            id, label = labels[x].split(' ')
            toCheck = 0 if label.strip() == 'original' else 1
            assert(labs[x] == toCheck)  

                




        
        