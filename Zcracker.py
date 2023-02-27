#!/usr/bin/python3

import zipfile
from argparse import ArgumentParser
from time import time

def prepare_args():
	"""prepare arguments
		return:
			args(argparse.Namespace)
	"""
	parser = ArgumentParser(description="ZIP File password Cracker ",usage="%(prog)s test.zip password.txt",epilog="Example: %(prog)s test.zip  passord.txt -v")
	parser.add_argument(metavar="test.zip",dest="zip_file",help="The Zip file to crack")
	parser.add_argument(metavar="password.txt",dest="password_file",help="Password file")
	parser.add_argument("-V","--verbose",dest="verbose",action="store_true",help="verbose output",default=False)
	parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0",help="Display Version")
	args = parser.parse_args()
	return args

def cracking_zipfile(zip_file,password_file):

	crack_file = zipfile.ZipFile(zip_file)

	f = open(password_file,'r')

	for password in f.readline():
		password = password.strip("\n").strip("\r")

		try:
			crack_file.extractall(pwd=password)
			print("Got it: "+ password + "Yes!!!!")

		except:
			print("I am doing my best.Please wait.....")

if __name__ == "__main__":
	arguments = prepare_args()
	file = cracking_zipfile(arguments.zip_file,arguments.password_file)
	start_time = time()
	end_time = time()
	if arguments.verbose:
		print()

	print(f"Time Taken: {round(end_time-start_time,2)}")