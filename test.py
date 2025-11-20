from PyDictionary import PyDictionary
import requests


print(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/gjrdbghjrdbhfuoesnfhjrtbdughnr").json())


dictionary = PyDictionary()

print(dictionary.meaning("indentation"))


print(list("indentation"))