class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # === edge case ===
        if len(s1) > len(s2):
            return False
        # =================

        # step 1: count alphabet เฉพาะ len(s1) ตัวแรก
        alphabet_idx_s1 = [0] * 26
        alphabet_idx_s2 = [0] * 26
        for i in range(len(s1)):
            alphabet_idx_s1[ord(s1[i]) - ord("a")] += 1
            alphabet_idx_s2[ord(s2[i]) - ord("a")] += 1
        # ถ้าเท่ากันก็คือเจอ anagram/permutation ละ ก็คือ True เลย
        if alphabet_idx_s1 == alphabet_idx_s2:
            return True

        # step 2: ไล่ check ทีละ len(s1) ไปเรื่อยๆ
        for i in range(len(s1), len(s2)):
            alphabet_idx_s2[ord(s2[i]) - ord("a")] += 1
            # shrink window
            alphabet_idx_s2[ord(s2[i - len(s1)]) - ord("a")] -= 1
            # ถ้าเจอ anagram/permutation ก็ True
            if alphabet_idx_s1 == alphabet_idx_s2:
                return True
        
        return False
