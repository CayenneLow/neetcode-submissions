class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Keep iterating start of window until find a character in t
        # Keep a map of character counts in the window
        # Once start of window is found, keep iterating end of window until either end of string or all characters in t is found
        # Loop start:
        # If right window is at end of string and not all characters in t is found, exit early
        # keep track of the min substring indexes to return 
        # When above condition is met, shrink the window by moving the left pointer, reducing the character count
        # When the window no longer contains all the characters in t, start expanding the right window
        #   If right window is at end of string and not all characters in t is found, exit early
        if len(s) < len(t):
            return ""
        minIndex = (0,0)
        minLength = None
        t_char_count = {}
        # O(t)
        for c in t:
            t_char_count[c] = t_char_count.get(c, 0) + 1

        t_chars_in_window = {}
        l = 0
        r = 0
        have = 0
        need = len(t_char_count.keys())
        # O(n)
        while l < len(s) and r < len(s):
            if s[r] in t_char_count:
                t_chars_in_window[s[r]] = t_chars_in_window.get(s[r], 0) + 1
                if t_chars_in_window[s[r]] == t_char_count[s[r]]:
                    have += 1

            # O(n)
            while l <= r and have == need:
                if minLength == None or (r - l + 1) < minLength:
                    minLength = r - l + 1
                    minIndex = (l, r + 1)
                if s[l] in t_chars_in_window:
                    t_chars_in_window[s[l]] -= 1
                    if t_chars_in_window[s[l]] == (t_char_count[s[l]] - 1):
                        have -= 1
                l += 1
            r += 1
        # Time complexity: O(n * t)
        # Space complexity: O(t)
        return s[minIndex[0]:minIndex[1]]
