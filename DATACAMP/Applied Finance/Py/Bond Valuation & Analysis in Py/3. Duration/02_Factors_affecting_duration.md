1. **Factors affecting duration**
Now let's look at the factors affecting duration.

2. **Duration as an 'average' time**
Duration can also be thought of as the 'average' time to get your money back. The longer you wait to get your money back, for example, if a bond has a long time to maturity, the more exposed you are to changes in interest rates, hence the duration is higher.

3. **Duration as the slope of the tangent line**
The technical definition of duration is that it is the derivative of price with respect to yield; this is how you find the actual formula for duration. This means duration is the slope of the tangent line on the price versus yield plot. To find the duration of a twenty year bond with a five percent coupon, and price of one hundred dollars, we can find its yield, then drawing a tangent line and taking the slope gives us its duration.

4. **Maturity vs. duration**
If a bond has a longer maturity, we will need to wait longer to recoup the original bond price. This leaves us exposed to changes in interest rates for a longer period of time, hence a bond with a higher maturity will have a higher duration.

5. **Coupon rate vs. duration**
In a similar way, the higher the coupon on a bond, the quicker we start getting our money back. This means we are less exposed to changes in interest rates during the life of the bond, and hence the duration of the bond is lower when the coupon is higher. This means a bond paying no coupons at all, such as a zero coupon bond, has a higher duration.

6. **Bond yield vs. duration**
Finally, let's consider the effect of bond yields on duration by plotting a graph of bond prices against yields to see where the curve is steepest. As duration is the slope of the tangent line at that point, we can see that when yields are lower, the curve is steeper, and so duration is higher. Hence bonds with lower yields have a higher duration.

7. **Ways of investigating duration**
There are a few ways to investigate the effect of maturity, coupons, and yields on duration. One way is to find the duration of two bonds where we change one of these factors and see which bond has the higher duration, as we did in the previous set of exercises. We can also plot a line graph of prices against yields like we did in the previous chapter. Finally, we can plot a graph of duration against the factor in question, which we will do now.

8. **Plotting bond maturity against duration**
Say we want to plot a graph of bond maturity against duration. Similar to how we plotted our graph of prices against yields, we begin by importing the relevant packages. Next, we create a numpy array of bond maturities up to 30 years using the np-dot-arange function. Then we store this in a pandas DataFrame with the column header "bond maturity." Then we calculate "price up", "price down", and "duration" in the same way that we did in the previous video, only this time we assign the result to columns in our DataFrame.

9. **Plotting bond maturity against duration**
Finally, we use the plt-dot-plot function to plot bond maturity on the x-axis and bond duration on the y-axis, add labels for both axes as well as a title, and show the graph. As we saw earlier, the longer the maturity, the higher the duration.

10. **Summary**
To summarize, the duration of a bond will increase when it has a longer time to maturity, pays a lower (or even zero) coupon, or has a lower yield.

11. **Let's practice!**
Now let's practice investigating the factors affecting duration!