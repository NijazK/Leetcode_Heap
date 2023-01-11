class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        if n == 0:
            return len(tasks)

        dic = Counter(tasks)

        max_values = max(dic.values())
        
        max_v_count = list(dic.values()).count(max_values)
        
        res = (max_values - 1) * (n + 1) + max_v_count
        return max(res, len(tasks))
