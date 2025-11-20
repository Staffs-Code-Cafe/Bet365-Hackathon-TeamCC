from wordfreq import zipf_frequency

def is_english_word(word: str, threshold: float = 2) -> bool:
    """
    Returns True if 'word' is a real English word (or English-like),
    otherwise returns False.

    threshold:
        1.5 = lenient (allows rare/obscure words)
        2.5 = good default
        3.0 = strict (common words only)
    """
    word = word.lower().strip()

    # Wordfreq Zipf frequency score
    freq = zipf_frequency(word, "en")

    return freq >= threshold


print(is_english_word("microservices"))    # True
print(is_english_word("eht"))    # False
print(is_english_word("florp"))    # True (looks English)
print(is_english_word("asdjlk"))   # False
