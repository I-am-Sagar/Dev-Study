1. **Convexity**
In the last video, we saw that using duration to predict bond prices involved some estimation error. Now we are going to explore why.

2. **Plotting predicted vs. actual prices**
To see how accurate duration is for predicting bond prices, let's create a graph showing actual bond prices against their predicted prices using duration. We begin by importing the necessary packages. Next, let's take a twenty year bond with a five percent coupon and five percent yield, find its price and dollar duration in the usual way, and save the results to price and dollar duration.

3. **Plotting predicted vs. actual prices**
Now we create a pandas DataFrame containing bond prices and yields in the same way we did earlier.

4. **Plotting predicted vs. actual prices**
Now we are going to add some extra columns. The first will be the yield change which calculates the difference between the current yield in each row and our original yield of five percent for the bond.

5. **Plotting predicted vs. actual prices**
Next we use our formula for predicting price changes from earlier. The price change of the bond will be minus one hundred times the duration times the bond price times the yield change as a decimal.

6. **Plotting predicted vs. actual prices**
For our last column, we find the predicted bond price by simply adding our starting bond price to the predicted price change from duration.

7. **Plotting predicted vs. actual prices**
Finally, we plot a graph of both predicted prices and actual prices against yields, add a legend and some labels to the axes, then show the plot.

8. **Limitations of duration**
Looking at this graph, there are three main takeaways. First, duration is a straight-line approximation of bond prices; it is a linear measure. Second, bond prices are not linear, they are convex, meaning the relationship between prices and yields is a curved line, not a straight one. Third, duration is useful for predicting bond prices for small changes in yields, where the gap between predicted and actual prices is small, but not for larger changes, where the difference becomes too big.

9. **What is convexity?**
To capture this curvature in bond prices, we use something called convexity. Convexity measures the curvature in the bond price that duration misses and is used alongside duration to improve bond price prediction and hence better measure interest rate risk in bonds and bond portfolios. If a bond has a higher convexity, this means a graph of the bond price against its yield will be more curved.

10. **Convexity formula**
As with duration, we use a simplified formula for calculating the convexity of a bond. First, we take the price of a bond for a one percent lower level of yields plus the price of a bond for a one percent higher level of yields and subtract two times the price of the bond at current yields. Next, we divide this by two times the price of the bond times the change in yields squared to get the convexity of the bond.

11. **Convexity example**
Take a ten year bond with a five percent annual coupon and four percent yield. We want to calculate its convexity using the formula from the previous slide. First, we find the bond price in the usual way and assign the result to the variable 'price'. Next, we find the price of the same bond for a one percent higher and lower level of yields, and assign the results to 'price up' and 'price down' respectively. Finally, we use our convexity formula along with our assigned variables, and print the result.

12. **Summary**
To summarize, duration is a linear approximation of bond prices, whilst bond prices are curved, meaning duration is only accurate for small changes in yields. Convexity measures this curvature of bond prices.

13. **Let's practice!**
Now let's practice finding the convexity of some bonds.