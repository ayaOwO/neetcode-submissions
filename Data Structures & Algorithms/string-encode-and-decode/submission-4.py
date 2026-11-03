class Solution:

    def encode(self, strs: List[str]) -> str:
        # use \ as espace char
        ans = ""
        for item in strs:
            ans += item + "ש"

        return ans

    def decode(self, s: str) -> List[str]:

        if s == "":
            return []
        return s.split("ש")[:-1]
