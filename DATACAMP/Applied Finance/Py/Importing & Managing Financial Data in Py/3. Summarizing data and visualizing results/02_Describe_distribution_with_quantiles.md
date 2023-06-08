1. **Describe the distribution of your data with quantiles**
In this segment we will look in more detail at how to describe the distribution of your data.

2. **Describe data distributions**
You have already taken the first steps in this direction when you calculated measures of central tendency like mean, median and mode, as well as the standard deviation. While these metrics provide a good first impression, you could get much more granular information on how your data is distributed. In this segment, we will focus on calculating and plotting quantiles.

3. **More on dispersion: quantiles**
Quantiles are measures of dispersion that are more robust to outliers. Quantiles divide your data into groups of equal size, each containing a certain percentage of your data. Quartiles divide your data into four groups, each containing 25%. Deciles divide your data into 10 groups, each containing 10%. The median corresponds to the 2nd quartile, or the 5th decile. The interquartile range of your data is the difference between the 3rd and the 1st quartile. Like the median, these metrics are more robust to outliers.

4. **Quantiles with pandas**
Pandas has a quantile method. Just pass the quantile you want to calculate as decimal value, representing the percentage of values that will be smaller. Here you can confirm that the point-five quantile is equal to the median. To calculate the interquartile range, you can calculate the first quartile at point-25,and the second at point-75. The difference is just the interquartile range. Notice how we can pass a list to calculate multiple quantiles, and select from the resulting pandas Series using single brackets.

5. **Quantiles with pandas & numpy**
As you have seen, pandas can calculate quantiles based on a list of values between 0 and 1. To calculate deciles, you can use numpy arange, which works just like the Python range function, but allows for decimal values from start to stop with difference step. Just provide this list of values to the method quantile, and pandas displays the corresponding values. In this example, we looked at deciles for market_cap.

6. **Visualize quantiles with bar chart**
You can plot the result by calling the plot method on the quantiles calculation; just add kind equals 'bar' to display the result as a bar plot.

7. **All statistics in one go**
Pandas provides a method to get all these metrics at once, called dot-describe. If you apply it to the Market Capitalization, you get all key summary stats, including the mean and median that you just calculated: number of observations, mean and standard deviation, and the minimum, 1st, 2nd, and 3rd quartile, and the max, also the 4th quartile. You'll again notice the presence of very large companies.

8. **All statistics in one go**
Finally, the dot-describe method takes a "percentiles" keyword to calculate any quantile. You can use again numpy-arange to create a list of values from start and stop, separated by 'step'. This is similar to Python's range function, as I said, but allows for decimal values. We're using a list starting a point-1 with steps of 0-point-1 up to 0-point-9 to get the deciles, which you can see displayed in the result for a more granular view of the distribution.

9. **Let's practice!**
Now roll up your sleeves to practice your new skills!