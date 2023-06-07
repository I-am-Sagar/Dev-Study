### Question 1: Calculating present value

Compound interest can have a very powerful effect over time. In this exercise, you will examine how much you need to invest upfront at different interest rates to achieve a financial target. numpy_financial has already been imported for you as npf.

Imagine you want to have saved USD 11,000 after 7 years and consider three different investments, each paying 3%, 4%, and 5% annual interest compounded monthly. If you contribute USD 100 per month, what initial lump sum should you also invest to achieve this goal?

**Instructions 1/3**

1. Calculate the upfront PV you need to invest at 3% annual interest compounded monthly, with monthly top-ups of USD 100 to reach USD 11,000 in 7 years, and print the result.

**Pre Code**

```py
# Calculate the upfront investment at 3% interest
pv_three_percent = -npf.pv(____)

# Print the result
print("3% Annual Interest: ", ____)
```

**Ans.**

```py
# Calculate the upfront investment at 3% interest
pv_three_percent = -npf.pv(rate=0.03 / 12, nper=7 * 12, pmt=-100, fv=11000)

# Print the result
print("3% Annual Interest: ", pv_three_percent)
```

**Instructions 2/3**

1. Calculate the upfront PV you need to invest at 4% annual interest compounded monthly, with monthly top-ups of USD 100 to reach USD 11,000 in 7 years, and print the result.

**Pre Code**

```py
# Calculate the upfront investment at 4% interest
pv_four_percent = ____

# Print the result
print("4% Annual Interest: ", ____)
```

**Ans.**

```py
# Calculate the upfront investment at 4% interest
pv_four_percent = -npf.pv(rate=0.04 / 12, nper=7 * 12, pmt=-100, fv=11000)

# Print the result
print("4% Annual Interest: ", pv_four_percent)
```

**Instructions 3/3**

1. Calculate the upfront PV you need to invest at 5% annual interest compounded monthly, with monthly top-ups of USD 100 to reach USD 11,000 in 7 years, and print the result.

**Pre Code**

```py
# Calculate the upfront investment at 5% interest
pv_five_percent = ____

# Print the result
print("5% Annual Interest: ", ____)
```

**Ans.**

```py
# Calculate the upfront investment at 5% interest
pv_five_percent = -npf.pv(rate=0.05 / 12, nper=7 * 12, pmt=-100, fv=11000)

# Print the result
print("5% Annual Interest: ", pv_five_percent)
```

### Question 2: Pricing zero coupon bonds

You have seen that the price of a zero coupon bond is simply the PV of a single cash-flow in the future. How much that single cash-flow is worth today will depend on how far it is into the future and what interest rate (yield) you discount it at. We will investigate this now.

To do this, you are going to price a zero coupon bond with a three year maturity and yield of 5% per year. Then you will change the maturity and yield and see how these factors affect the price.

In this exercise, you are going to work directly with the compound interest formula instead of using the npf.pv() function.

**Instructions 1/3**

1. Find the price of a zero coupon bond with a three year maturity, 5% yield, and USD 100 face value and print the result.

**Pre Code**

```py
# Calculate price of a 3 year 5% yield zero coupon bond
price_1 = ____

# Print the result
print("3 year 5% yield ZCB: ", ____)
```

**Ans.**

```py
# Calculate price of a 3 year 5% yield zero coupon bond
price_1 = 100 / (1 + 0.05) ** 3

# Print the result
print("3 year 5% yield ZCB: ", price_1)
```

**Instructions 2/3**

1. Find the price of a zero coupon bond with a ten year maturity, 5% yield, and USD 100 face value and print the result.

**Pre Code**

```py
# Calculate price of a 10 year 5% yield zero coupon bond
price_2 = ____

# Print the result
print("10 year 5% yield ZCB: ", ____)
```

**Ans.**

```py
# Calculate price of a 10 year 5% yield zero coupon bond
price_2 = 100 / (1 + 0.05) ** 10

# Print the result
print("10 year 5% yield ZCB: ", price_2)
```

**Instructions 3/3**

1. Find the price of a zero coupon bond with a three year maturity, 7% yield, and USD 100 face value and print the result.

**Pre Code**

```py
# Calculate price of a 3 year 7% yield zero coupon bond
price_3 = ____

# Print the result
print("3 year 7% yield ZCB: ", ____)
```

**Ans.**

```py
# Calculate price of a 3 year 7% yield zero coupon bond
price_3 = 100 / (1 + 0.07) ** 3

# Print the result
print("3 year 7% yield ZCB: ", price_3)
```

### Question 3: Impact of bond yields on price

In the financial markets, interest rates are constantly changing, and these changes will influence bond prices as the interest rate you use to discount the cash-flows of the bond (the yield) changes.

To get a better feel for how the prices of bonds behave with respect to yields, you will price a bond using a set yield to maturity, then price the same bond using both a higher and lower yield to maturity and see how this affects the bond price.

numpy_financial has already been imported for you as npf.

**Instructions 1/3**

1. Find the price of a 10 year bond with a face value of USD 100, annual coupon of 3%, yield of 4%, and print the result.

**Pre Code**

```py
# Find the price of a 10 year bond with 3% coupon and 4% yield
bond_yield_4 = -npf.pv(rate=____, nper=____, pmt=____, fv=____)

# Print the result
print("4% Yield Price: ", ____)
```

**Ans.**

```py
# Find the price of a 10 year bond with 3% coupon and 4% yield
bond_yield_4 = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)

# Print the result
print("4% Yield Price: ", bond_yield_4)
```

**Instructions 2/3**

1. Find the price of a 10 year bond with a face value of USD 100, annual coupon of 3%, yield of 3%, and print the result.

**Pre Code**

```py
# Find the price of a 10 year bond with 3% coupon and 3% yield
bond_yield_3 = ____

# Print the result
print("3% Yield Price: ", ____)
```

**Ans.**

```py
# Find the price of a 10 year bond with 3% coupon and 3% yield
bond_yield_3 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)

# Print the result
print("3% Yield Price: ", bond_yield_3)
```

**Instructions 3/3**

1. Find the price of a 10 year bond with a face value of USD 100, annual coupon of 3%, yield of 5%, and print the result.

**Pre Code**

```py
# Find the price of a 10 year bond with 3% coupon and 5% yield
bond_yield_5 = ____

# Print the result
print("5% Yield Price: ", ____)
```

**Ans.**

```py
# Find the price of a 10 year bond with 3% coupon and 5% yield
bond_yield_5 = -npf.pv(rate=0.05, nper=10, pmt=3, fv=100)

# Print the result
print("5% Yield Price: ", bond_yield_5)
```

### Question 4: Impact of coupons on price

You have looked at how changing the yield to maturity of a bond has a big impact on its price. Changing the coupon, i.e., the amount of money the bond pays in each period, can also have an impact on the bond's price. This is what you are going to investigate now by comparing bonds with high and low coupons.

numpy_financial has already been imported for you as npf.

**Instructions 1/3**

1. Find the price of a 10 year bond with a face value of USD 100, annual coupon of 2%, yield of 4%, and print the result.

**Pre Code**

```py
# Find the price of a 10 year bond with 2% coupon and 4% yield
bond_coupon_2 = -npf.pv(rate=____, nper=____, pmt=____, fv=____)

# Print the result
print("2% Coupon Price: ", ____)
```

**Ans.**

```py
# Find the price of a 10 year bond with 2% coupon and 4% yield
bond_coupon_2 = -npf.pv(rate=0.04, nper=10, pmt=2, fv=100)

# Print the result
print("2% Coupon Price: ", bond_coupon_2)
```

**Instructions 2/3**

1. Find the price of a 10 year bond with a face value of USD 100, annual coupon of 5%, yield of 4%, and print the result.

**Pre Code**

```py
# Find the price of a 10 year bond with 5% coupon and 4% yield
bond_coupon_5 = ____

# Print the result
print("5% Coupon Price: ", ____)
```

**Ans.**

```py
# Find the price of a 10 year bond with 5% coupon and 4% yield
bond_coupon_5 = -npf.pv(rate=0.04, nper=10, pmt=5, fv=100)

# Print the result
print("5% Coupon Price: ", bond_coupon_5)
```

**Instructions 3/3**

1. Find the price of a 10 year bond with a face value of USD 100, annual coupon of 10%, yield of 4%, and print the result.

**Pre Code**

```py
# Find the price of a 10 year bond with 10% coupon and 4% yield
bond_coupon_10 = ____

# Print the result
print("10% Coupon Price: ", ____)
```

**Ans.**

```py
# Find the price of a 10 year bond with 10% coupon and 4% yield
bond_coupon_10 = -npf.pv(rate=0.04, nper=10, pmt=10, fv=100)

# Print the result
print("10% Coupon Price: ", bond_coupon_10)
```

### Question 5: Discount vs. par vs. premium

Comparing a bond's coupon to its yield allows you to quickly tell if it is trading at a price above or below the level it was initially issued at (USD 100).

Let's practice applying the concept of a bond trading at a discount, at par, or at a premium.

**Instructions**

1. For each bond described, assign it to the right bucket.

**Ans.**

**Discount**

* 10 year bond with a price of 95.67
* 5 year bond with a coupon of 2% and yeild of 4%

**Par**

* 30 year bond with a price of 100
* 2 year bond with a coupon of 6% and yeild of 6%

**Premium**

* 7 year bond with a price of 105.83
* 20 year bond with a coupon of 5% and yeild of 3%

### Question 6: Plotting bond prices against yields

Being able to plot a graph of bond prices against yields can help to investigate what will happen to a bond or portfolio of bonds for different levels of interest rates in the market.

Now you are going to create a graph of bond prices against yields, but this time for two bonds of different maturities. You will do this by giving your pandas DataFrame extra columns for each additional bond. The bonds you will consider will both pay a 5% coupon, but now you will plot a 5 year and a 10 year bond.

numpy, numpy_financial, pandas, and matplotlib have already been imported for you as np, npf, pd, and plt, respectively.

**Instructions**

1. Create an array of bond yields from 0 to 20 (not inclusive) in increments of 0.1.
2. Convert this array into a pandas DataFrame and name the column bond_yield.
3. Add two more columns, one for each bond (5-year and 10-year), and find the price for a given level of yield.
4. Plot a graph of these bonds, setting the x-axis label to Yield (%) and y-axis label to Bond Price (USD).

**Pre Code**

```py
# Create an array of bond yields and convert to DataFrame
bond_yields = np.arange(____, ____, ____)
bond = pd.DataFrame(____, columns=['____'])

# Add columns for different bonds
bond['bond_price_5Y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=____, pmt=____, fv=____)
bond['bond_price_10Y'] = -npf.pv(rate=____, nper=____, pmt=____, fv=____)

# Plot graph of bonds
plt.plot(bond['bond_yield'], bond['bond_price_5Y'], label='5 Year Bond')
plt.plot(____, ____, label='10 Year Bond')
plt.xlabel(____)
plt.ylabel(____)
plt.legend()
plt.show()
```

**Ans.**

```py
# Create an array of bond yields and convert to DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add columns for different bonds
bond['bond_price_5Y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=5, pmt=5, fv=100)
bond['bond_price_10Y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=10, pmt=5, fv=100)

# Plot graph of bonds
plt.plot(bond['bond_yield'], bond['bond_price_5Y'], label='5 Year Bond')
plt.plot(bond['bond_yield'], bond['bond_price_10Y'], label='10 Year Bond')
plt.xlabel('Yield (%)')
plt.ylabel('Bond Price (USD)')
plt.legend()
plt.show()
```

### Question 7: Comparing zero coupon bond yields

Since changing the price of a bond affects the yield and the yield represents the return on investment, comparing different prices allows you to calculate the return you can make from different bonds of different prices.

In this exercise, you will compare the same zero coupon bond at different prices to see how it affects its yield. You will work directly with the formula calculated earlier.

Take a 5 year zero coupon bond with a face value of 100, and compare its yield when it has a price of USD 84.67 and USD 98.33.

**Instructions 1/2**

1. Find the yield of a 5 year zero coupon bond with a face value of USD 100 and price of USD 84.67.

**Pre Code**

```py
# Find the first zero coupon bond yield
bond_1 = ____

# Print the result
print("ZCB Price USD 84.67: ", ____)
```

**Ans.**

```py
# Find the first zero coupon bond yield
bond_1 = (100 / 84.67) ** (1 / 5) - 1

# Print the result
print("ZCB Price USD 84.67: ", bond_1)
```

**Instructions 2/2**

1. Find the yield of a 5 year zero coupon bond with a face value of USD 100 and price of USD 78.22.

**Pre Code**

```py
# Find the second zero coupon bond yield
bond_2 = ____

# Print the result
print("ZCB Price USD 78.22: ", ____)
```

**Ans.**

```py
# Find the second zero coupon bond yield
bond_2 = (100 / 78.22) ** (1 / 5) - 1

# Print the result
print("ZCB Price USD 78.22: ", bond_2)
```

### Question 8: Comparing coupon bond yields

Often you will be presented with several bonds with different characteristics, and it isn't clear which one has the highest yield.

In these cases, it can be helpful to find their yields in order to compare them properly, since the yield tells you which bond will give you the greatest return on your investment.

In this exercise, you will use the npf.rate() to compare three different bonds.

numpy_financial has already been imported for you as npf.

**Instructions 1/4**

1. Find the yield of a three-year bond paying a 3% annual coupon with a price of USD 92.

**Pre Code**

```py
# Bond with price of USD 92 paying 3% coupon for 3 years
bond_a = ____
print("Bond A: ", bond_a)
```

**Ans.**

```py
# Bond with price of USD 92 paying 3% coupon for 3 years
bond_a = npf.rate(nper=3, pmt=3, pv=-92, fv=100)
print("Bond A: ", bond_a)
```

**Instructions 2/4**

1. Find the yield of a five-year bond paying a 6% annual coupon with a price of USD 102.

**Pre Code**

```py
# Bond with price of USD 92 paying 3% coupon for 3 years
bond_a = npf.rate(nper=3, pmt=3, pv=-92, fv=100)
print("Bond A: ", bond_a)

# Bond with price of USD 102 paying 6% coupon for 5 years
bond_b = ____
print("Bond B: ", ____)
```

**Ans.**

```py
# Bond with price of USD 92 paying 3% coupon for 3 years
bond_a = npf.rate(nper=3, pmt=3, pv=-92, fv=100)
print("Bond A: ", bond_a)

# Bond with price of USD 102 paying 6% coupon for 5 years
bond_b = npf.rate(nper=5, pmt=6, pv=-102, fv=100)
print("Bond B: ", bond_b)
```

**Instructions 3/4**

1. Find the yield of a five-year bond paying a 3% annual coupon with a price of USD 95.

**Pre Code**

```py
# Bond with price of USD 92 paying 3% coupon for 3 years
bond_a = npf.rate(nper=3, pmt=3, pv=-92, fv=100)
print("Bond A: ", bond_a)

# Bond with price of USD 102 paying 6% coupon for 5 years
bond_b = npf.rate(nper=5, pmt=6, pv=-102, fv=100)
print("Bond B: ", bond_b)

# Bond with price of USD 95 paying 3% coupon for 5 years
bond_c = ____
print("Bond C: ", ____)
```

**Ans.**

```py
# Bond with price of USD 92 paying 3% coupon for 3 years
bond_a = npf.rate(nper=3, pmt=3, pv=-92, fv=100)
print("Bond A: ", bond_a)

# Bond with price of USD 102 paying 6% coupon for 5 years
bond_b = npf.rate(nper=5, pmt=6, pv=-102, fv=100)
print("Bond B: ", bond_b)

# Bond with price of USD 95 paying 3% coupon for 5 years
bond_c = npf.rate(nper=5, pmt=3, pv=-95, fv=100)
print("Bond C: ", bond_c)
```

**Instructions 4/4**

Which bond offers the greatest yield to maturity?

1. A 3 year bond paying a 3% annual coupon with a price of USD 92.
2. A 5 year bond paying a 6% annual coupon with a price of USD 102.
3. A 5 year bond paying a 3% annual coupon with a price of USD 95.

**Ans.** 1

<hr>