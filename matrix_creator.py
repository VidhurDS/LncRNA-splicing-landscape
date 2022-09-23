#eve = "SE"
eve = "RI"
#cell_line = "hela"
#cell_line = "u87"
cell_line = "k562"
file1 = "cell_line_based/" + cell_line + "_" + eve + "_heatmap_input.txt"
f1 = []
with open(file1, "r") as ins:
    f1 = ins.readlines()    # ins.readlines()[1:] if header
ins.close()

ofn = "cell_line_based/" + cell_line + "_" + eve + "_matrix.txt"
outfile = open(ofn, 'w')

ensg = []
exp = []
val = {}

for line in f1:
    line = line.strip()
    elements = line.split("\t")
    val[elements[0]] = elements[1]
    arr = elements[0].split(",")
    exp.append(arr[0])
    ensg.append(arr[1])

uexp = set(exp)
uensg = set(ensg)

head = "\t".join(uensg)
outfile.write(head + "\n")
for id_exp in uexp:
    outfile.write(id_exp)
    for gene in uensg:
        kstr = id_exp + "," + gene
        if kstr in val:
            outfile.write("\t" + str(val[kstr]))
        else:
            outfile.write("\t" + str(0))
    outfile.write("\n")
