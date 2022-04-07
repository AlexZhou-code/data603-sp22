# covid19 and unemployment rate in the United States

## Problem Statement

**After my initial processing and understanding of the data. I decided to focus more on the unemployment rate data.**

Use Spark to analyze, predict and visualize the distribution and number of COVID19 cases by state in the US.
Predict trends in unemployment claims based on reported COVID19 cases. This was done by performing a time series analysis of unemployment insurance claims in the U.S. from 1987 to April 18, 2020 and correlating the trends with COVID19 cases in the U.S.

## source data

The **COVID19 dataset**, from kaggle includes daily case and death counts for each U.S. state (updated every 5 days from January 1, 2020 to the present).
### sample
root
 |-- date: string (nullable = true)
 |-- county: string (nullable = true)
 |-- state: string (nullable = true)
 |-- fips: double (nullable = true)
 |-- cases: long (nullable = true)
 |-- deaths: long (nullable = true)

Weekly **unemployment insurance claims data** for all U.S. states from January 1, 1987 to April 18, 2020, as published by the U.S. Department of Labor. This data is not seasonally adjusted and is therefore ideal for exploring data patterns.

## What do I looking for
# Identify the states and counties most affected by covid. Show some charts with visuals .
There is definitely more to visualize about covid data than that, and I'm still seeking what I want.
# some prediction
predicts COVID cases for all states based on the affected population since January 2020. It was built using prophet, an open source library from facebook.
predicts weekly unemployment insurance claims independent of the pandemic based on historical data since 1987.
predict weekly unemployment insurance claims, using COVID cases as additional regressors in the model.

