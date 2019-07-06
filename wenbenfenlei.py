# -*- coding:utf-8 -*-
import jieba
import os
from utils import get_stopwords



def segment_data(filename, stopwords):


    counter=0
    data = []
    
    result=[]
    with open(filename,'r',encoding="utf-8") as f:#读取文件
        for line in f:#循环每一行
        	if (len(line.strip())==0):#去掉空行
        		continue
        	word_list = [x for x in jieba.cut(line.strip(), cut_all=False) if x not in stopwords]#分词，去掉停用词
        	wline=""#将分词列表转换为字符串用于写入文本
        	for w in word_list:#循环每个词

        		wline=wline+w.encode("gbk", 'ignore').decode("gbk", "ignore")+" "#删除乱码，
        	result.append(wline)#将删除乱码的词加入到列表中
        		

        	counter=counter+1#只选取500行内容进行写入	
			
        	# print(counter)

        	if (counter==500):
        		break  
    return result#循环分词列表	




if __name__ == '__main__':#入口函数
	path= "TestData"#读取待处理文件路径
	outfilepath="outputfile"#写入分好词的文件路径
	stopwords=get_stopwords()#获取停用词
	
	files= os.listdir(path)

	for file in files: #遍历文件夹

		if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开

			filename= os.path.basename(file)#打开的处理文本名
		# 	print "",f #打印结果
		# outfile.write(""+f+"\n")
			filepath="TestData/"+filename#处理文本名的路径

		outputfilename="output_"+filename#
		outfile=outfilepath+"/"+outputfilename
		writer=open(outfile,"w",encoding="utf-8")
		print(filepath)
		results=segment_data(filepath,stopwords)

		# print(results)
		
		for line in results:
			print(line)
			writer.write(line+"\n")#写出数据
	writer.close()