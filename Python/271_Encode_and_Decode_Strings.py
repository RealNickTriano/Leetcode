"""
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network
and is decoded back to the original list of strings.

Please implement encode and decode

Example 1:

    Input: ["lint", "code", "love", "you"]
    Output: ["lint", "code", "love", "you"]
    Explanation:
    One possible encode method is: "lint:;code:;love:;you"

Example 2:
    Input: ["we", "say", ":", "yes"]
    Output: ["we", "say", ":", "yes"]
    Explanation:
    One possible encode method is: "we:;say:;:::;yes"
"""
from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # for each string in strs concat the string + ":"
        # if the string is a : then add : before
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "$" + s
        return encoded_string

    def decode(self, string: str) -> List[str]:
        decoded_value = []
        i = 0
        while i < len(string):
            j = i
            while string[j] != "$":
                j += 1
            length = int(string[i:j])
            word_start = j + 1
            decoded_value.append(string[word_start:word_start + length])
            i = word_start + length

        return decoded_value


sol = Solution()
print(sol.encode(["weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "sayaaaaaaaaaaaa", ":", "yes"]))
print(sol.decode(sol.encode(["weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "sayaaaaaaaaaaaa", ":", "yes"])))
