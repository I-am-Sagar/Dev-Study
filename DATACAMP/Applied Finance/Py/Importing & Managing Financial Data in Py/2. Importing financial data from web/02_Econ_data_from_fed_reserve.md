1. **Economic data from the Federal Reserve**
In this chapter you will learn how to get economic data from the Federal Reserve.

2. **Economic data from FRED**
The Fed has an online portal called Federal Reserve Economic Data or FRED. This service offers almost 500,000 data series in a broad range of categories like economic growth and employment, monetary and fiscal policy, or demographics, industry trends and commodity prices. Depending on the subject, time series may be available at daily, monthly or annual frequencies.

3. **Get data from FRED**
Each series has a code that you need to access the data, and that you can obtain from the FRED website. Just navigate to fred dot stlouisfed dot org, and search for a topic.

1 https://fred.stlouisfed.org/

4. **Get data from FRED**
A search for the term interest rate produces over 1,400 results. Let's pick the 10-year Treasury Rate at daily frequency.

5. **Get data from FRED**
The page for this series displays additional detail, including the code required to import the data with the pandas DataReader.

6. **Interest rates**
Importing economic data works just like the stock data. As before, import the DataReader class from the data module in the pandas data_reader package, and import date from the datetime package. Then, define the series code 'DGS10' for the 10-yr Treasury yield that you just got from the website. The data source now changes to 'fred'. The website showed that data is available since 1962, so let's choose this as start date, and skip the end date to obtain the most recent data. Use these parameters to create a DataReader object to load your data into a variable called data. Calling the info method on the resulting DataFrame shows that the DatetimeIndex has over 14,400 rows, from 1962 to the most recent trading day. With 13,800 valid observations, there are about 600 missing values for this 55 year period.

7. **Stock prices: Visualization**
Before we plot the data for the Treasury yield, let's rename the column to 10-yr Treasury instead of the less intuitive DGS10. Pandas has a rename method that you can apply to either row or column labels. It accepts a dictionary, where the keys are the current names, and the values are the new names that you would like to assign. With the renamed column just call the plot method and assign the series name 10-yr Treasury as title.

8. **Combine stock and economic data**
let us now combine stock and economic data. Let's set 2000 as the start date. As the economic data point, let's use the oil price. Provide series code, label and start date for the data source to the DataReader, and you get a DataFrame with the oil price time series. Let's combine the oil price with the stock price of Exxon Mobil. Pass ticker, start date and the data source to the DataReader to get a second DataFrame that you assign to the variable 'stock'. You can use the pandas concat function to combine both DataFrames. We will select only the close column from the stock DataFrame, and pass it together with the oil price DataFrame as a list to the function. Before, you have concatenated DataFrames vertically, or stacked them, aligning on the columns. Now, you will concatenate the two DataFrames horizontally, while pandas aligns the data on the index, so that the dates match up. We achieve this by passing the parameter axis=1. Using dot-info, you see that the result contains both the stock and the oil price.

9. **Combine stock and economic data**
In this slide you see how you can rename the 2 columns by simply assigning 2 new labels, 'Exxon' and 'Oil Price'. You can now plot both columns. Note how pandas automatically generates a legend. Also note how the Exxon stock price has remained stable despite the drop in oil prices over the last two years.

10. **Let's practice!**
Let's now move on to some exercises.