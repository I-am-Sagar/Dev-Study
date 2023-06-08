1. **Visualize the distribution of your data**
Now you have an array of summary metrics at your disposal. These are very useful as you have seen, but you also need to visualize your data.

2. **Always look at your data!**
Take a look at this example. These four data sets look very different. However, when you calculate mean and standard deviation, you obtain identical values for each of them. And if you draw a simple trend line through the data, they also appear to have the same linear relationship. So, always remember, identical metrics can represent very different data distributions.

3. **Introducing seaborn plots**
Let's take a look how to create crisp visualizations of your data. In this video, you will start learning about seaborn, an excellent plotting package based on matplotilb. You will first learn how to use the distplot, which is a swiss army knife when it come to visualizing the distribution of a variable. You will see how to easily use it to plot a histogram, or a kernel density plot. In the exercise, you'll also see how to produce a rugplot.

4. **10 year treasury: trend and distribution**
First, let's use seaborn distplot, which integrates histograms with Kernel Density Estimation, which is a smooth version of a histogram. For illustration, let's import 10 year treasury interest rates for the last 55 years using the already familiar pandas DataReader. After inspecting the result with the info method, you'll notice that the number of rows in the DatetimeIndex does not match the number of observations for your series. To properly plot the distribution, we need to first eliminate the missing values. For this purpose, pandas offers the dropna method that drops all rows with at least one missing value. An alternative to dropping missing values is the method fillna, which replaces all missing values with a new value. You could, for instance, pass the mean or median as argument. A quick look at the summary statistics provided by describe shows that the mean is bit higher than the median, suggesting that the data has a positive skew, with a longer tail on the right.

5. **10 year treasury: time series trend**
Let's drop the missing values, using inplace equals True to avoid the creation of a new DataFrame. This saves some memory and helps when you have lot of data. A plot of the time series trend shows the pronounced interest rate peak in the early eighties after a significant change in monetary policy to address rising inflation.

6. **10 year treasury: historical distribution**
In contrast to the time series perspective, you can use Seaborn's distribution plot to draw a histogram together with a Kernel Density estimate. As you have seen, the histogram creates bins, or ranges, and plots the counts of the subset of the data that falls into each bin to reflect the frequency distribution. The result is exact - the number displayed is the exact share of observations for a given bin. The Kernel Density estimate, on the other hand, provides a smooth approximation of the frequency distribution. As you can see, the approximation is close but not perfect. It is particularly useful to quickly compare different distributions.

7. **10 year treasury: trend and distribution**
You can improve your plot by adding vertical lines that mark interesting values. A call to the distplot function returns a matplotlib object called axis. You can assign this object to a variable, and then add elements to the same plot. To add a vertical line, just call the axvline method on this axes objects, and provide it with the value where to plot. We are using the historical median of the interest rate. You can also set the color, and select a linestyle - we are using two dashes to create a dotted line.

8. **Let's practice!**
The seaborn documentation provides very detailed instructions on how to implement many additional design options. And now, let's practice.