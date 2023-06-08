1. **What are ARCH and GARCH**
In this lesson, let's dive into the GARCH models.

2. **First came the ARCH**
Before GARCH, first came the ARCH models. ARCH stands for "Auto-Regressive Conditional Heteroskedasticity", and was developed by American economist Robert F. Engle in 1982. Here "conditional heteroscedasticity" means the data has time-dependent varying characteristic and unpredictable. Due to his contribution, Engle won the Nobel prize in economics in 2003.

3. **Then came the GARCH**
Based on ARCH, GARCH models were developed by Danish economist Tim Bollerslev in 1986. The "G" in GARCH stands for "Generalized". Fun fact: Bollerslev wrote about the GARCH models in his Ph.D thesis, under the supervision of Engle, who was the inventor of ARCH models.

4. **Related statistical terms**
Before diving into the GARCH model equations, let's clarify some basic terms. A white noise process contains a sequence of random variables that cannot be predicted. A time series is white noise if the variables are independent and identically distributed with a mean of zero. A residual is the difference between the observed value of a variable at time t and its predicted value based on information available prior to time t. If the prediction model is working properly, successive residuals are uncorrelated with each other, that is, they constitute a white noise time series. In other words, the model has taken care of all the predictable components of a time series, left only the unpredictable white noise part.

5. **Model notations**
Assume at time t, we want to predict the return r_t using information as of time t-1. This can be denoted as the expected, or mean return mu of time t. The prediction won't be perfect, so predicted return r_t is equal to the mean return mu_t plus the residual epsilon_t. Similarly, we can predict the volatility of time t as the expected variance given information known as of time t-1. Volatility is not directly observable, but it is related to the prediction error. As discussed earlier, if the prediction works well, the residual should equal to the volatility times a random variable from a white noise process. Now it comes down to how to predict the volatility at time t? Let's see how ARCH and GARCH models tackle this.

6. **Model equations: ARCH**
The equation of ARCH model with lag p is defined as follows. In essence it models variance as a weighted average of past residuals up to lag p. Hence ARCH(1) model states: variance of time t equals to a constant omega, plus alpha times residual squared of time t-1.

7. **Model equations: GARCH**
In practice, GARCH models are more commonly used by researchers. The GARCH(p,q) model equation is as follows. Besides p-period lags of residuals, GARCH models add q-period lags of variances for predicting the current variance. Hence a basic GARCH (1,1) model states: the variance of time t is the sum of three components: a constant omega, alpha times residual squared of time t-1, and beta times variance of time t-1.

8. **Model intuition**
Don't be intimidated by the equations. GARCH models can be understood intuitively. First the model is autoregressive in nature. It tries to estimate the volatility at time t on the basis of information known as of time t-1. Second, it estimates volatility as a weighted average of past information.

9. **GARCH(1,1) parameter constraints**
To make a GARCH(1,1) process realistic, there are two conditions. First, it requires all the parameters, omega, alpha, and beta, to be non-negative. This ensures the variance can't be negative. Second, alpha plus beta should be less than one, which ensures the model estimated variance is always "mean-reverting" to the long-run variance. The long-run variance equals to omega divided by one minus alpha minus beta.

10. **GARCH(1,1) parameter dynamics**
The rule of thumb regarding model parameter is: the larger the alpha, the bigger the immediate impact of the shocks. Here the shocks are expressed as residuals, or prediction errors. If we keep the alpha fixed, the larger the beta, the longer the duration of the impact, that is, high or low volatility periods tend to persist.

11. **Let's practice!**
That's a lot for you to digest. Now it's time to practice!