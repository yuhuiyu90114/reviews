data = []
num = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		num += len(line)
		data.append(line)
print('總共有{}筆'.format(len(data)))
print('平均留言長度是', num/len(data))
