class Solution:

    def encode(self, strs: List[str]) -> str:
        sbuilder = ""
        for s in strs:
            sbuilder += str(len(s))
            sbuilder += "#"
            sbuilder += s
        return sbuilder

    def decode(self, s: str) -> List[str]:
        print("Received: " + s)
        l = []
        i = 0
        while i < len(s):
            s_length, word_start_index = self._get_length(s, i)
            l.append("".join(s[word_start_index:(word_start_index+s_length)]))
            i = word_start_index + s_length
        return l
    
    def _get_length(self, s: str, index:int) -> tuple[int, int]:
        i = index
        while s[i] != "#":
            i += 1
        return int(s[index:i]), i + 1