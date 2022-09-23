
ofn = "RI_matrix.txt"
u87_in = []
with open("u87_" + ofn, 'r') as ins:
    u87_in = ins.readlines()
ins.close()

hela_in = []
with open("hela_" + ofn, 'r') as ins:
    hela_in = ins.readlines()
ins.close()

k562_in = []
with open("k562_" + ofn, 'r') as ins:
    k562_in = ins.readlines()
ins.close()

outfile = open("RI_merged_matrix.txt", 'w')

u87 = {}
k562 = {}
hela = {}

u87_ensg = u87_in[0].split("\t")
k562_ensg = k562_in[0].split("\t")
hela_ensg = hela_in[0].split("\t")
u87_ensg.pop(0)
k562_ensg.pop(0)
hela_ensg.pop(0)
u87_ensg[-1] = u87_ensg[-1].strip()
k562_ensg[-1] = k562_ensg[-1].strip()
hela_ensg[-1] = hela_ensg[-1].strip()
u87_exp = []
k562_exp = []
hela_exp = []

for line in u87_in[1:len(u87_in)]:
    line = line.strip()
    ele = line.split("\t")
    exp = ele[0]
    u87_exp.append(exp)
    for i in range(0 ,len(u87_ensg)):
        kstr = exp + "_" + u87_ensg[i]
        u87[kstr] = ele[i+1]

for line in k562_in[1:len(k562_in)]:
    line = line.strip()
    ele = line.split("\t")
    exp = ele[0]
    k562_exp.append(exp)
    for i in range(0 ,len(k562_ensg)):
        kstr = exp + "_" + k562_ensg[i]
        k562[kstr] = ele[i+1]

for line in hela_in[1:len(hela_in)]:
    line = line.strip()
    ele = line.split("\t")
    exp = ele[0]
    hela_exp.append(exp)
    for i in range(0 ,len(hela_ensg)):
        kstr = exp + "_" + hela_ensg[i]
        hela[kstr] = ele[i+1]


all_ensg = u87_ensg + k562_ensg + hela_ensg
all_ensg = set(all_ensg)
all_exp = u87_exp + k562_exp + hela_exp
all_exp = set(all_exp)
head = "\t".join(all_ensg)
outfile.write("Cell_line\tExperiment\t" + head + "\n")

for exp in all_exp:
    outfile.write("u87\t" + exp)
    for gene in all_ensg:
        kstr = exp + "_" + gene
        if kstr in u87:
            outfile.write("\t" + u87[kstr])
        else:
            outfile.write("\t0")
    outfile.write("\n")

for exp in all_exp:
    outfile.write("k562\t" + exp)
    for gene in all_ensg:
        kstr = exp + "_" + gene
        if kstr in k562:
            outfile.write("\t" + k562[kstr])
        else:
            outfile.write("\t0")
    outfile.write("\n")

for exp in all_exp:
    outfile.write("hela\t" + exp)
    for gene in all_ensg:
        kstr = exp + "_" + gene
        if kstr in hela:
            outfile.write("\t" + hela[kstr])
        else:
            outfile.write("\t0")
    outfile.write("\n")
