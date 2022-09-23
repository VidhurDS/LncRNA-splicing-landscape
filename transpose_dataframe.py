import pandas as pd

raw_mat = pd.read_csv("RI_merged_matrix.txt", sep = "\t")

raw_mat = raw_mat.T
raw_mat.to_csv("RI_transpose_matrix.txt", sep="\t")

"""
rm2 = raw_mat

for i in range(0,raw_mat.shape[0]):
    len_arr = raw_mat.iloc[raw_mat.iloc[i,].nonzero()]
    if len(len_arr) > 1:
"""
