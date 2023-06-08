1. **Why do we need GARCH models**
Hi, My name is Chelsea Yang. I am a quantitative analyst working in finance, and a data science enthusiast. In this course, we will learn about GARCH models.

2. **Course overview**
GARCH stands for "Generalized AutoRegressive Conditional Heteroskedasticity", and it is a popular approach to model volatility. This course contains 4 chapters. In chapter 1 "GARCH Model Fundamentals", we will discuss what GARCH models are, why we use them, and how to apply GARCH models in Python. In chapter 2 "GARCH Model Configuration", we will dive into specific GARCH model assumptions, and learn how to define a practical model for financial time series data. In chapter 3 "Model Performance Evaluation", we will learn various metrics we can use to assess model performance, and select a better model. In the last chapter "GARCH in Action", we will learn some practical applications of GARCH models in financial risk and portfolio management, which include calculations of value-at-risk, dynamic covariance, and stock Beta.

3. **What is volatility**
So first, what exactly is "volatility"? In finance, volatility is a statistical measure of the dispersion of asset returns over time. It is often computed as the standard deviation or variance of price returns. In this course we will use the term "volatility" to describe standard deviation or variance interchangeably. Volatility describes uncertainties surrounding the potential price movement of financial assets. It is an essential concept widely used in risk management, portfolio optimization, and more. And it has been one of the most active areas of research in empirical finance and time series analysis. In general, the higher the volatility, the riskier a financial asset.

4. **How to compute volatility**
We can compute the volatility as the standard deviation of price returns following three easy steps. Step 1 is to calculate the returns as percentage price changes. Step 2 is to calculate the sample mean return of a chosen n-period. And step 3 is to derive the sample standard deviation. Also recall standard deviation is the square root of variance.

5. **Compute volatility in Python**
Before you get a headache by looking at the math formulas, the good news is you can implement them in Python easily. To compute percentage changes as returns, apply "pct_change()" method from the "pandas" package to the price data. Then apply "std()" method to the return data to compute the standard deviation. Voila!

6. **Volatility conversion**
Assume we measure volatility as the standard deviation of returns, then monthly volatility can be obtained by multiplying daily volatility by the square root of 21, which is the average number or trading days in a month. Similarly, annual volatility can be obtained by multiplying daily volatility by the square root of 252, which is the average number or trading days in a year.

7. **The challenge of volatility modeling**
A common assumption in time series modeling is that volatility remains constant over time. However, heteroskedasticity, literally means "different dispersion" in ancient Greek, is frequently observed in financial return data. Volatility tends to increase or decrease systematically over time.

8. **Detect heteroskedasticity**
A straightforward way to detect heteroskedasticity in a time series is to plot the data and observe its behavior over time. Compared with homoskedastic data, the volatility of heteroskedastic data does not appear stable, but exhibits time-dependent fluctuations.

9. **Volatility clustering**
Volatility index (or VIX), derived from S&P 500 option prices, is a barometer of the US stock market expected volatility and risk sentiment. As shown in the historical price chart, VIX demonstrates "volatility clustering", that is, periods of high or low volatility tend to persist. Large price changes are very likely to be followed by more large changes, and vice versa. Volatility clustering happens because markets tend to respond to new information shocks with dramatic price movement, and it takes time for the shocking effect to resolve and dissipate.

10. **Let's practice!**
Now let's practice what you have learned so far!