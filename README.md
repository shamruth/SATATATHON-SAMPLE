
Data Preprocessing and Validation for Statathon
Project Overview
This project demonstrates a robust data cleaning and preprocessing pipeline using Python. The script takes a raw CSV file (data.csv), identifies and handles various data quality issues, and outputs a cleaned and validated dataset. The entire process is designed to prepare data for reliable analysis and modeling.

The key stages of the pipeline include:

Loading Data: Ingesting the dataset while recognizing multiple types of missing value placeholders.

Imputation: Filling in missing numerical data using a statistical measure (median).

Outlier Detection & Treatment: Identifying and capping outliers in the age column using the Interquartile Range (IQR) method.

Data Validation: Enforcing a logical rule (e.g., an individual must be at least 18 to have a 'Graduate' degree) and correcting inconsistencies.

Data Processing Pipeline
1. Handling Missing Values
The script begins by loading data.csv into a pandas DataFrame. It is configured to recognize a comprehensive list of common missing value strings ("NA", "N/A", "", etc.) and treat them as NaN (Not a Number).

2. Imputing Numerical Data
To ensure the dataset is complete, missing values in numerical columns are imputed.

Strategy: Median Imputation

Reasoning: The median is used because it is robust to outliers, providing a more stable measure of central tendency for skewed data compared to the mean.

3. Outlier Detection and Capping
Outliers can significantly distort statistical analyses and machine learning models. This script identifies and handles them in the age column.

Method: Interquartile Range (IQR)

The first quartile (Q1) and third quartile (Q3) are calculated.

The IQR is computed as Q3 - Q1.

Outliers are defined as any data points that fall below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR.

Treatment: Capping

Instead of removing outliers, which can lead to information loss, they are "capped." This means any value exceeding the upper bound is replaced with the upper bound, and any value below the lower bound is replaced with the lower bound.

4. Data Validation and Correction
The final step enforces data integrity by checking for logical inconsistencies.

Rule: An individual with an 'education' level of 'Graduate' must have an age of 18 or greater.

Action: Any rows that violate this rule are identified. The script then automatically corrects the 'education' value for these rows to 'High School', resolving the inconsistency.