# Time complexity O(n). Space complexity O(n).
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        pattern_map = {}
        string_map = {}
        for word, cur_pattern in zip(words, pattern):
            if word in string_map and string_map[word] != cur_pattern:
                return False
            if cur_pattern in pattern_map and pattern_map[cur_pattern] != word:
                return False
            string_map[word] = cur_pattern
            pattern_map[cur_pattern] = word
        return True


# Without using split
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {}
        string_map = {}
        pattern_index = 0
        cur_word = []
        for right in range(len(s) + 1):
            if right == len(s) or s[right] == ' ':
                word = ''.join(cur_word)
                if (pattern_index == len(pattern)
                        or pattern_map.get(pattern[pattern_index], word) != word
                        or string_map.get(word, pattern[pattern_index]) != pattern[pattern_index]):
                    return False
                pattern_map[pattern[pattern_index]] = word
                string_map[word] = pattern[pattern_index]
                pattern_index += 1
                cur_word = []
            else:
                cur_word.append(s[right])
        if pattern_index == len(pattern):
            return True
        return False
