# Database Management for Polyadenylation Sites

<img src="flask/static/db.jpg" width="10%" height="10%">


## Table of Contents

I. Introduction

II. Schema

III. Column Description

IV. 

V.

VI. Acknowledgements

VII. References



## I. Introduction

P



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

## VI. Summary

This study performed several machine learning models to predict housing prices for regression and classification.  Gradient boosting regression outperforms all other models with the highest R2.  Present CNN model was built on a simple two convolutional layers.  A deeper network and further tuning of hyperparameters may be neccessary for future improvement.


## VII. Addendum

**Convolutional Neural Network**.  In the first CNN model, there was a clear overfitting of the training set.  The validation loss was higher than training loss, and steadily increasing.  To improve the model, more CNN layers were added; however, with slightly less trainable parameters.   Batch normalizaton layers were also added.  Furthermore, the optimizer was changed from adam to stochastic gradient descent (SGD) with nesterov (momentum=0.9, decay=1e-6).  The dropout rate was increased from 0.1 to 0.2.  The image size was reduced from (300, 300) to (256, 256).  The new CNN architecture was shown here: https://github.com/wcjohnchen/capstoneProject2/blob/main/data/cnn_architecture.txt.  It may also be useful to apply kernel regularizer (on weights) and/or activity regularizer (on layer output) to the convolutional layers or consider transfer learning strategies in order to achieve a higher accurary in the future implementation.


Learning rate = 0.00005, optimizer = SGD.

**Supplementary Figure 1**.  A plot of train vs validation accuracy.

![](figure/accuracy.jpg)



**Supplementary Figure 2**.  A plot of train vs validation loss.


![](figure/loss.jpg)


Train accuracy: 0.5744; precision: 0.5994; recall: 0.4619.

Test accuracy: 0.5492; precision: 0.5790; recall: 0.4465.


With the model fitted, the CNN model shows an accuracy of 54.9% for the test set for this image classification study.


**Random Forest, Gradient Boosting, and Extreme Gradient Boosting Classifiers**.  Random forest, gradient boosting, and XGBoost models for classification were also added.  Both gradient boosting and XGBoost models achieved high accurary of 84.2% on the test set.

Random forest classifier: best parameters: {'max_depth': None, 'max_features': 'auto', 'min_samples_leaf': 1, 'n_estimators': 300, 'oob_score': True}

Gradient boosting classifier:  best parameters: {'learning_rate': 0.05, 'max_depth': 5, 'max_features': 'auto', 'n_estimators': 4500, 'subsample': 0.15}

XGBoost: best parameters: best parameters: {'colsample_bytree': 0.9, 'gamma': 0.5, 'learning_rate': 0.1, 'max_depth': 7, 'min_child_weight': 1, 'n_estimators': 3500, 'subsample': 0.9}


**Supplementary Figure 3**.  A confusion matrix for gradient boosting classification.

![](figure/confusion_matrix.jpg)


**Supplementary Table 1**.  Overall training and test results for classification.

![](figure/summary_classification.jpg)


**Flask Application**.  Flask was implemented to integrate the gradient boosting classification model into the web application for housing prediction in Southern California.  User may input the name of city, number of bedroom, bathroom, and squared feet.  The output will display one of three following classes: low price (under 499,999), medium price (between 500,000 and 999,999), or high price (above 1,000,000).


**Supplementary Figure 4**.  A Flask application for maching learning.  The gradient boosting classification model was embedded.  (A) An input example that was classified as 'above 1,000,000', and (B) another example classified as 'under 499,999'.

A)

![](figure/flaskapp.jpg)


B)

![](figure/flaskapp2.jpg)
