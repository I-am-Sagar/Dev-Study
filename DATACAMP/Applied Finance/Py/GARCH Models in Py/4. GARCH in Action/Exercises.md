### Question 1: VaR concept

VaR is an important concept in financial risk management to quantify the downside risk. With GARCH models, VaR can incorporate the time-varying characteristics of volatility and give more realistic estimations of potential losses.

Which of the following statements is incorrect?

1. A 1-day 5% VaR of one million dollars means there is a 5% probability the portfolio will fall in value by one million dollars or less over a 1-day period.
2. Incorporating GARCH models in the VaR calculation can help make more realistic loss estimations.
3. A loss which exceeds the VaR value is termed a "VaR exceedance".

**Ans.** 1

### Question 2: Compute parametric VaR

In this exercise, you will practice estimating dynamic 5% daily VaRs with a parametric approach.

Recall there are three steps to perform a forward VaR estimation. Step 1 is to use a GARCH model to make variance forecasts. Step 2 is to obtain the GARCH forward-looking mean and volatility. And Step 3 is to compute the quantile according to a given confidence level. The parametric approach estimates quantiles from an assumed distribution assumption.

A GARCH model has been fitted with historical Bitcoin return data up to 1/1/2019, then it has generated mean and variance forecasts, saved in mean_forecast and variance_forecast respectively. The GARCH model assumes a Student's t-distribution, and its v (degree of freedom) is saved in nu.

**Instructions**

1. Compute 0.05 quantile from the assumed Student's t-distribution.
2. Calculate VaR using mean_forecast, variance_forecast from the GARCH model and the quantile from the previous step.

**Pre Code**

```py
# Obtain the parametric quantile
q_parametric = basic_gm.____.____(____, nu)
print('5% parametric quantile: ', q_parametric)
    
# Calculate the VaR
VaR_parametric = ____.values + np.sqrt(____).values * ____
# Save VaR in a DataFrame
VaR_parametric = pd.DataFrame(VaR_parametric, columns = ['5%'], index = variance_forecast.index)

# Plot the VaR
plt.plot(VaR_parametric, color = 'red', label = '5% Parametric VaR')
plt.scatter(variance_forecast.index,bitcoin_data.Return['2019-1-1':], color = 'orange', label = 'Bitcoin Daily Returns' )
plt.legend(loc = 'upper right')
plt.show()
```

**Ans.**

```py
# Obtain the parametric quantile
q_parametric = basic_gm.distribution.ppf(0.05, nu)
print('5% parametric quantile: ', q_parametric)
    
# Calculate the VaR
VaR_parametric = mean_forecast.values + np.sqrt(variance_forecast).values * q_parametric
# Save VaR in a DataFrame
VaR_parametric = pd.DataFrame(VaR_parametric, columns = ['5%'], index = variance_forecast.index)

# Plot the VaR
plt.plot(VaR_parametric, color = 'red', label = '5% Parametric VaR')
plt.scatter(variance_forecast.index,bitcoin_data.Return['2019-1-1':], color = 'orange', label = 'Bitcoin Daily Returns' )
plt.legend(loc = 'upper right')
plt.show()
```

### Question 3: Compute empirical VaR

In this exercise, you will practice estimating dynamic 5% daily VaRs with an empirical approach.

The difference between parametric VaR and empirical VaR is how the quantiles are estimated. The parametric approach estimates quantiles from an assumed distribution assumption, while the empirical approach estimates quantiles from an observed distribution of the standardized residuals.

You will use the same GARCH model as the previous exercise. The mean and variance forecasts are saved in mean_forecast and variance_forecast respectively. The empirical standardized residuals have also been calculated and saved in std_resid.

**Instructions**

1. Compute 0.05 quantile from the GARCH standardized residuals std_resid.
2. Calculate VaR using mean_forecast, variance_forecast from the GARCH model and the quantile from the previous step.

**Pre Code**

```py
# Obtain the empirical quantile
q_empirical = ____.____(____)
print('5% empirical quantile: ', q_empirical)

# Calculate the VaR
VaR_empirical = ____.values + np.sqrt(____).values * ____
# Save VaR in a DataFrame
VaR_empirical = pd.DataFrame(VaR_empirical, columns = ['5%'], index = variance_forecast.index)

# Plot the VaRs
plt.plot(VaR_empirical, color = 'brown', label = '5% Empirical VaR')
plt.plot(VaR_parametric, color = 'red', label = '5% Parametric VaR')
plt.scatter(variance_forecast.index,bitcoin_data.Return['2019-1-1':], color = 'orange', label = 'Bitcoin Daily Returns' )
plt.legend(loc = 'upper right')
plt.show()
```

**Ans.**

```py
# Obtain the empirical quantile
q_empirical = std_resid.quantile(0.05)
print('5% empirical quantile: ', q_empirical)

# Calculate the VaR
VaR_empirical = mean_forecast.values + np.sqrt(variance_forecast).values * q_empirical
# Save VaR in a DataFrame
VaR_empirical = pd.DataFrame(VaR_empirical, columns = ['5%'], index = variance_forecast.index)

# Plot the VaRs
plt.plot(VaR_empirical, color = 'brown', label = '5% Empirical VaR')
plt.plot(VaR_parametric, color = 'red', label = '5% Parametric VaR')
plt.scatter(variance_forecast.index,bitcoin_data.Return['2019-1-1':], color = 'orange', label = 'Bitcoin Daily Returns' )
plt.legend(loc = 'upper right')
plt.show()
```

### Question 4: Covariance concept

Covariance is used in various areas in portfolio management. With GARCH models, one can compute the dynamic covariance to incorporate the time-varying characteristic of volatility. And in Modern Portfolio Theory, covariance demonstrates the diversification benefit of combining different types of assets.

Which of the following statements is incorrect?

1. MPT (Modern Portfolio Theory) states that given a certain level of expected return, one can construct an optimal portfolio with the minimum possible risk.
2. When two asset prices tend to move together in the same direction, they have a negative covariance, and vice versa.
3. Dynamic covariance can be computed by multiplying correlation coefficient between asset returns by their volatility from GARCH models.

**Ans.** 2

### Question 5: Compute GARCH covariance

Covariance describes the relationship of movement between two price return series. Recall dynamic covariance can be computed by ρ * σ1 * σ2, where σ1, σ2 are volatility estimates from GARCH models, and ρ is the simple correlation between GARCH standardized residuals.

In this exercise, you will practice computing dynamic covariance with GARCH models. Specifically you will use two foreign exchange time series data: EUR/USD and USD/CAD (shown in the plot). Their price returns have been fitted by two GARCH models, and the volatility estimates are saved in vol_eur and vol_cad. In addition, their standardized residuals are saved in resid_eur and resid_cad respectively. In addition, the numpy package has been imported as np.

**Instructions**

1. Calculate correlation between GARCH standardized residuals resid_eur and resid_cad.
2. Calculate covariance with GARCH volatility vol_eur, vol_cad and the correlation computed in the previous step.
3. Plot the calculated covariance.

**Pre Code**

```py
# Calculate correlation
corr = np.____(____, ____)[0,1]
print('Correlation: ', corr)

# Calculate GARCH covariance
covariance =  ____ * ____ * ____

# Plot the data
plt.plot(____, color = 'gold')
plt.title('GARCH Covariance')
plt.show()
```

**Ans.**

```py
# Calculate correlation
corr = np.corrcoef(resid_eur, resid_cad)[0,1]
print('Correlation: ', corr)

# Calculate GARCH covariance
covariance =  corr * vol_eur * vol_cad

# Plot the data
plt.plot(covariance, color = 'gold')
plt.title('GARCH Covariance')
plt.show()
```

### Question 6: Compute dynamic portfolio variance

In this exercise, you will practice computing the variance of a simple two-asset portfolio with GARCH dynamic covariance.

The Modern Portfolio Theory states that there is an optimal way to construct a portfolio to take advantage of the diversification effect, so one can obtain a desired level of expected return with the minimum risk. This effect is especially evident when the covariance between asset returns is negative.

Suppose you have a portfolio with only two assets: EUR/USD and CAD/USD currency pairs. Their variance from the GARCH models have been saved in variance_eur and variance_cad, and their covariance has been calculated and saved in covariance. Compute the overall portfolio variances by varying the weights of the two assets, and visualize their differences.

**Instructions**

1. Set the EUR/USD weight Wa1 in portfolio a to 0.9, and Wb1 in portfolio b to 0.5.
2. Calculate the variance portvar_a for portfolio a with variance_eur, variance_cad and covariance; do the same to compute portvar_b for portfolio b.

**Pre Code**

```py
# Define weights
Wa1 = ____
Wa2 = 1 - Wa1
Wb1 = ____
Wb2 = 1 - Wb1

# Calculate portfolio variance
portvar_a = Wa1**2 * ____ + Wa2**2 * ____ + 2*Wa1*Wa2 *____
portvar_b = Wb1**2 * ____ + Wb2**2 * ____ + 2*Wb1*Wb2*____

# Plot the data
plt.plot(portvar_a, color = 'green', label = 'Portfolio a')
plt.plot(portvar_b, color = 'deepskyblue', label = 'Portfolio b')
plt.legend(loc = 'upper right')
plt.show()
```

**Ans.**

```py
# Define weights
Wa1 = 0.9
Wa2 = 1 - Wa1
Wb1 = 0.5
Wb2 = 1 - Wb1

# Calculate portfolio variance
portvar_a = Wa1**2 * variance_eur + Wa2**2 * variance_cad + 2*Wa1*Wa2*covariance
portvar_b = Wb1**2 * variance_eur + Wb2**2 * variance_cad + 2*Wb1*Wb2*covariance

# Plot the data
plt.plot(portvar_a, color = 'green', label = 'Portfolio a')
plt.plot(portvar_b, color = 'deepskyblue', label = 'Portfolio b')
plt.legend(loc = 'upper right')
plt.show()
```

### Question 7: Beta concept

Beta is a popular tool used in portfolio management to gauge investment risks. A stock Beta measures the volatility of an individual stock in relation to the general market. Dynamic Beta can be computed with GARCH models to account for the time-varying quality of volatility.

Which of the following statements is incorrect?

1. Beta measures the risk of an investment that cannot be reduced by diversification.
2. A stock with a Beta greater than 1 indicates it is more volatile than the general market.
3. The greater the stock Beta, the lower the required rate of return of the stock.

**Ans.** 3

### Question 8: Compute dynamic stock Beta

Suppose Elon Musk is your idol and you are considering investing in some Tesla stocks. As a shrewd portfolio manager, you decide to do due diligence by checking Tesla stock Beta over the years. Beta is a measure of a stock's volatility in relation to the market, which can serve as a gauge of investment risks.

Recall you need the stock volatility, market (S&P 500 as a proxy) volatility and their return correlation to compute Beta. Correlation can be computed from standardized residuals.

Model fitted volatility has been preloaded for Tesla in teslaGarch_vol, and for S&P 500 in spGarch_vol. In addition, model standardized residuals are preloaded in teslaGarch_resid and spGarch_resid respectively.

**Instructions**

1. Compute the correlation coefficient between Tesla and S&P 500 using standardized residuals from fitted GARCH models (teslaGarch_resid, spGarch_resid).
2. Compute Tesla stock Beta using Tesla volatility (teslaGarch_vol), S&P 500 volatility (spGarch_vol) and correlation computed from the previous step.

**Pre Code**

```py
# Compute correlation between SP500 and Tesla
correlation = np.corrcoef(____, ____)[0, 1]

# Compute the Beta for Tesla
stock_beta = ____ * (____ / ____)

# Plot the Beta
plt.title('Tesla Stock Beta')
plt.plot(stock_beta)
plt.show()
```

**Ans.**

```py
# Compute correlation between SP500 and Tesla
correlation = np.corrcoef(teslaGarch_resid, spGarch_resid)[0, 1]

# Compute the Beta for Tesla
stock_beta = correlation * (teslaGarch_vol / spGarch_vol)

# Plot the Beta
plt.title('Tesla Stock Beta')
plt.plot(stock_beta)
plt.show()
```
<hr>