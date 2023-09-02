import sys
import re

s = sys.stdin.readline()
x = re.findall("<main>(.*)</main>", s)
for d in re.findall("(<div title=.*?</div>)", x[0]):
    print("title :", re.findall("title=\"(.*)\">", d)[0])
    for p in re.findall("<p>(.*?)</p>", d):
        p = re.sub("<[\w\s/]*>","", p).lstrip().rstrip()
        p = re.sub("[\s]+", " ", p)
        print(p)
        
    