from wordfreq import zipf_frequency
import requests
from wordfreq import zipf_frequency
chars = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "."
]

nonWords = [
    "ni","no","na","fo","yb","eb", "etautculf", ".ways", "nad", "nI"]

authURL = "https://dcrypt.run/auth"
fragURL = "https://dcrypt.run/fragment"
valURL = "https://dcrypt.run/validate"
para = [""] * 76


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






def get_new_token():
    """Fetch a new token, safely handling errors."""
    try:
        r = requests.post(authURL, headers={"accept": "application/json", "team": "CC"})
        data = r.json()
    except Exception as e:
        print("Auth request error:", e)
        return None

    if "token" not in data:
        print("Auth error:", data)
        return None

    return data["token"]
endKey = get_new_token()
print("Token:", endKey)
print(requests.post(valURL, headers={"team": "CC", "token":endKey, "accept": "application/json", "Content-Type": "application/json"}, json={"submission": "In a world built on microservices teams must work within an ecosystem that constantly shifts beneath them. Tokens expire data arrives in fragments responses fluctuate under load and chaos events disrupt the flow without warning. Progress depends on interpreting incomplete signals reacting with precision and staying calm when the system behaves in unexpected ways. Each fragment reveals part of the truth and only by assembling them with patience and clarity can the full narrative be uncovered."}))