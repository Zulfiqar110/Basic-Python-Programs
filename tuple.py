name = input("Enter file:")
if len(name) < 3 : name = "asd.txt"
handle = open(name)
dc = dict()
for lines in handle:
    if lines.startswith("From "):
        words = lines.split()
        time = words[5].split(":")
        hr = time[0]
        dc[hr] = dc.get(hr,0) + 1

for k,v in sorted(dc.items()):
    print(k,v)
