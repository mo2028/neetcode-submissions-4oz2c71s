class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        containsPerm = False

        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_count = Counter(s1)
        window_count = Counter()

        for i in range(len_s2):
            # Add one more letter on the right side of the window
            window_count[s2[i]] += 1

            # Remove one letter from the left side of the window if the window is larger than s1
            if i >= len_s1:
                if window_count[s2[i - len_s1]] == 1:
                    del window_count[s2[i - len_s1]]
                else:
                    window_count[s2[i - len_s1]] -= 1

            # Compare window with s1
            if s1_count == window_count:
                return True

        return False


