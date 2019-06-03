import random
import os
import sys

if len(sys.argv) < 2:
    print('Usage: python GenerateSmallSample [n]')
else:
    # Sample N lines
    N = int(sys.argv[1])

    # Filter out long lines
    lines = set()

    with open('valid.cd', 'r') as f:
        with open('filtered.cd', 'w') as w:
            curLine = 0
            for line in f:
                if len(line) <= 1024:
                    w.write(line)
                    lines.add(curLine)
                curLine += 1
            
    with open('valid.en', 'r') as f:
        with open('filtered.en', 'w') as w:
            curLine = 0
            for line in f:
                if curLine in lines:
                    w.write(line)
                curLine += 1


    if N > len(lines):
        print("N was too large, setting to all lines:", len(lines))
        N = len(lines)
        
    randLines = random.sample(range(0,len(lines)), N)

    with open('filtered.cd', 'r') as cd:
        with open('filtered.en', 'r') as en:
            with open('sampled.cd', 'w') as cdout:
                with open('sampled.en', 'w') as enout:
                    curLine = 0
                    for line in cd:
                        if curLine in randLines:
                            cdout.write(line)
                        curLine += 1
                    curLine = 0
                    for line in en:
                        if curLine in randLines:
                            enout.write(line)
                        curLine += 1
    
    os.remove('filtered.cd')
    os.remove('filtered.en')

    print('Generated sample of', N, 'lines!')