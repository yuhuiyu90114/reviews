data = []
num = 0
count_100 = 0
count_good = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		num += len(line)
		data.append(line)
print('總共有{}筆'.format(len(data)))
print('平均留言長度是', num/len(data))
for d in data:
	if len(d) < 100:
		count_100 += 1
print('留言長度少於100共有{}筆'.format(count_100))
for d in data:
	if 'good' in d:
		count_good += 1
print('共有{}筆留言含good'.format(count_good))