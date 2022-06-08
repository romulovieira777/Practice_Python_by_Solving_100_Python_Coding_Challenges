"""
Exercise No. 88

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map
to any letters.
    1 2 3
    4 5 6
    7 8 9
    * 0 #

Examples:
    letter_combinations("23") -> ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    letter_combinations("532") -> ['jda', 'jdb', 'jdc', 'jea', 'jeb', 'jec', 'jfa', 'jfb', 'jfc', 'kda', 'kdb', 'kdc',
                                   'kea', 'keb', 'kec', 'kfa', 'kfb', 'kfc', 'lda', 'ldb', 'ldc', 'lea', 'leb', 'lec',
                                   'lfa', 'lfb', 'lfc']

"""


def letter_combinations(digits):
    dic = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    ans = ['']
    for d in digits:
        ans = [a + e for a in ans for e in dic[int(d)]]
    return ans


print(letter_combinations("532"))
