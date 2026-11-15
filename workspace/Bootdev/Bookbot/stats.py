

def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_character_dict(text: str) -> dict[str, int]:
    character_count: dict[str, int] = {}
    for character in text:
        lowered = character.lower()
        if lowered in character_count:
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1
    return character_count


def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    chars_list:list[tuple[str, int]] = []
    for char in num_chars_dict:  # noqa: PLC0206
        count = num_chars_dict[char]
        chars_list.append((char, count))
    return sorted(chars_list, reverse=True, key=sort_on)
