import sys
import re
line1 = sys.stdin.readline()
def segmenter_new(line):
    line = re.sub(r'(\. )', r'\g<1>\n', line)
    return line
while line1:
    line1 = segmenter_new(line1)
    sys.stdout.write(line1)
    line1 = sys.stdin.readline()
