#file1 = "TypeSpecific_SE_SUMMARY_RMATs.txt"
file1 = "TypeSpecific_RI_SUMMARY_RMATs.txt"
f1 = []
with open(file1, "r") as ins:
    f1 = ins.readlines()    # ins.readlines()[1:] if header
ins.close()

#ofn = "SE_heatmap_input.txt"
ofn = "RI_heatmap_input.txt"
outfile1 = open("cell_line_based/u87_" + ofn, 'w')
outfile2 = open("cell_line_based/k562_" + ofn, 'w')
outfile3 = open("cell_line_based/hela_" + ofn, 'w')

u87 = {}
k562 = {}
hela = {}
name = {}


for line in f1:
    line = line.strip()
    elements = line.split("\t")
    kstr = elements[0] + "," + elements[3]
    if elements[1] == "u87":
        if kstr in u87:
            u87[kstr] += 1
        else:
            u87[kstr] = 1
    elif elements[1] == "k562":
        if kstr in k562:
            k562[kstr] += 1
        else:
            k562[kstr] = 1
    elif elements[1] == "hela":
        if kstr in hela:
            hela[kstr] += 1
        else:
            hela[kstr] = 1


for key in u87:
    outfile1.write(key + "\t" + str(u87[key])+"\n")

for key in k562:
    outfile2.write(key + "\t" + str(k562[key])+"\n")

for key in hela:
    outfile3.write(key + "\t" + str(hela[key])+"\n")
