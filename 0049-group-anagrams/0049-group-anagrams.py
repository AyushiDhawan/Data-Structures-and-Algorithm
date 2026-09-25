class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        count = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in count:
                count[key] = []
            count[key].append(word)
        return list(count.values())

        