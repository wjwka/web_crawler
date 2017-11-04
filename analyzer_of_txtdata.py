import matplotlib.pyplot as plt
import collections
from operator import itemgetter


with open("grades.txt", 'r') as f:
    raw = f.read()
raw = str(raw)
# print raw
raw = raw.split('\n')
grade = []
for item in raw:
    grade.append(item.split(' ')[-1])
grade = sorted(grade)
frequency = collections.Counter(grade)
sorted(frequency.items(), key=itemgetter(0))
print frequency
x_axis = frequency.keys()
y_axis = frequency.values()
print x_axis
print y_axis
# for item in frequency.keys():
#     x_axis.append(item)
#     y_axis.append(frequency.items)
# print x_axis
# print y_axis
min_grade = min(grade)
max_grade = max(grade)
