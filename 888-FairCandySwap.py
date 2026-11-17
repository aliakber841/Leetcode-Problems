class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA=0
        for i in range(len(aliceSizes)):
            sumA+=aliceSizes[i]
        sumB=0
        for i in range(len(bobSizes)):
            sumB+=bobSizes[i]

        diff=(sumB-sumA)//2
        hash_set=set(bobSizes)
        for a in aliceSizes:
            b=a+diff
            if b in hash_set:
                return [a,b]