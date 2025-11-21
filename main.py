import requests
from concurrent.futures import ThreadPoolExecutor, as_completed



def get_token():
    url = "https://dcrypt.run/auth"
    headers = {"team": "Code Cafe"}
    
    r = requests.post(url, headers=headers)
    data = r.json()
    print(data)
    try:
        return data["token"]
    except:
        raise Exception("Failed to retrieve token")


def get_fragment(token):
    url = "https://dcrypt.run/fragment"
    headers = {"team": "Code Cafe", "token": token}
    try:
        data = requests.get(url, headers=headers, timeout=3)
    except:
        return {"error": "Funny Request"}
    try:
        print(data[''])
        return data.json()
    except:
        return {"error": "Failed to parse JSON"}




def fetch_20_fragments(token):
    fragment_results = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [
            executor.submit(get_fragment, token)
            for _ in range(20)
        ]

        for future in as_completed(futures):
            fragment_results.append(future.result())

    return fragment_results


def mergeFragments(fragList):
    try:
        for i in fragList:
                index = i['position']
                para[index] = i['word']
    except:
        pass

# Run


if __name__ == "__main__":
    para = [""] * 76
    chars = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    ".", ",", "!", "?", " ", "0", "1", "2", "3", "4", "5",
    "6", "7", "8", "9"
    ]   


    while "" in para:
        token = get_token()
        fragments = fetch_20_fragments(token)

        mergeFragments(fragments)

    print("Received", len(fragments), "fragments:")
    for frag in fragments:
        print(frag)
