1. **Factors affecting convexity**
Let's take a look at some of the factors that affect the convexity of a bond.

2. **Convexity is a benefit**
Let's look at our chart of actual bond prices versus the prices predicted using only duration. Convexity can be roughly thought of as the difference between these two lines. Notice that when yields fall, bond prices not only rise; they rise by more than what we would have predicted using only duration. Similarly, when yields rise, bond prices fall, but by less than what we would have predicted using only duration. So in both cases, our bond price outperformed what we would have imagined using just duration. In other words, convexity is a benefit to the owner of a bond, regardless of whether yields rise or fall.

3. **Investigating convexity**
Since convexity is a bit more complicated than duration, we can't get the same intuition for how convexity is affected by different factors. Instead, the simplest way to investigate the effect of different factors on a bond's convexity is to either compare the convexity of two different bonds directly, plot the factor against convexity graphically, or directly look at the curvature of the price/yield relationship. We will demonstrate these different methods by examining the effect of maturity, coupon rate, and yield level on a bond's convexity.

4. **Coupon vs. convexity**
Let's examine the effect of a bond's coupon rate on its convexity by directly calculating the convexity of two bonds; one with a low coupon and one with a high coupon. Take two ten year bonds, both with a five percent yield and face value of one hundred dollars, but the first is a zero coupon bond, and the second pays a ten percent coupon. We begin by finding the price of the zero coupon bond, calculating the price for a shift higher and lower in yields, then find the convexity using our convexity formula. We then repeat the exact same process but setting the coupon to ten percent, and print the convexity of both bonds. We can see they bonds paying a lower coupon have a higher level of convexity.

5. **Maturity vs. convexity**
We can also see which bond has a higher convexity by plotting a graph of their prices against their yields and seeing which price-yield line has the most curvature. We create an array of bond yields inside a pandas DataFrame in the usual way, then add one column for each bond, changing only the maturity. We then plot a graph of both bond prices against yields along with labels for the axes, a title, and a legend. By comparing the curvature of both bonds, we can immediately see that the bond with the higher maturity has greater convexity.

6. **Yield vs. convexity**
Finally, we can plot a graph of a factor against convexity directly, as we did with duration. Take a ten year bond with a five percent annual coupon. We create an array of yields inside a DataFrame as usual, then add columns for the bond price at current yields as well as a shift up and down in yields. Next, we add a column for convexity using the formula from earlier and plot the bond convexity against yields. We can see from the graph that the convexity of a bond decreases as yields increase.

7. **Summary**
To summarize, convexity benefits the bondholder since it means we lose less money when yields rise and make more money when yields fall than if the bond had duration and no convexity. Convexity increases for a bond with a higher maturity, lower coupon, or lower yield.

8. **Let's practice!**
Now let's practice investigating these factors affecting convexity.