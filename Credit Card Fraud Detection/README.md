## Problem Statement
We want to detect fraud transactions as many as possible, and at the same time, we want to reduce false negatives and false positives.
  - Any fraud transactions being misclassified as normal will be considered as false negatives. These will lead to fraud cost.
  - Any transactions (fraud and non-fraud) that are classified as fraud will be reviewed by the staff to check whether they are true fraud or not. Those true positives and false positives will lead to monitoring cost.

**BUSINESS METRICS** : Fraud cost (false negative) and monitoring cost (true positive and false positive)

## Attribute Information
- **Time** : Number of seconds elapsed between this transaction and the first transaction
- **V1 - V28** : Unknown variables (may be result of a PCA Dimensionality reduction to protect user identities and sensitive features)
- **Amount** : Amount of transactions
- **Class**	: 1 (Fraud) and 0 (non-Fraud)

## Dataset
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Time</th>
      <th>V1</th>
      <th>V2</th>
      <th>V3</th>
      <th>V4</th>
      <th>V5</th>
      <th>V6</th>
      <th>V7</th>
      <th>V8</th>
      <th>V9</th>
      <th>V10</th>
      <th>V11</th>
      <th>V12</th>
      <th>V13</th>
      <th>V14</th>
      <th>V15</th>
      <th>V16</th>
      <th>V17</th>
      <th>V18</th>
      <th>V19</th>
      <th>V20</th>
      <th>V21</th>
      <th>V22</th>
      <th>V23</th>
      <th>V24</th>
      <th>V25</th>
      <th>V26</th>
      <th>V27</th>
      <th>V28</th>
      <th>Amount</th>
      <th>Class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>-1.359807</td>
      <td>-0.072781</td>
      <td>2.536347</td>
      <td>1.378155</td>
      <td>-0.338321</td>
      <td>0.462388</td>
      <td>0.239599</td>
      <td>0.098698</td>
      <td>0.363787</td>
      <td>0.090794</td>
      <td>-0.551600</td>
      <td>-0.617801</td>
      <td>-0.991390</td>
      <td>-0.311169</td>
      <td>1.468177</td>
      <td>-0.470401</td>
      <td>0.207971</td>
      <td>0.025791</td>
      <td>0.403993</td>
      <td>0.251412</td>
      <td>-0.018307</td>
      <td>0.277838</td>
      <td>-0.110474</td>
      <td>0.066928</td>
      <td>0.128539</td>
      <td>-0.189115</td>
      <td>0.133558</td>
      <td>-0.021053</td>
      <td>149.62</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>1.191857</td>
      <td>0.266151</td>
      <td>0.166480</td>
      <td>0.448154</td>
      <td>0.060018</td>
      <td>-0.082361</td>
      <td>-0.078803</td>
      <td>0.085102</td>
      <td>-0.255425</td>
      <td>-0.166974</td>
      <td>1.612727</td>
      <td>1.065235</td>
      <td>0.489095</td>
      <td>-0.143772</td>
      <td>0.635558</td>
      <td>0.463917</td>
      <td>-0.114805</td>
      <td>-0.183361</td>
      <td>-0.145783</td>
      <td>-0.069083</td>
      <td>-0.225775</td>
      <td>-0.638672</td>
      <td>0.101288</td>
      <td>-0.339846</td>
      <td>0.167170</td>
      <td>0.125895</td>
      <td>-0.008983</td>
      <td>0.014724</td>
      <td>2.69</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>-1.358354</td>
      <td>-1.340163</td>
      <td>1.773209</td>
      <td>0.379780</td>
      <td>-0.503198</td>
      <td>1.800499</td>
      <td>0.791461</td>
      <td>0.247676</td>
      <td>-1.514654</td>
      <td>0.207643</td>
      <td>0.624501</td>
      <td>0.066084</td>
      <td>0.717293</td>
      <td>-0.165946</td>
      <td>2.345865</td>
      <td>-2.890083</td>
      <td>1.109969</td>
      <td>-0.121359</td>
      <td>-2.261857</td>
      <td>0.524980</td>
      <td>0.247998</td>
      <td>0.771679</td>
      <td>0.909412</td>
      <td>-0.689281</td>
      <td>-0.327642</td>
      <td>-0.139097</td>
      <td>-0.055353</td>
      <td>-0.059752</td>
      <td>378.66</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>-0.966272</td>
      <td>-0.185226</td>
      <td>1.792993</td>
      <td>-0.863291</td>
      <td>-0.010309</td>
      <td>1.247203</td>
      <td>0.237609</td>
      <td>0.377436</td>
      <td>-1.387024</td>
      <td>-0.054952</td>
      <td>-0.226487</td>
      <td>0.178228</td>
      <td>0.507757</td>
      <td>-0.287924</td>
      <td>-0.631418</td>
      <td>-1.059647</td>
      <td>-0.684093</td>
      <td>1.965775</td>
      <td>-1.232622</td>
      <td>-0.208038</td>
      <td>-0.108300</td>
      <td>0.005274</td>
      <td>-0.190321</td>
      <td>-1.175575</td>
      <td>0.647376</td>
      <td>-0.221929</td>
      <td>0.062723</td>
      <td>0.061458</td>
      <td>123.50</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.0</td>
      <td>-1.158233</td>
      <td>0.877737</td>
      <td>1.548718</td>
      <td>0.403034</td>
      <td>-0.407193</td>
      <td>0.095921</td>
      <td>0.592941</td>
      <td>-0.270533</td>
      <td>0.817739</td>
      <td>0.753074</td>
      <td>-0.822843</td>
      <td>0.538196</td>
      <td>1.345852</td>
      <td>-1.119670</td>
      <td>0.175121</td>
      <td>-0.451449</td>
      <td>-0.237033</td>
      <td>-0.038195</td>
      <td>0.803487</td>
      <td>0.408542</td>
      <td>-0.009431</td>
      <td>0.798278</td>
      <td>-0.137458</td>
      <td>0.141267</td>
      <td>-0.206010</td>
      <td>0.502292</td>
      <td>0.219422</td>
      <td>0.215153</td>
      <td>69.99</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

## Distribution of the amount of fraud transactions
<p align="center">
  <img src="output_0_2.png" />
</p>

This dataset is heavily imbalanced. Only 0.2 % were fraud transactions. The average amount of fraud transactions (fraud cost) is RM 122.21. Assuming the salary of financial staff in Malaysia is RM 6780 and one transaction takes 5 minutes to be checked and one person works for 40 hours per week for 4 weeks, the monitoring cost is RM 3.53 per transaction.
> 5 minutes = 1 transaction

> 1 hour = 12 transactions

> 4 x 40 hours = 1920 transactions

> RM 6780 / 1920 transactions = RM 3.53 per transaction

## Results
Six different models were built. The models were evaluated using 5-folds cross-validation. Random Forest achieved the lowest _Cost (RM)_, followed by K-Nearest Neighbors and so on. Notice that the higher the F1-score, the lower the cost. But the problem with Random Forest and K-Nearest Neighbors is they took a long time to train.
  - Random Forest took 17.6 minutes to train for 5-folds.
  - K-Nearest Neighbors took 1 hour 48 minutes to train for 5-folds.
  - Decision Tree only took 1.6 minutes to train for 5-folds.

Random Forest will be used as baseline model, and we will tune the hyperparameters of Decision Tree and implement threshold analysis to beat the baseline score. Fraud cost costs higher compare to monitoring cost. So, to get a higher F1-score, recall score must never decrease. It either stays the same or increases. Recall score of our baseline is crucial here.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>False positive</th>
      <th>False negative</th>
      <th>True positive</th>
      <th>Recall</th>
      <th>Precision</th>
      <th>F1-score</th>
      <th>Cost (RM)</th>
      <th>Time to compute (seconds)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Random Forest</th>
      <td>5.4</td>
      <td>21.4</td>
      <td>77.0</td>
      <td>0.782560</td>
      <td>0.935981</td>
      <td>0.851794</td>
      <td>2906.27</td>
      <td>1057.5</td>
    </tr>
    <tr>
      <th>K-Nearest Neighbors</th>
      <td>6.8</td>
      <td>21.8</td>
      <td>76.6</td>
      <td>0.778437</td>
      <td>0.91871</td>
      <td>0.842548</td>
      <td>2958.68</td>
      <td>6494.0</td>
    </tr>
    <tr>
      <th>Decision Tree</th>
      <td>22.0</td>
      <td>22.8</td>
      <td>75.6</td>
      <td>0.768275</td>
      <td>0.776378</td>
      <td>0.771336</td>
      <td>3131.04</td>
      <td>96.0</td>
    </tr>
    <tr>
      <th>Support Vector Machines</th>
      <td>4.0</td>
      <td>34.6</td>
      <td>63.8</td>
      <td>0.648341</td>
      <td>0.943000</td>
      <td>0.767628</td>
      <td>4467.88</td>
      <td>2334.9</td>
    </tr>
    <tr>
      <th>Logistic Regression</th>
      <td>9.2</td>
      <td>37.8</td>
      <td>60.6</td>
      <td>0.615997</td>
      <td>0.870195</td>
      <td>0.717379</td>
      <td>4866.02</td>
      <td>13.8</td>
    </tr>
    <tr>
      <th>Naive Bayes</th>
      <td>1246.2</td>
      <td>16.8</td>
      <td>81.6</td>
      <td>0.829272</td>
      <td>0.061520</td>
      <td>0.114525</td>
      <td>6741.92</td>
      <td>3.9</td>
    </tr>
  </tbody>
</table>
</div>

## Hyperparamter Tuning
These are the best hyperparameters for Decision Tree.
> param_grid = {'max_leaf_nodes': 15, 'min_samples_leaf': 1e05, 'min_impurity_decrease': 8}

By choosing 0.375 as threshold, and limiting our recall score to be not lower than our baseline's recall score, F1-score increases to 82 %. Because of the recall score increases a bit, we managed to beat the baseline score.

The key takeaway here is even though the percentage difference of _Cost (RM)_ of our tuned Decision Tree and baseline is not even 1 %, we still managed to decrease training time (training cost) by 99.5 %.
