def highest_palindrome(s, k):
    def helper(s_list, left, right, k):
        if left >= right:
            return ''.join(s_list) if k >= 0 else '-1'

        if s_list[left] == s_list[right]:
            return helper(s_list, left + 1, right - 1, k)

        if k > 0:
            higher = max(s_list[left], s_list[right])
            s_list[left] = s_list[right] = higher
            return helper(s_list, left + 1, right - 1, k - 1)
        else:
            return '-1'

    def maximize(s_list, left, right, k):
        if left >= right:
            return ''.join(s_list)

        if s_list[left] == s_list[right]:
            if k > 0 and s_list[left] != '9':
                s_list[left] = s_list[right] = '9'
                return maximize(s_list, left + 1, right - 1, k - 2)
            return maximize(s_list, left + 1, right - 1, k)

        if k > 0:
            s_list[left] = s_list[right] = '9'
            return maximize(s_list, left + 1, right - 1, k - 1)

        return ''.join(s_list)

    s_list = list(s)

    result = helper(s_list, 0, len(s_list) - 1, k)
    if result == '-1':
        return '-1'

    return maximize(list(result), 0, len(result) - 1, k)

s = input("Masukkan string angka: ")
k = int(input("Masukkan jumlah perubahan maksimal: "))

print(highest_palindrome(s, k))
