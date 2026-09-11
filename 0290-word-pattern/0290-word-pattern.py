class Solution(object):
    def wordPattern(self, pat, s):
        m = {}
        j = 0
        for i in range(len(pat)):
            val = ""
            while j < len(s) and s[j] != ' ':
                val += s[j]
                j += 1
            j += 1
            if pat[i] not in m:
                if val in m.values():
                    return False
                m[pat[i]] = val
            else:
                if m[pat[i]] != val:
                    return False
        if j <= len(s):
            remaining = s[j:]
            if remaining.strip() != "":
                return False
        words = s.split()
        if len(words) != len(pat):
            return False

        return True