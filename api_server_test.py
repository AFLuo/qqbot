import requests as req
if __name__=='__main__':
    url="http://127.0.0.1:7861/sdapi/v1/txt2img"
    # content={
    #     "prompt":"sexy loli",
    #     "samples":"1",
    #     "negative_prompt":"",
    #     "width":"786",
    #     "height":"512",
    # }
    req.post(url)