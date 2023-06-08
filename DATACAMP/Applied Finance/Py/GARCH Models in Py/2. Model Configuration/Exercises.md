### Question 1: Fat tails and skewness

GARCH models enable one to specify the distribution assumptions of the standardized residuals. By default, a normal distribution is assumed, which has a symmetric, bell-shaped probability density curve. Other options include Student's t-distribution and skewed Student's t-distribution.

Which of the following statements is incorrect?

1. A distribution with fat tails implies greater possibility to observe extreme events.
2. The smaller the degrees of freedom v of a Student's t-distribution, the more peaked the distribution curve.
3. When lambda = 0, the skewed Student's t-distribution is identical to a Student's t-distribution.
4. A distribution with a negative skew means the left tail of the distribution curve is longer.

**Ans.** 2

### Question 2: Plot distribution of standardized residuals

GARCH models make distribution assumptions of the standardized residuals. Recall residuals are the differences between predicted returns and the mean returns. And standardized residuals are the residuals divided by the model estimated volatility.

In this exercise, you will practice computing the standardized residuals from a fitted GARCH model, and then plot its histogram together with a standard normal distribution normal_resid.

A GARCH model has been defined and fitted with S&P 500 price return data. The fitted result can be accessed as gm_result. In addition matplotlib has been preloaded as plt.

**Instructions**

1. Obtain model estimated residuals and save it in gm_resid.
2. Obtain model estimated volatility and save it in gm_std.
3. Calculate the standardized residuals gm_std_resid.
4. Plot a histogram of gm_std_resid.

**Pre Code**

```py
# Obtain model estimated residuals and volatility
gm_resid = gm_result.____
gm_std = gm_result.____

# Calculate the standardized residuals
gm_std_resid = ____ /____

# Plot the histogram of the standardized residuals
plt.____(____, bins = 50, 
         facecolor = 'orange', label = 'Standardized residuals')
plt.____(normal_resid, bins = 50, 
         facecolor = 'tomato', label = 'Normal residuals')
plt.legend(loc = 'upper left')
plt.show()
```

**Ans.**

```py
# Obtain model estimated residuals and volatility
gm_resid = gm_result.resid
gm_std = gm_result.conditional_volatility

# Calculate the standardized residuals
gm_std_resid = gm_resid /gm_std

# Plot the histogram of the standardized residuals
plt.hist(gm_std_resid, bins = 50, 
         facecolor = 'orange', label = 'standardized residuals')
plt.hist(normal_resid, bins = 50, 
         facecolor = 'tomato', label = 'Normal residuals')
plt.legend(loc = 'upper left')
plt.show()
```

### Question 3: Fit a GARCH with skewed t-distribution

The default normal distribution assumption of the standardized residuals used in GARCH models are not representative of the real financial world. Fat tails and skewness are frequently observed in financial return data.

In this exercise, you will improve the GARCH model by using a skewed Student's t-distribution assumption. In addition, you will compare the model estimated volatility with that from a model with a normal distribution assumption by plotting them together.

A GARCH model with the default normal distribution assumption has been fitted for you, and its volatility estimation is saved in normal_vol.

**Instructions 1/2**

1. Define a GARCH model skewt_gm with a skewed Student's t-distribution assumption.
2. Fit the model and save the result in skewt_result.

**Pre Code**

```py
# Specify GARCH model assumptions
skewt_gm = arch_model(sp_data['Return'], p = 1, q = 1, mean = 'constant', vol = 'GARCH', ____ = '____')
# Fit the model
skewt_result = skewt_gm.____()
```

**Ans.**

```py
# Specify GARCH model assumptions
skewt_gm = arch_model(sp_data['Return'], p = 1, q = 1, mean = 'constant', vol = 'GARCH', dist = 'skewt')
# Fit the model
skewt_result = skewt_gm.fit()
```

**Instructions 2/2**

1. Save the model estimated conditional volatility in skewt_vol.
2. Plot skewt_vol together with the normal GARCH estimations and the actual return data.

**Pre Code**

```py
# Specify GARCH model assumptions
skewt_gm = arch_model(sp_data['Return'], p = 1, q = 1, mean = 'constant', vol = 'GARCH', dist = 'skewt')
# Fit the model
skewt_result = skewt_gm.fit()

# Get model estimated volatility
skewt_vol = skewt_result.____

# Plot model fitting results
plt.plot(____, color = 'gold', label = 'Skewed-t Volatility')
plt.plot(normal_vol, color = 'red', label = 'Normal Volatility')
plt.plot(sp_data['Return'], color = 'grey', 
         label = 'Daily Returns', alpha = 0.4)
plt.legend(loc = 'upper right')
plt.show()
```

**Ans.**

```py
# Specify GARCH model assumptions
skewt_gm = arch_model(sp_data['Return'], p = 1, q = 1, mean = 'constant', vol = 'GARCH', dist = 'skewt')
# Fit the model
skewt_result = skewt_gm.fit()

# Get model estimated volatility
skewt_vol = skewt_result.conditional_volatility

# Plot model fitting results
plt.plot(skewt_vol, color = 'gold', label = 'Skewed-t Volatility')
plt.plot(normal_vol, color = 'red', label = 'Normal Volatility')
plt.plot(sp_data['Return'], color = 'grey', 
         label = 'Daily Returns', alpha = 0.4)
plt.legend(loc = 'upper right')
plt.show()
```

### Question 4: Check mean model assumptions

A GARCH model has been defined and fitted, with its result saved as gm_result. Run a command in the console to take a look at the model fitting summary, and answer the question below:

Which mean model assumption is used when defining the GARCH model?

1. Zero mean
2. Autoregressive mean
3. Constant mean

**Ans.** 2

### Question 5: Effect of mean model on volatility predictions

In practice, returns and volatility are modeled in separate processes. Typically the mean assumptions influence predicted returns, but have a minor effect on the volatility estimations.

In this exercise, you will examine the impact of GARCH model mean assumptions on volatility estimations by comparing two GARCH models. They have been defined with different mean assumptions and fitted with S&P 500 data.

The model with "constant mean" assumption has results saved in cmean_result, and estimated volatility saved in cmean_vol. The model with "AR(1)" or 1-lag autoregressive mean assumption has results saved in armean_result, and estimated volatility saved in armean_vol. The matplotlib.pyplot and numpy modules have been imported as plt and np respectively.

**Instructions**

1. Print out and review model fitting summaries of cmean_result and armean_result.
2. Plot the volatility estimation cmean_vol and armean_vol from both models.
3. Use .corrcoef() function from numpy package to calculate the correlation coefficient.

**Pre Code**

```py
# Print model summary of GARCH with constant mean
print(____.____())
# Print model summary of GARCH with AR mean
print(____.____())

# Plot model volatility 
plt.plot(____, color = 'blue', label = 'Constant Mean Volatility')
plt.plot(____, color = 'red', label = 'AR Mean Volatility')
plt.legend(loc = 'upper right')
plt.show()

# Check correlation of volatility estimations
print(np.____(____, ____)[0,1])
```

**Ans.**

```py
# Print model summary of GARCH with constant mean
print(cmean_result.summary())
# Print model summary of GARCH with AR mean
print(armean_result.summary())

# Plot model volatility 
plt.plot(cmean_vol, color = 'blue', label = 'Constant Mean Volatility')
plt.plot(armean_vol, color = 'red', label = 'AR Mean Volatility')
plt.legend(loc = 'upper right')
plt.show()

# Check correlation of volatility estimations
print(np.corrcoef(cmean_vol, armean_vol)[0,1])
```

### Question 6: Modeling of asymmetric responses of volatility

GARCH models assume positive and negative news has a symmetric impact on volatility. However, in reality the market tends to take the stairs up and the elevator down. In other words, the impact is usually asymmetric, and negative news tends to affect the volatility more than positive news.

Which of the following statements is incorrect?

1. The "news impact curve" captures the asymmetric shock effect on volatility.
2. The leverage effect refers to the observed tendency of an asset's volatility to be negatively correlated with the asset's returns.
3. GJR-GARCH can be implemented in Python by specifying o = 1 when defining the model.
4. GJR-GARCH is the only choice to model the asymmetric response of volatility to positive and negative news.

**Ans.** 4

### Question 7: Fit GARCH models to cryptocurrency

Financial markets tend to react to positive and negative news shocks very differently, and one example is the dramatic swings observed in the cryptocurrency market in recent years.

In this exercise, you will implement a GJR-GARCH and an EGARCH model respectively in Python, which are popular choices to model the asymmetric responses of volatility. You will work with a cryptocurrency dataset bitcoin_data, which contains two columns: "Close" price and "Return".

The bitcoin_data dataset has been preloaded for you, and the historical prices in the column "Close" have been plotted.

**Instructions 1/2**

1. Define a GJR-GARCH model as gjr_gm.
2. Print and review the model fitting summary of gjrgm_result.

**Pre Code**

```py
# Specify model assumptions
gjr_gm = arch_model(bitcoin_data['Return'], p = 1, q = 1, o = ____, vol = 'GARCH', dist = 't')

# Fit the model
gjrgm_result = gjr_gm.fit(disp = 'off')

# Print model fitting summary
print(____.____())
```

**Ans.**

```py
# Specify model assumptions
gjr_gm = arch_model(bitcoin_data['Return'], p = 1, q = 1, o = 1, vol = 'GARCH', dist = 't')

# Fit the model
gjrgm_result = gjr_gm.fit(disp = 'off')

# Print model fitting summary
print(gjrgm_result.summary())
```

**Instructions 2/2**

1. Define an EGARCH model as egarch_gm.
2. Print and review the model fitting summary of egarch_result.

**Pre Code**

```py
# Specify model assumptions
egarch_gm = arch_model(bitcoin_data['Return'], p = 1, q = 1, o = ____, vol = '____', dist = 't')

# Fit the model
egarch_result = egarch_gm.fit(disp = 'off')

# Print model fitting summary
print(____.____())
```

**Ans.**

```py
# Specify model assumptions
egarch_gm = arch_model(bitcoin_data['Return'], p = 1, q = 1, o = 1, vol = 'EGARCH', dist = 't')

# Fit the model
egarch_result = egarch_gm.fit(disp = 'off')

# Print model fitting summary
print(egarch_result.summary())
```

### Question 8: Compare GJR-GARCH with EGARCH

Previously you have fitted a GJR-GARCH and EGARCH model with Bitcoin return time series. In this exercise, you will compare the estimated conditional volatility from the two models by plotting their results.

The GJR-GARCH model estimated volatility is saved in gjrgm_vol, and EGARCH model estimated volatility is saved in egarch_vol. You will plot them together with actual Bitcoin return observations, which can be accessed by column ”Return” in bitcoin_data.

**Instructions**

1. Plot the actual Bitcoin returns.
2. Plot GJR-GARCH estimated volatility.
3. Plot EGARCH estimated volatility.

**Pre Code**

```py
# Plot the actual Bitcoin returns
plt.plot(bitcoin_data['____'], color = 'grey', alpha = 0.4, label = 'Price Returns')

# Plot GJR-GARCH estimated volatility
plt.plot(____, color = 'gold', label = 'GJR-GARCH Volatility')

# Plot EGARCH  estimated volatility
plt.plot(____, color = 'red', label = 'EGARCH Volatility')

plt.legend(loc = 'upper right')
plt.show()
```

**Ans.**

```py
# Plot the actual Bitcoin returns
plt.plot(bitcoin_data['Return'], color = 'grey', alpha = 0.4, label = 'Price Returns')

# Plot GJR-GARCH estimated volatility
plt.plot(gjrgm_vol, color = 'gold', label = 'GJR-GARCH Volatility')

# Plot EGARCH  estimated volatility
plt.plot(egarch_vol, color = 'red', label = 'EGARCH Volatility')

plt.legend(loc = 'upper right')
plt.show()
```

### Question 9: Why use rolling window forecast

Rolling window forecast is very popular in financial modeling, because it is adaptive to new market observations as time moves forward. It is commonly implemented with either an "expanding window" or a "fixed window" approach.

Which of the following statements is incorrect?

1. Out-of-sample forecast is preferred in financial time series modeling, because it prevents lookback bias.
2. An implicit time-series modeling assumption is that model parameters are stable over time. But this barely holds true in a turbulent market environment.
3. For a rolling-window forecast, the optimal window size is a trade-off between bias and variance.
4. The more data we include in the sample to fit a GARCH model, the better the forecast we can get.

**Ans.** 4

### Question 10: Fixed rolling window forecast

Rolling-window forecasts are very popular for financial time series modeling. In this exercise, you will practice how to implement GARCH model forecasts with a fixed rolling window.

First define the window size inside .fit(), and perform the forecast with a for-loop. Note since the window size remains fixed, both the start and end points increment after each iteration.

The S&P 500 return series has been preloaded as sp_data, and a GARCH(1,1) model has been predefined in basic_gm. The start and end points of the initial sample window has been pre-defined in start_loc and end_loc respectively.

**Instructions 1/3**

1. Define the fixed rolling window size by specifying first_obs = and last_obs = in the .fit() function.

**Pre Code**

```py
for i in range(30):
    # Specify fixed rolling window size for model fitting
    gm_result = basic_gm.fit(first_obs = i + ____, 
                             last_obs = i + ____, update_freq = 5)
```

**Ans.**

```py
for i in range(30):
    # Specify fixed rolling window size for model fitting
    gm_result = basic_gm.fit(first_obs = i + start_loc, 
                             last_obs = i + end_loc, update_freq = 5)
```

**Instructions 2/3**

1. Perform GARCH forecast and save the result of each iteration.

**Pre Code**

```py
for i in range(30):
    # Specify fixed rolling window size for model fitting
    gm_result = basic_gm.fit(first_obs = i + start_loc, 
                             last_obs = i + end_loc, update_freq = 5)
    # Conduct 1-period variance forecast 
    temp_result = gm_result.____(horizon = 1).____
    fcast = temp_result.iloc[i + end_loc]
    forecasts[fcast.name] = fcast
# Save all forecast to a DataFrame   
forecast_var = pd.DataFrame(forecasts).T
```

**Ans.**

```py
for i in range(30):
    # Specify fixed rolling window size for model fitting
    gm_result = basic_gm.fit(first_obs = i + start_loc, 
                             last_obs = i + end_loc, update_freq = 5)
    # Conduct 1-period variance forecast and save the result
    temp_result = gm_result.forecast(horizon = 1).variance
    fcast = temp_result.iloc[i + end_loc]
    forecasts[fcast.name] = fcast
# Save all forecast to a DataFrame    
forecast_var = pd.DataFrame(forecasts).T
```

**Instructions 3/3**

1. Plot the variance forecast results.

**Pre Code**

```py
for i in range(30):
    # Specify fixed rolling window size for model fitting
    gm_result = basic_gm.fit(first_obs = i + start_loc, 
                             last_obs = i + end_loc, update_freq = 5)
    # Conduct 1-period variance forecast and save the result
    temp_result = gm_result.forecast(horizon = 1).variance
    fcast = temp_result.iloc[i + end_loc]
    forecasts[fcast.name] = fcast
# Save all forecast to a dataframe    
forecast_var = pd.DataFrame(forecasts).T

# Plot the forecast variance
plt.plot(____, color = 'red')
plt.plot(sp_data.Return['2019-4-1':'2019-5-10'], color = 'green')
plt.show()
```

**Ans.**

```py
for i in range(30):
    # Specify fixed rolling window size for model fitting
    gm_result = basic_gm.fit(first_obs = i + start_loc, 
                             last_obs = i + end_loc, update_freq = 5)
    # Conduct 1-period variance forecast and save the result
    temp_result = gm_result.forecast(horizon = 1).variance
    fcast = temp_result.iloc[i + end_loc]
    forecasts[fcast.name] = fcast
# Save all forecast to a DataFrame       
forecast_var = pd.DataFrame(forecasts).T

# Plot the forecast variance
plt.plot(forecast_var, color = 'red')
plt.plot(sp_data.Return['2019-4-1':'2019-5-10'], color = 'green')
plt.show()
```

### Question 11: Compare forecast results

Different rolling window approaches can generate different forecast results. In this exercise, let's take a closer look by comparing these forecast results.

First, you will use a GARCH model to predict Bitcoin return volatility with an expanding window and a fixed rolling window approach respectively. Then you will plot both forecast results together to visualize the difference.

The Bitcoin dataset is preloaded in bitcoin_data, and feel free to explore its columns 'Close' and 'Return'. Variance forecast generated with an expanding window approach is saved in variance_expandwin, and that with a fixed rolling window approach is saved in variance_fixedwin.

**Instructions 1/3**

1. Print out the first 5 rows of variance forecast stored in variance_expandwin and variance_fixedwin respectively.

**Pre Code**

```py
# Print top 5 rows of variance forecast with an expanding window
print(____.____())
# Print top 5 rows of variance forecast with a fixed rolling window
print(____.____())
```

**Ans.**

```py
# Print top 5 rows of variance forecast with an expanding window
print(variance_expandwin.head())
# Print top 5 rows of variance forecast with a fixed rolling window
print(variance_fixedwin.head())
```

**Instructions 2/3**

1. Calculate volatility from variance forecast with an expanding window and a fixed rolling window approach respectively. Use a pre-defined function from numpy (imported as np).

**Pre Code**

```py
# Print top 5 rows of variance forecast with an expanding window
print(variance_expandwin.head())
# Print top 5 rows of variance forecast with a fixed rolling window
print(variance_fixedwin.head())

# Calculate volatility from variance forecast with an expanding window
vol_expandwin = ____.____(variance_expandwin)
# Calculate volatility from variance forecast with a fixed rolling window
vol_fixedwin = ____.____(variance_fixedwin)
```

**Ans.**

```py
# Print top 5 rows of variance forecast with an expanding window
print(variance_expandwin.head())
# Print top 5 rows of variance forecast with a fixed rolling window
print(variance_fixedwin.head())

# Calculate volatility from variance forecast with an expanding window
vol_expandwin = np.sqrt(variance_expandwin)
# Calculate volatility from variance forecast with a fixed rolling window
vol_fixedwin = np.sqrt(variance_fixedwin)
```

**Instructions 3/3**

1. Plot both volatility forecast calculated from the previous step in one chart.

**Pre Code**

```py
# Print header of variance forecasts with expanding and fixed window
print(variance_expandwin.head())
print(variance_fixedwin.head())

# Calculate volatility from variance forecast with an expanding window
vol_expandwin = np.sqrt(variance_expandwin)
# Calculate volatility from variance forecast with a fixed rolling window
vol_fixedwin = np.sqrt(variance_fixedwin)

# Plot volatility forecast with an expanding window
plt.plot(____, color = 'blue')
# Plot volatility forecast with a fixed rolling window
plt.plot(____, color = 'red')
plt.plot(bitcoin_data.Return['2019-4-1':'2019-9-15'], color = 'chocolate')
plt.show()
```

**Ans.**

```py
# Print header of variance forecasts with expanding and fixed window
print(variance_expandwin.head())
print(variance_fixedwin.head())

# Calculate volatility from variance forecast with an expanding window
vol_expandwin = np.sqrt(variance_expandwin)
# Calculate volatility from variance forecast with a fixed rolling window
vol_fixedwin = np.sqrt(variance_fixedwin)

# Plot volatility forecast with an expanding window
plt.plot(vol_expandwin, color = 'blue')
# Plot volatility forecast with a fixed rolling window
plt.plot(vol_fixedwin, color = 'red')
plt.plot(bitcoin_data.Return['2019-4-1':'2019-9-15'], color = 'chocolate')
plt.show()
```

<hr>