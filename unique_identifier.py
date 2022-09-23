with open("RBP_binding_sites_ENCODE_CLIPdb.txt", "r") as ins2:
    f2 = ins2.readlines()  # ins2.readlines()[1:] if header
ins2.close()

outfile = open("stats_rbp_biding_sites.txt", 'w')

rbp_count = {}
cell_count = {}

print "Total binding sites: " + str(len(f2))
outfile.write("Total binding sites: " + str(len(f2)) + "\n")

for line in f2:
    line = line.strip()
    ele = line.split("\t")
    temp = ele[3].split("|")
    rbp = temp[0]
    cell_line = temp[1]
    if rbp in rbp_count:
        rbp_count[rbp] += 1
    else:
        rbp_count[rbp] = 1

    if cell_line in cell_count:
        cell_count[cell_line] += 1
    else:
        cell_count[cell_line] = 1

print "Total RBPs: " + str(len(rbp_count))
outfile.write("Total RBPs: " + str(len(rbp_count)) + "\n")
print "Total cell lines: " + str(len(cell_count))
outfile.write("Total cell lines: " + str(len(cell_count)) + "\n")
outfile.write("RBP\tnumber_of_binding_sites\n")

for key in rbp_count:
    outfile.write(key + "\t" + str(rbp_count[key]) + "\n")

outfile.write("\n\ncell_line\tnumber_of_binding_sites\n")

for key in cell_count:
    outfile.write(key + "\t" + str(cell_count[key]) + "\n")
