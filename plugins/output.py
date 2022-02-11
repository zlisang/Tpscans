#写入一行指定文本内容到输出文件 output.txt
def writer_text(text):
    try:
        file = open("./output.txt",'a+')
        file.writelines(text+"\n")
        file.close()
    except:
        pass