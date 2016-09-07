# from see import *; log_on(__file__) #\s*?(# )*?(log|st)\(.*\)` @RFVenter` http://www.rfv.io
import argparse

args = argparse.ArgumentParser()

args.add_argument('-input', help='input file')
args.add_argument('-output', help='output file')

arguments = vars(args.parse_args())
input_file_name = arguments['input']
output_file_name = arguments['output']

#define the patern used for the matches
patterns = {'*': 'identical',  
			':': 'very similar',
			'.': 'weakly similar',
			' ': 'dissimilar'}

#open the input file and extract the necesary data
with open(input_file_name) as input_file:
	#get rid of the first 3 lines of each file
	input_file.readline(); input_file.readline(); input_file.readline()

	#grab the relevant data
	lines = []
	for line in input_file.readlines():
		if line.startswith('                          '): lines.append(line[26:-1])
	data = ''.join(lines)

#go through the data and creat 4 tables for each type of posible match, with the places where they are found
matches = {'identical': [],
		   'very similar': [],
		   'weakly similar': [],
		   'dissimilar': []}
for x, match in enumerate(data): matches[patterns[match]].append(str(x+1))

#open the output file and save the results
with open(output_file_name, 'w') as output_file:
	output_file.write('dissimilar:\n%s\n\n' % ('+'.join(matches['dissimilar'])))
	output_file.write('weakly similar:\n%s\n\n' % ('+'.join(matches['weakly similar'])))
	output_file.write('very similar:\n%s\n\n' % ('+'.join(matches['very similar'])))
	output_file.write('identical:\n%s\n\n' % ('+'.join(matches['identical'])))