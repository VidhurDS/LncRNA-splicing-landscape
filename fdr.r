raw <- read.csv("raw_pval_hela.txt", header=TRUE,sep="\t")
out_mat = as.matrix(raw)

for (i in 1:nrow(raw)){
  x=raw[i,]
  FDR <- p.adjust(x[1,2:length(x)], method= "fdr")
  out_mat[i,2:length(x)] = FDR
}

write.table(out_mat,"hela_pval_FDR.txt", col.names = TRUE, row.names = FALSE, sep="\t",quote=F )

#### k562

raw <- read.csv("raw_pval_k562.txt", header=TRUE,sep="\t")
out_mat = as.matrix(raw)

for (i in 1:nrow(raw)){
  x=raw[i,]
  FDR <- p.adjust(x[1,2:length(x)], method= "fdr")
  out_mat[i,2:length(x)] = FDR
}

write.table(out_mat,"k562_pval_FDR.txt", col.names = TRUE, row.names = FALSE, sep="\t",quote=F )
