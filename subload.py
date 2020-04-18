#!/usr/bin/python3

import os, re

location = os.getcwd()

# Load all the videos name in vid_file
Vid_file = 'Vid_file.txt'
Videos = []

Srt_file = 'Srt_file.txt'
Srts = []

# subtitles are not yet downloaded 
Vid_location = 'Vid_location.txt'
Videos_todo = []

def clear_file(file_name):
	open(file_name,"w").close()


def load_Vid_Srt_file():
	clear_file(Vid_file) 
	clear_file(Srt_file)

	for file in os.listdir(location):
		if file.endswith('.mkv') or file.endswith('.mp4'):
			
			newfile=file.replace(']','').replace('[','').replace(' ','.').replace('(','').replace(')','').replace("'",'')
			os.rename(r''+file,r''+newfile)

			with open(Vid_file , 'a') as FL:
				# file = file[:-4]
				Videos.append(newfile)
				FL.write(newfile + '\n')

		elif file.endswith('.srt'):
			with open(Srt_file , 'a') as FL:
				file = file[:-4]
				Srts.append(file)
				FL.write(file + '\n')
	

def load_location():
	clear_file(Vid_location)
	for name in Videos:
		sub = name[:-4]
		if sub not in Srts:
			Videos_todo.append(name)
			with open(Vid_location , 'a') as FL:
				FL.write(name+'\n')


def load_subtitel(name):
	
	os.system( 'subliminal download -l en ' + name + " > logs.txt")
	FL = open("logs.txt",'r')
	for line in FL:
		line = line.strip()
		if re.match(r"Downloaded 1 subtitle",line):
			FL.close()
			os.rename(r''+name[:-4]+'.en.srt',r''+name[:-4]+'.srt')
			return

	print("\n\n\nSubtitle not found for {} \n\n\n\n".format(name))
	



def main():
	load_Vid_Srt_file()
	load_location()
	Videos_todo.sort()

	for loc in Videos_todo:
		print('Searching subtitle of {}.\n'.format(loc))
		load_subtitel(loc)

	os.remove('Srt_file.txt')
	os.remove('Vid_file.txt')
	os.remove('Vid_location.txt')
	os.remove('logs.txt')

if __name__ == "__main__":
	main()
