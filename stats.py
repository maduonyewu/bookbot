def get_word_count(text):
    count = len(text.split())
    return count

def get_character_count(text):
    count = {}
    for c in text:
        c = c.lower()
        if c not in count:
            count[c] = 0
        count[c] += 1
    return count

def sort_dict(dictionary):
    sorted_dict = sorted(dictionary.items(), reverse=True, key=lambda item: item[1])
    return dict(sorted_dict)
