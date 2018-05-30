#!/usr/bin/env python3
#coding: utf-8

from PIL import Image
import argparse


def get_char(r, g, b, alpha=256):

	if alpha == 0:
		return " "

	ascii_chart = list("qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm ")
	grey = (2126 * r + 7152 * g + 722 * b) / 10000

	# assign grey number to char in ascii_chart
	char_index = int((grey / float(alpha)) * len(ascii_chart))
	return ascii_chart[char_index]


def write_file(out_file, text):
	
	with open(out_file, 'w') as f:
		f.write(text)


def main(in_file, width, height, out_file):

	im = Image.open(in_file)
	im = im.resize((width, height), Image.NEAREST)

	text = ""
	for j in xrange(height):
		for i in xrange(width):
			rgb_info = im.getpixel((i, j))
			text += get_char(*rgb_info)
		text += "\n"

	print(text)
	write_file(out_file, text)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("in_file", help="Name of Input File")
	parser.add_argument("out_file", help="Name of Output File")
	parser.add_argument("--width", type=int, default=50)
	parser.add_argument("--height", type=int, default=50)

	args = parser.parse_args()
	main(args.in_file, args.width, args.height, args.out_file)
