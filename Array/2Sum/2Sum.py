class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        myMap = {}
        for n in range(len(num)):
            myMap[num[n]] = n
        for n in range(len(num)):
            tmp = target - num[n]
            if myMap.has_key(tmp) and n != myMap[tmp]:
                return (n + 1, myMap[tmp] + 1)
            
