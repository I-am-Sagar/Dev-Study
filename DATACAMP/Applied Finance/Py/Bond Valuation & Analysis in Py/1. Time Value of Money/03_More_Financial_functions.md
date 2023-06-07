1. **More financial functions**
Welcome back! In this lesson, we are going to look at three more functions to help solve time value of money problems before moving on to bond pricing.

2. **The nper() function**
The nper function tells you how long it will take you to grow your money to a set amount, given an interest rate per period called rate, a regular payment per period pmt, a present value pv, and a future value fv. Note that if we don't specify the future value, then the function assumes it is zero by default, as this function is often used to calculate how long it takes to pay off debt, i.e., to make the value of the debt obligation zero.

3. **The nper() function**
Let's look at an example; say you want to save seven thousand dollars for a car. You have a savings account that offers five percent per year compounded monthly. If you save two hundred and seventy dollars per month, how long will it take you to save up? We input the annual rate divided by twelve to convert it to a monthly rate, write our monthly addition as a negative cash-flow, set the pv to zero as we start with nothing and set the fv to seven thousand. We see that it takes just over twenty four months to reach our goal.

4. **The pmt() function**
The pmt function tells you what fixed payment you need in order to grow the present value pv to a future value fv given a fixed interest rate (rate) and number of periods nper.

5. **The pmt() function**
Let's use an example that involves borrowing instead of saving. You get a two hundred and seventy five thousand dollar mortgage on your first house. The mortgage rate is three point five percent per year compounded monthly. How much do you need to pay on your mortgage each month to have the house paid off in ten years? Inside the pmt function, we convert the annual rate of three point five percent to a monthly rate as it is compounded monthly. The periods are in months, so we multiply ten years by twelve months to get the number of periods. The pv is positive two hundred and seventy five thousand as it is money we received to buy the house, and the fv is zero as we want our mortgage to have disappeared by the end of the term. Giving these inputs to the function, we see that we need to pay two thousand seven hundred and nineteen dollars per month to pay off the mortgage within ten years.

6. **The rate() function**
The rate function tells us what interest rate will grow the present value of some money at a present value of pv to a future value fv for a given number of periods nper and a regular payment per period pmt.

7. **The rate() function**
Imagine you want to retire in thirty years with one million dollars in the bank. Starting at zero, you can invest one thousand five hundred dollars into your pension each month. What return will you need to make on your investments to achieve your goal? Working on a monthly basis, the number of periods in thirty years will be thirty times twelve, the monthly payment will be negative one thousand five hundred as we pay this each month, the pv is zero as we start with nothing, and the fv is positive one million as this is what we will have in thirty years. As we are working on a monthly basis, the rate function will give us an interest rate per month, so we multiply the result by twelve to get an annual figure, and see that we need to earn three point seven seven percent per year on our investments to retire in thirty years!

8. **Let's practice!**
Let's practice using these functions in real-world scenarios!