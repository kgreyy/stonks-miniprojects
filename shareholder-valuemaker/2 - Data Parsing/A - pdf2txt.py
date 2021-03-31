from tika import parser
import ast
from multiprocessing import Pool
import numpy

'''Data in .PDF disclosure files that are encoded as text are parsed as numerical data'''

def tagabasa(chunk):
    '''Starts a tika process for each core'''
    print("Process created.")
    x = 0
    for file_path in chunk:
        file = parser.from_file(file_path)
        with open(".".join(file_path.split(".")[:-1])+".txt","w+",encoding="utf-8") as f:
            if file["content"] is not None:
                out = file["content"].strip()
                print(out[:30])
                f.write(out)
            else:
                print("No content!")
            print("DONE!" + str(x))
        x+=1

def unpack(li):
    '''Transforms lists of lists into one-level form'''
    out = []
    for x in li:
        if isinstance(x, list):
            out.extend(unpack(x))
        else:
            out.append(x)
    return out

def main(cores):
    with open("log_filtered.txt","r",encoding="utf-8") as f:
        paths = unpack(ast.literal_eval(f.read()))
    print(paths)

    # Allows for async processing of files
    pool = Pool(cores)
    chunkedList = makeChunk(paths,cores)
    pool.map(tagabasa,chunkedList)
    pool.close()

def makeChunk(list, n):
    '''Divides data into the number of cores to utilize'''
    return numpy.array_split(list,n)

if __name__ == "__main__":
    cores = 8
    main(cores)
