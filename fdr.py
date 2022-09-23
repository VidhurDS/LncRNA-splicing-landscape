import pandas as pd
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import FloatVector

stats = importr('stats')

infile = "head_lnc_co_exp.txt"
df = pd.read_csv(infile, sep=' ', na_values='.')
print df[[3]]
#p_adjust = stats.p_adjust(FloatVector(pvalue_list), method = 'BH')


"""
infile = "sample_figure_input2.txt"
# infile = "sample_figure_input1.txt"
df = pd.read_csv(infile, sep='\t', na_values='.')
df = df.set_index('Tissue')
df.T.plot(kind='box', figsize=(12, 8))
plt.xticks(rotation='vertical')
fig = plt.gcf()
fig.subplots_adjust(bottom=0.4)

#plt.show()
plt.savefig('foo1.png')
"""