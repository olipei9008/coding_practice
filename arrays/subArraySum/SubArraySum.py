## Given: an array of numbers and a specified value target
## Return: 1-based index of leftmost and rightmost elements
## of the first subarray (left to right) whose elements sum to up to the target
## OR return -1 if no such subarray exists

class SubArraySum:
    def __init__(self, numArray, target):
        self.numArray = numArray
        self.target = target

    ## Brute force way of finding a subarray sum
    ## O(n^2) time and O(1) space
    def find_subarray_bruteforce(self):
        for index1 in range(len(self.numArray)):
            for index2 in range(len(self.numArray)):
                if index1 == index2:
                    pass
                else:
                    currentsum = sum(self.numArray[index1:index2+1])
                    if currentsum == self.target:
                        return [index1+1, index2+1]
        return [-1]

    ## Sliding window method
    ## O(n) time and O(1) space
    def find_subarray_sliding_window(self):
        index1 = 0
        index2 = 1

        while index1 < index2 < len(self.numArray):
            currentsum = sum(self.numArray[index1:index2])
            if currentsum == self.target:
                return [index1+1, index2]
            elif currentsum < self.target:
                index2 += 1
            else:
                index1 += 1
                index2 = index1 + 1

        return [-1]
