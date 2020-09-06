import glob

def sortFileContent(filename):
    file_handle = open(filename, "r")
    words = []
    for line in file_handle:
        words += line.split()
    file_handle.close()
    sortedList = sorted(words)
    outfile = open(filename, "w")
    outfile.write("\n".join(sortedList))
    return sortedList

# data
data = {}

# force sort entry in file
for file in glob.glob("*.txt"):
    print("Processing "+ file)
    data[file] = sortFileContent(file)

# keep in stocks diffs from etf and spac
cleaned = list(set(data["stocks.txt"]) - set(data["etf.txt"]) - set(data["spac.txt"]))

outfile = open("cleaned.txt", "w")
outfile.write("\n".join(cleaned))
sortFileContent("cleaned.txt")