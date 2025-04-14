# Database Management for Polyadenylation Sites

<br>

<img src="flask/static/db.jpg" width="12.5%" height="12.5%">

<br>

## Table of Contents

I. Introduction

II. Schema

III. Column Description

IV. 

V.

VI. Acknowledgements

VII. References

XI. Technologies

<br>

## I. Introduction

PolyADB4-LR database (v4.01-LR) stores information for an extended set of polyadenylation (polyA) sites found in human genome using 3’READS+ deep sequencing.  The polyA sites were additionally supported by long read sequencing and data generated from machine learning, and annotated via NCBI database and by IsoQuant-assigned long reads of ENCODE and GTEx.  This database contains 658,880 entries, 638,089 unique polyA sites, and 33,614 unique genes, and is based on ~2.3 billion 3’READS+ sequencing reads and ~600 million long reads.


<br>

## II. Schema





**Figure 1**.  Histograms of the housing dataset.

![](figure/histograms.png)




## IV. Regression Models

Hyperparameter optimization:

Random forest: best parameters: {'max_depth': None, 'max_features': 'auto', 'min_samples_leaf': 1, 'n_estimators': 1550, 'oob_score': True}

Decision tree: best parameters: {'max_depth': 15, 'max_features': 'auto'}

Gradient boosting regression: best parameters: {'learning_rate': 0.01, 'max_depth': 10, 'max_features': 'auto', 'n_estimators': 4250, 'subsample': 0.15}

Ridge regression: best parameters: {'alpha': 0.0}

Lasso regression: best parameters: {'alpha': 0.001}


| Column | Description |
| ------ | ---- |
|Key |number of long-read transcription end sites (from the GTEx V9 ONT cDNA dataset) that were matched to the polyA site location. polyAID: classification probability for putative polyA site within a sequence expected to occur (https://github.com/zhejilab/PolyaModelsHuman). |
|Gene Symbol |chr2 |
|PasID |
|Type |
|PSE |
|AvgRPM |



**Figure 5**.  Gradient boosting regression: training set: RMSE vs learing rate at specific estimators.

![](figure/train_rmse_lr.png)


**Figure 6**.  Gradient boosting regression: test set: RMSE vs learing rate at specific estimators.

![](figure/test_rmse_lr.png)


<br>

## VI. Acknowledgements

I would like to express gratitude to Dr. Bin Tian’s lab for data availability and contribution.

<br>

## VII. Reference

Cheng Y, Miura RM, and Tian B.  2006.  Prediction of mRNA polyadenylation sites by support vector machine.  Bioinformatics, 22(19):2320-5.  doi: 10.1093/bioinformatics/btl394.

Glinos DA, Garborcauskas G, Hoffman P, Ehsan N, Jiang L, Gokden A, Dai X, Aguet F, Brown KL, Garimella K, Bowers T, Costello M, Ardlie K, Jian R, Tucker NR, Ellinor PT, Harrington ED, Tang H, Snyder M, Juul S, Mohammadi P, MacArthur DG, Lappalainen T, and Cummings BB.  2022.  Transcriptome variation in human tissues revealed by long-read sequencing.  Nature, 608(7922):353-359.  doi: 10.1038/s41586-022-05035-y.

Hoque M, Ji Z, Zheng D, Lou W, Li W, You B, Park JY, Yehia G, and Tian B.  2013.  Analysis of alternative cleavage and polyadenylation by 3' region extraction and deep sequencing.  Nat Methods, 10(2):133-9.  doi: 10.1038/nmeth.2288.

Lee JY, Yeh I, Park JY, and Tian B.  2007.  PolyA_DB 2: mRNA polyadenylation sites in vertebrate genes.  Nucleic Acids Res, 35:D165-8.  doi: 10.1093/nar/gkl870.

Reese F, Williams B, Balderrama-Gutierrez G, Wyman D, Çelik MH, Rebboah E, Rezaie N, Trout D, Razavi-Mohseni M, Jiang Y, Borsari B, Morabito S, Liang HY, McGill CJ, Rahmanian S, Sakr J, Jiang S, Zeng W, Carvalho K, Weimer AK, Dionne LA, McShane A, Bedi K, Elhajjajy SI, Upchurch S, Jou J, Youngworth I, Gabdank I, Sud P, Jolanki O, Strattan JS, Kagda MS, Snyder MP, Hitz BC, Moore JE, Weng Z, Bennett D, Reinholdt L, Ljungman M, Beer MA, Gerstein MB, Pachter L, Guigó R, Wold BJ, and Mortazavi A.  2023.  The ENCODE4 long-read RNA-seq collection reveals distinct classes of transcript structure diversity.  bioRxiv.  doi: 10.1101/2023.05.15.540865.

Stroup EK, and Ji Z. 2023. Deep learning of human polyadenylation sites at nucleotide resolution reveals molecular determinants of site usage and relevance in disease. Nature Commun, 14(1):7378:1-17.  doi: 10.1038/s41467-023-43266-3.

Wang R, Nambiar R, Zheng D, and Tian B.  2017.  PolyA_DB 3 catalogs cleavage and polyadenylation sites identified by deep sequencing in multiple genomes.  Nucleic Acids Res, 46(D1):D315-D319.  doi: 10.1093/nar/gkx1000.

Zhang H, Hu J, Recce M, and Tian B.  2005.  PolyA_DB: a database for mammalian mRNA polyadenylation.  Nucleic Acids Res, 33:D116-20.  doi: 10.1093/nar/gki055.

Zheng D, Liu X, and Tian B.  2016.  3'READS+, a sensitive and accurate method for 3' end sequencing of polyadenylated RNA.  RNA, 22(10):1631-9.  doi: 10.1261/rna.057075.116.

<br>

## XI. Technologies

Database, PostgreSQL, SQL, pgAdmin4, Jupyter Notebook, Python, Git, Linux, Machine Learning, Deep Learning

