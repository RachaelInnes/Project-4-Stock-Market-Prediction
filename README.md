

## TITLE: Group 4 Project, Stock Price Prediction, to Buy or Sell ?

## Introduction
Stock trading plays a crucial role in the global economy, offering investors opportunities to grow their wealth and achieve financial goals. However, the stock market is inherently volatile and unpredictable, posing significant challenges for investors striving to make informed decisions. Factors such as market trends, economic indicators, and geopolitical events can all influence stock prices, making it difficult to predict future movements accurately.
In this context, predictive analytics emerges as a powerful tool for financial decision-making. By leveraging advanced algorithms and data analysis techniques, predictive analytics can identify patterns and trends that may not be immediately apparent to human analysts. This enables investors to make more informed and strategic decisions, potentially improving their investment outcomes and reducing risks.

## Objective
To develop a machine learning model that predicts short-term stock price movements, specifically whether a user should buy or sell shares of a particular stock based on historical price data.

## Data Collection

We used data for Google, Microsoft, IBM, and Amazon from 1st January 2020 to 1st January 2024, totaling 1003 rows of data, which included:

- Date
- Open and Close Price
- Volume of Shares
- High and Low share prices for the day


## Data Cleaning
The data was cleaned and scaled prior to uploading it into a PostgreSQL database to ensure that it could be usable for machine learning, the types of activities undertaken were:

- Set the “Date” as an index, the csv was in a slightly unusual pattern with index lines at the top as well as in columns.
- Dropped any rows with missing values
- Used Standard Scaler to scale the data
- Saved the cleaned as one CSV file, "Cleaned_Stock_Data" in readiness to upload to the database.

## Creating a database
A database called “Stock Market Project” was created to store the data in readiness for machine learning. Once data was uploaded and tables successfully created the preparation had been completed for machine learning.

## Visualisation
A line graph was plotted using Matplot lib to plot the data of each company from 2020 to 2023 this was just to get a very high level visual on the data for each company over this period. 



 
