1. **Summary statistics by category with seaborn**
In this video, you will learn how to visualize summary statistics for numeric variables to easily compare these statistics for different categories.

2. **Categorical plots with seaborn**
You will again be using seaborn, the plotting package for statistical charts. Seaborn offers specialized charts to combine categorical with numerical variables. These plots allow you to visualize estimates of summary statistics for a numerical variable for multiple categories. The summary statistics include familiar measures of central tendency and dispersion The goal of this analysis is to understand how changes in the levels of a categorical variable impact a numerical variable. One example that you already encountered to visualize the average market cap for sector or IPO year. Seaborn adds valuable visual detail to the analysis.

3. **The basics: countplot**
The most basic plot is the countplot, which visualizes the number of observations per category. Let's illustrate the countplot using the NASDAQ listing data. Countplot just displays the number of observations for each category, similar to when you used groupby with size. Similar to other seaborn plots, the countplot takes a DataFrame in long format. To create a countplot, just pass the NASDAQ DataFrame, and the column you want to plot on the x-axis. It helps to rotate the labels since some of the sector names are a bit longer. The matplotlib method xticks allows you do to do by passing a value that indicates the rotation in degrees.

4. **countplot, sorted**
To create a sorted countplot, first create a list of the sorted category labels. You can use the tools from the last video. Just group NASDAQ by sector, and calculate the size for each group, and sort the result in descending order. As you can see, you got the sorted count of observations by category. To extract the index as a list, just call dot-index-dot-tolist on the series.

5. **countplot, sorted**
Now you can pass this list to countplot's parameter 'order', and countplot now displays in sorted order.

6. **countplot, multiple categories**
countplot is also useful to show the number of observations for combinations of categories. Let's create a reduced dataset that just contains companies with IPO after 2014. Convert the variable year to integer, and then pass the column IPO year to the countplot's hue parameter. Seaborn now produces a grouped bar chart that shows the number of observations for each sector and IPO year.

7. **Compare stats with PointPlot**
The pointplot is a useful tool to compare statistics for more than one categorical variable. We first create a new variable called IPO that indicates whether the IPO occurred before or after the year 2000. We then add this variable to the pointplot to differentiate the average market cap by sector by this second category. As expected, for most sectors, market capitalization is higher for older companies, but this is not true for all cases.

8. **Let's practice!**
Now let's practice these new skills.
