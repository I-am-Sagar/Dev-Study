1. **Simple interest & compound interest**
Hello and welcome to Bond Valuation and Analysis in Python! My name is Josh, and I work as an options trader at an investment bank. In this course, we are going to learn how to price bonds, as well as calculate their main risks.

2. **Simple interest**
Before we look at bonds, we first need to understand the concept of interest. Interest is money earned on a deposit, or paid on a loan. Simple interest means the interest depends only on the initial deposit or loan. Say we deposit one thousand dollars in a savings account, paying simple interest of five percent each month. We want to know how much simple interest we will have earned after a year, as well as the new value of our account.

3. **Simple interest**
Let's start by introducing some lingo we will use throughout the course. PV, or present value, is the amount of money we have now; it's how much our money is worth today. FV, or future value, is the amount of money we will have at some point in the future. r is the interest rate we earn per period, and n is the number of periods. The simple interest we earn is the amount of money we invest, multiplied by the interest rate and the number of periods. The future value is the initial value of the account plus the interest earned.

4. **Simple interest**
In this example, the PV is one thousand as that's the money we have deposited, the interest rate is five percent, or zero-point-zero-five per month, and the number of periods is twelve as interest is paid each month for a year. Multiplying these together gives fifty dollars per month for twelve months which is six hundred dollars in interest. Finally, by adding the interest to the starting value of our account, we see that our account grows to a value of one thousand six hundred dollars after a year.

5. **Compound interest**
In real life, it is much more common to be paid compound interest instead; meaning we also receive interest on our interest! Let's look at the same example as before using compound interest instead. After the first month, we have made five percent on one thousand dollars, which is fifty dollars. In the second month, we earn interest on our original deposit and the interest we have been paid already. We start with one thousand and fifty dollars and earn five percent which is fifty two dollars and fifty cents. After twelve months, we have one thousand seven hundred and ninety five dollars and eighty six cents, meaning we earned seven hundred and ninety five dollars and eighty six cents in interest compared to six hundred dollars if we had just earned simple interest.

6. **Compound interest**
One problem with the previous approach is that it can be very repetitive. Luckily there is a formula for calculating compound interest in just one line. For one period, notice that to calculate what our money grows to, we simply multiply the starting amount by one plus the interest rate. For two periods, we just do this process twice. Continuing on in the same way, for n periods, we simply multiply our initial money by one point zero five to the power of n.

7. **Compound interest**
Therefore the general formula for calculating how much money we have after n periods is our initial money (the present value) multiplied by one plus the interest rate per period to the power of the number of periods.

8. **Compound interest**
Implementing this in Python, we get the same answer as before of one thousand seven hundred and ninety five dollars and thirty six cents but in a much more efficient way.

9. **Let's practice!**
Now it's your turn to calculate simple and compound interest!