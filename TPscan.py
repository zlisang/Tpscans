import time

from scanCore import scan
import sys




# readUrl: 对指定文本文件进行读取，该文件内必须每行一个url，读取到url存放在集合urlList内
def readUrl(filename):
    list = []
    try:
        file = open(filename,'r')
        tmp = ''
        while True:
            tmp = file.readline()
            if tmp == '':
                break
            list.append(tmp[:-1])
    except:
        pass
    return list

if __name__ == '__main__':
    print('''
     ___________                    
    |_   _| ___ \                   
      | | | |_/ /__  ___ __ _ _ __  
      | | |  __/ __|/ __/ _` | '_ \ 
      | | | |  \__ \ (_| (_| | | | |
      \_/ \_|  |___/\___\__,_|_| |_|          
                    code by Lucifer 
                    Jiang 二次修改
                    -f urlFilename
    ''')
    file = ""
    for var in range(1, len(sys.argv)):
        if sys.argv[var] == '-f':
            try:
                file = sys.argv[var + 1]
            except:
                pass

    listurl = readUrl(file)
    for url in listurl:
        print(url)
        scan(url)