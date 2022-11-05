data = []
datag = []
datab = []
num = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		num += len(line)
		data.append(line)
print('總共有{}筆'.format(len(data)))
print('平均留言長度是', num/len(data))

data_100 = []
for d in data:
	if len(d) < 100:
		data_100.append(d)
print('留言長度少於100共有{}筆'.format(len(data_100)))
for d in data:
	if 'good' in d:
		datag.append(d)
print('共有{}筆留言含good'.format(len(datag)))
datab = [d for d in data if 'bad' in d]
print('共有{}筆留言含bad'.format(len(datab)))
#datab = []
#for d in data:
#	 if 'bad' in d:
#		bad.append(d)
#print('共有{}筆留言含bad'.format(len(datab)))
