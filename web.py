import requests

param1={"msg":"welcomeuser","isadmin":1}

param={"msg":"mobileuser","isadmin":1}
post1=requests.post("https://httpbin.org/anything",data=param1)
post=requests.post("https://httpbin.org/anything",data=param)
print(post1.text)
print(post.headers)
