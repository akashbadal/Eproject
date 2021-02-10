import datetime
alphabets = [str(x) for x in range(100000)]
a = datetime.datetime.now()

for item in alphabets:
    len(item)

b = datetime.datetime.now()

print((b-a).total_seconds())

a = datetime.datetime.now()

fn = len
for item in alphabets:
    fn(item)

b = datetime.datetime.now()
print((b-a).total_seconds())
