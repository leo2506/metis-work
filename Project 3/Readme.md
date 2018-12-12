# Good or Bad Loans?
![](https://github.com/leo2506/metis-work/blob/master/Project%203/personal_loan.jpg)
## Overview
The project is intended to build a classification model to detect risky clients and enhance policies against losses for Lending Club, a peer-to-peer loan company. The dataset is acquired from [Kaggle.com](https://www.kaggle.com/wendykan/lending-club-loan-data), which records loan data from 2007 to 2015. The dataset has 890,000 observations and 75 features in total. The model predicts whether an applicant is going to keep paying on time. 
## Project Design
I choose the variable “loan_status” as my dependent variable(target) and another 30 features about the client’s employment, annual income, homeownership, credit score level, number of financial inquiries over the last 6 months, collections among accounts other than Lending Club and the loan’s amount and term. 

Out of the 890,000 cases, there are around 700,000 with a loan status of “Current” or “Issued”, which has not been payed off yet or has not triggered a late event yet. I took these 700,000 cases out of my scope of analysis because it is hard to determine whether it is a good or bad loan. For the remaining 200,000 cases, I labeled ones with a loan status of “Charged Off”, “Late (1-30 days)”, “Late (31-120 days)”, “Default”, or “In Grace Period” as “bad” loans, and ones which have already been fully paid as "good" loans. 

My model was constructed to predict whether a loan will be good or bad after it gets approved. A sample of 10,000 data points were drawn to build up the model for computational efficiency. 

## Tools
- Python:
  - Data Cleaning: Pandas
  - Data Analysis: Numpy, Pandas, Scikit-learn, Jupyter
  - Presentation: Matplotlib, Seaborn
- Tableau, Powerpoint

## Repository Organization
**Name** | **Description**
---|---
[All_work.ipynb](All_work.ipynb) | A notebook contains all data cleaning, feature engineering, modeling, cost-benefit analysis, feature importance analysis
Cost Analysis.twb | A tableau workbook contains preliminary data analysis of average profit from fully paid clients and average loss from delinquent or default clients
[model.pkl](model.pkl) | Pickled best model(Gradient Boosting Classifier with Combine Sampling on the training)
[Data](/Data) | It contains all raw data and cleaned data
[Proposal](/Proposal) | This is the initial proposal which is already deprecated because the topic changed.
[Slides](/Slides) | Essential for an elevation pitch

