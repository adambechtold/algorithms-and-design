"""
String Encode and Decode

link: https://neetcode.io/problems/string-encode-and-decode
whiteboard: none
author: adambechtold
date: 2024-09-22
"""

DELIMETER = "#"


class Solution:

    def encode(self, strs: List[str]) -> str:
        s_encoded = ""
        for s in strs:
            s_encoded += self.encode_single_word(s)

        return s_encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        offset = 0

        while offset < len(s):
            next_word = self.get_next_word(s[offset:])
            offset = offset + len(self.encode_single_word(next_word))
            strs.append(next_word)

        return strs

    def encode_single_word(self, s: str) -> str:
        num_chars = len(s)
        return str(num_chars) + DELIMETER + s

    def get_next_word(self, s_encoded: str) -> str:
        if len(s_encoded) < 3:
            raise ValueError(
                s_encoded + " is not valid. Encoded strings are at least 3 chars long."
            )

        split_by_delimeter = s_encoded.split(DELIMETER)
        next_word_with_tailing_encoded_num = split_by_delimeter[1]

        try:
            num_chars = int(split_by_delimeter[0])
        except ValueError:
            raise ValueError("First char is not a number")

        next_word = next_word_with_tailing_encoded_num[0:num_chars]

        return next_word
