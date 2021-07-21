
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	Bryant_word_count = 0
	Lucy_word_count = 0
	Bryant_sticker_count = 0
	Lucy_sticker_count = 0
	Bryant_image_count = 0
	Lucy_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Bryant':
			if s[3] == '貼圖':
				Bryant_sticker_count += 1
			elif s[3] == '圖片':
				Bryant_image_count += 1
			else:
				for m in s[3:]:
					Bryant_word_count += len(m)
		elif name == '非洲酋長':
			if s[2] == '貼圖':
				Lucy_sticker_count += 1
			elif s[2] == '圖片':
				Lucy_image_count += 1
			else:
				 for m in s[2:]:
				 	Lucy_word_count += len(m)

	print('明恩說了:', Bryant_word_count, '傳了', Bryant_sticker_count, '個貼圖', Bryant_image_count, '張圖片')
	print('冠玗說了:', Lucy_word_count, '傳了', Lucy_sticker_count, '個貼圖', Lucy_image_count, '張圖片')

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:

			f.write(line + '\n')


def main():
	lines = read_file('[LINE]非洲酋長.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()