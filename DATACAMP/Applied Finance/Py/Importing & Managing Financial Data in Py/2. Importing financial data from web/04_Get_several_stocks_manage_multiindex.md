1. **Get several stocks & manage a MultiIndex**
In this chapter you will learn how to retrieve several stocks from Yahoo finance, and how to manage a DataFrame with more than a single index.

2. **Get data for several stocks**
You will be using the listing information to select several stocks at once, like for instance the largest 3 stocks per sector. You will then use Yahoo! finance to retrieve data for these stocks with a single DataReader object. In the process, you will learn about the pandas MultiIndex, which allows you to manage more complex datasets.

3. **Load prices for top 5 companies**
Let's start by loading prices for the largest five companies. As before use read_excel to load the NASDAQ listing information. Next, move the company ticker to the index. Instead of assigning the result to a new variable, you can also set the parameter inplace to true. After selecting the column Market Capitalization, you can apply a new method called nlargest. This method will return the largest n values for the series that you have selected. Assign the result to the variable top_5, and apply the method div to divide the values by 1 million to return the market cap in million US dollars. Now that you have selected the largest five companies, you can select the index of the series, and convert it to a list.

4. **Load prices for top 5 companies**
You can pass this list directly to the DataReader to get all information with a single call. The result is a DataFrame with two column levels, one for the tickers and another one for the variable names. You can move the ticker level to the index so you only have a single level of column headers using the method stack. This moves the stock tickers from the inner column level to the inner index level.

5. **Load prices for top 5 companies**
If you inspect the result with info, you will notice that the index is now a MultiIndex. A MultiIndex has more than a single identifier for each row. Here, each row is identified by the date and the stock ticker.

6. **Reshape your data: .unstack()**
You can further reshape your MultiIndex DataFrame by selecting a single column and applying the method unstack to the resulting Series. This moves the innermost index level, which contains the stock tickers, into the columns.

7. **From long to wide format**
Let's take a closer look at what we just did. Often this manipulation is referred to as moving from a long to a wide format. Starting with a MultiIndex Series, applying unstack creates a DataFrame, where each unique stock ticker is a column label. The date information remains as row labels, and continues to identify individual stock prices.

8. **Stock prices: Visualization**
To plot a DataFrame with several columns, you can use the keyword "subplots". When set to True, it displays each column on a separate chart.

9. **Let's practice!**
Let's now work through some exercises to practice your new skills!