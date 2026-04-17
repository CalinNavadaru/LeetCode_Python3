class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        is_first_letter_capital = word.isupper()
        capital_letters = sum(word[i].isupper() for i in range(1, len(word)))

        return (is_first_letter_capital and not capital_letters) or (
                    not is_first_letter_capital and not capital_letters) or \
            (is_first_letter_capital and capital_letters == len(word) - 1)
