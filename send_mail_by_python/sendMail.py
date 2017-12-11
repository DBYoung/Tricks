class sendMail:
    __sender = None
    __passwd = None
    __receiver = None
    __from = None
    __to = None
    __message = None
    __title = None
    def __init__(self,sender,passwd,receiver,_from,_to,message,title = "主题"):
        self.__sender = sender
        self.__passwd = passwd
        self.__receiver = receiver
        self.__from = _from
        self.__to = _to
        self.__message = message
        self.__title = title
    def __printMessage(self,value):
        if value:
            print("successed!")
        else:
            print("failed!")
    def send_mail(self):
        ret = True
        try:
            msg=MIMEText(self.__message,'plain','utf-8')
            msg['From']=formataddr([self.__from,self.__sender])  #括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr([self.__to,self.__receiver])  #括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject']=self.__title #邮件的主题，也可以说是标题

            server=smtplib.SMTP("smtp.163.com",25) #发件人邮箱中的SMTP服务器，端口是25
            server.login(self.__sender,self.__passwd)  #括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.__sender,[self.__receiver,],msg.as_string())  #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  #这句是关闭连接的意思
        except Exception:
            ret = False
        return self.__printMessage(ret)
