### Question 1: Keep it simple stupid

A rule of thumb for data science modeling is "KISS" (keep it simple stupid). In other words, always choose a parsimonious model with parameters that are relevant. There are statistical tests and measures to help you decide.

Which of the following statements is incorrect?

1. A complex model is preferred over a parsimonious model given comparable predicting power.
2. In statistical hypothesis testing, the p-value is the probability of observing your data if the null hypothesis is true.
3. As a rule of thumb, if the absolute value of the t-statistic is larger than 2, the null hypothesis should be rejected.
4. 5% is a commonly used threshold to measure the level of significance.

**Ans.** 1

### Question 2: Simplify the model with p-values

Leonardo da Vinci once said: "Simplicity is the ultimate sophistication." It also applies to data science modeling. In this exercise, you will practice using the p-values to decide the necessity of model parameters, and define a parsimonious model without insignificant parameters.

The null hypothesis is the parameter value is zero. If the p-value is larger than a given confidence level, the null hypothesis cannot be rejected, meaning the parameter is not statistically significant, hence not necessary.

A GARCH model has been defined and fitted by the Bitcoin return data. The model result is saved in gm_result.

**Instructions 1/2**

1. Print the model fitting summary.
2. Get the model parameters and p-values, and save them in a DataFrame para_summary.
3. Print and review para_summary.

**Pre Code**

```py
# Print model fitting summary
print(gm_result.____())

# Get parameter stats from model summary
para_summary = pd.DataFrame({'parameter':gm_result.____,
                             'p-value': gm_result.____})

# Print out parameter stats
print(____)
```

**Ans.**

```py
# Print model fitting summary
print(gm_result.summary())

# Get parameter stats from model summary
para_summary = pd.DataFrame({'parameter':gm_result.params,
                             'p-value': gm_result.pvalues})

# Print out parameter stats
print(para_summary)
```

**Instructions 2/2**

According to the p-values, which parameter below is not statistically significant given a confidence level of 5%?

1. omega
2. alpha
3. gamma
4. beta

**Ans.** 3

### Question 3: Simplify the model with t-statistics

Besides p-values, t-statistics can also help decide the necessity of model parameters. In this exercise, you will practice using t-statistics to assess the significance of model parameters.

The t-statistic is computed as the estimated parameter value subtracted by its expected mean (zero in this case), and divided by its standard error. The absolute value of the t-statistic is a distance measure, that tells you how many standard errors the estimated parameter is away from 0. As a rule of thumb, if the t-statistic is larger than 2, you can reject the null hypothesis.

You will work with the same GARCH model as the previous exercise. You can access the model fitting summary in gm_result.

**Instructions**

1. Get the model parameters, standard errors and t-statistic, and save them in the DataFrame para_summary.
2. Compute t-statistics manually using parameter values and their standard errors, and save the calculation result in calculated_t.
3. Print and review calculated_t.
4. Print and review para_summary.

**Pre Code**

```py
# Get parameter stats from model summary
para_summary = pd.DataFrame({'parameter':gm_result.____,
                             'std-err': gm_result.____, 
                             't-value': gm_result.____})

# Verify t-statistic by manual calculation
calculated_t = para_summary['____']/para_summary['____']

# Print calculated t-value
print(____)

# Print parameter stats
print(____)
```

**Ans.**

```py
# Get parameter stats from model summary
para_summary = pd.DataFrame({'parameter':gm_result.params,
                             'std-err': gm_result.std_err, 
                             't-value': gm_result.tvalues})

# Verify t-value by manual calculation
calculated_t = para_summary['parameter']/para_summary['std-err']

# Print calculated t-statistic
print(calculated_t)

# Print parameter stats
print(para_summary)
```

### Question 4: Detect autocorrelations

GARCH models make strict assumptions about the distribution characteristics of the standardized residuals. If the model is doing a good job at explaining the data, the standardized residuals should not exhibit data clustering or autocorrelations.

Which of the following statements is incorrect?

1. Ideally the standardized residual of a GARCH model should resemble a white noise process.
2. Autocorrelation is the correlation of a time series with a delayed copy of itself as a function of time lags.
3. An ACF plot is a visual representation of autocorrelations based on different time lags.
4. If the p-value from a Ljung-Box test is smaller than the specified significance level, it indicates the data is independently distributed.

**Ans.** 4

### Question 5: ACF plot

If a GARCH model is doing a good job, the standardized residuals should not exhibit autocorrelations. In this exercise, you will practice using an ACF plot to detect autocorrelations in the data.

The coefficient of correlation between two values in a time series is called the autocorrelation function (ACF), and an ACF plot is a visual representation of correlations between different lags. There are pre-defined functions in Python statsmodels packages that enable you to generate ACF plots easily.

A GARCH model has been fitted with the S&P 500 return data, and its standardized residuals have been calculated and saved in std_resid. The matplotlib.pyplot has been imported as plt.

**Instructions**

1. Import the module needed for ACF plots from the statsmodels package.
2. Plot the GARCH model standardized residuals saved in std_resid.
3. Generate an ACF plot of the standardized residuals, and set the confidence level to 0.05.

**Pre Code**

```py
# Import the Python module
from statsmodels.graphics.tsaplots import ____

# Plot the standardized residuals
plt.plot(____)
plt.title('Standardized Residuals')
plt.show()

# Generate ACF plot of the standardized residuals
____(std_resid, ____ = ____)
plt.show()
```

**Ans.**

```py
# Import the Python module
from statsmodels.graphics.tsaplots import plot_acf

# Plot the standardized residuals
plt.plot(std_resid)
plt.title('Standardized Residuals')
plt.show()

# Generate ACF plot of the standardized residuals
plot_acf(std_resid, alpha = 0.05)
plt.show()
```

### Question 6: Ljung-Box test

Another powerful tool to check autocorrelations in the data is the Ljung-Box test. In this exercise, you will practice detecting autocorrelation in the standardized residuals by performing a Ljung-Box test.

The null hypothesis of Ljung-Box test is: the data is independently distributed. If the p-value is larger than the specified significance level, the null hypothesis cannot be rejected. In other words, there is no clear sign of autocorrelations and the model is valid.

You will use the same GARCH model as the previous exercise. Its standardized residuals are saved in std_resid.

**Instructions**

1. Import the module needed for Ljung-Box tests from the statsmodels package.
2. Perform a Ljung-Box test up to lag 10, and save the result in lb_test.
3. Print and review p-values from the Ljung-Box test result.

**Pre Code**

```py
# Import the Python module
from statsmodels.stats.diagnostic import ____

# Perform the Ljung-Box test
lb_test = ____(std_resid , ____ = ____, return_df = True)

# Print the p-values
print('P-values are: ', ____.iloc[0,1])
```

**Ans.**

```py
# Import the Python module
from statsmodels.stats.diagnostic import acorr_ljungbox

# Perform the Ljung-Box test
lb_test = acorr_ljungbox(std_resid , lags = 10, return_df = True)

# Print the p-values
print('P-values are: ', lb_test.iloc[0,1])
```

### Question 7: Goodness of fit basics

Can the model do a good job explaining the data? In other words, how is the "goodness of fit"?

"Goodness of fit" describes how well the model fits a set of observations. Measures of "goodness of fit" typically summarize the discrepancy between observed values and the values estimated by the model. Common measures include the maximum likelihood and information criteria.

Which of the following statements is incorrect?

1. Making a model overly complex tends to overfit the data.
2. The bigger the AIC, the better the model.
3. The bigger the likelihood, the better the model.

**Ans.** 2

### Question 8: Pick a winner based on log-likelihood

In this exercise, you will practice using log-likelihood to choose a model with the best fit.

GARCH models use the maximum likelihood method to estimate parameters. In general, the bigger the log-likelihood, the better the model since it implies a bigger probability of having observed the data you got.

Two GARCH models with different distribution assumptions have been defined and fitted with the S&P 500 return data. The normal distribution GARCH is saved in normal_result, and the skewed Student's t-distribution GARCH is saved in skewt_result.

**Instructions 1/2**

1. Print and review model fitting summaries in normal_result and skewt_result respectively.
2. Print the log-likelihood in normal_result and skewt_result respectively.

**Pre Code**

```py
# Print normal GARCH model summary
print(____.____())
# Print skewed GARCH model summary
print(____.____())

# Print the log-likelihood of normal GARCH
print('Log-likelihood of normal GARCH :', ____.____)
# Print the log-likelihood of skewt GARCH
print('Log-likelihood of skewt GARCH :', ____.____)
```

**Ans.**

```py
# Print normal GARCH model summary
print(normal_result.summary())
# Print skewed GARCH model summary
print(skewt_result.summary())

# Print the log-likelihood of normal GARCH
print('Log-likelihood of normal GARCH :', normal_result.loglikelihood)
# Print the log-likelihood of skewt GARCH
print('Log-likelihood of skewt GARCH :', skewt_result.loglikelihood)
```

**Instructions 2/2**

Which model is better according to their log-likelihood values?

1. Normal GARCH
2. Skewt GARCH

**Ans.** 2

### Question 9: Pick a winner based on AIC/BIC

In this exercise, you will practice using information criteria to choose a model with the best fit.

Information criteria intend to measure the trade-off between goodness of fit and model complexity. AIC and BIC are two commonly used information criteria for model selection. They both impose penalties on model with more parameters, or more complex models. The lower the AIC or BIC, the better the model.

A GJR-GARCH model and EGARCH model have been defined and fitted with the S&P 500 return data. Their results can be accessed in gjrgm_result and egarch_result respectively.

**Instructions 1/2**

1. Print the AIC in gjrgm_result and egarch_result respectively.
2. Print the BIC in gjrgm_result and egarch_result respectively.

**Pre Code**

```py
# Print the AIC GJR-GARCH
print('AIC of GJR-GARCH model :', ____.____)
# Print the AIC of EGARCH
print('AIC of EGARCH model :', ____.____)

# Print the BIC GJR-GARCH
print('BIC of GJR-GARCH model :', ____.____)
# Print the BIC of EGARCH
print('BIC of EGARCH model :', ____.____)
```

**Ans.**

```py
# Print the AIC GJR-GARCH
print('AIC of GJR-GARCH model :', gjrgm_result.aic)
# Print the AIC of EGARCH
print('AIC of EGARCH model :', egarch_result.aic)

# Print the BIC GJR-GARCH
print('BIC of GJR-GARCH model :', gjrgm_result.bic)
# Print the BIC of EGARCH
print('BIC of EGARCH model :', egarch_result.bic)
```

**Instructions 2/2**

Which model is better according to their AIC/BIC values?

1. GJR-GARCH
2. EGARCH

**Ans.** 2

### Question 10: Backtesting basics

Backtesting is a common approach to assess model performance ex-post. "Ex-post" means "after the fact". During a backtesting, model forecasts are compared with the actual historical data to see how well the model would have performed.

Which of the following statements is incorrect?

1. "Out-of-sample" data is reserved for backtesting.
2. The bigger the MAE and MSE, the better the model performance.
3. There are pre-defined functions for calculating model prediction errors such as MAE and MSE in the Python sklearn.metrics package.

**Ans.** 2

### Question 11: Backtesting with MAE, MSE

In this exercise, you will practice how to evaluate model performance by conducting backtesting. The out-of-sample forecast accuracy is assessed by calculating MSE and MAE.

You can easily estimate prediction errors MSE and MAE with pre-defined functions in the sklearn.metrics package. The actual variance and predicted variance have been preloaded in actual_var and forecast_var respectively.

**Instructions**

1. In evaluate(), perform the MAE calculation by calling the corresponding function from sklean.metrics.
2. In evaluate(), perform the MSE calculation by calling the corresponding function from sklean.metrics.
3. Pass variables to evaluate() in order to perform the backtest.

**Pre Code**

```py
def evaluate(observation, forecast): 
    # Call sklearn function to calculate MAE
    mae = ____(observation, forecast)
    print('Mean Absolute Error (MAE): {:.3g}'.format(mae))
    # Call sklearn function to calculate MSE
    mse = ____(observation, forecast)
    print('Mean Squared Error (MSE): {:.3g}'.format(mse))
    return mae, mse

# Backtest model with MAE, MSE
evaluate(____, ____)
```

**Ans.**

```py
def evaluate(observation, forecast): 
    # Call sklearn function to calculate MAE
    mae = mean_absolute_error(observation, forecast)
    print('Mean Absolute Error (MAE): {:.3g}'.format(mae))
    # Call sklearn function to calculate MSE
    mse = mean_squared_error(observation, forecast)
    print('Mean Squared Error (MSE): {:.3g}'.format(mse))
    return mae, mse

# Backtest model with MAE, MSE
evaluate(actual_var, forecast_var)
```

<hr>