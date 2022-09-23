with open("/N/dc2/projects/MAMMALEXP/Felipe/genedalph/CLIP-LNC_ENST_ENCODE-CLIPdb_network_2018_02_08.txt", "r") as ins2:
#with open("sample_clip_file.bed", "r") as ins2:
    f2 = ins2.readlines()  # ins2.readlines()[1:] if header
ins2.close()

ofn = "RBP_binding_sites_ENCODE_CLIPdb.txt"
outfile = open(ofn, 'w')


def sorter(x, y):
    x = int(x)
    y = int(y)
    if x > y:
        mx = x
        mn = y
    elif y >= x:
        mx = y
        mn = x
    ostr = str(mn) + "\t" + str(mx)
    return ostr

site_arr = []

for line in f2:
    line = line.strip()
    ele = line.split(" ")
    coord = sorter(ele[1], ele[2])
    rbp = ele[3] + "|" + ele[4]
    oa = ele[0] + "\t" + coord + "\t" + rbp
    site_arr.append(oa)

site_arr = set(site_arr)

for each in site_arr:
    outfile.write(each + "\n")
