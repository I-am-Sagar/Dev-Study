1. **Volatility models for asymmetric shocks**
So far GARCH models assume symmetric shocks on volatility. In other words, positive or negative changes in price returns would have the same impact on volatility. What if this assumption does not hold? In this lesson, let's see how to model the asymmetric shocks on volatility.

2. **Asymmetric shocks in financial data**
In the real financial world, market tends to take the stairs up and elevators down. When things are good, prices go up slowly and steadily; when things turn bad, like during a financial crisis, everyone panics and prices take a sharp plunge.

3. **Leverage effect**
The leverage effect refers to the observed tendency of an asset's volatility to be negatively correlated with the asset's returns. Typically, rising stock prices are accompanied by declining volatility, and vice versa. An economic explanation of this phenomenon is: as equity prices decline, companies have relatively less equity values compared to their debt values. In other words, they become more leveraged since their debt to equity ratios go up, implying their stocks become riskier.

4. **GJR-GARCH**
GJR-GARCH is developed to address the asymmetric shock effect on volatility. Its equation is very similar to the standard GARCH model, except it adds a conditional parameter. When return shocks are negative, the conditional parameter will be included in the equation to account for the additional impact.

5. **GJR-GARCH in Python**
GJR-GARCH can be easily implemented in Python by specifying the "o" to be 1 when defining the model.

6. **EGARCH**
Another popular model choice to address the asymmetric shock effect is the EGARCH model. E stands for "exponential" since EGARCH is based on log variance instead of variance itself. The actual equation is a bit complicated so we will skip the nitty-gritty details. An intuitive takeaway is: EGARCH adds a conditional component to model the asymmetry in shocks similar to the GJR-GARCH. Also, since the equation is based on log variance, it does not require non-negative constraints on alpha, beta. Therefore it works faster for likelihood maximization during model fitting.

7. **EGARCH in Python**
EGARCH is implemented in Python by specifying the "o" to be 1, and "vol" to be "EGARCH" when defining the model

8. **Which model to use**
Both GJR-GARCH and EGARCH try to address the asymmetry shocks on volatility, and which model is better depends on the data. In practice, try fitting different models to the same dataset and select the one with the best performance. We will discuss model performance evaluation in more details in chapter 3.

9. **Let's practice!**
Now it's your turn!