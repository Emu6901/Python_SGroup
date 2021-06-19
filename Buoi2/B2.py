n = int(input())
d = {}
while n:
    n -= 1
    s = input()
    name, subject = "".join(s.split()[:-1]), s.split()[-1]
    if name not in d:
        d[name] = set()
    d[name].add(subject)
for name,subject in d.items():
    print(name,subject)