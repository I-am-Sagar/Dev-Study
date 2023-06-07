1. **Present value & zero coupon bonds**
Let's explore present value and zero coupon bonds.

2. **Present Value**
We've seen how money grows from what it's worth now (present value) to what it's worth in the future (future value). This process also works in reverse; we can take the future value of money and calculate what it is worth today.

3. **Present Value**
How do we calculate the present value of something if we know its future value? We take our compound interest equation from chapter one and rearrange it. We call this "discounting to present value" or just "discounting".

4. **Present Value**
Compounding means moving from present value to future value, discounting means moving from future value to present value; they are opposites.

5. **Present Value**
We saw that when compounding money, a higher interest rate or a longer time period increases the amount our money will grow to. This process works in reverse with discounting; increasing the interest rate or time period means money in the future is worth less today, because it is discounted by a greater amount.

6. **The pv() function**
Our final function from the NumPy Financial package is the pv function. For a future value, interest rate per period, number of time periods, and fixed payment per period, the pv function calculates what these future sums of money are worth today.

7. **The pv() function**
Say we want to have saved ten thousand dollars in 10 years and can earn 5% per year compounded annually. How much should we invest today to reach this goal? Using the pv function, we set rate as five percent, nper as ten, pmt as zero as we don't top up our investment, and fv as ten thousand dollars and get a result of six thousand dollars. Note that the answer is negative, because NumPy financial represents the money as a cash-flow, so negative numbers are amounts we pay (or invest), and positive numbers are amounts we receive. Going forward, we will add a minus sign before the function as we care about the price, not the direction of the cash-flow.

8. **The pv() function**
We can also use our rearranged formula from earlier to find the pv. Setting fv to ten thousand, r to five percent, and n to ten gives us the same figure.

9. **Bonds introduction**
A bond is debt issued by a government or company to raise money. Investors lend money to an entity by buying their bonds, and in return receive their money back over time plus interest. Bonds are typically used in investment portfolios to generate a relatively safe and steady income, unlike stocks which can be much more volatile and risky.

10. **Zero coupon bonds**
The simplest type of bond is the zero coupon bond. It pays a single cash-flow (called the face value) at a fixed point in the future called its maturity. Their name comes from the fact that they don't pay any intermediate cash-flows called coupons during their life. Zero coupon bonds are a real-world example of present value; their price is simply the pv of the cash-flow they pay.

11. **Zero coupon bonds**
They are typically issued for a price below face value, so what you pay for the bond is less than what you receive at maturity. This difference is called the yield, which is the annualized percentage return on your investment if you hold the bond to maturity.

12. **Zero coupon bonds**
Let's look at a bond with a three year maturity, face value of one hundred dollars, and yield of three point five percent. What is its price?

13. **Zero coupon bonds**
We use the pv function, and input the yield as the interest rate, as well as the number of years and face value of one hundred and get a price of ninety dollars. We can also use our equation from before to get the same answer.

14. **Let's practice!**
Now let's practice finding the present value and pricing zero coupon bonds!