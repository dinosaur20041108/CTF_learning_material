
import requests
url_="http://127.0.0.1:6889"
burp_proxy = {'http', 'http://127.0.0.1:8080'}
params_={
    '1+1>2':'op'
}
data_=params_
file_={
    "start":('op',"http 启动!!!")
}

res =requests.post(url=url_,params=params_,data=data_,files=file_, proxies= burp_proxy)
print(res.text)