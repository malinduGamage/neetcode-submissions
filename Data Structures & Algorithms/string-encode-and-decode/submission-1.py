class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return "😀"
        breaking_char = "🌍"
        return breaking_char.join(strs)

    def decode(self, s: str) -> List[str]:
        if (s == "😀"):
            return []
        return s.split("🌍")
