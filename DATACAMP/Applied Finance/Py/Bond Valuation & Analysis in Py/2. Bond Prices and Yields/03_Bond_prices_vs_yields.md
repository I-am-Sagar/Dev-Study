1. **Bond prices vs. bond yields**
Let's take a deeper look at the relationship between bond prices and yields.

2. **Historical government bond yields**
Bond yields in the financial markets can vary substantially over time, driven by various factors such as central bank interest rates and inflation expectations. In the last few years, we have even seen yields turn negative, meaning if you buy and hold such a bond to maturity, you expect to earn a negative return!

3. **Plotting bond prices vs. yields**
Lets plot a graph of bond prices against yields to understand the relationship better. We start by importing the packages numpy, numpy financial, pandas, and matplotlib.pyplot. Next, we create an array of bond yields using the numpy arange function, which takes as its inputs the starting value, ending value, and step increments. This will create an array of values from zero to twenty (not inclusive) in steps of zero-point-one.

4. **Plotting bond prices vs. yields**
Next, we convert this array into a pandas DataFrame using the pd-dot-DataFrame function and give this column the title "bond yield" using the argument columns, which is passed into the function as a list.

5. **Plotting bond prices vs. yields**
Now we add a second column to the DataFrame called bond price. Each row in this column will take the yield in that row and use it to calculate the price of a bond with that level of yield. For this example, we have chosen a ten year bond with a coupon of five percent inside our pv function.

6. **Plotting bond prices vs. yields**
Now we use the plt dot plot function to plot our graph with bond yield on the x-axis and bond price on the y-axis. Next, we add labels to our axes using the plt dot xlabel and ylabel functions. Then we add a title using plt dot title and finally show the graph using plt dot show. The graph shows the inverse relationship between bond prices and yields that we discussed earlier.

7. **The relationship between price and yield**
We have seen that prices move inversely to yields. One intuition for this is that increasing the yield means you apply a higher discount rate to each cash-flow of the bond, reducing their pv. As the bond price is the sum of these pv's, the bond price decreases. Another way of thinking about it is that since the cash-flows are fixed, paying a higher price for the same set of cash flows means the return on your investment (the yield to maturity), must be lower.

8. **The relationship between price and yield**
A bond is trading at a premium if its price is above one hundred and at a discount if its price is below one hundred. If its price is exactly one hundred, we say it is trading at par. As our bond pays a five percent coupon, notice on the graph that when the yield is less than five percent, the price is above one hundred, and when the yield is greater than five percent, the price is below one hundred. The red line is where the coupon rate equals the yield, and this is also when the bond price is trading at par. This rule applies to all bonds regardless of their coupon.

9. **The relationship between price and yield**
Finally, notice on the graph that the line we have plotted is not a straight line. This effect is called convexity and is something we will investigate more in chapter four.

10. **The relationship between price and yield**
To summarise, bond prices and yields move in opposite directions to each other. When bond prices are above one hundred, they are at a premium, and when they are below one hundred, they are at a discount. When they equal one hundred, the bond is at par. Finally, the price/yield relationship is non-linear.

11. **Let's practice!**
Now let's get some practice applying these concepts!