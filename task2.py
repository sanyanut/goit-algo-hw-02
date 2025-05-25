import collections


def is_palindrome(str):
    # all strings to lowercase including numeric values
    new_str = "".join(char for char in str if char.isalnum()).lower()

    char_deque = collections.deque()
    for char in new_str:
        char_deque.append(char)

    while len(char_deque) > 1:
        first = char_deque.popleft()
        last = char_deque.pop()

        if first != last:
            return False

    return True


# prints for testing
print(f"{is_palindrome('Joji')}")
print(f"{is_palindrome('Johnynhoj')}")
print(f"{is_palindrome('7elevenevele7')}")
