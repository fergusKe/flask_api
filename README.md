# flask_api

簡易 get, post api

### 安裝套件

```sh
$ cd flask_api
$ pip install -r requirements.txt
```

### 執行程式

```sh
$ python app.py # 啟動伺服器
$ python get.py # 執行 get.py (也可以執行 curl http://localhost:5000/chatbot)
$ python post.py # 執行 post.py (也可以執行 curl http://127.0.0.1:5000/chatbot -d "name=Mark&quation=aaa" -X POST -v)
```