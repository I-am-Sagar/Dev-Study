1. **Strategy return analysis**
Welcome back! In this chapter let's discuss more about strategy performance evaluation.

2. **Obtain detailed backtest stats**
In previous lessons we have built and backtested several trading strategies and visualized the strategy performance. Now let's look into the details of the backtest statistics. Suppose we have a strategy backtest result saved in bt underscore result. We can obtain all backtest statistics by calling dot stats and saving it in a DataFrame. The DataFrame is indexed by various performance metrics. There is a lot of information here, so let's focus on several important ones.

3. **Strategy returns**
The most basic metric for strategy performance evaluation is the rate of return. A rate of return is the net gain or loss of a portfolio or asset over a specified time period, for example daily, monthly, or yearly. To obtain the rate of return for different time periods, we can slice the stats dataframe resInfo by the metric names. For example, use daily underscore mean, monthly underscore mean and yearly underscore mean to get the daily, monthly, and annual return respectively. In the code, we format the output to be float numbers with 4 decimal points using the expression after the percentage sign operator. In the output, for example, the daily return is shown as point 1966 or 19 point 66 percent.

4. **Compound annual growth rate**
Another useful return metric is called compound annual growth rate, or CAGR. It is the rate of return that would be required for an asset or trading account to grow from its beginning balance to its ending balance, assuming all the profits were reinvested at the end of each year. For example, an asset may increase in value by 8% in one year, decrease in value by 3% the following year and increase in value by 5% in the next. CAGR helps smooth returns when growth rates are expected to be volatile and inconsistent. It also makes different alternative results easier to compare. We can obtain the CAGR by slicing the stats DataFrame with the name cagr.

5. **Plot return histogram**
We can plot the return histogram to check the distribution of returns. This is easily done by calling plot underscore histograms on bt underscore result. Use the freq argument to specify the return frequencies to be plotted, for example w for weekly. By default it will plot a histogram based on daily returns.

6. **Compare strategy lookback returns**
In addition, we can compare the return results of multiple strategies side by side. Suppose we have run a strategy optimization and have two backtest results saved in bt underscore results. Call display underscore lookback underscore returns on it, and we can compare the lookback returns of both strategies.

7. **Let's practice!**
Awesome start! Now it's your turn to practice!