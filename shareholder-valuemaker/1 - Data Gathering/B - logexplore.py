from stockapi import Company
import ast
from time import sleep
import re

with open("log.txt","r",encoding="utf-8") as f:
        paths = ast.literal_eval(f.read())

manySecurities = {x:[] for x in range(10)}
one = []

# Code quality: abyssmal, to improve soon

for x in paths.values():
    '''Determine how many files each company has and how many securities they
    have on the market'''
    if len(x)>1:
        manySecurities[len(Company(x[0].split('/')[1]).getSecuritiesInfo())].append(x)
        sleep(1)
    else:
        manySecurities[0].append(x)

for x in manySecurities[1]:
    '''For one-security companies with more than one file, the file with the
    phrase 'top' contains its ownership data'''
	for y in x:
		if y.lower().find('top')==-1:
			print(x)
			x.remove(y) # entries without top are removed

for x in manySecurities[1]:
    '''For one-security companies with more than one file, the file with the
    text (pdt?c|pcd|letter) contains company ownership data/cover letter'''
	for y in x:
		if re.match(".*(pdt?c|pcd|letter).*",y.lower()):
			x.remove(y) # entries matching this are irrelevant to data gathering
for x in manySecurities[2]:
    '''For two-security companies with more than one file, the files with the
    phrase 'top' contains its ownership data'''
	for y in x:
		if not re.match(".*(top).*",y.lower()):
			x.remove(y)
for x in manySecurities[3]:
    '''For three-security companies with more than one file, the files with the
    phrase 'top' contains its ownership data'''
	for y in x:
		if not re.match(".*(top).*",y.lower()):
			x.remove(y)
            
'''Companies with 4 or more securities were seen to have the same number of files
with each representing an individual security, hence no preprocessing'''
out = []
for x in manySecurities.values():
    out.extend(x)
with open('log_filtered.txt','w+') as f:
    f.write(str(out))
