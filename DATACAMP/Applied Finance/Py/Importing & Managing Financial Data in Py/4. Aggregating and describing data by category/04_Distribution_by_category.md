1. **Distributions by category with seaborn**
In this segment, you will learn how to visualize distributions for numeric variables, broken down by categories.

2. **Distributions by category**
In the last segment, you focused on summary statistics like the number for observations per category, or the mean of a numeric variable by category. Now you will visualize the shape of the distribution of a variable differentiated by levels of a categorical variable so that you can see how the numeric variable changes. For instance, you will analyze how the distribution of the market capitalization changes for different levels of the sector, or by IPO Year. This type of analysis provides a more detailed view at your data, similar to when you progressed from summary statistics to distributional plots in the last chapter.

3. **Clean data: removing outliers**
We'll use the NASDAQ companies once again, with market cap expressed in USD million. To get a better view of the distribution of your data, let's remove inactive companies with market cap of 0, and outliers with very large market capitalization. You could choose the 90th percentile as a cutoff for outliers at the high end. Now that you have removed outliers, you are ready to explore the Boxplot.

4. **Boxplot: quartiles and outliers**
The box plot is a classic statistical chart based on key quantiles of a distribution. The syntax is similar to the plots you have seen in the last video. The box plot requires that you provide a DataFrame, and: The label of one categorical column for the x axis, and The label of one quantitative column for display on the y-axis. After providing the data, the boxplot outlines the distribution of the numeric variable market cap for each level of the categorical variable Sector as follows: The box starts at the 1st and ends at the 3rd quartile. The horizontal bar at the center of the box is the second quartile, ie, the median. The interquartile range is the difference between the 3rd and the 1st quartile, represented by the vertical length of the box The two whiskers extending from the top and bottom are one and a half times the interquartile range in length (but limited by 0 at the lower end). Data points outside this range are marked as outliers. In our example, you can see that the company sizes vary significantly at the top end for each sector. While the median is similar for each sector, the third quartile, inter quartile range, and number of outliers differ greatly.

5. **A variation: SwarmPlot**
A useful variation is the swarmplot. It displays all observations, while attempting to avoid overlap. It is most useful when the number of observations is limited.

6. **Let's practice!**
Now go ahead and solve your final exercises!