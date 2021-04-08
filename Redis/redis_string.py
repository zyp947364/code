from redis import StrictRedis

if __name__ == "__main__":
    # 创建一个strictredis对象，链接redis数据库
    try:
        sr = StrictRedis(password=123456)
        # 添加一个key，为name value为zyp
        # res = sr.set("name","zyp")
        # print(res)

        # 修改name的值为hello
        # res = sr.set("name","hello")
        # print(res)

        # 获取name值
        # res = sr.get("name")
        # print(res)

        # 删除name 
        # res = sr.delete("name")
        # res = sr.delete("a1","a2") # 可以删除多个
        # print(res) # 返回删除键值对的个数

        # 获取数据库中所有的键
        res = sr.keys()
        print(res)
    except Exception as e:
        print(e)