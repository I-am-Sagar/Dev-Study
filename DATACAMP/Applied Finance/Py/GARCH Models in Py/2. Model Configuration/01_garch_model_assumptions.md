1. **Distribution assumptions**
Hi and welcome back! In this chapter, let's dive into GARCH model assumptions, and see how we can define a better model.

2. **Why make assumptions**
Volatility is not a directly observable quantity and is estimated through price return fluctuations. Returns equal to the mean returns plus residuals, and residuals are a stochastic return shocks dependent on the size of the volatility. Therefore to model volatility, GARCH models require making distribution assumptions of both the residuals and the mean returns. And to define a good model, we want to have assumptions most representative of the actual data.

3. **Standardized residuals**
Let's discuss the GARCH models assumptions about the standardized residuals first. Recall residuals are the differences between predicted returns and the mean returns. And standardized residuals are the residuals divided by the model estimated volatility. By default GARCH models assume a normal distribution for the standardized residuals, which is the familiar symmetric bell-shaped curve we often see. But the financial world is rarely that ideal.

4. **Residuals in GARCH**
In Python, the GARCH model residuals can be accessed from the fitted model result by "resid", and the GARCH volatility can be accessed by "conditional_volatility". Hence the standardized residuals are calculated as model residuals divided by conditional volatility. We can also plot a histogram of the standardized residuals to review its distribution curve.

5. **Fat tails**
Oftentimes, the distribution curves of price returns exhibit fats tails. That is, there is a higher probability to observe very large returns, either positive or negative, than under a normal distribution.

6. **Skewness**
The distribution curves also tend to exhibit skewness, or asymmetry. Negative skew means the left tail of the distribution curve is longer, so the mass of the distribution is on the right of the figure. Vice versa, positive skew has a longer right tail, and the mass of the distribution is concentrated on the left.

7. **Student's t-distribution**
To improve the GARCH models with assumptions more representative of real financial data, we can specify the distribution assumption to be "Student's t-distribution". The Student's t-distribution is symmetric and bell-shaped, like the normal distribution, but has heavier tails, meaning that it is more prone to producing values that fall far from its mean. The nu parameter of a Student's t-distribution indicates its shape. The larger the nu, the more peaked the curve becomes.

8. **GARCH with t-distribution**
To specify the distribution assumption to Student's t-distribution in Python, simply set "dist" equal to "t" when defining the GARCH model. After fitting the model, we can find nu parameter under the "Distribution" section of the model summary.

9. **GARCH with skewed t-distribution**
In addition, to model asymmetry in the distribution, we can specify the distribution assumption to be "skewed Student's t-distribution". In Python, simply set "dist" equal to "skewt" when defining a GARCH model. In addition to nu, A skewed Student's t-distribution has parameter lambda to indicate the skewness. When lambda equals to 0, the distribution is identical to a standard Student's t-distribution and symmetric. When lambda is less than 0, the distribution is negatively skewed, and vice versa. Lambda is within the range of -1 and 1.

10. **Let's practice!**
Now it is your turn!