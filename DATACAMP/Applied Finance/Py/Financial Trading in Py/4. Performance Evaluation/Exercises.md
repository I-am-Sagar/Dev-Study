### Question 1: Review return results of a backtest

You implemented a trend-following strategy using a simple moving average indicator. You backtested it using the Amazon stock historical price data from 2019 to 2020, and the result plot is shown on the right. Now you would like to review the return statistics from the backtest result.

The bt backtest result has been provided in bt_result and is ready to use.

**Instructions**

1. Obtain all backtest stats from bt_result and save them in resInfo.
2. Print the daily, monthly, and yearly returns from resInfo.
3. Print the compound annual growth rate (CAGR) from resInfo.

**Pre Code**

```py
# Obtain all backtest stats
resInfo = ____

# Get daily, monthly, and yearly returns
print('Daily return: %.4f'% ____)
print('Monthly return: %.4f'% ____)
print('Yearly return: %.4f'% ____)

# Get the compound annual growth rate
print('Compound annual growth rate: %.4f'% ____)
```

**Ans.**

```py
# Obtain all backtest stats
resInfo = bt_result.stats

# Get daily, monthly, and yearly returns
print('Daily return: %.4f'% resInfo.loc['daily_mean'])
print('Monthly return: %.4f'% resInfo.loc['monthly_mean'])
print('Yearly return: %.4f'% resInfo.loc['yearly_mean'])

# Get the compound annual growth rate
print('Compound annual growth rate: %.4f'% resInfo.loc['cagr'])
```

### Question 2: Plot return histograms of a backtest

Continue with the same strategy backtest result from the previous exercise. Now you would like to plot return histograms to further examine the characteristics of the return distribution.

The bt backtest result has been provided in bt_result and is ready to use. In addition, matplotlib.pyplot has been imported as plt.

**Instructions 1/2**

1. Plot the daily return histogram using bt_result, setting bins to 50.

**Pre Code**

```py
# Plot the daily return histogram
bt_result.____(____)
plt.show()
```

**Ans.**

```py
# Plot the daily return histogram
bt_result.plot_histograms(bins=50)
plt.show()
```

**Instructions 2/2**

1. Plot the weekly return histogram using bt_result, setting bins to 50.

**Pre Code**

```py
# Plot the weekly return histogram
bt_result.____(____, ____)
plt.show()
```

**Ans.**

```py
# Plot the weekly return histogram
bt_result.plot_histograms(bins=50, freq='w')
plt.show()
```

### Question 3: Compare return results of multiple strategies

With the same strategy using a simple moving average indicator, you also conducted a strategy optimization by varying the lookback periods of the moving average indicator from 30 to 50 days. You backtested both strategies using the Google stock historical price data from 2017 to 2020. Now you are about to compare the backtest results.

The bt backtest results of both strategies have been provided in bt_results and are ready to use.

**Instructions 1/2**

1. Plot the backtest results from bt_results.
2. Obtain the lookback return results from bt_results for both strategies.

**Pre Code**

```py
# Plot the backtest result
____(title='Backtest result')
plt.show()

# Get the lookback returns
lookback_returns = ____
print(lookback_returns)
```

**Ans.**

```py
# Plot the backtest result
bt_results.plot(title='Backtest result')
plt.show()

# Get the lookback returns
lookback_returns = bt_results.display_lookback_returns()
print(lookback_returns)
```

**Instructions 2/2**

According to the backtest results, which strategy has better performance?

1. Strategy 1
2. Strategy 2

**Ans.** 2

### Question 4: Review performance with drawdowns

You implemented a signal-based strategy using two moving average indicators. You performed a backtest using the Tesla stock historical price data from 2019 to 2020, and the result plot is shown on the right. Now you would like to evaluate the strategy performance, specifically the downside volatility, by reviewing the drawdown result from the backtest.

The bt backtest result has been provided in bt_result and is ready to use.

**Instructions**

1. Obtain all backtest stats from bt_result and save them in resInfo.
2. Get the average drawdown from resInfo.
3. Get the average drawdown days from resInfo.

**Pre Code**

```py
# Obtain all backtest stats
resInfo = ____

# Get the average drawdown
avg_drawdown = ____
print('Average drawdown: %.2f'% avg_drawdown)

# Get the average drawdown days
avg_drawdown_days = ____
print('Average drawdown days: %.0f'% avg_drawdown_days)
```

**Ans.**

```py
# Obtain all backtest stats
resInfo = bt_result.stats

# Get the average drawdown
avg_drawdown = resInfo.loc['avg_drawdown']
print('Average drawdown: %.2f'% avg_drawdown)

# Get the average drawdown days
avg_drawdown_days = resInfo.loc['avg_drawdown_days']
print('Average drawdown days: %.0f'% avg_drawdown_days)
```

### Question 5: Calculate and review the Calmar ratio

Continue with the same strategy. From the previous exercise, you know that the average drawdown is approximately 11%, and that the average period is 22 days. Now you would like to get a better understanding of the risk-return profile of it. You plan to review the CAGR, max drawdown, then use them to calculate the Calmar ratio and assess the result.

The resInfo DataFrame that contains all backtest statistics has been provided for you.

**Instructions**

1. Get the compound annual growth rate (CAGR) from resInfo.
2. Get the max drawdown from resInfo.
3. Calculate the Calmar ratio using cagr and max_drawdown.
4. Obtain the Calmar ratio directly from resInfo and review it.

**Pre Code**

```py
# Get the CAGR
cagr = ____
print('Compound annual growth rate: %.4f'% cagr)

# Get the max drawdown
max_drawdown = ____
print('Maximum drawdown: %.2f'% max_drawdown)

# Calculate Calmar ratio manually
calmar_calc = ____ / ____ * (-1)
print('Calmar Ratio calculated: %.2f'% calmar_calc)

# Get the Calmar ratio
calmar = ____
print('Calmar Ratio: %.2f'% calmar)
```

**Ans.**

```py
# Get the CAGR
cagr = resInfo.loc['cagr']
print('Compound annual growth rate: %.4f'% cagr)

# Get the max drawdown
max_drawdown = resInfo.loc['max_drawdown']
print('Maximum drawdown: %.2f'% max_drawdown)

# Calculate Calmar ratio manually
calmar_calc = cagr / max_drawdown * (-1)
print('Calmar Ratio calculated: %.2f'% calmar_calc)

# Get the Calmar ratio
calmar = resInfo.loc['calmar']
print('Calmar Ratio: %.2f'% calmar)
```

### Question 6: Evaluate strategy performance by Sharpe ratio

The Sharpe ratio is a risk-adjusted return measure developed by Nobel laureate William F. Sharpe. It is calculated as the average return over the risk-free rate divided by the standard deviation of the excess return.

You will calculate and review the Sharpe ratio of a signal-based strategy. The strategy generates long or short signals using two moving average indicators, and has been backtested using the 3-year historical price data of the Google stock. The backtest statistics has been provided in resInfo.

**Instructions**

1. Get annual return and volatility from resInfo and save them in yearly_mean and yearly_vol respectively.
2. Calculate the Sharpe ratio manually using yearly_return and yearly_vol.
3. Print the annualized Sharpe ratio directly obtained from resInfo.

**Pre Code**

```py
# Get annual return and volatility
yearly_return = ____
print('Annual return: %.2f'% yearly_return)
yearly_vol = ____
print('Annual volatility: %.2f'% yearly_vol)

# Calculate the Sharpe ratio manually
sharpe_ratio = ____ / ____
print('Sharpe ratio calculated: %.2f'% sharpe_ratio)

# Print the Sharpe ratio
print('Sharpe ratio %.2f'% ____)
```

**Ans.**

```py
# Get annual return and volatility
yearly_return = resInfo.loc['yearly_mean']
print('Annual return: %.2f'% yearly_return)
yearly_vol = resInfo.loc['yearly_vol']
print('Annual volatility: %.2f'% yearly_vol)

# Calculate the Sharpe ratio manually
sharpe_ratio = yearly_return / yearly_vol
print('Sharpe ratio calculated: %.2f'% sharpe_ratio)

# Print the Sharpe ratio
print('Sharpe ratio %.2f'% resInfo.loc['yearly_sharpe'])
```

### Question 7: Evaluate strategy performance by Sortino ratio

The Sortino ratio is the excess return over the risk-free rate divided by the downside deviation, and thus it measures the excess return to "bad" volatility. In other words, it doesn't penalize the volatility of positive excess returns.

You will use the Sortino ratio to evaluate the same strategy from the previous exercise and see if it tells a different story. As a reminder, the strategy is a signal-based strategy using two moving average indicators. The strategy backtest statistic using Google 3-year historical stock price data has been loaded in resInfo. The Sharpe ratios have been printed for you and are visible in the console.

**Instructions 1/2**

1. Print the annual Sortino ratio from resInfo.
2. Print the monthly Sortino ratio from resInfo.

**Pre Code**

```py
# Print annual Sortino ratio
yearly_sortino = ____
print('Annual Sortino ratio: %.2f'% yearly_sortino)

# Print monthly Sortino ratio
monthly_sortino = ____
print('Monthly Sortino ratio %.2f'% monthly_sortino)
```

**Ans.**

```py
# Print annual Sortino ratio
yearly_sortino = resInfo.loc['yearly_sortino']
print('Annual Sortino ratio: %.2f'% yearly_sortino)

# Print monthly Sortino ratio
monthly_sortino = resInfo.loc['monthly_sortino']
print('Monthly Sortino ratio %.2f'% monthly_sortino)
```

**Instructions 2/2**

Which one below is not a conclusion you would draw based on the Sharpe ratio and Sortino ratio result?

1. The strategy performance is suboptimal looking at its Sharpe Ratio result.
2. The strategy performance is excellent looking at its Sortino Ratio result.
3. The strategy performance is suboptimal looking at its Sortino Ratio result.

**Ans.** 3

<hr>