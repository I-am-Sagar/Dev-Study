1. **Validation of GARCH model assumptions**
GARCH models make strict assumptions about the distribution characteristics of their standardized residuals. If the model is doing a good job of explaining the data, the standardized residuals should resemble a white noise process, which does not exhibit data clustering or autocorrelation. In this lesson, let's learn how to verify this.

2. **Visual check**
For starters, we can do a visual check by plotting the standardized residuals. As seen in the charts, the raw return data exhibits clear signs of clustering. After fitting the GARCH models, the standardized residuals don't show much clustering and are close to a random white noise movement.

3. **Autocorrelation**
We can also use autocorrelation to detect non-randomness in the standardized residuals. Autocorrelation describes the correlation of a variable with itself given a time lag. When there is a pattern such that values in the time series can be predicted based on preceding values in the series, the data exhibits autocorrelation. Existence of autocorrelation in the standardized residuals indicates the model may not be sound. We can use ACF plots or statistical tests such as Ljung-Box to detect autocorrelations in the data.

4. **ACF plot**
The coefficient of correlation between two values in a time series is called the autocorrelation function or ACF. For example, a lag 1 autocorrelation is the correlation between values that are one period apart. More generally, a lag k autocorrelation is the correlation between values that are k-period apart. An ACF plot is a visual representation of correlations between different lags. As seen in the plot, at lag 0 the correlation is 1 as the data is perfectly correlated with itself. Moving along the x-axis, the plot shows correlations of different lags. We can also specify a confidence level using alpha. For example, an alpha of point-05 means there is 5% chance the correlation will fall outside the band even the true correlation is zero.

5. **ACF plot in Python**
We can easily generate ACF plot with Python function "plot_acf() from the "statsmodels" package. Specify the alpha in the function to explicitly set a confidence level, then corresponding confidence intervals will be plotted.

6. **Ljung-Box test**
The Ljung–Box test, named after Greta Ljung and George Box, is a statistical test of whether any of a group of autocorrelations of a time series are different from zero. Instead of testing randomness at each distinct lag, it tests the "overall" randomness based on a number of lags. The null hypothesis of Ljung-Box test is: the data is independently distributed. Recall we reject the null hypothesis if the p-value is smaller than the specified significance level, such as 5%. In other words, the p-value less than 5% indicates that the residuals are not independently distributed, hence the model is not adequate.

7. **Ljung-Box test Python**
We can use "acorr_ljungbox()" function provided in the "statsmodels" package to perform a Ljung-Box test. Use "lags" to set the maximum number of time lags up to which the test will be performed. From the test results, the p-values can be viewed form the second row of the results.

8. **Let's practice!**
Now it's your turn!