import csv

file = "ghostys.csv"
file1 = open('ghostys.csv')
csv_f = csv.reader(file1)

ghosts = []
inputm = []
subs = []
#subs2 = []
#line_count = 0
final = []
#iter = 1

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

'''def drop_lowest(sequence):
    for n in sequence:
        final.append(list.remove((min(n))))'''

#length = file_len(file)

for row in csv_f:
    ghosts.append(row)
    inputm.append(row)

for g in ghosts[1:]:
    for i in inputm[1:]:
        while g[0] == i[0]:
            subs.append(i)
            next
        else:
            break
            #i.pop(min(i[1])
            #final.append(i)

print(subs)
#print(inputm[1][0:])
#print("line break")
#print(inputm)

'''with open('output.csv', 'w') as outFile1:
    for i in ghosts[1:]:
        subs.append(i)
        if i[0] == iter and iter < length:
            print(i)
            subs2.append(subs)
            iter += 1
            final.append(min(subs, key=lambda x: x[1]))
        #final.append(list.pop(min(i)))
        #while i == i[1:]:
            #print(i[0])
        #for m in inputm:
            #print(m)
            while line_count <= length:
                while i[1:7] == i[1:7]:
                    subs.append(i)
                    line_count += 1
                    subs.remove(min(subs))
                    final.append(subs)
                    subs.clear()
                    continue
                else:
                    break
            else:
                break
for i in ghosts:
    for m in inputm:
        while i[1:][0] == m[1:][0]:
            subs.append(i)
            continue
            while line_count <= length:
            while i[0] == m[0]:
               ###print("line count is ", line_count)
               subs.append(ghosts)
               line_count += 1
        else:
           break
print(i)'''
