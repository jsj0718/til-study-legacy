# python tabto4.py a.txt b.txt

import sys

input = sys.argv[1]
output = sys.argv[2]

f = open(input)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " " * 4)

f = open(output, "w")
f.write(space_content)
f.close()

print(input)
print(output)
