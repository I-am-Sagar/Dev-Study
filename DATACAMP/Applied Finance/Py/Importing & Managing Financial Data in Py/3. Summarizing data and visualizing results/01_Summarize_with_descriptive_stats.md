1. **Summarize your data with descriptive stats**
In this chapter, you will learn how to summarize your data.

2. **Be on top of your data**
The goal here is to capture key quantitative characteristics that allow you to better understand and manage your data. We'll address in this chapter a few ways to summarize your data, including: Which values are central, typical, or representative? How widely are the values dispersed, and are there outliers? What does the overall distribution of your data look like?

3. **Central tendency**
Let's first look at measures of the Central Tendency, which is a value considered to be at the center, or most typical, of your data. First, you can calculate the mean: just sum up your data, and divide by the number of observations. Second, the median is the value that partitions your data so that 50% of values are smaller, and 50% are larger. Finally, the mode is the most frequent value. There can be several modes if multiple values occur with the same frequency. In practice, this looks as follows: For a symmetric distribution, these three measures are identical: the mean equals the median, and this value also occurs most frequently.

4. **Central tendency**
This changes if the data is skewed: the large values extending further to the right give the appearance of a long tail. In this case, the mean gets pulled toward the extreme values in the long tail. The mode still represents the single peak of this distribution, and the median lies in between.

5. **Central tendency**
The next example shows a distribution with two peaks. Again, the mean moves further towards the extreme values, this time on the left, and the median lies between the mean and the mode. The takeaway is that the mean is more sensitive to outliers than the median, which better measures the midpoint of your data, unless the data is following a symmetric distribution.

6. **Calculate summary statistics**
Let's now use pandas to calculate these statistics, using the familiar NASDAQ listings data. First, select the market capitalization, and divide the values by 10 to the power of 6, or 1 million, to represent the data in million dollars. Mean, median, and mode are built into pandas. Apply the methods to the market cap series, and you'll see that the mean is much larger than the median, while the mode is 0.

7. **Calculate summary statistics**
If you plot the distribution, which you will learn later in this chapter, you'll see why this is the case: there are a few very large companies, and these outliers drive up the mean. There is also a significant number of companies with 0 market cap, which are companies that are currently not traded.

8. **Dispersion**
Another important aspect of your data how close they are on average to their midpoint, or how different they are. This is also called the dispersion. To learn more about the dispersion of your data, you can calculate the variance and standard deviation. The variance is the sum of all the squared differences between your data and the mean, divided by the number of observations minus 1. The standard deviation is the square root of the variance. Just like the mean, this measure is more sensitive to outliers - the large companies drive up both mean and standard deviation, and an interval of 1 standard deviation around the mean extends into negative territory, yielding a poor summary of dispersion.

9. **Calculate variance and standard deviation**
To calculate the variance, just use the built-in method var. Assign it to a variable called variance, and then take the square root of it using the numpy method for this purpose. As you can see, the result is the same as calculating the standard deviation directly using the built-in pandas method for the standard deviation, dot-std.

10. **Let's practice!**
Now let's move on to some exercises to apply your new skills!