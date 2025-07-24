import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)  
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        
        while maxHeap or prev:
            if prev and not maxHeap: #extra char left out
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # since we store -cnt, adding 1 moves it closer to 0
            
            if prev: #push back prev value
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:  
                prev = [cnt, char]
        
        return res
