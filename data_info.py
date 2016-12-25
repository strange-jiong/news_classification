#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-25 16:23:59
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
import os


def data_info(path):
	"""
	统计数据集语料信息
	"""
	file_list = []
	if os.path.exists('./%s' % path):
		file_list = os.listdir(path)

	if not file_list:
		print 'file not exist!!!'
		exit()

	res = {}
	for each in file_list:


		count = 0
		res[each] = []

		file_txt_list = os.listdir(os.path.join(path, each))

		txt_num = len(file_txt_list)
		print txt_num
		for each_txt in file_txt_list:
			# print 'cd %s/%s'%(path,each)
			# os.system('cd %s/%s'%(path,each))
			# print os.getcwd()
			file = open('%s/%s/%s' % (path, each, each_txt), 'r')
			# for each_line in file.readline():
			# print len(file.readline().split(' '))
			res[each].append(len(file.readline().split(' ')))
			count += 1
			# print count
			file.close()
		# print count
		# print type(each)
		# each=each.decode('gbk')
		print each

		plt.plot(range(txt_num), res[
			each],   'o')
		plt.title('category')
		plt.xlabel('txt num')
		plt.ylabel('term num')
		plt.ylim((0, 600))
		plt.show()
	plt.legend(loc='upper left', numpoints=1)
	# plt.show()
data_info('./test4')
