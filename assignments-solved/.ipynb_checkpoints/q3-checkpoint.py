import requests


URI = "https://dbpedia.org/person/Hermann_Knoblauch"
res = requests.get(url = URI)
print(f"URL: {URI}\n\nResponds code: {res.status_code}\n\nResponds content: {res.content}\n\n\n")

URI = "https://dbpedia.org/resource/Hermann_Knoblauch"
res = requests.get(url = URI)
print(f"URL: {URI}\n\nResponds code: {res.status_code}\n\nResponds content: {res.content}\n")