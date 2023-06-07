1. **Coupon paying bonds**
Now let's build on what we've learned to look at coupon paying bonds next.

2. **Coupon bond definition**
The coupon bond is the most common type of bond in the financial markets. The key difference between the zero coupon bond and the coupon paying bond is that the coupon bond also pays regular cash-flows during its life, called coupons. At maturity, the bond pays a coupon as well as its face value, which is typically set to one hundred dollars. Coupons are usually paid once or twice per year, and the number of coupons paid per year is called the frequency. The yield to maturity is the annual return an investor makes if they buy the bond at the current market price and hold it until maturity.

3. **Coupon bond example**
Let's have a look at an example now. Consider a coupon bond with a maturity of three years that pays a three percent annual coupon, has a face value of one hundred dollars, and yield to maturity of four percent. Its cash flows will look like this: Each year we will get paid a three dollar coupon, except in the last year where we get paid both a coupon and the one hundred dollar face value. Note that the cash flow paid each period is the coupon in percent multiplied by the face value. These values are all fixed in advance and don't change!

4. **Coupon bond pricing**
Let's see how a coupon bond can be broken up into a series of zero coupon bonds. Since we know how to price a zero coupon bond, we find the pv of each cash-flow, as if it were its own zero coupon bond, and add all these pvs together to get the price of the coupon bond. Using the same coupon bond from earlier, we break up its cash-flows into three zero coupon bonds, each with a face value equal to the cash-flow. The first two bonds will represent the coupons of three dollars, and the third bond will represent the coupon of three dollars and face value of one hundred dollars. Then we price these three zero coupon bonds in the same way as before.

5. **Coupon bond pricing**
Using our compound interest formula, the one year zero coupon bond will have a pv of two dollars and eighty eight cents, the two year zero coupon bond will have a pv of two dollars and seventy seven cents, and the three year zero coupon bond will have a pv of ninety one dollars and fifty seven cents. Adding these together gives a price of ninety seven dollars and twenty two cents.

6. **Coupon bond formula**
So our formula for a coupon bond is just a sum of zero coupon bonds, where C is the coupon paid in each time period, r is the yield to maturity of the bond, P is the face value (or principal) paid at maturity, and n is the number of time periods.

7. **Using the pv() function**
Luckily, the pv function can do this entire process for us in just one step. Taking the same bond, we set the rate as the bond yield, nper as the number of years, pmt as the coupon, and fv as the principal paid at maturity, and get the same price. As the bond is paying us a coupon, pmt is now positive. We also put a minus sign before the function to get a positive number for the price. Also note that the npf dot pv function deals with the coupons and face value separately, so we set the fv to one hundred, not one hundred and three.

8. **Let's practice!**
Now let's get some practice pricing bonds!