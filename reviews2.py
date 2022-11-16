import time
import progressbar


def read_file(filename):
	lines = []
	count = 0
	bar = progressbar.ProgressBar(max_value=1000000)	
	with open(filename, 'r') as f:
		for line in f:
			lines.append(line)
			count += 1
			bar.update(count)
	return lines


def count_file(lines):
# 	start_time = time.time()	
	wc = {}
	for line in lines:
		words = line.split()
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1
#	end_time = time.time()				
#	time = end_time - start_time
#	print('花了{}秒'.format(time))
	return wc


def print_file(wc):
	for word in wc:
		if wc[word] > 1000000:
			print('{} {:,}'.format(word, wc[word]))
	print(len(wc))


def lookup_file(wc):
	while True:
		word = input('你要查哪個字:')
		if word == 'q':
			break
		if word in wc:
			print('{}共出現{}次'.format(word, wc[word]))
		else:
			print('{}未出現在留言中'.format(word))
	print("感謝使用此查詢系統!")


def main():
	lines = read_file('reviews.txt')
	wc = count_file(lines)
	print_file(wc)
	lookup_file(wc)

main()
