import json
import time
import requests
import random

class User:
    def __init__(self, mid, nick, comment):
        self.mid = mid
        self.nick = nick
        self.comment = comment
# 抱歉， 本人JAVA 码畜 。。。。 Python 不怎么熟悉， 勉强拿着 Python 试试手， 顺便把我的王者荣耀账号抽了
userList = []
# 所有用户列表   
 
def fetchURL(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    # 请求拿到数据 

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        print(url)
        return r.text
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")


def parserHtml(html):
    s = json.loads(html)
    for i in range(20):
        try:
            comment = s['data']['replies'][i]
            user = User(comment['mid'], comment['member']
                        ['uname'], comment['content']['message'])
            userList.append(user)
        except:
            print("拿到了所有的List")
            return False
    return True
# 解析之后丢到 userList 里


url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=753010065&pn=0'
html = fetchURL(url)
s = json.loads(html)
totalComment = int(s['data']['page']['acount'])
print(' 已获取全部评论 总评论数为：',totalComment)


for page in range(0, 9400):
    url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=753010065&pn=' + str(page)
    jsonstr = fetchURL(url)
    result = parserHtml(jsonstr)
    if(result == False):
        break

print('去重中 ： 》》',)
userNamsNotRepeatArr = []


for user in userList:
    userNamsNotRepeatArr.append(user.nick)

userNamsNotRepeatArr = list(set(userNamsNotRepeatArr)) # 转Set 去重
print("去重之后 共有" , len(userNamsNotRepeatArr),'人')

a_Lucky =  random.randint(0,len(userNamsNotRepeatArr))

print(userNamsNotRepeatArr[a_Lucky])  # 程序已经写好， 
