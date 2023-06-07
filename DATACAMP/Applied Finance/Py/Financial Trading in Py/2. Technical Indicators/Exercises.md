### Question 1: Calculate and plot two EMAs

A 12-period EMA and 26-period EMA are two moving averages used in calculating a more complex indicator called MACD (Moving Average Convergence Divergence). The MACD turns two EMAs into a momentum indicator by subtracting the longer EMA from the shorter one. Before learning more about MACD, you want to get familiar with its components first. You decide to calculate two EMAs using the Google daily stock prices and plot them in one chart.

The daily historical price data of the Google stock has been loaded in stock_data. Also, talib has been imported for you, and matplotlib.pyplot has been imported as plt.

**Instructions**

1. Calculate a 12-day EMA of the Close price and save it in a new column EMA_12.
2. Calculate a 26-day EMA of the Close price and save it in a new column EMA_26.
3. Plot the 12-day EMA and 26-day EMA together with the Close price.

**Pre Code**

```py
# Calculate 12-day EMA
stock_data['EMA_12'] = ____(stock_data['____'], ____)
# Calculate 26-day EMA
stock_data['EMA_26'] = ____

# Plot the EMAs with price
____(stock_data['____'], label='EMA_12')
____(stock_data['____'], label='EMA_26')
____(stock_data['____'], label='Close')

# Customize and show the plot
plt.legend()
plt.title('EMAs')
plt.show()
```

**Ans.**

```py
# Calculate 12-day EMA
stock_data['EMA_12'] = talib.EMA(stock_data['Close'], timeperiod=12)
# Calculate 26-day EMA
stock_data['EMA_26'] = talib.EMA(stock_data['Close'], timeperiod=26)

# Plot the EMAs with price
plt.plot(stock_data['EMA_12'], label='EMA_12')
plt.plot(stock_data['EMA_26'], label='EMA_26')
plt.plot(stock_data['Close'], label='Close')

# Customize and show the plot
plt.legend()
plt.title('EMAs')
plt.show()
```

### Question 2: SMA vs. EMA

SMA and EMA are both commonly-used trend indicators. SMA gives equal weight to all data points, while EMA applies more weight to recent data points. You have some Google stock price data and want to decide on a moving average indicator to use. You plan to calculate both the SMA and EMA with the same lookback period and plot them in one chart.

The daily historical price data of the Google stock has been loaded in stock_data. Also, talib has been imported for you, and matplotlib.pyplot has been imported as plt.

**Instructions**

1. Calculate a 50-day SMA of the Close price and save it in a new column SMA.
2. Calculate a 50-day EMA of the Close price and save it in a new column EMA.
3. Plot the SMA and EMA together with the Close price.

**Pre Code**

```py
# Calculate the SMA
stock_data['SMA'] = ____(stock_data['____'], ____)
# Calculate the EMA
stock_data['EMA'] = ____(stock_data['____'], ____)

# Plot the SMA, EMA with price
____(stock_data['____'], label='SMA')
____(stock_data['____'], label='EMA')
____(stock_data['____'], label='Close')

# Customize and show the plot
plt.legend()
plt.title('SMA vs EMA')
plt.show()
```

**Ans.**

```py
# Calculate the SMA
stock_data['SMA'] = talib.SMA(stock_data['Close'], timeperiod=50)
# Calculate the EMA
stock_data['EMA'] = talib.EMA(stock_data['Close'], timeperiod=50)

# Plot the SMA, EMA with price
plt.plot(stock_data['SMA'], label='SMA')
plt.plot(stock_data['EMA'], label='EMA')
plt.plot(stock_data['Close'], label='Close')

# Customize and show the plot
plt.legend()
plt.title('SMA vs EMA')
plt.show()
```

### Question 3: Understand the ADX

ADX stands for Average Directional Movement Index. It is used by traders to quantify the overall strength of a trend.

Which of the following statements is incorrect?

1. In general, an ADX value below 25 suggests the asset price is not trending strongly, or merely moving sideways.
2. ADX can suggest the direction of a trend, either bullish or bearish.
3. ADX is bounded between 0 and 100.

**Ans.** 2

### Question 4: Calculate the ADX

The average directional movement index (ADX) was developed by J. Welles Wilder as an indicator of trend strength. It combines two other indicators, the plus directional index (+DI) and minus directional indicator (-DI), and is obtained using lengthy calculations. However, with Python, you can calculate it with one line of code. In this exercise, you will implement your first ADX indicator using daily price data of the Tesla stock.

The historical daily price data has been loaded in stock_data. Also, talib has been imported for you.

**Instructions**

1. Calculate the ADX using the appropriate function from talib, and the High, Low and Close columns in the stock_data. Save it in a new column ADX_14.
2. Calculate the ADX . This time change the default time period to 21, and save it in a new column ADX_21.
3. Print the last five rows of stock_data.

**Pre Code**

```py
# Calculate the ADX with the default time period
stock_data['ADX_14'] = ____(stock_data['____'],
                            stock_data['____'], 
                            stock_data['____'])

# Calculate the ADX with the time period set to 21
stock_data['ADX_21'] = ____

# Print the last five rows
print(stock_data.____())
```

**Ans.**

```py
# Calculate the ADX with the default time period
stock_data['ADX_14'] = talib.ADX(stock_data['High'],
                                 stock_data['Low'], 
                                 stock_data['Close'])

# Calculate the ADX with the time period set to 21
stock_data['ADX_21'] = talib.ADX(stock_data['High'],
                                 stock_data['Low'], 
                                 stock_data['Close'], 
                                 timeperiod=21)
# Print the last five rows
print(stock_data.tail())
```

### Question 5: Visualize the ADX

The ADX can quantify the strength of a trend, but does not suggest the bullish or bearish trend direction. Typically an ADX value above 25 indicates that a trending market is present. To better understand it, you will calculate the ADX and plot it along with the price data.

As in the previous exercise, you will use historical daily price data of the Tesla stock, which has been loaded in as stock_data. Also, talib has been imported for you, and matplotlib.pyplot has been imported as plt.

**Instructions 1/2**

1. Calculate the 14-day (by default) ADX, and save it in a column called ADX.
2. Create two subplots named ax1 and ax2.
3. Plot the Close price in the subplot ax1 on top and ADX in the subplot ax2 at the bottom.

**Pre Code**

```py
# Calculate ADX
stock_data['ADX'] = ____(stock_data['____'], stock_data['____'], stock_data['____'])

# Create subplots
fig, (ax1, ax2) = ____(2)

# Plot ADX with the price
ax1.set_ylabel('Price')
____(stock_data['____'])
ax2.set_ylabel('ADX')
____(stock_data['____'], color='red')

ax1.set_title('Price and ADX')
plt.show()
```

**Ans.**

```py
# Calculate ADX
stock_data['ADX'] = talib.ADX(stock_data['High'], stock_data['Low'], stock_data['Close'])

# Create subplots
fig, (ax1, ax2) = plt.subplots(2)

# plot ADX with the price
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('ADX')
ax2.plot(stock_data['ADX'], color='red')

ax1.set_title('Price and ADX')
plt.show()
```

**Instructions 2/2**

In mid-September 2020, the stock price started to move sideways around $400. How was this reflected in the ADX value?

1. The ADX was rising.
2. The ADX was falling.
3. The ADX was moving sideways.

**Ans.** 2

### Question 6: Understand the RSI

RSI stands for Relative Strength Indicator, and is a very popular momentum indicator. Momentum measures the rate of the rising or falling in the asset prices.

Which of the following statements is incorrect?

1. The larger the RSI value, the stronger the momentum.
2. RSI is bounded between 0 and 100.
3. Traditionally, an RSI value over 70 indicates an oversold market condition, which means that the asset is undervalued and the price may rally.

**Ans.** 3

### Question 7: Calculate the RSI

The RSI calculation follows a straightforward formula. RS, or Relative Strength, is the average of upward price changes in a chosen n periods, divided by the average of downward price changes over those n periods.

RSI = 100 - 100/(1 + RS)

Where: RS = average of upward price changes / average of downward price changes

All these calculations can be handled in Python with one line of code. In this exercise, you will do your first RSI calculation using historical daily price data of the Google stock.

The daily price data has been loaded as stock_data. Also, talib has been imported for you.

**Instructions**

1. Calculate the RSI using the appropriate method from talib and the Close column in the price data. Save it in a new column called RSI_14.
2. Calculate the RSI using a time period of 21 and save it in a new column called RSI_21.
3. Print the last five rows of stock_data.

**Pre Code**

```py
# Calculate RSI with the default time period
stock_data['RSI_14'] = ____(stock_data['____'])

# Calculate RSI with a time period of 21
stock_data['RSI_21'] = ____

# Print the last five rows
print(stock_data.____())
```

**Ans.**

```py
# Calculate RSI with the default time period
stock_data['RSI_14'] = talib.RSI(stock_data['Close'])

# Calculate RSI with a time period of 21
stock_data['RSI_21'] = talib.RSI(stock_data['Close'], timeperiod=21) 

# Print the last five rows
print(stock_data.tail())
```

### Question 8: Visualize the RSI

The RSI is a momentum indicator that oscillates between 0 and 100. Typically an RSI over 70 indicates an overbought market condition, which means the asset is overvalued and the price may reverse. An RSI below 30 suggests an oversold market condition, which means the asset is undervalued and the price may rally. To better understand it, you will calculate the RSI and plot it along with the price data.

As you did in the previous exercise, you will use historical daily price data of the Google stock, which has been loaded as stock_data. Also, talib has been imported for you and matplotlib.pyplot has been imported as plt.

**Instructions 1/2**

1. Calculate a 14-day (by default) RSI, and save it in column called RSI.
2. Create two subplots named ax1 and ax2.
3. Plot the Close price in the subplot ax1 on top, and the RSI in the subplot ax2 on the bottom.

**Pre Code**

```py
# Calculate RSI
stock_data['RSI'] = ____(stock_data['____'])

# Create subplots
fig, (ax1, ax2) = plt.____(2)
# Plot RSI with the price
ax1.set_ylabel('Price')
____(stock_data['____'])
ax2.set_ylabel('RSI')
____(stock_data['____'], color='orangered')

ax1.set_title('Price and RSI')
plt.show()
```

**Ans.**

```py
# Calculate RSI
stock_data['RSI'] = talib.RSI(stock_data['Close'])

# Create subplots
fig, (ax1, ax2) = plt.subplots(2)
# plot RSI with the price
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('RSI')
ax2.plot(stock_data['RSI'], color='orangered')

ax1.set_title('Price and RSI')
plt.show()
```

**Instructions 2/2**

In March 2020, the RSI reached a low value of around 30. What happened to the stock price afterwards?

1. The stock price kept falling.
2. The stock price was moving sideways.
3. The stock price bottomed up and started to rise.

**Ans.** 3

### Question 9: Understand Bollinger Bands

Bollinger Bands are a popular type of volatility indicator developed by John Bollinger. They intend to answer the question: is the price too high or too low on a relative basis?

Which of the following statements is incorrect?

1. If the price moves very close to the lower band, it suggests the price is relatively too expensive.
2. The wider the Bollinger Bands, the more volatile the asset price.
3. The middle line of Bollinger Bands is an n-period simple moving average line.

**Ans.** 1

### Question 10: Implement Bollinger Bands

Bollinger Bands are envelopes plotted above and below a simple moving average of the price. Because the distance of the bands is based on the standard deviation, they adjust to volatility swings in the underlying price.

To better understand the impact of standard deviation specification on Bollinger bands, you will implement and plot two sets of Bollinger Bands on the same dataset.

You will use historical Bitcoin price data, which has been preloaded as bitcoin_data. The talib library has also been imported for you.

**Instructions 1/2**

1. Define Bollinger Bands using 1 standard deviation for both the upper and lower bands.
Plot the upper and lower bands.

**Pre Code**

```py
# Define the Bollinger Bands with 1-sd
upper_1sd, mid_1sd, lower_1sd = ____(bitcoin_data['Close'], 
                                     ____,
                                     ____,
                                     timeperiod=20)
# Plot the upper and lower Bollinger Bands 
plt.plot(bitcoin_data['Close'], color='green', label='Price')
plt.plot(____, color='tomato', label="Upper 1sd")
plt.plot(____, color='tomato', label='Lower 1sd')

# Customize and show the plot
plt.legend(loc='upper left')
plt.title('Bollinger Bands (1sd)')
plt.show()
```

**Ans.**

```py
# Define the Bollinger Bands with 1-sd
upper_1sd, mid_1sd, lower_1sd = talib.BBANDS(bitcoin_data['Close'],
                                             nbdevup=1,
                                             nbdevdn=1,
                                             timeperiod=20)
# Plot the upper and lower Bollinger Bands 
plt.plot(bitcoin_data['Close'], color='green', label='Price')
plt.plot(upper_1sd, color='tomato', label="Upper 1sd")
plt.plot(lower_1sd, color='tomato', label='Lower 1sd')

# Customize and show the plot
plt.legend(loc='upper left')
plt.title('Bollinger Bands (1sd)')
plt.show()
```

**Instructions 2/2**

1. Define Bollinger Bands using 2 standard deviations for both the upper and lower bands.
Plot the upper and lower bands.

**Pre Code**

```py
# Define the Bollinger Bands with 2-sd
upper_2sd, mid_2sd, lower_2sd = ____(bitcoin_data['Close'],
                                     ____,
                                     ____,
                                     timeperiod=20)
# Plot the upper and lower Bollinger Bands 
plt.plot(bitcoin_data['Close'], color='green', label='Price')
plt.plot(____, color='orange', label='Upper 2sd')
plt.plot(____, color='orange', label='Lower 2sd')

# Customize and show the plot
plt.legend(loc='upper left')
plt.title('Bollinger Bands (2sd)')
plt.show()
```

**Ans.**

```py
# Define the Bollinger Bands with 2-sd
upper_2sd, mid_2sd, lower_2sd = talib.BBANDS(bitcoin_data['Close'],
                                             nbdevup=2,
                                             nbdevdn=2,
                                             timeperiod=20)
# Plot the upper and lower Bollinger Bands 
plt.plot(bitcoin_data['Close'], color='green', label='Price')
plt.plot(upper_2sd, color='orange', label='Upper 2sd')
plt.plot(lower_2sd, color='orange', label='Lower 2sd')

# Customize and show the plot
plt.legend(loc='upper left')
plt.title('Bollinger Bands (2sd)')
plt.show()
```

<hr>