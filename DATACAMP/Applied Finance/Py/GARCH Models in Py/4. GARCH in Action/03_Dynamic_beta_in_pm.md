1. **Dynamic Beta in portfolio management**
In this lesson, we will learn the Beta as an important risk measure used in finance, discuss its role in portfolio management, and how to compute dynamic Beta with GARCH models.

2. **What is Beta**
In finance, stock Beta is a risk measure for an individual stock in relation to the general market. For US stocks, the S&P 500 index is commonly used as a proxy for the general market. Beta is important because it measures the risk of an investment that cannot be reduced by diversification. In other words, it does not measure the risk of an investment asset held on a stand-alone basis, but the amount of risk the investment adds to the portfolio.

3. **Beta in portfolio management**
In portfolio management, Beta is a useful gauge of investment risk of individual stocks in comparison with the general market. As the general market has a Beta of 1, a stock with Beta greater than 1 indicates the stock is theoretically riskier. For example, a stock with a Beta of 1-point-2 implies the stock is about 20% more volatile than the general market. Likewise, a stock with Beta less than 1 implies it is less volatile.

4. **Beta in CAPM**
Stock Beta is needed to compute the risk premium for an individual stock. The higher the Beta, the riskier the stock, and hence the higher the required rate of return. CAPM, which stands for "Capital Asset Pricing Model", is a classic model in portfolio management. The CAPM equation demonstrates how to determine the required rate of return of an investment asset. Use stocks for example: to compute the required rate of return, we need the risk free rate, market expected return and the stock Beta as input to the equation. Commonly risk free rate is the return of government treasury as a proxy, market expected return for stocks is S&P 500, and Beta is multiplied by the difference between market return and risk free rate, or market premium, to derive the expected extra return of a stock.

5. **Dynamic Beta with GARCH**
A stock Beta can be computed by multiplying correlation between the stock returns and market returns by the stock volatility, then divided by the market volatility. The correlation and volatility are estimated from the GARCH models, which take account the time-varying characteristic of risks.

6. **Calculate dynamic Beta in Python**
The sample code demonstrates how to calculate dynamic stock Beta in relation to the general market, which use the S&P 500 index as a proxy. First, we can estimate the correlation from the GARCH standardized residuals. Recall the standardized residuals can be computed using the fitted GARCH model. Then the stock Beta can be computed by multiplying the correlation and stock volatility, then divided by the market volatility.

7. **Let's practice!**
Now it's your turn. Happy practice!