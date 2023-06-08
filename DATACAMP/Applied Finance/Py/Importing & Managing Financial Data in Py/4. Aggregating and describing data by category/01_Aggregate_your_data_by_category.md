1. **Aggregate your data by category**
In this chapter, you will learn how to aggregate data by category.

2. **Summarize numeric data by category**
So far we have focused on summarizing quantitative variables. You have selected one or several quantitative variables, and computed descriptive statistics like the mean, the standard deviation, quantiles, and others. The goal was to get a crisp summary of the distributional characteristics. The next step is to use categorical variables to split your data into groups, and then to analyze and compare the distribution of quantitative variables for these different groups. For example, you can calculate the highest market cap for each of the three stock exchanges, or the median market capitalization by IPO year. In this video, you will learn how to calculate the average market capitalization by sector for companies listed on the NASDAQ.

3. **Group your data by sector**
As a reminder, here's the NASDAQ listing data that we already loaded. Your next steps will be: Divide the market capitalization by 1 million to represent it in million dollars for easier display, and drop the original column. Group your data by Sector, and then calculate the average market cap in million US dollars for each sector.

4. **Group your data by sector**
Here's how you can go about this: First transform the market capitalization into million-dollar units. Now you don't need the original market capitalization column anymore. You can eliminate it with the drop method. Just specify one or several column labels to get rid of. If you want to drop several columns, pass a list with the labels, for a single column, a string is just fine. Be careful to pass the parameter axis=1 to drop a column; per default, pandas will try to rows instead of columns. Now you're ready to group your data by calling the pandas groupby method, which creates a new object. This method expects you to pass a column label for a categorical column. Assign the grouped data to the variable nasdaq_by_sector. You can then iterate over this new object in a loop. In each iteration, the object returns two items, just like a dictionary: First, a key that corresponds to the category represented by this group of data Second, a DataFrame containing the information for this group Just select the market cap column of the returned DataFrame, and apply an aggregation like the mean to it. As you can see, the code returns both the name of the category, and the average market cap in million dollars for this category.

5. **Keep it simple and skip the loop**
Pandas actually makes it easier to aggregate by categories. Instead of using a for loop, you can just select any numerical column from your grouped data, and apply an aggregate statistic. We are again using the mean to aggregate the market cap in millions per sector on the NASDAQ. Pandas returns a series with the category names as row labels, and the aggregate statistics as values.

6. **Visualize category summaries**
Let us visualize the category summaries as a horizontal bar chart. We first pick a title, and then call the plot method on the Series containing the average market cap for each sector. Select kind as 'barh' to tell pandas that you want a horizontal bar plot. Notice that you can add a label to the x-axis using plt-dot-xlabel.

7. **Aggregate summary for all numeric columns**
You can also calculate the mean for all numeric columns by applying the aggregate statistic directly to the grouped data, instead of selecting one or more columns.

8. **Let's practice!**
Now let's move on to the exercises!