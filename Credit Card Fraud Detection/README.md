## Problem Statement:
We want to reduce fraud transactions being misclassified as non-fraud as many as possible. The cost is too high if we fail to do so.
Any fraud transactions predicted by the model should be verified by the staff to whether they are real fraud or not.
Fraud cost and monitoring cost are our cost functions and we will try to reduce it.

## Attribute Information:
- **Time**	: Number of seconds elapsed between this transaction and the first transaction
- **V1-V28**: Unknown variables (may be result of a PCA Dimensionality reduction to protect user identities and sensitive features)
- **Amount**: Amount of transactions
- **Class**	: 1 (Fraud) and 0 (non-Fraud)
