class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        hash = Counter(arr1)
        res = []

        for n in arr2:
            if hash[n]:
                for _ in range(hash[n]):
                    res.append(n)
                hash[n] = 0

        for key, val in hash.items():
            if val:
                for _ in range(val):
                    res.append(key)

        return res
