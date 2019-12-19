from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import html,base64,json,time,sys
import win32con
import win32clipboard as wincld
from main import Ui_MainWindow
import frozen_dir
SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)
import urllib.parse
class MainWindows(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindows,self).__init__(parent)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setFixedSize(self.width(), self.height()) ##设置宽高不可变
        self.timer = QTimer()  #设定一个定时器用来显示时间
        self.setWindowIcon(QtGui.QIcon('./main.png'))
        self.timer.timeout.connect(self.showtime)
        self.timer.start()
        self.Ui.encode_Button.clicked.connect(self.encode)  # 编码按钮
        self.Ui.decode_Button.clicked.connect(self.decode)  # 解码按钮
        self.Ui.clear_Button.clicked.connect(self.clear)  # clear
        self.Ui.Copy_Source_Button.clicked.connect(lambda:self.Copy_text('Source'))  # copy_source
        self.Ui.Copy_ResultButton.clicked.connect(lambda:self.Copy_text('result'))  # copy_result
        self.Ui.tihuan.clicked.connect(self.tihuan)  # tihuan
        self.readfile()
        self.Ui.panduan.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['public']['panduan'])) )  # panduan
        self.Ui.chaxunliehshu.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['public']['chaxunliehshu'])) )  # chaxunliehshu
        self.Ui.user.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['public']['user'])) )  # user
        self.Ui.version.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['public']['version'])) )  # version
        self.Ui.path.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['public']['path'])) )  # path
        self.Ui.single_databases.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Order']['single_databases'])) )  # single_databases
        self.Ui.current_databases.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Order']['current_databases'])) )  # current_databases
        self.Ui.all_databases.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Order']['all_databases'])) )  # all_databases
        self.Ui.single_tables.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Order']['single_tables'])) )  # single_tables
        self.Ui.all_tables.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Order']['all_tables'])) )  # all_tables
        self.Ui.single_columns.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Order']['single_columns'])) )  # single_columns
        self.Ui.all_columns.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Order']['all_columns'])) )  # all_columns
        self.Ui.mangzhu_databases.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Blinds']['mangzhu_databases'])) )  # mangzhu_databases
        self.Ui.mangzhu_tables.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Blinds']['mangzhu_tables'])) )  # mangzhu_tables
        self.Ui.mangzhu_lumns.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['Blinds']['mangzhu_columns'])) )  # mangzhu_lumns
        self.Ui.data.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['others']['data'])) )  # data
        self.Ui.others.clicked.connect(lambda:self.Ui.Source_text.setText(str(json_data[self.Ui.sql_type.currentText()]['others']['others'])) )  # others

    def readfile(self):
        global json_data
        f=open('data.json','r',encoding='utf-8')
        json_data=json.load(f)
        f.close()
    def showtime(self):  #显示时间
        datetime = QDateTime.currentDateTime()
        text = datetime.toString("yyyy-MM-dd hh:mm:ss")
        self.Ui.time.setText(text)

    #编码
    def encode(self):
        if __name__ == '__main__':
            text = self.Ui.Source_text.toPlainText()
            code_type =self.Ui.encode_type.currentText()
            if code_type=='URL-UTF8':
                self.URLencode(text,'utf8')
            if code_type == 'URL-GB2312':
                self.URLencode(text, 'gb2312')
            if code_type=='Unicode':
                self.Unicodeencode(text)
            if code_type=='Escape(%U)':
                self.Escapeencode(text)
            if code_type=='HtmlEncode':
                self.Htmlencode(text)
            if code_type=='ASCII':
                self.ASCIIencode(text)
            if code_type=='Base64':
                self.base64encode(text)
            if code_type=='Str<->Hex':
                self.Strtohexencode(text)
            if code_type=='SQL-Char':
                self.Charencode(text)
            if code_type=='SQL-Hex':
                self.Hexencode(text)
    def URLencode(self,text,type):
        # 先进行gb2312编码
        if type=='utf8':
            text = text.encode('utf-8')
            text = urllib.parse.quote(text)
        if type=='gb2312':
            text = text.encode('gb2312')
            text = urllib.parse.quote(text)
        self.Ui.Result_text.setText(text)
    def Unicodeencode(self,text):
        text =text.encode('unicode_escape')
        self.Ui.Result_text.setText(str(text, encoding='utf-8'))
    def Escapeencode(self,text):
        text =text.encode('unicode_escape')
        self.Ui.Result_text.setText(str(text, encoding='utf-8').replace('\\u','%u'))
    def Htmlencode(self,text):
        text = html.escape(text)
        self.Ui.Result_text.setText(str(text))
    def ASCIIencode(self,text):
        result = ''
        for i in text:
            result=str(result)+str(ord(str(i)))+' '
        self.Ui.Result_text.setText(str(result)[:-1])
    def base64encode(self,text):
        text = base64.b64encode(text.encode("utf-8"))
        self.Ui.Result_text.setText(str(text,encoding='utf-8'))
    def Strtohexencode(self,text):
       result = ''
       for i in text:
           single =str(hex(ord(str(i))))
           result =result+single
       self.Ui.Result_text.setText('0x'+(str(result)).replace('0x',''))
    def Charencode(self,text):
        result = ''
        for i in text:
            single =str(ord(str(i)))
            result =result+'char(%s)+'%single
        self.Ui.Result_text.setText(str(result)[:-1])
    def Hexencode(self,text):
        result = ''
        for i in text:
            single =str(hex(ord(str(i))))
            result =result+'hex(%s)+'%single
        self.Ui.Result_text.setText((str(result)[:-1]).replace('0x',''))
    #解码
    def decode(self):
        if __name__ == '__main__':
            text = self.Ui.Source_text.toPlainText()
            code_type =self.Ui.encode_type.currentText()
            if code_type=='URL-UTF8':
                self.URLdecode(text,'utf8')
            if code_type == 'URL-GB2312':
                self.URLdecode(text, 'gb2312')
            if code_type=='Unicode':
                self.Unicodedecode(text)
            if code_type=='Escape(%U)':
                self.Escapedecode(text)
            if code_type=='HtmlEncode':
                self.Htmldecode(text)
            if code_type=='ASCII':
                self.ASCIIdecode(text)
            if code_type=='Base64':
                self.base64decode(text)
            if code_type=='Str<->Hex':
                self.Strtohexedecode(text)
            if code_type=='SQL-Char':
                self.Chardecode(text)
            if code_type=='SQL-Hex':
                self.Hexdecode(text)
    def URLdecode(self,text,type):
        if type=='utf8':
            text = urllib.parse.unquote(text)
        if type=='gb2312':
            text = urllib.parse.unquote(text, 'gb2312')
        self.Ui.Result_text.setText(str(text))
    def Unicodedecode(self,text):
        text =bytes(text,encoding = "utf8").decode('unicode_escape')
        # print(text)
        self.Ui.Result_text.setText(text)
    def Escapedecode(self,text):
        text =text.replace('%u','\\u').replace('%U','\\u')
        text =bytes(text,encoding = "utf8").decode('unicode_escape')
        # print(text)
        self.Ui.Result_text.setText(text)
    def Htmldecode(self,text):
        # h=HTMLParser()
        self.Ui.Result_text.setText(html.unescape(text))
    def ASCIIdecode(self,text):
        if ':' in text:
            text=text.split(":")
        if ' ' in text:
            text=text.split(" ")
        if ';' in text:
            text=text.split(";")
        if ',' in text:
            text=text.split(",")
        result = ''
        for i in text:
            if i !='':
                # print(chr(int(i)))
                result=result+chr(int(i))
        # print(result)
        self.Ui.Result_text.setText(str(result))
    def base64decode(self,text):
        text = base64.b64decode(text.encode("utf-8"))
        self.Ui.Result_text.setText(str(text,encoding='utf-8'))
    def Strtohexedecode(self,text):
        text=text.replace('0x','').replace('0X','')
        text =str(bytes.fromhex(text), encoding = "utf-8")
        self.Ui.Result_text.setText(str(text))
    def Chardecode(self,text):
        text=text.replace('char(','').replace(')','').split("+")
        result=''
        for i in text:
            if i !='':
                # print(chr(int(i)))
                result=result+chr(int(i))
        self.Ui.Result_text.setText(str(result))
    def Hexdecode(self,text):
        text=text.replace('hex(','').replace(')','').split("+")
        result=''
        for i in text:
            if i !='':
                result=result+chr(int(str(i),16))
        self.Ui.Result_text.setText(str(result))
    def clear(self):
        self.Ui.Source_text.clear()
        self.Ui.Result_text.clear()

    def Copy_text(self,text):
        if  text=='Source':
            data = self.Ui.Source_text.toPlainText()
        if  text=='result':
            data = self.Ui.Result_text.toPlainText()
        # 访问剪切板，存入值
        wincld.OpenClipboard()
        wincld.EmptyClipboard()
        wincld.SetClipboardData(win32con.CF_UNICODETEXT, data)
        wincld.CloseClipboard()
    def tihuan(self):
        source_text=self.Ui.tihuan_source.text()
        result_text=self.Ui.tihuan_result.text()
        text =self.Ui.Source_text.toPlainText()
        text=text.replace(source_text,result_text)
        self.Ui.Source_text.setText(str(text))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    # f=open('./qss/white.qss', 'r',encoding='utf-8')
    # qssStyle= f.read()
    # window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())
