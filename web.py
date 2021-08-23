import requests

param={"msg":"mobileuser","isadmin":1}
post=requests.post("https://httpbin.org/anything",data=param)

print(post.headers)
