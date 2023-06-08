1. **Select stocks and get data from Yahoo! Finance**
In this video, you will learn how you can select stocks based on conditions.

2. **Select stocks based on criteria**
In particular, you’ll be using the listing information provided by the stock exchanges. Available criteria to select one or more stock tickers are the stock exchange itself, sector or industry, the IPO year, the market capitalization, or any combination of these.

3. **Get ticker for largest company**
Let's start by selecting the stock ticker for the largest company by market capitalization listed on the NYSE. You already know how to use read_excel to import the companies listed on this exchange. One way to find the largest company is to sort the data by market capitalization using sort_values while passing the parameter ascending equals False to sort in descending order. Select the columns Stock symbol and Company name, and display the first rows using dot-head. You will find that Johnson & Johnson, Exxon, and JP Morgan are the three largest NYSE stocks. You can use dot-iloc to select the first row of the sorted DataFrame. You will remember that dot-iloc is used for integer based selection. Just pass 0 for the first row, and assign the result to a new variable largest_by_market_cap. Since the result is a pandas Series, you can just select the row label Stock Symbol, and obtain the string JNJ for Johnson & Johnson.

4. **Get ticker for largest company**
There's another, more elegant way to select the ticker of the largest company. First, use set_index to move the stock symbol into the index of the DataFrame. Call dot-info on the new DataFrame, and you'll now find Stock Symbols in the index, instead of integers. Now that your target is in the index, you can use the method idxmax. Select Market Capitalization as the column that you will use as criterion, and apply idxmax. The method returns the index value that corresponds to the largest market capitalization, which is, of course, the same that we got by sorting by this criterion and selecting the ticker from the first row.

5. **Get ticker for largest tech company**
You can drill down further. Let's look at the available values in the sector column. The dot-unique method returns the unique values in a given column as a numpy array. To filter rows that meet a condition, pass the condition to the loc selector. To select rows with companies in the tech sector, use this condition as the first entry for loc, which is responsible for selecting rows. You formulate the condition by selecting a column and applying a logical operator like equal. Pandas will select the rows where the condition is true. You can use head with parameter 2 to see that at least the first two companies are clearly from this sector, with Oracle topping the list for the NYSE. Let's use this new filtering technique together with idxmax. We have already moved the ticker to the index, so we just need to filter out the tech companies, and in addition, select the Market Capitalization column. Then apply idxmax to get the ticker for Oracle as a result.

6. **Get data for largest tech company with 2017 IPO**
We can filter by multiple conditions using the logical operators and and or. Just make sure you enclose each condition with parentheses. Let's see which tech company on the NYSE with IPO in 2017 has the largest market capitalization. You get the ticker by using loc to apply these two conditions, then selecting the column market cap, and calling idxmax. Provide the ticker to the DataReader with data_source yahoo. If you omit the start date, the DataReader will return all available data since 2010. To plot price trend and volume, select the columns 'Close' and 'Volume'.

7. **Visualize price and volume on two axes**
Let's look at a plot. To plot two columns that are measured on different scales on the same chart, you can use the secondary_y parameter and select a column that will be measured on the right hand axis. Also note that we are using a pyplot feature called tight_layout that improves the layout by reducing whitespace. You'll probably find the result looks better, and notice that Snapchat has been the IPO with the highest market capitalization in 2017 so far.

8. **Let's practice!**
Let's now go on to practice your new skills.