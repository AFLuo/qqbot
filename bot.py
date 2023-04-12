import nonebot
if __name__=="__main__":
    'test string'
    'test string 2'
    nonebot.init()
    nonebot.load_builtin_plugins()
    nonebot.run(host='127.0.0.1',port=8080)