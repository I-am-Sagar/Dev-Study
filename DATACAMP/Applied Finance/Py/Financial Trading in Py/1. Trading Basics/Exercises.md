### Question 1: The concept of trading

Financial trading is the buying and selling of financial assets with the goal of making a profit.

Which of the following statements is incorrect?

1. Compared with investing, trading has a shorter time horizon and tries to profit from market fluctuations.
2. Trading is taking calculated risks, and only bears the risk when the risk-reward ratio is favorable.
3. Trading primarily takes long positions in the market. 

**Ans.** 1

### Question 2: Plot a time series line chart

Cryptocurrencies are a new category of assets, and you are interested in exploring them more. You have some daily historical price data of Bitcoin saved in a CSV file. You want to get familiar with the data by doing some basic exploration and plotting.

The pandas package has been imported as pd (for the rest of the course as needed), and matplotlib.pyplot has been imported as plt.

**Instructions 1/2**

1. Load the CSV file 'bitcoin_data.csv' , specify the Date column as index, and save it in bitcoin_data.
2. Print the first 5 rows of the data.

**Pre Code**

```py
# Load the data
bitcoin_data = ____.____(____, ____, parse_dates=True)

# Print the top 5 rows
print(____.____())
```

**Ans.**

```py
# Load the data
bitcoin_data = pd.read_csv('bitcoin_data.csv', index_col='Date', parse_dates=True)

# Print the top 5 rows
print(bitcoin_data.head())
```

**Instructions 2/2**

1. Plot the daily high and low prices of the bitcoin_data.

**Pre Code**

```py
# Load the data
bitcoin_data = pd.read_csv('bitcoin_data.csv', index_col='Date', parse_dates=True)

# Print the top 5 rows
print(bitcoin_data.head())

# Plot the daily high price
____(____['____'], color='green')
# Plot the daily low price
____(____['____'], color='red')

plt.title('Daily high low prices')
plt.show()
```

**Ans.**

```py
# Load the data
bitcoin_data = pd.read_csv('bitcoin_data.csv', index_col='Date', parse_dates=True)

# Print the top 5 rows
print(bitcoin_data.head())

# Plot the daily high price
plt.plot(bitcoin_data['High'], color='green')
# Plot the daily low price
plt.plot(bitcoin_data['Low'], color='red')

plt.title('Daily high low prices')
plt.show()
```

### Question 3: Plot a candlestick chart

A candlestick chart is a style of chart that packs multiple pieces of price information into one chart. It can provide you with a good sense of price action and visual aid for technical analysis.

You will plot a candlestick chart using the same data as the previous exercise, which has been preloaded as bitcoin_data. Also, plotly.graph_objects has been imported as go.

**Instructions**

1. Define a candlestick object using columns from bitcoin_data.
2. Create a plot using the candlestick object defined in the previous step.
3. Display the candlestick chart.

**Pre Code**

```py
# Define the candlestick data
candlestick = ____(
    x=bitcoin_data.index,
    open=bitcoin_data['____'],
    high=bitcoin_data['____'],
    low=bitcoin_data['____'],
    close=bitcoin_data['____'])

# Create a candlestick figure   
fig = ____(data=[____])
fig.update_layout(title='Bitcoin prices')                        

# Show the plot
fig.____()
```

**Ans.**

```py
# Define the candlestick data
candlestick = go.Candlestick(
    x=bitcoin_data.index,
    open=bitcoin_data['Open'],
    high=bitcoin_data['High'],
    low=bitcoin_data['Low'],
    close=bitcoin_data['Close'])

# Create a candlestick figure   
fig = go.Figure(data=[candlestick])
fig.update_layout(title='Bitcoin prices')                        

# Show the plot
fig.show()
```

### Question 4: Resample the data

In this exercise, you will switch your hat from a day trader to a swing trader and then a position trader, and manipulate the data to suit your needs.

You will work with 4-hour currency exchange rates of Euros (EURUSD) data. The data has been loaded as eurusd_4h.

**Instructions 1/2**

1. Resample the data to obtain daily data using the mean and print the top five rows.

**Pre Code**

```py
# Resample the data to daily by calculating the mean values
eurusd_daily = eurusd_4h.____('____').____()

# Print the top 5 rows
print(eurusd_daily.____())
```

**Ans.**

```py
# Resample the data to daily by calculating the mean values
eurusd_daily = eurusd_4h.resample('D').mean()

# Print the top 5 rows
print(eurusd_daily.head())
```

**Instructions 2/2**

1. Resample the data to obtain weekly data using the mean and print the top five rows.

**Pre Code**

```py
# Resample the data to weekly by calculating the mean values
eurusd_weekly = eurusd_4h.____('____').____()

# Print the top 5 rows
print(eurusd_weekly.____())
```

**Ans.**

```py
# Resample the data to weekly by calculating the mean values
eurusd_weekly = eurusd_4h.resample('W').mean()

# Print the top 5 rows
print(eurusd_weekly.head())
```

### Question 5: Plot a return histogram

As a trader, it is important to analyze an asset's return profile, such as ranges of price changes, return distributions, etc. Over the years, Tesla fans and short sellers have been either betting on or against Tesla stocks aggressively, leading to volatile stock prices. You have some Tesla historical daily price data and want to verify this phenomenon.

The stock data has been preloaded in tsla_data, and matplotlib.pyplot has been imported as plt. Additional customizations to the plot such as a title and axis labels have already been provided for you.

**Instructions**

1. Calculate the daily percent change using the Close price and save it in a new column named daily_return.
2. Plot a histogram of daily_return, setting the bin size to 100.

**Pre Code**

```py
# Calculate daily returns
tsla_data['daily_return'] = tsla_data['____'].____() * 100

# Plot the histogram
tsla_data['____'].____(____, color='red')
plt.ylabel('Frequency')
plt.xlabel('Daily return')
plt.title('Daily return histogram')
plt.show()
```

**Ans.**

```py
# Calculate daily returns
tsla_data['daily_return'] = tsla_data['Close'].pct_change() * 100

# Plot the histogram
tsla_data['daily_return'].hist(bins=100, color='red')
plt.ylabel('Frequency')
plt.xlabel('Daily return')
plt.title('Daily return histogram')
plt.show()
```

### Question 6: Calculate and plot SMAs

Daily price data is inherently messy and noisy. You want to analyze the Apple stock daily price data, and plan to add a simple moving average (SMA) indicator to smooth out the data. Specifically, you decide to use the 50-day SMA.

The stock data has been preloaded in aapl_data, and matplotlib.pyplot has been imported as plt. Additional customizations to the plot such as a title and legend have already been provided for you.

**Instructions**

1. Calculate the 50-day SMA using the Close price, and save it in a new column named sma_50.
2. Plot a line chart using the data in the columns sma_50 and Close.

**Pre Code**

```py
# Calculate SMA
aapl_data['sma_50'] = aapl_data['____'].____.mean()

# Plot the SMA
____(aapl_data['____'], color='green', label='SMA_50')
# Plot the close price
____(aapl_data['____'], color='red', label='Close')

# Customize and show the plot
plt.title('Simple moving averages')
plt.legend()
plt.show()
```

**Ans.**

```py
# Calculate SMA
aapl_data['sma_50'] = aapl_data['Close'].rolling(window=50).mean()

# Plot the SMA
plt.plot(aapl_data['sma_50'], color='green', label='SMA_50')
# Plot the close price
plt.plot(aapl_data['Close'], color='red', label='Close')

# Customize and show the plot
plt.title('Simple moving averages')
plt.legend()
plt.show()
```

### Question 7: The bt process

The bt package provides a flexible framework for defining and backtesting trading strategies in Python. A trading strategy is a method of buying and selling financial assets based on predefined rules. Backtesting is a way to assess the effectiveness of a strategy by testing it on historical data.

**Instructions**

1. Order the steps to correctly define and backtest a trading strategy with bt.

**Ans.**

Order is:

1. Get the historical data, either from bt.get() or loading data from existing csv file.
2. Define the strategy using bt.Strategy() and pass in the strategy name and the algos needed.
3. Create the backtest with bt.Backtest(), pass in the strategy and data, and run the backtest.
4. Plot and evaluate the backtest result to access the strategy's viability.  

### Question 8: Define and backtest a simple strategy

You want to create a strategy to trade the so-called "FAANG" stocks, which is an acronym referring to the stocks of the five most popular and best-performing American technology companies: Facebook, Amazon, Apple, Netflix, and Alphabet (a.k.a. Google).

The idea is simple, you will hold an equal amount of each stock in your portfolio. Every week the strategy will buy or sell shares as needed in order to balance the equal weights.

First, you will inspect the data for the "FAANG" stocks. Second, you will define the strategy, which specifies buying an equal amount of each stock, and rebalance every week. Lastly, you will run the backtest and plot the result.

The bt package has been imported for you. The historical price data of the "FAANG" has been preloaded in bt_data.

**Instructions 1/4**

1. Inspect the top 5 rows of the stock data in bt_data.

**Pre Code**

```py
# Print the top five rows
print(____.____())
```

**Ans.**

```py
# Print the top five rows
print(bt_data.head(5))
```

**Instructions 2/4**

1. Define a strategy bt_strategy using the appropriate method in bt, and specify that it should run weekly and give each stock an equal weight.

**Pre Code**

```py
# Define the strategy
bt_strategy = bt.Strategy('Trade_Weekly', 
                         [____,
                          bt.algos.SelectAll(),
                          _____,
                          bt.algos.Rebalance()])
```

**Ans.**

```py
# Define the strategy
bt_strategy = bt.Strategy('Trade_Weekly', 
                         [bt.algos.RunWeekly(),
                          bt.algos.SelectAll(),
                          bt.algos.WeighEqually(),
                          bt.algos.Rebalance()])
```

**Instructions 3/4**

1. Create a backtest bt_test.
2. Run the backtest and save the result as bt_res.

**Pre Code**

```py
# Define the strategy
bt_strategy = bt.Strategy('Trade_Weekly', 
                         [bt.algos.RunWeekly(),
                          bt.algos.SelectAll(),
                          bt.algos.WeighEqually(),
                          bt.algos.Rebalance()])
# Create a backtest
bt_test = ____(____, ____)
# Run the backtest
bt_res = ____(____)
```

**Ans.**

```py
# Define the strategy
bt_strategy = bt.Strategy('Trade_Weekly', 
                         [bt.algos.RunWeekly(),
                          bt.algos.SelectAll(),
                          bt.algos.WeighEqually(),
                          bt.algos.Rebalance()])
# Create a backtest
bt_test = bt.Backtest(bt_strategy, bt_data)
# Run the backtest
bt_res = bt.run(bt_test)
```

**Instructions 4/4**

1. Plot the backtest result of bt_res.

**Pre Code**

```py
# Define the strategy
bt_strategy = bt.Strategy('Trade_Weekly', 
                         [bt.algos.RunWeekly(),
                          bt.algos.SelectAll(),
                          bt.algos.WeighEqually(),
                          bt.algos.Rebalance()])
# Create a backtest
bt_test = bt.Backtest(bt_strategy, bt_data)
# Run the backtest
bt_res = bt.run(bt_test)
# Plot the test result
____(title="Backtest result")
plt.show()
```

**Ans.**

```py
# Define the strategy
bt_strategy = bt.Strategy('Trade_Weekly', 
                         [bt.algos.RunWeekly(),
                          bt.algos.SelectAll(),
                          bt.algos.WeighEqually(),
                          bt.algos.Rebalance()])
# Create a backtest
bt_test = bt.Backtest(bt_strategy, bt_data)
# Run the backtest
bt_res = bt.run(bt_test)
# Plot the test result
bt_res.plot(title="Backtest result")
plt.show()
```

<hr>