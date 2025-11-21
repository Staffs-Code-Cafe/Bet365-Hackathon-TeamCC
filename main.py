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

    r = requests.get(url, headers=headers, timeout=10)
    return r.json()




def fetch_20_fragments(token):
    fragment_results = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        # create 20 parallel jobs
        futures = [
            executor.submit(get_fragment, token)
            for _ in range(20)
        ]

        # gather results as they finish
        for future in as_completed(futures):
            fragment_results.append(future.result())

    return fragment_results


# Run

if __name__ == "__main__":
    token = get_token()
    fragments = fetch_20_fragments(token)

    print("Received", len(fragments), "fragments:")
    for frag in fragments:
        print(frag)
