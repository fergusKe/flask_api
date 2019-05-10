import requests

r = requests.get('http://127.0.0.1:5000/chatbot')

print(r.status_code)
print(r.text)

# curl http://localhost:5000/chatbot