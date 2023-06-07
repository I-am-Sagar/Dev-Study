1. **Future value & compounding frequencies**
In the previous lesson, we looked at how much we could earn in compound interest by depositing some money in a savings account.

2. **Compound interest with multiple cash flows**
However, in practice, we may want to make regular monthly deposits instead of a single one-off deposit, or start with a lump sum and top it up each month. How do we calculate the interest we have earned now? Imagine we deposit one thousand dollars in an account offering three percent monthly interest, and at the end of each month, we top it up by another one hundred dollars. How much money will we have after three months?

3. **Compound interest with multiple cash flows**
One approach is to break the problem down into four parts; the amount our initial deposit grows to, and the amount our three top-ups grow to. Our initial deposit will grow by three percent per month for three months. Our first top-up isn't invested until one month later, so it will only earn compound interest for two months. Our second top-up is invested after two months, so will earn compound interest for one month. At the end of the third month, we have invested another one hundred dollars, but it hasn't earned any interest yet. Summing these values, we end up with one thousand four hundred and one dollars and eighty two cents after three months. As we invested a total of one thousand three hundred dollars, this means we earned one hundred and one dollars and eighty two cents in interest.

4. **The future value function**
The problem with this approach is that it becomes very repetitive for longer periods of time with many top-ups. Fortunately, a package called numpy-financial (imported using the alias npf) contains functions that allow us to perform these calculations in a single line of code. Let's look at the fv function by typing a question mark before the function in the console. It takes as its inputs: rate, which is the interest rate per period, nper, which is the number of periods, pmt, which is the amount we add (or withdraw) per period, and pv, which is the initial amount we invest. Note that pmt and pv are represented as cash-flows, so if we are adding money, it is a negative number, and if we are receiving money, it is positive. The output it returns is the future value of the investment.

5. **The future value function**
Let's apply the fv function to the same problem; our rate is three percent per month, the number of periods is three months, our payment per month is minus one hundred, and the pv is minus one thousand as we pay one thousand into the savings account to begin. These numbers are negative as we are paying the money into the account, rather than receiving it.

6. **The future value function**
The fv function gives us the same answer as before but in just one line of code.

7. **Compounding frequencies**
So far, we have considered cases where the interest rate is paid once per period. Consider three examples; where a five percent annual interest payment is paid annually, monthly, and daily, called the compounding frequency.

8. **Compounding frequencies**
We find the correct rate by dividing the annual interest by the frequency at which it is paid, and multiplying the number of periods by this frequency. For example, if the rate is monthly, we divide the rate by twelve and multiply the number of periods by twelve as there are twelve months in the year. The higher the compounding frequency, the more money we end up with. This is because the sooner we receive an interest payment, the sooner this interest can also start earning compound interest by being reinvested.

9. **Let's practice!**
Now it's your turn to get some practice with the fv function and compounding frequencies!