import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from statistics import mean
from functools import reduce
import re
import collections

def tagasala(paths):
    '''Sifts through files and classifies them into sub-categories which can be
    parsed by the same algorithm (regex format)'''
    x=0
    types = {}
    for x in range(1,25):
        types[x] = []
    notypes = []
    empty = []
    for file_path in paths:
        txtFN = ".".join(file_path.split(".")[:-1])+".txt"
        with open(txtFN,"r",encoding="utf-8") as f:
            one = f.readline()
            allz = f.read()
            if allz=="":
                empty.append(txtFN)
            elif one.find("Stock Transfer Service Inc.                              Page No.        1")!=-1:
                (types[1]).append(txtFN)
            elif allz.find("Stock Transfer Service Inc.                              Page No.        1")!=-1:
                (types[2]).append(txtFN)
            elif allz.find("Stock Transfer Service Inc.")!=-1:
                (types[3]).append(txtFN)#.split("/")[1])
            elif allz.find("TRUST AND INVESTMENT SERVICES GROUP")!=-1:
                (types[4]).append(txtFN)
            elif allz.find("Stockholder Name Shares Percentage")!=-1:
                (types[5]).append(txtFN)
            elif one.find("Stockholder Name Shares Percentage")!=-1:
                (types[6]).append(txtFN)
            elif allz.find("Business Date: June 30, 2020\nBPNAME HOLDINGS")!=-1:
                (types[7]).append(txtFN)
            elif allz.find("STOCKHOLDER'S NAME TOTAL")!=-1:
                (types[8]).append(txtFN)
            elif one.find("Microsoft Word - ")!=-1:
                (types[9]).append(txtFN)
            elif allz.find("STOCKHOLDER'S NAME OUTSTANDING & OUTSTANDING & TOTAL PERCENTAGE")!=-1:
                (types[10]).append(txtFN)
            elif allz.find("Rank Last Name First Name Middle Name Shares (Sum) Percentage")!=-1:
                (types[12]).append(txtFN)
            elif allz.find("Rank Name Holdings")!=-1:
                (types[14]).append(txtFN)
            elif allz.find("RANK STOCKHOLDER NAME OUTSTANDING SHARES PERCENTAGE TOTAL")!=-1:
                (types[13]).append(txtFN)
            elif allz.find("Name No. of Shares Percentage")!=-1:
                (types[15]).append(txtFN)
            elif re.search("RANK NAME(\s){1,3}TOTAL(\s){1,3}SHARES(\s){1,3}PERCENTAGE",allz):
                (types[16]).append(txtFN)
            elif allz.find("  RANK                  STOCKHOLDER NAME                   Common       TOTAL SHARES     % OF O/S")!=-1:
                (types[17]).append(txtFN)
            elif re.search("COUNT.+ACCOUNT.+REGISTRATION.+HOLDINGS",allz):
                (types[18]).append(txtFN)
            elif allz.find("NAME SHAREHOLDINGS RANK")!=-1:
                (types[19]).append(txtFN)
            elif re.search("1 of \d+\n\nBusiness",one+allz[:9]):
                (types[20]).append(txtFN)
            elif allz.find("Count Stockholder Name Number Of Shares Percentage")!=-1:
                (types[21]).append(txtFN)
            elif allz.find("SH NAME TOTAL NO. OF SHARES PERCENTAGE")!=-1: #No. of\n\nShares Amount of App. % to Total, STOCKHOLDER'S NAME OUTSTANDING & PERCENTAGE\nISSUED SHARES TO
                (types[22]).append(txtFN)
            elif re.search("Rank.+\n(-){90,}",allz):
                (types[23]).append(txtFN)
            elif allz.find("Business Date: September 30, 2020\nBPNAME HOLDINGS")!=-1:
                (types[11]).append(txtFN)
            else:
                notypes.append(txtFN)
            #elif all.find("STOCKHOLDER'S NAME SHARES")!=-1:
                #print("!"+txtFN)
            '''
            elif re.search("percentage",one+firstX(all,14),re.IGNORECASE):
                print("!!"+txtFN)
                (types[12]).append(txtFN)'''

    print(len(notypes)," files haven't be classified:(")
    return types

def main():
    with open("log_filtered.txt","r",encoding="utf-8") as f:
        paths = unpack(ast.literal_eval(f.read()))
    types = tagasala(paths)

    for w in types.keys():
        print(w,len(types[w]),types[w])

    with open('types.txt','w') as f:
        f.write(str(types))

if __name__=="__main__":
    main()
