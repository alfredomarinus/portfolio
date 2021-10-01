## Problem Statement
We want to reduce misclassification of fraud and normal transactions.
  - Any fraud transactions being misclassified as normal is considered as false negatives. We will lose money.
  - Any normal transactions being misclassified as fraud is considered as false positives. Customer might stop using our products/services and move to other platforms.

**BUSINESS METRIC** : Money loss (fraud cost) - calculated using false negative (measured by recall)  
**ADDITIONAL METRIC** : Customer churn - calculated using false positive (measured by precision)  
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\mathrm{F1-score=2*\frac{Precision&space;*&space;Recall}{Precision&space;&plus;&space;Recall}}" title="\mathrm{F1-score=2*\frac{Precision * Recall}{Precision + Recall}}" />
</p>


## Attribute Information
- **Time** : Number of seconds elapsed between this transaction and the first transaction
- **V1 - V28** : Unknown variables (may be result of a PCA Dimensionality reduction to protect user identities and sensitive features)
- **Amount** : Amount of transactions
- **Class**	: 1 (Fraud) and 0 (non-Fraud) 


**NUMBER OF ROWS**: 284,807

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
  <img src="images/image-1.png" />
</p>

This dataset is imbalanced. Only 0.2 % are fraud transactions. The average amount of fraud transactions (fraud cost) is RM 122.21. Since the amount of fraud transactions is heavily skewed, we will be using median instead, which is RM 9.25.

## Cross-validation
This dataset is separated into training set (70 %) and test set (30 %). Training set is used for model development while test set is used for model evaluation.  

We will be using 5-fold cross-validation to estimate the performance of six different machine learning models on unseen data. Random Forest achieved the highest F1-score, followed by K-Nearest Neighbors and so on. Naive Bayes has the least money loss, but it could not compensate with its high number of false positive. More customers have high tendency to stop using our products/services. This can affect our customer life value (CLV).

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>False positive</th>
      <th>False negative</th>
      <th>Recall</th>
      <th>Precision</th>
      <th>F1-score</th>
      <th>Money loss (RM)</th>
      <th>Time to compute (seconds)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Random Forest</th>
      <td>3</td>
      <td>14</td>
      <td>0.784336</td>
      <td>0.945763</td>
      <td>0.856868</td>
      <td>129.50</td>
      <td>623.8</td>
    </tr>
    <tr>
      <th>K-Nearest Neighbors</th>
      <td>5</td>
      <td>15</td>
      <td>0.769091</td>
      <td>0.919808</td>
      <td>0.836921</td>
      <td>138.75</td>
      <td>2062.5</td>
    </tr>
    <tr>
      <th>Support Vector Machines</th>
      <td>2</td>
      <td>23</td>
      <td>0.644336</td>
      <td>0.946674</td>
      <td>0.765423</td>
      <td>212.75</td>
      <td>1126.9</td>
    </tr>
    <tr>
      <th>Decision Tree</th>
      <td>18</td>
      <td>17</td>
      <td>0.735758</td>
      <td>0.731769</td>
      <td>0.732916</td>
      <td>157.25</td>
      <td>59.7</td>
    </tr>
    <tr>
      <th>Logistic Regression</th>
      <td>6</td>
      <td>25</td>
      <td>0.620326</td>
      <td>0.867202</td>
      <td>0.721762</td>
      <td>231.25</td>
      <td>11.8</td>
    </tr>
    <tr>
      <th>Naive Bayes</th>
      <td>892</td>
      <td>10</td>
      <td>0.842005</td>
      <td>0.058520</td>
      <td>0.109428</td>
      <td>92.50</td>
      <td>2.2</td>
    </tr>
  </tbody>
</table>
</div>

## Model development and evaluation
Since Random Forest has a much better performance, we will be using it for further development. We will train it using the training set and evaluate it using the test set.  

Random Forest with normal threshold achieved 82 % F1-score with RM 416.25 loss.
  - 45 fraud transactions are misclassified as normal.
  - 7 customers have high tendency to churn.  

To improve this model, we have to make sure both recall and precision do not decrease. It either increases or stays the same.  

## Implementation of threshold analysis
By using 0.46 as the new threshold, the model can achieve the highest F1-score. Random Forest with new threshold achieved 84 % F1-score with RM 370.00 loss, about 11 % decrease, and the same number of potential customers to churn, which is 7.
