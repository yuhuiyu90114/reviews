def read_file(filename):
	lines = []
	with open('reviews.txt', 'r') as f:
		for line in f:
			lines.append(line)
	return lines

def count_file(lines):
	wc = {}
	for line in lines:
		words = line.split(' ')
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1
	return wc


def print_file(wc):
	for word in wc:
		if wc[word] > 1000000:
			print(word, wc[word])
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
