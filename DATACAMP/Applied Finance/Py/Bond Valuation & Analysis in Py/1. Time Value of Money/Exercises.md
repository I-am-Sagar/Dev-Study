### Question 1: Calculating simple interest

Learning to calculate simple interest is an important first step in building up to calculating the price of a bond.

Here you will apply what you have learned to calculate simple interest on a savings account.

A savings account offers a 3% interest rate (simple interest) per year paid yearly. You decide to invest USD 10,000 in this account for a period of 10 years.

**Instructions**

1. Assign the present value, rate, and number of periods to pv, r, and n, respectively.
2. Using the formula for simple interest, calculate and print the total amount of simple interest earned after 10 years.
3. Calculate and print the value of the account after 10 years.

**Pre Code**

```py
# Assign present value, rate and number of periods
pv = ____
r = ____
n = ____

# Calculate total amount of simple interest earned
simple_interest = ____
print(simple_interest)

# Calculate value of the savings account
fv = ____
print(fv)
```

**Ans.**

```py
# Assign present value, rate and number of periods
pv = 10000
r = 0.03
n = 10

# Calculate total amount of simple interest earned
simple_interest = pv * r * n
print(simple_interest)

# Calculate value of the savings account
fv = pv + simple_interest
print(fv)
```

### Question 2: Calculating compound interest

Compound interest is much more applicable in the real world and is an important feature in calculating the price of a bond, as you will see in the next chapter.

Now imagine the same savings account pays 3% per year as compound interest instead of simple interest. As before, you invest USD 10,000 for a period of ten years.

**Instructions**

1. Assign the present value, rate, and number of periods to pv, r, and n, respectively.
2. Find how much money the savings account will have after ten years and print the result.
3. Calculate and print the amount of interest earned over the ten years.

**Pre Code**

```py
# Assign present value, rate and number of periods
pv = ____
r = ____
n = ____

# Calculate the value of the savings account
fv = ____
print(fv)

# Calculate the total amount of compound interest earned
compound_interest = ____
print(compound_interest)
```

**Ans.**

```py
# Assign present value, rate and number of periods
pv = 10000
r = 0.03
n = 10

# Calculate the value of the savings account
fv = pv * (1 + r) ** n
print(fv)

# Calculate the total amount of compound interest earned
compound_interest = fv - pv
print(compound_interest)
```

### Question 3: Calculating future value

Calculating future value is an important step in building up to bond pricing as the process of pricing a bond is actually calculating future value in reverse. Here you will find the future value of an investment using the npf.fv() formula from earlier.

**Instructions**

1. Import the numpy_financial package using the alias npf.
2. Calculate the future value of an investment of USD 10,000 with top-ups of USD 5,000 each year for 30 years earning 5% annual interest and assign the result to savings.
3. Print the result.

**Pre Code**

```py
# Import numpy_financial package using the alias npf
____

# Calculate the future value of an investment
savings = npf.fv(rate=____, nper=____, pmt=____, pv=____)

# Print the result
____
```

**Ans.**

```py
# Import numpy_financial package using the alias npf
import numpy_financial as npf

# Calculate the future value of an investment
savings = npf.fv(rate=0.05, nper=30, pmt=-5000, pv=-10000)

# Print the result
print(savings)
```

### Question 4: Calculating compounding frequencies
Different compounding frequencies can greatly affect how much your money will grow. In this exercise, we are going to compare three different savings accounts, each offering a different annual rate at a different compounding frequency, to see which one will grow your money the most.

In each example you will start with an initial investment of $10,000 that you invest for ten years. numpy_financial has already been imported for you as npf.

**Instructions 1/4**

1. Calculate the future value of USD 10,000 invested in a savings account offering 5% annual interest paid once per year for 10 years and assign to account_1.

**Pre Code**

```py
# Calculate the growth of USD 10,000 invested in the first account
account_1 = npf.fv(rate=____, nper=____, pmt=____, pv=____)

# Print the value of the first savings account
____
```

**Ans.**

```py
# Calculate the growth of USD 10,000 invested in the first account
account_1 = npf.fv(rate=0.05, nper=10, pmt=0, pv=-10000)

# Print the value of the first savings account
print(account_1)
```

**Instructions 2/4**

1. Now calculate the value of USD 10,000 invested in a savings account offering 4.5% annual interest paid monthly (i.e., 12 times per year) for 10 years and assign to account_2.

**Pre Code**

```py
# Calculate and print the growth of USD 10,000 invested in the first account
account_1 = npf.fv(rate=0.05, nper=10, pmt=0, pv=-10000)

# Calculate the growth of USD 10,000 invested in the second account
account_2 = npf.fv(____, ____, ____, ____)

# Print the value of the second savings account
____
```

**Ans.**

```py
# Calculate and print the growth of USD 10,000 invested in the first account
account_1 = npf.fv(rate=0.05, nper=10, pmt=0, pv=-10000)

# Calculate the growth of USD 10,000 invested in the second account
account_2 = npf.fv(rate=0.045/12, nper=10*12, pmt=0, pv=-10000)

# Print the value of the second savings account
print(account_2)
```

**Instructions 3/4**

1. Now calculate the value of USD 10,000 invested in a savings account offering 4.9% annual interest paid daily (i.e., 365 times per year) for 10 years and assign to account_3.

**Pre Code**

```py
# Calculate and print the growth of USD 10,000 invested in the first account
account_1 = npf.fv(rate=0.05, nper=10, pmt=0, pv=-10000)

# Calculate and print the growth of USD 10,000 invested in the second account
account_2 = npf.fv(rate=0.045/12, nper=10*12, pmt=0, pv=-10000)

# Calculate the growth of USD 10,000 invested in the third account
account_3 = npf.fv(____, ____, ____, ____)

# Print the value of the third savings account

```

**Ans.**

```py
# Calculate and print the growth of USD 10,000 invested in the first account
account_1 = npf.fv(rate=0.05, nper=10, pmt=0, pv=-10000)

# Calculate and print the growth of USD 10,000 invested in the second account
account_2 = npf.fv(rate=0.045/12, nper=10*12, pmt=0, pv=-10000)

# Calculate the growth of USD 10,000 invested in the third account
account_3 = npf.fv(rate=0.049/365, nper=10*365, pmt=0, pv=-10000)

# Print the value of the third savings account
print(account_3)
```

**Instructions 4/4**

Over ten years, which account grew your money the most?

1. Account 1 paying 5% annual interest once per year.
2. Account 2 paying 4.5% annual interest monthly.
3. Account 3 paying 4.9% annual interest daily.

**Ans.** 3


### Question 5: Calculating the number of periods

One real-life example that uses these functions is calculating how long it will take you to reach a certain financial goal, be it growing your wealth, saving for something specific, or paying off debt.

How long will it take you to save USD 30,000 if you save USD 1,250 per quarter invested in a fund that offers 4.5% annual returns compounded quarterly?

**Instructions**

1. Import the numpy_financial package using the alias npf.
2. Use the npf.nper() function to calculate how long it will take you to reach your savings goal based on the information above and save this to number_periods.
3. Print the result.

**Pre Code**

```py
# Import numpy_financial package using alias npf
____

# Calculate how long it will take to reach the savings goal
number_periods = ____

# Print the result
____
```

**Ans.**

```py
# Import numpy_financial package using alias npf
import numpy_financial as npf

# Calculate how long it will take to reach the savings goal
number_periods = npf.nper(rate=0.045/4, pmt=-1250, pv=0, fv=30000)

# Print the result
print(number_periods)
```

### Question 6: Calculating the payment amount

Another real-life problem you might encounter is how much money you need to save each month to hit a financial target within a set time.

You saw earlier that to pay off a mortgage of USD 275,000 in ten years with an annual interest rate of 3.5% compounded monthly, you needed to pay USD 2,719 per month.

If, instead, you wanted to take twenty years to pay off the mortgage, calculate how much you would need to pay per month now.

**Instructions**

1. Import the numpy_financialpackage using the alias npf.
2. Use the npf.pmt() function to calculate the required monthly payment and save this to required_return.
3. Print the result.

**Pre Code**

```py
# Import the numpy_financial package using the alias npf
____

# Calculate monthly payment required
required_payment = ____

# Print the result
____
```

**Ans.**

```py
# Import the numpy_financial package using the alias npf
import numpy_financial as npf

# Calculate monthly payment required
required_payment = npf.pmt(rate=0.035/12, nper=20*12, pv=275000, fv=0)

# Print the result
print(required_payment)
```

### Question 7: Calculating the required interest rate

If you have a certain financial goal in mind, such as saving a set amount of money by a set time, you can calculate what return will achieve this goal.

This is useful if, for example, you wanted to check if the goal you have set is realistic given current levels of interest rates.

Earlier, you saw that to retire in 30 years with USD 1,000,000 in the bank by investing USD 1,500 per month, you needed to earn an annual return of 3.77%. Calculate how much higher this return would need to be if you wanted to retire with USD 2,000,000 instead, again using monthly compounding.

**Instructions**

1. Import the numpy_financial package using the alias npf.
2. Use the npf.rate() function to calculate the required return and save this to required_return.
3. Print the result.

**Pre Code**

```py
# Import the numpy_financial package using the alias npf


# Calculate return on investments required: required_return
required_return = ____

# Print the result
```

**Ans.**

```py
# Import the numpy_financial package using the alias npf
import numpy_financial as npf

# Calculate return on investments required: required_return
required_return = 12 * npf.rate(nper=30*12, pmt=-1500, pv=0, fv=2000000)

# Print the result
print(required_return)
```

### Question 8: Solving real-world problems

Now you are going to use the functions you have learned to solve some real-life problems:

You want to start investing and find a bond paying a 3% annual rate compounded monthly. If you invest USD 100 per month, how much will you have after five years?

You are saving for a deposit on a house. You need to save up USD 15,000 and have saved USD 5,000 so far. If you save USD 250 per month, how many months until you reach your goal?

You are 22 years old and want to retire at 65 with USD 1 million in the bank. If you can grow your money at 5% per year, how much should you invest per month?

**Instructions 1/3**

1. Find how much a USD 100 per month investment at a 3% annual rate compounded monthly grows to after 5 years.

**Pre Code**

```py
# Calculate how much USD 100 per month compounding at 3% grows to after 5 years
total_savings = npf.___(rate=____, nper=____, pmt=____, pv=____)
print(total_savings)
```

**Ans.**

```py
# Calculate how much USD 100 per month compounding at 3% grows to after 5 years
total_savings = npf.fv(rate=0.03/12, nper=5*12, pmt=-100, pv=0)
print(total_savings)
```

**Instructions 2/3**

1. Find the time to save USD 15,000 starting with USD 5,000 and adding USD 250 per month at 5% interest compounded monthly.

**Pre Code**

```py
# Calculate the time to reach a USD 15,000 deposit on a house
time_to_goal = npf.____(rate=____, pmt=____, pv=____, fv=____)
print(time_to_goal)
```

**Ans.**

```py
# Calculate the time to reach a USD 15,000 deposit on a house
time_to_goal = npf.nper(rate=0.05/12, pmt=-250, pv=-5000, fv=15000)
print(time_to_goal)
```
**Instructions 3/3**

1. Find the monthly savings to retire with USD 1,000,000 starting with USD 0, earning 5% interest compounded monthly.

**Pre Code**

```py
# Calculate the monthly contributions needed to retire with USD 1,000,000
monthly_contributions = npf.____(rate=____, nper=(65-22)*12, pv=____, fv=____)
print(monthly_contributions)
```

**Ans.**

```py
# Calculate the monthly contributions needed to retire with USD 1,000,000
monthly_contributions = npf.pmt(rate=0.05/12, nper=(65-22)*12, pv=0, fv=1000000)
print(monthly_contributions)
```

<hr>