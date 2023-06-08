1. **More ways to aggregate your data**
In this video, you will learn more sophisticated ways to aggregate your data by categories.

2. **Many ways to aggregate**
In the previous video, you learned how to group your data by one categorical variable, and how then to aggregate one or more quantitative columns. In practice, you often want to summarize your data in more detailed ways. Fortunately, pandas makes it easy to do so. For instance, you may want to group by two or more variables, or you may want to apply multiple aggregations. Examples of more detailed aggregations include calculating the median market capitalization both by sector and IPO year, or calculating both the mean and the standard deviation for the stock price per year.

3. **Several aggregations by category**
Let us try out several aggregations per category first. We start again with the familiar NASDAQ listing information, compute the market cap in millions, and group the data by sector as before. You will now learn about a pandas method called agg. Once you've grouped your data by Sector you can select one or more columns. We'll again use the market cap in millions. Now, the agg method allows you to pass a list with names of statistical metrics. Pandas will then calculate each of these metrics for the selected column. The resulting DataFrame will have the categories as row labels, and the metrics as columns with appropriate labels. There are several other metrics that you can use with this method like the median, the standard deviation, or the min, or the maximum.

4. **Several aggregations plus new labels**
After aggregation you may want to rename you columns to something other than the default metric name. To do so, just pass the statics you want to compute to the agg method, and then call the rename method with a dictionary for the column keyword parameter. The keys of the dictionary are the metric names, and the values are your desired new labels. In this example we renamed the market cap column containing the count to 'number of observations' instead of size, and the column containing the mean to 'average'.

5. **Different statistics by column**
The agg method allows you yet another way to aggregate your grouped data. If you call this method on the grouped data before selecting a column, you can pass a dictionary to select both columns and methods. Create a dictionary, and select as keys one or more numeric columns. In the example, we are using the market cap and the IPO Year. Then, select as values of the dictionary the statistical methods that you would like to calculate for these columns. You see that pandas returns a DataFrame with the original column labels, but the values now correspond to the statistics that you have picked.

6. **Aggregate by two categories**
Let's now see how you can aggregate by two or more categories at the same time. Instead of passing a single column to the groupby method, create a list with several column labels. Pandas will group your data accordingly. From the result, select a numeric columns and apply an aggregate statistic. The result is a now a pandas series with a MultiIndex, which you learned about in chapter 2. Each level of the MultiIndex corresponds to one of the variables that you used to group your data.

7. **Select from MultiIndex**
Finally, let’s take a look at how you can select values from this DataFrame with MultiIndex: Use the selector loc to select from a MultiIndex. If you select a single label from the first index level using loc, then pandas returns a Series with a single index that only contains values from the second level of the MultiIndex.

8. **Select from MultiIndex**
You can also select several categories from the first level of the MultiIndex. Just pass a list with labels from the first index level, and pandas will return a series with MultiIndex just containing the selected subset of categories. In this example, we have selected Basic Industries and Transport to just show the average market cap per IPO year for these two sectors.

9. **Let's practice!**
Let's now practice your new skills.