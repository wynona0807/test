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
        	wline=""
        	for w in word_list:#循环每个词

        		wline=wline+w.encode("gbk", 'ignore').decode("gbk", "ignore")+" "#删除乱码，
        	result.append(wline)
        		

        	counter=counter+1	
			
        	# print(counter)

        	if (counter==500):
        		break  
    return result	




if __name__ == '__main__':
	path= "TestData"
	outfilepath="outputfile"
	stopwords=get_stopwords()
	
	files= os.listdir(path)

	for file in files: #遍历文件夹

		if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开

			filename= os.path.basename(file)
		# 	print "",f #打印结果
		# outfile.write(""+f+"\n")
			filepath="TestData/"+filename

		outputfilename="output_"+filename
		outfile=outfilepath+"/"+outputfilename
		writer=open(outfile,"w",encoding="utf-8")
		print(filepath)
		results=segment_data(filepath,stopwords)

		# print(results)
		
		for line in results:
			print(line)
			writer.write(line+"\n")
	writer.close()