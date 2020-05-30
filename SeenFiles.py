import time		# importing time for working with time
import os		# importing os for work with system
import glob 	# importing for seach file with "*."
import shutil	# importing for moving files

                                     

					   		# error funcion
def error_file_notfound():
	print('Error. Files this types not found\n')
	


		 		# search information function  
def search():
	dir = input('Select name of directory: ')	# input directiory where be start search
	os.chdir(dir)								# using directory for search files
	print('Scanning...')
	print()
	time.sleep(2)

	global list_txt					# create global list for all users use
	list_txt = []
	for txt in glob.glob("*.txt"):	# search file with end .txt
		print(txt)
		list_txt.append(txt)		# add all files with end .txt in list


	global list_dat					# create global list for all users use
	list_dat = []	
	for dat in glob.glob("*.dat"):	# search file with end .dat
		print(dat)
		list_dat.append(dat)		# add all files with end .dat in list


	global list_cvs					# create global list for all users use
	list_cvs = []
	for cvs in glob.glob("*.cvs"):	# search file with end .cvs
		print(cvs)
		list_cvs.append(cvs)		# add all files with end .cvs in list


	global list_html					# create global list for all users use
	list_html = []
	for html in glob.glob("*.html"):	# search file with end .html
		print(html)
		list_html.append(html)	 	 	# add all files with end .html in list


	global list_css					# create global list for all users use
	list_css = []
	for css in glob.glob("*.css"):	# search file with end .css
		print(css)
		list_css.append(css)		# add all files with end .css in list                                           
			


							# adding files function
def add_files():
	time.sleep(2)
	if list_txt != []:						# if function for found file in directory
		print("TXT files adding: ")
		for txt in list_txt:
			info_intro = open(txt, "r")		# open file for reading and taking info from him
			sh_date = info_intro.read()		# reading contents of file
			print()
			print(txt)						# output name of file
			print(sh_date)					# output all info which is in this file
			with open("TXTS.txt", "a") as txt_file:					# open txt file with date
				txt_file.write(txt + "\n" + str(sh_date) + "\n\n")	# write name of files with contents
		print() 
		time.sleep(2)
	else:
		print("TXT files adding: ")
		time.sleep(1)
		error_file_notfound()

		# NEW ADDING BLOCK

	print()
	time.sleep(2)
	if list_dat != []:						# if function for found file in directory              
		print("DAT files adding: ")
		for dat in list_dat:
			info_intro = open(dat, "r")		# open file for reading and taking info from him
			sh_date = info_intro.read()		# reading contents of file
			print()
			print(dat)						# output name of file
			print(sh_date)					# output all info which is in this file
			with open("DATS.txt", "a") as dat_file:					# open txt file with date
				dat_file.write(dat + "\n" + str(sh_date) + "\n\n")	# write name of files with contents
		print()
		time.sleep(2)
	else:
		print("DAT files adding: ")
		time.sleep(1)
		error_file_notfound()

		# NEW ADDING BLOCK	

	print()
	time.sleep(2)
	if list_cvs != []:						# if function for found file in directory
		print("CVS files adding: ")
		for cvs in list_cvs:
			info_intro = open(cvs, "r")		# open file for reading and taking info from him
			sh_date = info_intro.read()		# reading contents of file
			print()
			print(cvs)						# output name of file
			print(sh_date)					# output all info which is in this file
			with open("CVS`s.txt", "a") as cvs_file:				# open txt file with date
				cvs_file.write(cvs + "\n" + str(sh_date) + "\n\n")	# write name of files with contents
		print()
		time.sleep(2)
	else:
		print("CVS files adding: ")
		time.sleep(1)
		error_file_notfound()

		# NEW ADDING BLOCK

	print()
	time.sleep(2)
	if list_html != []:							# if function for found file in directory
		print("HTML files adding: ")
		for html in list_html:
			info_intro = open(html, "r")		# open file for reading and taking info from him
			sh_date = info_intro.read()			# reading contents of file
			print()
			print(html)							# output name of file
			print(sh_date)						# output all info which is in this file
			with open("HTMLS.txt", "a") as html_file:					# open txt file with date
				html_file.write(html + "\n" + str(sh_date) + "\n\n")	# write name of files with contents
		print()	
		time.sleep(2)
	else:
		print("HTML files adding: ")
		time.sleep(1)
		error_file_notfound()

		# NEW ADDING BLOCK
	
	print()
	time.sleep(2)
	if list_css != []:						# if function for found file in directory
		print("CSS files adding: ")
		for css in list_css:
			info_intro = open(css, "r")		# open file for reading and taking info from him
			sh_date = info_intro.read()		# reading contents of file
			print()
			print(css)						# output name of file
			print(sh_date)					# output all info which is in this file
			with open("CSS`s.txt", "a") as css_file:				# open txt file with date
				css_file.write(css + "\n" + str(sh_date) + "\n\n")	# write name of files with contents
		print()
		time.sleep(2)
	else:
		print("CSS files adding: ")
		time.sleep(1)
		error_file_notfound()
		print()
				# The end of adding files



		# Creating folder and moving all files in folder

def to_folder_all_files():
	os.mkdir("All_Files")
	print("Creating folder...")
	print()
	time.sleep(2)
	if list_txt != []:								# review file in directory
		print("Moving txt...")
		shutil.move('TXTS.txt', 'All_Files')		# write file of txt in archive
		time.sleep(1)
		print("Done moving")
		print()
	else:
		print("Moving txt...")
		time.sleep(1)
		error_file_notfound()						# funcion of error


	if list_dat != []:								# review file in directory
		print("Moving dat...")
		shutil.move('DATS.txt', 'All_Files')		# write file of txt in archive
		time.sleep(1)
		print("Done moving")
		print()
	else:
		print("Moving dat...")
		time.sleep(1)
		error_file_notfound()						# funcion of error


	if list_cvs != []:								# review file in directory
		print("Moving cvs...")
		shutil.move('CVS`s.txt', 'All_Files')		# write file of txt in archive
		time.sleep(1)
		print("Done moving")
		print()
	else:
		print("Moving cvs...")
		time.sleep(1)
		error_file_notfound()						# funcion of error


	if list_html != []:								# review file in directory
		print("Moving html...")
		shutil.move('HTMLS.txt', 'All_Files')		# write file of txt in archive
		time.sleep(1)
		print("Done moving")
		print()
	else:
		print("Moving html...")
		time.sleep(1)
		error_file_notfound()						# funcion of error


	if list_css != []:								# review file in directory
		print("Moving css...")
		shutil.move('CSS`s.txt', 'All_Files')		# write file of txt in archive
		time.sleep(1)
		print("Done moving")
		print()
	else:
		print("Moving css...")
		time.sleep(1)
		error_file_notfound()						# funcion of error
	time.sleep(2)
	print("All right!")								# end of moving
	print()

    

		# Creating work of script

						# Central code doing
os.system('cls')
search()
print()
print('Adding files...')
print()
add_files()				# adding files in category
to_folder_all_files()	# adding files in folder