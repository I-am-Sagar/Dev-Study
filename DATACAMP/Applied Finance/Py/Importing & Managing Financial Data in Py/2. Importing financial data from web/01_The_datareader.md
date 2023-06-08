1. **The DataReader: Access financial data online**
In this chapter, you will learn how to import financial data from the internet.

2. **pandas_datareader**
The pandas data_reader is a great package that provides easy access to a range a financial data sources on the web. You will see that it takes very little code to import data directly into a pandas DataFrame. Available web sources include IEX (with free API key) and Yahoo! Finance for stock prices and derivatives. There is also plenty of global economics data from the Federal Reserve research portal, the World Bank, the OECD, or EuroStat, as well as exchange rates from OANDA.

3. **Stock prices: Yahoo! Finance**
Let's get started with an example on how to import stock prices for Google using Yahoo! Finance. First you need to import DataReader class from the data module in the pandas data_reader package as illustrated in the first line. Since you will request a time series of stock prices, you need to import the datetime library that provides the functionality to define a range of dates needed for your request. First, you need to define a start date. Just use the datetime library's date object and provide the year, month and day of your desired date. Let's start on January 1st 2015. For the end date, let's use December 31, 2016. Now you just need two more inputs: the stock ticker, and the data source - let's use the ticker for Google, and Yahoo! finance as source. With these variables defined, you can create a DataReader object. This reads the data from Yahoo! finance, and imports it into a DataFrame that we will call stock_data.

4. **Stock prices: Yahoo! Finance**
If you call the dot-info method to view the structure of this DataFrame, you'll learn the following: The DataFrame has a DatetimeIndex with 504 entries. It contains one row for each day, starting on January 2, 2015, the first trading day of that year, and it ends on Dec 30, 2016, the last trading day of 2016. There are 6 columns. The first 4 columns summarize the price distribution for any given day. They contain the first price, the highest price, the lowest price and the last price, also called 'Close'. The last column has the adjusted close price, which reflects corporate actions like stock splits or dividends. Finally, you also get the volume, which is the number of shares traded on any day, and that indicates the activity for a stock.

5. **Stock prices: Yahoo! Finance**
To display the DataFrame content, you can select the the first three rows using dot-head, and the last three rows using dot-tail, and combine the result using pd-dot-concat as we did in the last video.

6. **Stock prices: Visualization**
You can also visualize the time series for the close price using the matplotlib library that you have become familiar with in the Intermediate Python for Data Science course. pandas allows for easy access to the matplotlib functionality through built-in dot-plot method. Use single brackets to select the column, and call the plot method. You can create a title for the plot by passing the ticker variable to the title parameter. To show the plot, you just need to call plt dot show.

7. **Let's practice!**
Let's now move on and practice loading data from the internet.