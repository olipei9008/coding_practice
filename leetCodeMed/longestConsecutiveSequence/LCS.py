class LCS:

    def __init__(self, nums):
        self.nums = nums

    # Not optimal, but gets the job done
    def find_len_lcs(self):
        if self.nums:

            # Keep track of current count and longest count
            current_len = 0
            len_lcs = 0
            sorted_nums = sorted(self.nums)

            # Create iterator for traversing through nums list
            it = iter(sorted_nums)
            prev = next(it) # Store the first number in previous number
            current_len += 1
            for num in sorted_nums:
                if len_lcs < current_len:
                    len_lcs = current_len
                if num == prev:
                    continue
                elif num == prev + 1:
                    current_len += 1
                    if len_lcs < current_len:
                        len_lcs = current_len
                    prev = num
                else:
                    current_len = 1
                    prev = num
            return len_lcs

        else:
            return 0

    # Uses hashing to make the code run faster
    def find_len_lcs_optimal(self):
        st = set()
        res = 0

        # Hash all the array elements
        for val in self.nums:
            st.add(val)

        # Check each possible sequence from the start
        # then update length
        for val in self.nums:

            # If current element is the starting element of a sequence
            if val in st and (val - 1) not in st:

                # Then check for next elements in the sequence
                cur = val
                cnt = 0
                while cur in st:
                    # Remove this number to avoid recomputation
                    st.remove(cur)
                    cur += 1
                    cnt += 1

                # Update optimal length
                res = max(res, cnt)

        return res