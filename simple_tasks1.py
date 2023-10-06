# 1. Print all elements less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print([elem for elem in a if elem < 5])


# 2. We need to return a list that consists of elements common to these two lists.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(filter(lambda elem: elem in a, b)))


# 3. Sort dict by value
mDict = {"Bereza": 10, "Alice": 4, "China": 17, "Hurricane": 20}
print(sorted(mDict.items(), key=lambda items: items[1], reverse=True))


# 4. Write a program to merge several dictionaries into one
mDict1 = {"Race": 100, "Shooter": 50, "Arcade": 15}
mDict2 = {"Action": 67, "Sandbox": 104}
mDict1.update(mDict2)

print(mDict1)


# 5. Find the 3 keys with the highest values in the dictionary
mDict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f':20}

mDictCopy = mDict.copy()
maxKey1 = max(mDictCopy.items(), key=lambda pair: pair[1])[0]
mDictCopy.pop(maxKey1)
maxKey2 = max(mDictCopy.items(), key=lambda pair: pair[1])[0]
mDictCopy.pop(maxKey2)
maxKey3 = max(mDictCopy.items(), key=lambda pair: pair[1])[0]

print(maxKey1, maxKey2, maxKey3)

# OR
result = sorted(mDict, key=mDict.get, reverse=True)[:3]


# 6. Pascal's triangle
def pascal_triangle(n=5):
    prev_row = []
    row = []

    for i in range(n):
        for j in range(1, len(row)):
            row[j] = prev_row[j - 1] + prev_row[j]

        row.append(1)
        prev_row = row.copy()
        print(row)

pascal_triangle(10)

# OR
def pascal_triangle2(n):
    row = [1]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + [0], [0] + row)]

# row = [1, 1, 0] + [0, 1, 1] = [1, 2, 1]
# row = [1, 2, 1, 0] + [0, 1, 2, 1] = [1, 3, 3, 1]

pascal_triangle2(6)


# 7. Check if a string is a palindrome
str1 = "aboba"
str2 = "abobba"

def is_palindrome(m_str = ""):
    left = list(m_str[:int(len(m_str) / 2)])
    right = list(reversed(m_str[int(len(m_str) / 2) + 1:]))

    return left == right

print(is_palindrome(str1))
print(is_palindrome(str2))

# OR
def is_palindrome2(string):
    return string == string[::-1]

# 8. Given an integer n, calculate n + nn + nnn
n = 108
print (n + int(str(n) * 2) + int(str(n) * 3))