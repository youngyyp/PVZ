# -*- coding: utf-8 -*-

import tkinter as tk

import tkinter.messagebox

import pickle

import requests

from lxml import etree

import validators

import tkinter


    # 界面显示主程序
class ShowUI():
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("测试系统")
        self.root.geometry('700x400')
        # 运行代码时记得添加一个gif图片文件，不然是会出错的
        self.canvas = tkinter.Canvas(self.root, height=400, width=700)  # 创建画布
        self.image_file = tkinter.PhotoImage(file="zombie_1.png")  # 加载图片文件
        self.image = self.canvas.create_image(50, 100, anchor='nw', image=self.image_file)  # 将图片置于画布上
        self.canvas.pack(side='top')  # 放置画布（为上端）
        # 标签 用户名密码
        tk.Label(self.root, text='用户名:').place(x=100, y=150)
        tk.Label(self.root, text='密码:').place(x=100, y=190)

        # 用户名输入框
        self.new_name = tk.StringVar()

        self.var_usr_name = tk.StringVar()

        entry_usr_name = tk.Entry(self.root, textvariable=self.var_usr_name)

        entry_usr_name.place(x=160, y=150)

        # 密码输入框

        var_usr_pwd = tk.StringVar()

        entry_usr_pwd = tk.Entry(self.root, textvariable=var_usr_pwd, show='*')

        entry_usr_pwd.place(x=160, y=190)

        # 登录 注册按钮

        bt_login = tk.Button(self.root, text='登录', command=usr_log_in)

        bt_login.place(x=140, y=230)

        bt_logup = tk.Button(self.root, text='注册', command=usr_sign_up)

        bt_logup.place(x=210, y=230)

        bt_logquit = tk.Button(self.root, text='退出', command=ShowUI.usr_sign_quit)

        bt_logquit.place(x=280, y=230)

        # 主循环

        self.root.mainloop()
    # 退出的函数
    def usr_sign_quit(self):
        self.root.destroy()

    def is_url(self,url):

        if validators.url(url) == True:

            return True

        else:

            return False

    # 登录函数

    def usr_log_in(self):

        # 输入框获取用户名密码

        usr_name = self.var_usr_name.get()

        usr_pwd = self.var_usr_name.get()

        # 从本地字典获取用户信息，如果没有则新建本地数据库

        try:

            with open('usr_info.pickle', 'rb') as usr_file:

                usrs_info = pickle.load(usr_file)

        except FileNotFoundError:

            with open('usr_info.pickle', 'wb') as usr_file:

                usrs_info = {'admin': 'admin'}

                pickle.dump(usrs_info, usr_file)

        # 判断用户名和密码是否匹配

        if usr_name in usrs_info:

            if usr_pwd == usrs_info[usr_name]:

                tk.messagebox.showinfo(title='welcome',

                                       message='欢迎您：' + usr_name)

                usr_sign_quit()

                top = tkinter.Tk()

                def is_entry_right():

                    if is_url(link_entry.get()):

                        ur = link_entry.get()

                        for i in range(0, 1000, 50):

                            url = ur.replace("pn=0", "pn={}".format(i))

                            print(url)

                            try:

                                r = requests.get(url, timeout=20)

                            except:

                                tkinter.messagebox.showerror('wrong!', 'can not get the url\n请求网址失败')

                                return

                            html = etree.HTML(r.text)

                            img_list = html.xpath(

                                './/div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/text()')

                            l = len(img_list)

                            for i in range(l):
                                with open('title.txt', 'a', encoding='utf-8')as fp:
                                    fp.write(img_list[i] + '\n')

                        tkinter.messagebox.showinfo('success!', 'successfully download images!')



                    else:

                        tkinter.messagebox.showwarning('wrong!', 'wrong url or path\n错误的地址或路径')

                # 设置窗口标题和大小

                top.title('爬取贴吧')

                top.geometry('500x500+100+100')

                # 默认存储格式设置

                choice = tkinter.StringVar()

                choice.set('.txt')

                # 开始抓取按钮

                button = tkinter.Button(top, text="开始抓取", command=is_entry_right)

                button.pack()

                # 网站地址

                link_add = tkinter.Label(top, text='抓取的地址:')

                link_add.pack()

                # 网站地址输入

                link_entry = tkinter.Entry(top, width=100)

                link_entry.pack()

                # 开始主循环

                top.mainloop()

            else:

                tk.messagebox.showerror(message='密码错误')

        # 用户名密码不能为空

        elif usr_name == '' or usr_pwd == '':

            tk.messagebox.showerror(message='用户名或密码为空')

        # 不在数据库中弹出是否注册的框

        else:

            is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')

            if is_signup:
                usr_sign_up()

    # 注册函数

    def usr_sign_up(self):

        # 确认注册时的相应函数

        def signtowcg():

            # 获取输入框内的内容

            nn = self.new_name.get()

            np = new_pwd.get()

            npf = new_pwd_confirm.get()

            # 本地加载已有用户信息,如果没有则已有用户信息为空

            try:

                with open('usr_info.pickle', 'rb') as usr_file:

                    exist_usr_info = pickle.load(usr_file)

            except FileNotFoundError:

                exist_usr_info = {}

                # 检查用户名存在、密码为空、密码前后不一致

            if nn in exist_usr_info:

                tk.messagebox.showerror('错误', '用户名已存在')

            elif np == '' or nn == '':

                tk.messagebox.showerror('错误', '用户名或密码为空')

            elif np != npf:

                tk.messagebox.showerror('错误', '密码前后不一致')

            # 注册信息没有问题则将用户名密码写入数据库

            else:

                exist_usr_info[nn] = np

                with open('usr_info.pickle', 'wb') as usr_file:

                    pickle.dump(exist_usr_info, usr_file)

                tk.messagebox.showinfo('欢迎', '注册成功')

                # 注册成功关闭注册框

                self.root.destroy()

    # 新建注册界面

        window_sign_up = tk.Toplevel(self.root)

        window_sign_up.geometry('350x200')

        window_sign_up.title('注册')

        # 用户名变量及标签、输入框



        tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)

        tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)

        # 密码变量及标签、输入框

        new_pwd = tk.StringVar()

        tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)

        tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)

        # 重复密码变量及标签、输入框

        new_pwd_confirm = tk.StringVar()

        tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)

        tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)

        # 确认注册按钮及位置

        bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',

                                       command=signtowcg)

        bt_confirm_sign_up.place(x=150, y=130)