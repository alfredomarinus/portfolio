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

## Cross Validation
Five different models were built. The models were evaluated using 5-folds cross-validation. Random Forest achieved the lowest _Cost (RM)_, followed by Decision Tree and so on. Notice that the higher the F1-score, the lower the cost.

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
      <td>3.4</td>
      <td>14.2</td>
      <td>51.6</td>
      <td>0.784289</td>
      <td>0.938401</td>
      <td>0.853864</td>
      <td>1929.60</td>
      <td>599.6</td>
    </tr>
    <tr>
      <th>Decision Tree</th>
      <td>17.2</td>
      <td>16.8</td>
      <td>49.0</td>
      <td>0.744895</td>
      <td>0.748099</td>
      <td>0.744129</td>
      <td>2286.90</td>
      <td>57.9</td>
    </tr>
    <tr>
      <th>Support Vector Machines</th>
      <td>2.4</td>
      <td>23.4</td>
      <td>42.4</td>
      <td>0.644336</td>
      <td>0.946674</td>
      <td>0.765423</td>
      <td>3017.91</td>
      <td>1077.0</td>
    </tr>
    <tr>
      <th>Logistic Regression</th>
      <td>6.2</td>
      <td>25.0</td>
      <td>40.8</td>
      <td>0.620326</td>
      <td>0.867202</td>
      <td>0.721762</td>
      <td>3221.22</td>
      <td>8.6</td>
    </tr>
    <tr>
      <th>Naive Bayes</th>
      <td>891.6</td>
      <td>10.4</td>
      <td>55.4</td>
      <td>0.842005</td>
      <td>0.058520</td>
      <td>0.109428</td>
      <td>4615.08</td>
      <td>2.4</td>
    </tr>
  </tbody>
</table>
</div>

We will be using Random Forest for model development because it has good score. Fraud cost costs higher compare to monitoring cost. So, recall score must never decrease. It either stays the same or increases.

## Model development
We will implement threshold analysis to this model. With normal threshold (0.5), the model achieved 82 % F1-score with RM 5822.18 total loss.
With optimal threshold (0.33), the model F1-score only increased by 4 %. The good thing is the total loss was decreased to RM 4523.77, in percentage, 22 %.
