1. **Mean reversion strategy**
In this lesson, let's learn to build and backtest a mean reversion strategy.

2. **RSI-based mean reversion strategy**
The philosophy of mean reversion strategy is: buy the fear and sell the greed. Or put it more plainly: buy the dip and sell the peak. Let's look at an example of a mean-reversion strategy involving the RSI indicator. When the RSI rises to a relatively high value, 70 for example, it is a short signal, as it suggests the asset is likely overbought and the price may soon reverse. Meanwhile, when the RSI drops to a relatively low value, 30 for example, it is a long signal, as it suggests the asset is likely oversold and the price may soon rally.

3. **Calculate the indicator**
First, let's calculate the indicators with the talib RSI function, and save the result as a DataFrame with to underscore frame.

4. **Construct the signal**
Then we can construct the signal. First, create a signal DataFrame by copying the RSI indicator DataFrame. Let's define: when the RSI value is less than 30, it suggests the asset is likely approaching an oversold condition, so set the signal to one to enter a long position. Conversely, when the RSI value is larger than 70, it suggests the asset is likely approaching an overbought condition, so set the signal to minus one to enter a short position. If the RSI value is in between, set the signal to zero indicating no trade positions.

5. **Plot the signal**
To plot the signal with the price together, use bt merge to combine multiple DataFrames, then call dot plot. Note we don't merge the RSI indicator with the price since they are on different scales. Recall in chapter two we learned RSI is bounded between 0 to 100. Instead, we can place the RSI plot along with the signal plot to observe where to take long or short trades based on RSI values.

6. **Define the strategy with the signal**
Now we are ready to implement the signal in the strategy. Just as in the previous lesson, call algos WeighTarget and pass in the signal DataFrame. The signal value will dictate which period will have long positions, short positions, or no positions.

7. **Backtest the signal-based strategy**
Once we have the strategy defined, create and run a backtest and see how it performs.

8. **Plot backtest result**
Last, let's plot and review the backtest result. Since the RSI-based mean reversion strategy tries to take advantage of temporary market imbalances, it tends to trade more frequently, Also if the RSI value does not indicate an overbought or oversold market condition, no trade is taken so the profit line is flat. Overall, the strategy is profitable based on the historical period backtested.

9. **Let's practice!**
Great progress! Now it's your turn to practice.

