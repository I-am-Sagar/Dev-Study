1. **Dynamic covariance in portfolio optimization**
In this lesson, we will discuss the concept of covariance and how to calculate dynamic covariance with GARCH models. We will also learn the role of covariance in portfolio management, and see how it can be used in portfolio optimization.

2. **What is covariance**
Covariance is a statistical tool used to determine the relationship of movement between two variables. In finance, the variables can be price returns of different assets. A positive covariance means two asset prices tend to move in the same direction. For example, when the European economy was recovering, Euros and British Pounds appreciated in value simultaneously. A negative covariance means asset prices tend to move in the opposite direction. For example, when the economy was slowing down, people took money away from the stock market and invested in safer assets like government treasuries. So stock prices were declining while fixed income prices were rising. As you can see in the plot, if variable X and Y have positive covariance, they tend to increase in value together; while with negative covariance, X tend to increase in value when Y decreases in value.

3. **Dynamic covariance with GARCH**
GARCH model takes the time-varying characteristic of volatility into consideration. Dynamic covariance can be computed by multiplying correlation coefficient between asset returns by their volatility from GARCH models.

4. **Calculate GARCH covariance in Python**
We can compute GARCH covariance in Python in 4 steps. Step 1 is to fit GARCH models for each return series and obtain their volatility estimations. THe sample code shows: suppose we have two foreign currency asset Euro and Canadian dollars, and their return time series data has been fitted by two GARCH models: gm_eur and gm_cad. We can directly obtain the volatility from the GARCH models. Step 2 is to compute the standardized residuals from the fitted GARCH models as shown in the sample code.

5. **Calculate GARCH covariance in Python (cont.)**
Step 3 is to compute the correlation coefficient as the simple correlation between standardized residuals. This can be done using "corrcoef()" method from the "numpy" package. And the last step is to compute the covariance by multiplying the correlation and GARCH volatility together.

6. **Modern portfolio theory (MPT)**
Modern portfolio theory or MPT is a classic portfolio management theory pioneered by the Nobel laureate Harry Markwitz in his 1952 paper "Portfolio Selection". In a nutshell, MPT states that there is an optimal way to structure a portfolio with various assets to take advantage of the diversification effect. The optimal portfolio can yield the maximum possible return with the minimum risk. In other words, an investor can construct a portfolio of multiple assets that will maximize returns for a given level of risk. Likewise, given a desired level of expected return, an investor can construct a portfolio with the lowest possible risk.

7. **MPT intuition**
Suppose we have a simple portfolio of two assets, and their weights are represented by W1 and W2. The portfolio variance can be computed by this formula with asset weights, variances of individual asset returns, and their covariance. Note when combing assets into a portfolio, MPT shows including assets with a negative covariance can reduce the overall risk of the portfolio. In this sense, an individual asset's return is less important than how the asset behaves in relation to each other, or in the context of the entire portfolio. Intuitively, for example, normally stocks and bonds tend to move in the opposite directions. By investing in both, when the stock market tanks, bond prices tend to rise, so the overall portfolio won't suffer as much or breakeven. Last but not least, incorporating GARCH models while computing the covariance, we can make more realistic estimations during the portfolio construction process.

8. **Let's practice!**
Now it's your turn!