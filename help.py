import bisect
from collections import defaultdict

# Reverse
a = [1,2,3,4]
a.reverse()

# Sorting
a = [[1,20], [4,12], [2,41], [2,40]]
a.sort(key=lambda x: x[1], reverse=True)

# Sort based on first value, if same then sort based on second value in descending order
b = sorted(a, key=lambda x: (x[0], -x[1]))

# List comprehension
a = [1,2,3,4]
a = [x for x in a if x%2 == 0] # [2,4]
a = [1 if x%2 == 0 else 0 for x in a] # [0, 1, 0, 1]

# Enumerate
a = [30,40,10,20]
pairs = list(enumerate(a,start=0))

# defaultdict
d = defaultdict(int) # default value is 0
d = defaultdict(lambda: -1) # default value is -1

# bisect_left, bisect_right
a = [1, 2, 2, 3, 4, 4, 4, 5, 6]
index = bisect.bisect_left(a, 4) # returns index 4
index = bisect.bisect_right(a, 4) # returns index 7

a = [[1,2],[1,3],[1,4],[2,3]]
index = bisect.bisect_left(a, 1, key=lambda x: x[0])
print(index)

