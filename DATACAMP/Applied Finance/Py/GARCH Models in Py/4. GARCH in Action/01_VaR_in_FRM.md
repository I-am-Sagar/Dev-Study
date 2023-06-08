1. **VaR in financial risk management**
Hi and welcome back. Great progress! So far you have learned how to define realistic GARCH models, make forecasts and evaluate model performance. In this last chapter of the course, we will discuss some practical applications of GARCH models in the financial world. Let's start with VaR in risk management.

2. **Risk management mindset**
Regarding financial investing, Warren Buffett once famously said: Rule number 1: Never lose money. Rule number 2 Never forget Rule number 1. Of course it is unrealistic to never lose money. But what Buffett was referring to was the mindset of a sensible investor. Don't go into an investment with a cavalier attitude that it's OK to lose. Always be prepared and be informed. Successful investors does not neglect the importance of risk management. They are always aware of the downside risk.

3. **What is VaR**
VaR stands for "Value at Risk". It is an important concept in risk management to quantify the potential losses. VaR is always discussed with three ingredients: a portfolio, a time horizon and a probability. VaR value indicates given a time horizon, the portfolio is likely to lose at least this much money given a specified probability.

4. **VaR examples**
For example, a 1-day 5% VaR of one million dollars means there is a 5% probability the portfolio will fall in value by 1 million dollars or more over a 1-day period. Likewise, a 10-day 1% VaR of $9 million means there is a 1% probability the portfolio will fall in value by 9 million dollars or more over a 10-day period. This can also be phrased as over the 10-day period, there is a 99% probability the portfolio will lose less than 9 million dollars.

5. **VaR in risk management**
In financial risk management, VaR is designed to gauge potential portfolio losses and set risk limits. When the portfolio loss exceeds the VaR, it is called a VaR exceedance. In the plot, the returns plotted by orange dots circled in black are examples of VaR exceedance, since they have fallen below the VaR threshold line in red. Suppose a 5% daily VaR and 250 trading days in a year, a valid VaR model should have less than 13 VaR exceedances within a year, that is 5% times 250. If there are more exceedances, the model is underestimating the risk.

6. **Dynamic VaR with GARCH**
During financial crisis, volatility clusters and losses tend to occur several days in a row. GARCH models incorporate the time-varying characteristic of volatility, hence enable us to make more realistic VaR estimation. VaR can be calculated as the portfolio expected mean return plus a quantile times the portfolio volatility. The quantile depends on a chosen confidence level, say 95% or 99%. Portfolio expected mean and volatility can be obtained from GARCH model forecast. Note we get variance forecast directly from GARCH model, so we need to compute its square root before plugging in the VaR calculation.

7. **Dynamic VaR calculation**
Here are how to estimate dynamic VaR step by step. VaR is forward looking, so first we fit a GARCH model and use it to make variance forecast.

8. **Dynamic VaR calculation (cont.)**
Step 2 is to obtain forward-looking mean and volatility from the forecast. And step 3 is to obtain the quantile according to a given confidence level. With GARCH, the quantile can be estimated parametrically with an assumed distribution, or empirically using historical data. Next let's discuss the parametric VaR and empirical VaR approach one by one.

9. **Parametric VaR**
The parametric VaR with GARCH is estimated using quantiles from a parametric approach. That is, it is based on GARCH assumed distribution of the standardized residuals. The Python code demonstrates how to implement it.

10. **Empirical VaR**
The empirical VaR with GARCH is estimated with an empirical approach. That is, it is based on the observed distribution of the GARCH standardized residuals. The Python code demonstrates how to implement it.

11. **Let's practice!**
That is a lot to digest. Let's practice!