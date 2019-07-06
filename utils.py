# -*- coding:utf-8 -*-
import os


def get_stopwords():
	path="stopwords.txt"
	stopwords =[]
	with open(path,'r',encoding="utf-8") as f:
		for line in f:
			
			line=line.strip()
			# print(line)

			
			stopwords.append(line)

	
	return stopwords
if __name__ == '__main__':
	stopwords=get_stopwords()
	print(stopwords)
	
	# path= "C:/python/TestData"
	# files= os.listdir(path)

	# for file in files: #遍历文件夹

	# 	if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开

	# 		f = os.path.basename(file)
	# 	# 	print "",f #打印结果
	# 	# outfile.write(""+f+"\n")
	# 		filename="TestData/"+f