import os.path

fh = open("filenames.txt", "r")
out = open("All_AS_events_summary.txt", "w")
all_names = []

for line in fh:
    line = line.strip()
    all_names.append(line)

fh.close()
k = "MATS Report"
j = "Report Legend"
n = 0

for fn in all_names:
    fp = "/N/dc2/projects/MAMMALEXP/Felipe/lncRNA_KO/FASTQs/Correct_CCM/fastqs/RMAT_out/" + fn + "/summary.txt"
    if os.path.isfile(fp):
        tmp = open(fp, "r")
        out.write("#" + "\n" + fn + "\n")
        for line in tmp:
            if k in line:
                n = 1
            elif j in line:
                n = 0
            if n == 1:
                out.write(line)
    else:
        print (fp)
