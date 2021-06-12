import os
import re

eni=input("Enter the network id")

with open ('flow.txt', 'r') as f:
	for line in f:
		if str(eni) in line and ACCEPT in line:
			print (line)