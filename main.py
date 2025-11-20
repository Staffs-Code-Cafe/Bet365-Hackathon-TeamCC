import requests
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


def get_fragment(key):
    """Fetch a single fragment using the token."""
    try:
        r = requests.get(fragURL, headers={"team": "CC", "token": key}, timeout=0.5)
        data = r.json()
    except Exception as e:
        print("Fragment request error:", e)
        return None

    print("Fragment:", data)

    # Validate required fields
    if "position" not in data or "word" not in data:
        return None

    try:
        pos = int(data["position"])
    except:
        return None

    if 0 <= pos < len(para):
        temp = ""
        temp_list = []
        for i in data["word"]:
            if i in chars:
                temp += i
            else:
            
                break
        try:
            if temp in nonWords:
                    temp_list= list(temp)
                    temp_list.reverse()
                    temp = " ".join(temp_list)
            elif (requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{temp}").json())["title"] is None:
                temp_list= list(temp)
                temp_list.reverse()
                temp = " ".join(temp_list)
        except:
            para[pos] = temp
        
    return True


def fill_sentence():

    key = get_new_token()
    if not key:
        print("Could not obtain initial token")
        return ""

    request_count = 0
    while "" in para:

        # Refresh key every 20 requests
        if request_count >= 20:
            print("\nRefreshing token...\n")
            key = get_new_token()
            if not key:
                print("Could not refresh token")
                return ""
            request_count = 0

        success = get_fragment(key)
        request_count += 1
        for i in para:
            print(i)

        if not success:
            print("Failed fragment fetch, continuing...")

    # Build final sentence
    return " ".join(para)


# ---- RUN ----

endKey = get_new_token()
full_sentence = fill_sentence()
print("\n✔ FULL SENTENCE:\n")
print(full_sentence)
requests.post(valURL, headers={"team": "CC", "token":endKey}, body={"submission": full_sentence})

