class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        new_arr = [0] * 26

        for i in range(len(s)):
            new_arr[ord(s[i]) - ord("a")] += 1

            new_arr[ord(t[i]) - ord("a")] -= 1

        for num in new_arr:
            if num != 0:
                return False 
        
        return True 