class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for i,j in points:
            dis = math.sqrt((i**2)+(j**2))
            pts.append([dis,[i,j]])
        
        heap = []
        res = []

        for i, j in pts:
            heappush(heap,[i,j])
        
        while k:
            a = heappop(heap)
            res.append(a[1])
            k -= 1
        return res
