from collections import defaultdict
import io
import os
import re

attendance = defaultdict(lambda: [])

files = ['reports/' + f for f in os.listdir('reports') if re.match(r'SessionDetailReport[0-9]+\.csv', f)]

for file in files:
    with io.open(file, encoding="utf-16") as f:
        data = f.readlines()
        visited = defaultdict(lambda: 0)

        for i in range(3, len(data)):
            line = [str(info) for info in data[i].split('\t')]

            name = line[1].title()
            visited[name] += 1
            if visited[name] <= 1:
                attendance[name].append(line[3])
            else:
                print('%s was found %d times in the file %s' % (name, visited[name], file))


print('\n%d unique names attended.\n' % len(attendance))
for name, dates in attendance.iteritems():
    print('%s attended %d times. %s' % (name, len(dates), ', '.join(dates)))
