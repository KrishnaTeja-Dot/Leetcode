class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap ={}
        for i in range(len(numbers)):
            k = target - numbers[i]
            if k in hashmap:
                return [hashmap[k], i+1]
            hashmap[numbers[i]] = i+1