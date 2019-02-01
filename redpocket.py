#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'Aegon'
import itchat
import tkinter.messagebox
import winsound



def alarm():
    # Windows嗡鸣声
    winsound.Beep(1000, 3000)
    # 提示文本消息
    tkinter.messagebox.showinfo('重要提醒','有人发红包了！')


@itchat.msg_register('Note', isGroupChat=True)
def get_note(msg):
    if 'best wishes' in msg['Text']:
        print('note:',msg['Text'])
        alarm()

# 接受消息
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def _(msg):
    print('text:',msg['Text'])

itchat.auto_login(hotReload=True)
itchat.run()
itchat.logout()