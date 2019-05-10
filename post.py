import requests

data = {'name': 'Mark', 'quation': 'aaa'}

# 將資料加入 POST 請求中
r = requests.post('http://127.0.0.1:5000/chatbot', data = data)

print(r.status_code)
print(r.text)

# curl http://127.0.0.1:5000/chatbot -d "name=Mark&quation=aaa" -X POST -v