trainset = set()

with open('sampled.cd', 'r') as c:
    with open('sampled.en', 'r') as e:
        with open('sampled_model.en', 'r') as em:
            with open('human_readable.md', 'w') as md:
                code = c.readlines()
                comments = e.readlines()
                outputs = em.readlines()
                for x in range(0, len(code)):
                    md.write('id', x, '\n')
                    md.write('Code snippet:\n```\n')
                    codestring = ""
                    for line in code[x].split(r'\n'):
                        codestring += line
                        codestring += '\n'
                    md.write(codestring.strip())
                    md.write('\n```\n')
                    #md.write('Original comment:\n```\n')
                    #md.write(comments[x].strip())
                    #md.write('\n```\n')
                    md.write('Generated comment:\n```\n')
                    md.write(outputs[x].strip())
                    md.write('\n```')
                    md.write('\n---\n')