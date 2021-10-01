ASCII_ALPHABET_LEN = 128


def is_unique_characters_bool_arr(s: str) -> bool:
    # assume 128-character (ASCII) alphabet
    if len(s) > ASCII_ALPHABET_LEN:
        return False
    found_chars = [False for _ in range(ASCII_ALPHABET_LEN)]
    for char in s:
        if found_chars[ord(char)]:
            return False  # already found
        found_chars[ord(char)] = True
    return True


def is_unique_characters(s: str) -> bool:
    # use a bitvector; assumes a->z
    bitvector: int = 0
    for char in s:
        val: int = ord(char) - ord('a')
        if bitvector & (1 << val) > 0:
            return False
        bitvector |= 1 << val
    return True


if __name__ == '__main__':
    print('is_unique_characters_bool_arr(balance):',
          is_unique_characters_bool_arr('balance'))
    print('is_unique_characters_bool_arr(red):',
          is_unique_characters_bool_arr('red'))
    print('is_unique_characters_bool_arr():',
          is_unique_characters_bool_arr(''))
    print('is_unique_characters(balance):', is_unique_characters('balance'))
    print('is_unique_characters(magic):', is_unique_characters('magic'))
