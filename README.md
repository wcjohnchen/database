# Database Management for Polyadenylation Sites

<img src="flask/static/db.jpg" width="15%" height="15%">


## Table of Contents

I. Introduction

II. Schema

III. Column Description

IV. 

V.

VI. Acknowledgements

VII. References



## I. Introduction

PolyADB4-LR database stores information for a specific set of polyadenylation (polyA) sites found in human genome using 3’READS+ deep sequencing that were additionally supported by long read sequencing, and data generated from machine learning.  Present polyA sites were annotated via NCBI database and by IsoQuant-assigned long reads of ENCODE and GTEx.  This database contains 658,880 entries, 638,089 unique polyA sites, and 33,614 unique genes, and is based on ~2.3 billion 3’READS+ sequencing reads and ~600 million long reads.



## II. Schema
1. Data pre-processing and exploratory data analysis

    Extract and clean data, identify features in the dataset, plot distribution, and determine correlations.  The dataset is available at: https://www.kaggle.com/ted8080/house-prices-and-images-socal.


2. Modeling

    Regression.  Supervised learning models were implented using Sckit-Learn.  The data was split into 70% training and 30% test set.  The dependent variable was log transformed.  The predictor variables were standardized specifically for linear models.  Grid search with k-fold cross validation (k = 5) was performed to find the optimal hyperparameters.  MAE: mean absolute error; MSE: mean standard error; RMSE: root mean standard error.

    Classification.  A 2-D CNN model was implented using Tensorflow-Keras.  The architectural design of the neural network was shown on Table 2.  The housing prices were grouped into three categories: low (0 to 499,999), medium (500,000 to 999,999), and high (1,000,000 and above).  Training, validation, and test data consist of 10,832, 1,547, and 3,095 images respectively.

3. Technologies

    Python, Numpy, Pandas, Matplotlib, Seaborn, Sckit-Learn, Tensorflow, Keras, AWS EC2, Flask.


## III. Exploratory Data Analysis

The dataset contains 15,474 housing entries and corresponding images.  A list of features in the dataset includes:

1. Image ID (identifier)
2. Street (address)
3. City (address)
4. City code (identifier)
5. Bed (number of bedroom)
6. Bath (number of bathroom)
7. Square feet (number of square feet)
8. Price (housing price)


**Figure 1**.  Histograms of the housing dataset.

![](figure/histograms.png)


**Figure 2**.  Scatter plots of the housing dataset.

![](figure/scatterplots.png)


**Figure 3**.  Correlation matrix of the housing dataset.

![](figure/correlation_matrix.png)


## IV. Regression Models

Hyperparameter optimization:

Random forest: best parameters: {'max_depth': None, 'max_features': 'auto', 'min_samples_leaf': 1, 'n_estimators': 1550, 'oob_score': True}

Decision tree: best parameters: {'max_depth': 15, 'max_features': 'auto'}

Gradient boosting regression: best parameters: {'learning_rate': 0.01, 'max_depth': 10, 'max_features': 'auto', 'n_estimators': 4250, 'subsample': 0.15}

Ridge regression: best parameters: {'alpha': 0.0}

Lasso regression: best parameters: {'alpha': 0.001}



**Figure 4**.  Residual plots of the models.

![](figure/residual_rf.png)

![](figure/residual_dt.png)

![](figure/residual_gbr.png)

![](figure/residual_ridge.png)

![](figure/residual_lasso.png)


**Figure 5**.  Gradient boosting regression: training set: RMSE vs learing rate at specific estimators.

![](figure/train_rmse_lr.png)


**Figure 6**.  Gradient boosting regression: test set: RMSE vs learing rate at specific estimators.

![](figure/test_rmse_lr.png)


**Figure 7**.  Gradient boosting regression: permutation importances of the training set.

![](figure/permutation.png)


**Table 1**.  Overall training and test results.

![](figure/table.jpg)


## V. Image Classification

Model selection: 2-D CNN

Predict classes: high, medium, low price



**Figure 8**.  Representative housing Images.

![](figure/house_images.png)


**Table 2**.  CNN architecture.

![](figure/model_parameters.jpg)


Learning rate = 0.000001, optimizer = adam, epoch = 100 total

**Figure 9**.  Graph of accuracy (last 50 epochs).

![](figure/cnn_train_val_acc.jpg)

**Figure 10**.  Graph of loss function (last 50 epochs).

![](figure/cnn_train_val_loss.jpg)

Test accuracy = 0.5861, precision = 0.5305, recall = 0.6046

## VI. Acknowledgements




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

