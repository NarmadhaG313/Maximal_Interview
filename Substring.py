from collections import defaultdict
import sys
string=input()
count= len(set(list(string)))
n = len(string)
dist = defaultdict(int)
first = 0
sl = sys.maxsize
dist_ch = 0 
for j in range(n):
    dist[string[j]] += 1
    if dist[string[j]] == 1:
        dist_ch += 1
        
    if count == dist_ch:
        while dist[string[first]] > 1:
            if dist[string[first]] > 1:
              dist[string[first]] -= 1
            first += 1
          
        cl = j - first + 1
        sl = min(sl, cl)
print (sl)
