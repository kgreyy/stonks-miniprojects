import ast
import re
import pandas as pd

def swapLastFirst(name):
    '''Swaps first and last name as needed, todo: handle edgecases in the next line'''
    if name.find(",")==-1 or re.search('\&\/OR|INC| JR\.\S| II\.?\S| III\.?\S| IV\.\S| V\.?\S|TRUSTEES| SR\.?\S|CO\.\S',name) is not None:
        return name
    arr = name.split(', ')
    w = re.search(" OR | AND | AKA ",name)
    if len(arr)<3:
        print('corrected')
        return ' '.join(arr[::-1])
    elif w is not None and len(arr)==3:
        mga = name.split(w.group())
        print(w.group())
        res = []
        for x in mga:
            res.append(swapLastFirst(x))
        return ' '.join(res)
    else:
        print('WTF '+name)
        return name

def parsenga(path):
    '''Parses types 1 and 2 into interpretable ownership data: number of shares'''
    res = {}
    parse = lambda x: re.finditer(" +(1?[0-9]?[0-9])   (.+)\s+(\d\S+)\s+(\S+%)",x)
    with open(path,"r") as f:
        ob = f.read()
        data = parse(ob)
        #check = [x.group(1) for x in data]
        name = re.finditer(" +(.+)\n{1,2} +List of Top 100 Stockholders",ob)
        ooo = list(set([x.group(1) for x in name]))
        if len(ooo)==0:
            print(path)
        print(ooo)
    '''
    for checking if the number of entries is valid - maintenance
    leng = len(check)
    iden = min(leng+1,101)

    for x in range(1,iden):
        if str(x) not in check:
            print(path)
            print("error")
            break
    '''
    y = 0
    res[ooo[y]] = {}
    for x in data:
        if x.group(1) in res[ooo[y]]:
            y+=1
            res[ooo[y]] = {}
        res[ooo[y]][swapLastFirst(x.group(2).rstrip())] = x.group(3)# other obtainable data: ,x.group(4) # key = name, data = (shares, %owned)
    return res

def type10(path):
    '''Parses type 10 into interpretable ownership data: number of shares'''
    res = {}
    print(path)
    with open(path,"r") as f:
        ob = f.read()
        data = re.finditer("(\d{1,3} )?(.+) +(\d{1,3}(?:,\d{3})*) +(\d{1,3}(?:,\d{3})*) +(\d{1,3}(?:,\d{3})*) (\d{1,2}(?:\.\d*)?)",ob)
        #check = [x.group(1) for x in data]
        name = re.search("COMPANY NAME ?: *(.+)",ob)
        if name is None:
            ooo = path.split('/')[1]
        else:
            ooo = name.group(1)

    res[ooo] = {}
    for x in data:
        res[ooo][swapLastFirst(x.group(2).rstrip())] = x.group(5)#,x.group(5))
    return res
'''
WIP function!
def type16(path):
    with open(path,"r") as f:
        ob = f.read()
        print(path)
        print(re.search("RANK NAME TOTAL SHARES\nPERCENTAGE",ob))

        # dulo = re.search("End ?\n*of ?\n*Report|THIS IS A COMPUTER GENERATED REPORT AND IF ISSUED WITHOUT ALTERATION, DOES NOT REQUIRE ANY SIGNATURE\.|the report \(SEC Form 23B\) submitted to SEC and PSE\.",ob,flags=re.I).span()[0]
        # data = re.finditer("(\d{1,3})? *\n* *(\D+) *\n* *(\d{1,3}(?:,\d{3})*) *\n* *(\d{1,2}(?:\.\d*))",ob[:dulo])
        # print(len(list(data)))
'''
def dict2df(dict, name):
     return pd.DataFrame.from_dict(dict,orient='index',columns=[name]).head(10)

if __name__=="__main__":
    with open("types.txt","r",encoding="utf-8") as f:
        paths = ast.literal_eval(f.read())

    cur = {}
    # NOTE: Requires lots of data cleaning and review!!!
    for x in range(len(paths[1])):
            cur = {**cur,**parsenga(paths[1][x])}
    for x in range(len(paths[10])):
            cur = {**cur,**type10(paths[10][x])}
    out = pd.DataFrame()
    for entry in cur.keys():
        out = out.merge(dict2df(cur[entry], entry),left_index=True,right_index=True,how='outer')
    print(out.head(100))
    out = out.drop('A 2 0 0 1 1', axis=0) # false match
    out.to_csv("ownership_data.csv")


for x in range(1,20):
    print(x,len(paths[x]))
