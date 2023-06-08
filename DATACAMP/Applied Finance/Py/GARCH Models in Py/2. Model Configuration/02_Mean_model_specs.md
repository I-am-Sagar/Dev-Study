1. **Mean model specifications**
In the previous lesson, we discussed the distribution assumptions for GARCH models. In this lesson, let's discuss mean model assumptions.

2. **Constant mean by default**
By default GARCH models in Python use a constant mean assumption, which generally works well with most of the common financial asset data.

3. **Zero mean assumption**
We can also specify a zero mean assumption. This is useful if the mean of the time series has been modeled separately by another process, such as autoregressive (AR), moving-average (MA) or ARMA models. And we are using residuals from that model to estimate volatility. Many practitioners prefer this approach to separate the process of mean and volatility modeling.

4. **Autoregressive mean**
In addition, we can choose to model the mean as an autoregressive process, so the current mean is correlated with the previous data. This can be implemented in Python by setting the mean model to "AR" and specifying the number of lags. Due to the scope of this course, we will not dive into autoregressive models, such as AR, MA or ARMA models. If you are interested in learning more about them, check out other great courses on DataCamp such as "Time Series Analysis in Python".

5. **Let's practice!**
Now it is your turn to practice!