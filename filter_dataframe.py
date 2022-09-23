# edit se transpose matrix to remove first line
mat = []
with open("RI_transpose_matrix.txt", "r") as ins:
    mat = ins.readlines()
ins.close()

main_in = []
with open("TypeSpecific_RI_SUMMARY_RMATs.txt", "r") as ins:
    main_in = ins.readlines()[1:]
ins.close()
name = {}
for line in main_in:
    line = line.strip()
    ele = line.split("\t")
    name[ele[3]] = ele[4]

outfile = open("RI_filtered_matrix.txt", 'w')
outfile2 = open("RI_ENSG_count.txt", 'w')

cell = mat[0].split("\t")
cell[-1] = cell[-1].strip()
exp = mat[1].split("\t")
exp[-1] = exp[-1].strip()
head = ''
for i in range(0,len(cell)):
    head = head + exp[i] + "(" + cell[i] + ")" + "\t"
head = "Gene_name" + "\t" + head + "\n"

outfile.write(head)
for line in mat[2:len(mat)]:
    line = line.strip()
    ele = line.split("\t")
    num = 0
    for each in ele[1:len(ele)]:
        if int(each) > 0:
            num += 1
    if num > 1:
        outfile.write(name[ele[0]] + "\t" + line + "\n")
        outfile2.write(name[ele[0]] + "\t" + str(num) + "\n")
