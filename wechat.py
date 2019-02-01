#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'Aegon'
#-*- coding:utf-8 -*-
import itchat
from itchat.content import *
import requests
import json

@itchat.msg_register(TEXT)
def reply_text(msg):
    from_text = msg['Text']
    # 消息带有 ‘#’ 前缀为翻译
    if from_text[0] == '#':
        to_text = baidu_trans(from_text[1:])
        itchat.send(to_text, msg['FromUserName'])
    else:
        to_text   = tuling(from_text)
        itchat.send(to_text,msg['FromUserName'])


def tuling(info):

    appkey   = "d22645cd9f284c36b7e68e64a7a4fe4c"
    url      = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    req      = requests.get(url)
    content  = req.text
    data     = json.loads(content)
    answer   = data['text']

    return answer


def baidu_trans(info):
    url = 'http://fanyi.baidu.com/v2transapi'
    keywords = {
        'from': 'zh',
        'to': 'en',
        'query': info,

    }
    req = requests.post(url, keywords)
    data = req.json()
    try:
        result = data['dict_result']['simple_means']['word_means']
        return ';'.join(result)

    except:

        return data['trans_result']['data'][0]['dst']


def main():
    itchat.auto_login(hotReload=True)
    itchat.run()

if __name__ == '__main__':
    main()


