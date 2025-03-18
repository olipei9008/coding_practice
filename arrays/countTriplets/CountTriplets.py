class CountTriplets:

    def __init__(self, numArray):
        self.numArray = numArray

    ## Really simple solution using basically 3 nested loops
    ## O(n^3) time, O(1) space
    def count_triplets_nohash(self):
        count = 0
        for i in range(len(self.numArray)):
            for j in range(i, len(self.numArray)):
                if i == j:
                    pass
                else:
                    sum = self.numArray[i] + self.numArray[j]
                    if sum in self.numArray:
                        count += 1
        return count