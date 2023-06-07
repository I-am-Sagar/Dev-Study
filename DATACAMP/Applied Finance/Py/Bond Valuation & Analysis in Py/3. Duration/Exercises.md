### Question 1: Interest rate sensitivity of two bonds

Knowing the interest rate sensitivity of a bond or portfolio of bonds is important for investors. It allows them to gauge how exposed they are to changes in interest rates and make sure this exposure is within their risk tolerance.

In this exercise, you will compare the price impact on two bonds from a change in interest rates to establish which bond has a higher level of interest rate sensitivity.

You will consider two bonds; a ten year and a twenty year bond, both paying an annual coupon of 3%, with a face value of USD 100. numpy_financial has been imported for you as npf.

**Instructions 1/4**

1. Find the price of a 10 year bond with a 3% coupon and 3% yield and print the result.

**Pre Code**

```py
# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = ____
print("10 Year Bond 3% Yield: ", bond_1)
```

**Ans.**

```py
# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)
print("10 Year Bond 3% Yield: ", bond_1)
```

**Instructions 2/4**

1. Now find the price of the same 10 year bond but with a 4% yield instead and print the result.

**Pre Code**

```py
# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)
print("10 Year Bond 3% Yield: ", bond_1)

# Price a 10 year bond with 3% annual coupon at 4% yield and print
bond_2 = ____
print("10 Year Bond 4% Yield: ", bond_2)
```

**Ans.**

```py
# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)
print("10 Year Bond 3% Yield: ", bond_1)

# Price a 10 year bond with 3% annual coupon at 4% yield and print
bond_2 = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)
print("10 Year Bond 4% Yield: ", bond_2)
```
**Instructions 3/4**

1. Now find the price of a 20 year bond with a 3% coupon and 3% yield and print the result.

**Pre Code**

```py
# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)
print("10 Year Bond 3% Yield: ", bond_1)

# Price a 10 year bond with 3% annual coupon at 4% yield and print
bond_2 = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)
print("10 Year Bond 4% Yield: ", bond_2)

# Price a 20 year bond with 3% annual coupon at 3% yield and print
bond_3 = ____
print("20 Year Bond 3% Yield: ", bond_3)
```

**Ans.**

```py
# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)
print("10 Year Bond 3% Yield: ", bond_1)

# Price a 10 year bond with 3% annual coupon at 4% yield and print
bond_2 = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)
print("10 Year Bond 4% Yield: ", bond_2)

# Price a 20 year bond with 3% annual coupon at 3% yield and print
bond_3 = -npf.pv(rate=0.03, nper=20, pmt=3, fv=100)
print("20 Year Bond 3% Yield: ", bond_3)
```
**Instructions 4/4**

1. Now find the price of the same 20 year bond but with a yield of 4% instead and print the result.

**Pre Code**

```py
# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)
print("10 Year Bond 3% Yield: ", bond_1)

# Price a 10 year bond with 3% annual coupon at 4% yield and print
bond_2 = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)
print("10 Year Bond 4% Yield: ", bond_2)

# Price a 20 year bond with 3% annual coupon at 3% yield and print
bond_3 = -npf.pv(rate=0.03, nper=20, pmt=3, fv=100)
print("20 Year Bond 3% Yield: ", bond_3)

# Price a 20 year bond with 3% annual coupon at 4% yield and print
bond_4 = ____
print("20 Year Bond 4% Yield: ", ____)
```

**Ans.**

```py
# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)
print("10 Year Bond 3% Yield: ", bond_1)

# Price a 10 year bond with 3% annual coupon at 4% yield and print
bond_2 = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)
print("10 Year Bond 4% Yield: ", bond_2)

# Price a 20 year bond with 3% annual coupon at 3% yield and print
bond_3 = -npf.pv(rate=0.03, nper=20, pmt=3, fv=100)
print("20 Year Bond 3% Yield: ", bond_3)

# Price a 20 year bond with 3% annual coupon at 4% yield and print
bond_4 = -npf.pv(rate=0.04, nper=20, pmt=3, fv=100)
print("20 Year Bond 4% Yield: ", bond_4)
```

### Question 2: Zero coupon and coupon bond duration

Duration is a measure of interest rate risk that can be applied to any bond, regardless of whether it pays a coupon or not.

In this exercise, you are going to calculate the duration of a zero coupon bond with a ten year maturity, face value of USD 100, and a yield to maturity of 3%, and compare its duration to the same bond paying a 3% annual coupon. numpy_financial has already been imported for you as npf.

**Instructions 1/2**

1. Find the duration of a 10 year zero coupon bond with a 3% yield, then print the result.

**Pre Code**

```py
# Find the price of the zero coupon bond at current yield levels
price = ____

# Find the price of the zero coupon bond at 1% higher yield levels
price_up = ____

# Find the price of the zero coupon bond at 1% lower yield levels
price_down = ____

# Calculate duration using the formula and print result
duration = (____ - ____) / (____ * ____ * ____)
print("Zero Coupon Bond Duration: ", ____)
```

**Ans.**

```py
# Find the price of the zero coupon bond at current yield levels
price = -npf.pv(rate=0.03, nper=10, pmt=0, fv=100)

# Find the price of the zero coupon bond at 1% higher yield levels
price_up = -npf.pv(rate=0.04, nper=10, pmt=0, fv=100)

# Find the price of the zero coupon bond at 1% lower yield levels
price_down = -npf.pv(rate=0.02, nper=10, pmt=0, fv=100)

# Calculate duration using the formula and print result
duration = (price_down - price_up) / (2 * price * 0.01)
print("Zero Coupon Bond Duration: ", duration)
```

**Instructions 2/2**

1. Find the duration of a 10 year bond with a 3% coupon and 3% yield, then print the result.

**Pre Code**

```py
# Find the price of the coupon bond at current yield levels
price = ____

# Find the price of the coupon bond at 1% higher yield levels
price_up = ____

# Find the price of the coupon bond at 1% lower yield levels
price_down = ____

# Calculate duration using the formula
duration = ____

# Print the result
print("Coupon Paying Bond Duration: ", ____)
```

**Ans.**

```py
# Find the price of the coupon bond at current yield levels
price = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)

# Find the price of the coupon bond at 1% higher yield levels
price_up = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)

# Find the price of the coupon bond at 1% lower yield levels
price_down = -npf.pv(rate=0.02, nper=10, pmt=3, fv=100)

# Calculate duration using the formula
duration = (price_down - price_up) / (2 * price * 0.01)

# Print the result
print("Coupon Paying Bond Duration: ", duration)
```

### Question 3: The bond with the highest duration

By applying your knowledge of the factors affecting a bond's duration, you can often tell which bond will have the highest duration without directly calculating it.

This is useful if, for example, you need to quickly decide which bond in a portfolio will be the riskiest.

Which of the bonds from the options below will have the highest duration?

1. A 10 year bond with a 5% annual coupon and 4% yield.
2. A 20 year zero coupon bond with a 2% yield.
3. A 10 year bond with a 3% annual coupon and 4% yield.
4. A 20 year zero coupon bond with a 3% yield.

**Ans.** 2

### Question 4: Comparing the duration of two bonds directly

A quick way to check the impact of a factor on duration is to find the duration of two different bonds where you increase this factor and see what effect it has on the bond's duration.

In this exercise, you will calculate the duration of a 10 year and a 20 year bond, both paying an annual coupon of 3%, with a face value of USD 100, and yield to maturity of 5%.

numpy_financial is already imported for you as npf.

**Instructions 1/2**

1. Find the duration of the 10 year bond and print the result.

**Pre Code**

```py
# Find & print duration of 10 year bond with 3% coupon & 5% yield
price_10y = -npf.pv(rate=0.05, nper=____, pmt=____, fv=____)
price_up_10y = -npf.pv(rate=0.06, nper=____, pmt=____, fv=____)
price_down_10y = -npf.pv(rate=0.04, nper=____, pmt=____, fv=____)
duration_10y = (____ - ____) / (____ * ____ * ____)
print("10 Year Bond: ", ____)
```

**Ans.**

```py
# Find & print duration of 10 year bond with 3% coupon & 5% yield
price_10y = -npf.pv(rate=0.05, nper=10, pmt=3, fv=100)
price_up_10y = -npf.pv(rate=0.06, nper=10, pmt=3, fv=100)
price_down_10y = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)
duration_10y = (price_down_10y - price_up_10y) / (2 * price_10y * 0.01)
print("10 Year Bond: ", duration_10y)
```

**Instructions 2/2**

1. Find the duration of the 20 year bond and print the result.

**Pre Code**

```py
# Find & print duration of 20 year bond with 3% coupon & 5% yield
price_20y = ____
price_up_20y = ____
price_down_20y = ____
duration_20y = ____
print("20 Year Bond: ", ____)
```

**Ans.**

```py
# Find & print duration of 20 year bond with 3% coupon & 5% yield
price_20y = -npf.pv(rate=0.05, nper=20, pmt=3, fv=100)
price_up_20y = -npf.pv(rate=0.06, nper=20, pmt=3, fv=100)
price_down_20y = -npf.pv(rate=0.04, nper=20, pmt=3, fv=100)
duration_20y = (price_down_20y - price_up_20y) / (2 * price_20y * 0.01)
print("20 Year Bond: ", duration_20y)
```

### Question 5: Using the steepness of the price/yield line

In the previous video, you saw that you can plot a graph of bond prices against yields and check its steepness visually to determine where it has the highest duration.

In this exercise, you are going to replicate this plot yourself to see how bond yields affect bond duration. You will consider a 20 year bond with a 5% coupon and face value of USD 100.

numpy, numpy_financial, pandas, and matplotlib have already been imported for you as np, npf, pd, and plt, respectively.

**Instructions 1/4**

1. Create an array of bond yields from 0 to 20 in increment sizes of 0.1.
2. Convert this array into a pandas DataFrame called bond and name the column bond_yield.

**Pre Code**

```py
# Create an array of bond yields
bond_yields = np.arange(____, ____, ____)

# Convert this array into a pandas DataFrame and add column title
bond = pd.DataFrame(____, ____)
```

**Ans.**

```py
# Create an array of bond yields
bond_yields = np.arange(0, 20, 0.1)

# Convert this array into a pandas DataFrame and add column title
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])
```

**Instructions 2/4**

1. Add the column bond_price to the DataFrame and assign it a 20 year bond with a 5% coupon and face value of USD 100, whose yield depends on the value of bond_yield.

**Pre Code**

```py
# Create an array of bond yields
bond_yields = np.arange(0, 20, 0.1)

# Convert this array into a pandas DataFrame and add column title
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add bond price column with price varying according to the yield
bond['bond_price'] = -npf.pv(rate=bond['____'] / ____, nper=____, pmt=____, fv=____)
```

**Ans.**

```py
# Create an array of bond yields
bond_yields = np.arange(0, 20, 0.1)

# Convert this array into a pandas DataFrame and add column title
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add bond price column with price varying according to the yield
bond['bond_price'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=5, fv=100)
```

**Instructions 3/4**

1. Plot a graph of the bond_yield column on the x-axis against the bond_price column on the y-axis.
2. Give the x-axis the label 'Yield (%)'.
3. Give the y-axis the label 'Bond Price (USD)'.

**Pre Code**

```py
# Create an array of bond yields
bond_yields = np.arange(0, 20, 0.1)

# Convert this array into a pandas DataFrame and add column title
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add bond price column with price varying according to the yield
bond['bond_price'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=5, fv=100)

# Plot graph of bond yields against prices, add x-axis and y-axis labels, show plot
plt.plot(____, ____)
plt.xlabel(____)
plt.ylabel(____)
plt.show()
```

**Ans.**

```py
# Create an array of bond yields
bond_yields = np.arange(0, 20, 0.1)

# Convert this array into a pandas DataFrame and add column title
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add bond price column with price varying according to the yield
bond['bond_price'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=5, fv=100)

# Plot graph of bond yields against prices, add x-axis and y-axis labels, show plot
plt.plot(bond['bond_yield'], bond['bond_price'])
plt.xlabel('Yield (%)')
plt.ylabel('Bond Price (USD)')
plt.show()
```

**Instructions 4/4**

Looking at the slope of the graph at different levels of yield, what bond has a higher duration, a bond with a low yield or a bond with a high yield?

1. A bond with high yield to maturity 
2. A bond with low yield to maturity

**Ans.** 2

### Question 6: Plotting duration vs. the factor

Plotting a graph of duration against a factor such as maturity, coupons, or yields is a great way to see how the factor affects the duration of a bond.

In the video, we plotted a graph of duration against maturity. In this exercise, you are going to do the same thing for the coupon rate. You will use a 10 year bond with a yield of 5% and face value of USD 100.

numpy, numpy_financial, pandas, and matplotlib have already been imported for you as np, npf, pd, and plt, respectively.

**Instructions**

1. Create an array of coupons from 0 to 10 in increment sizes of 0.1, and convert to a pandas DataFrame.
2. Add four additional columns to the DataFrame; price, price_up, price_down, and duration for the bond.
3. Plot a graph with bond_coupon on the x-axis and duration on the y-axis.

**Pre Code**

```py
# Create array of coupon rates and assign to pandas DataFrame
bond_coupon = np.arange(____, ____, ____)
bond = pd.DataFrame(____, columns=['____'])

# Calculate bond price, price_up, price_down, and duration
bond['price'] = -npf.pv(rate=0.05, nper=10, pmt=bond['bond_coupon'], fv=100)
bond['price_up'] = ____
bond['price_down'] = ____
bond['duration'] = (bond['____'] - bond['____']) / (2 * bond['____'] * 0.01)

# Plot coupon vs. duration, add labels & title, show plot
plt.plot(____, ____)
plt.xlabel('Coupon (%)')
plt.ylabel('Duration (%)')
plt.show()
```

**Ans.**

```py
# Create array of coupon rates and assign to pandas DataFrame
bond_coupon = np.arange(0, 10, 0.1)
bond = pd.DataFrame(bond_coupon, columns=['bond_coupon'])

# Calculate bond price, price_up, price_down, and duration
bond['price'] = -npf.pv(rate=0.05, nper=10, pmt=bond['bond_coupon'], fv=100)
bond['price_up'] = -npf.pv(rate=0.05 + 0.01, nper=10, pmt=bond['bond_coupon'], fv=100)
bond['price_down'] = -npf.pv(rate=0.05 - 0.01, nper=10, pmt=bond['bond_coupon'], fv=100)
bond['duration'] = (bond['price_down'] - bond['price_up']) / (2 * bond['price'] * 0.01)

# Plot coupon vs. duration, add labels & title, show plot
plt.plot(bond['bond_coupon'], bond['duration'])
plt.xlabel('Coupon (%)')
plt.ylabel('Duration (%)')
plt.show()
```

### Question 7: Percent duration and dollar duration

Dollar duration and DV01 are more commonly used in the real world to quickly measure the interest rate risk of a bond or portfolio. They can also be used for other financial instruments that contain some interest rate risk.

In this exercise, you are going to find the dollar duration and DV01 of a bond. The bond has a 30 year maturity, coupon rate of 3.5%, yield to maturity of 5%, and face value of USD 100.

numpy_financial has already imported for you as npf.

**Instructions**

1. Find the duration of a 30 year bond with a coupon rate of 3.5% and yield of 5% in the usual way.
2. Find the dollar duration of the bond.
3. Find the DV01 of the bond.

**Pre Code**

```py
# Find the duration of the bond
price = ____
price_up = ____
price_down = ____
duration = ____

# Find the dollar duration of the bond
dollar_duration = ____ * ____ * ____
print("Dollar Duration: ", ____)

# Find the DV01 of the bond
dv01 = ____ * ____ * ____
print("DV01: ", ____)
```

**Ans.**

```py
# Find the duration of the bond
price = -npf.pv(rate=0.05, nper=30, pmt=3.5, fv=100)
price_up = -npf.pv(rate=0.06, nper=30, pmt=3.5, fv=100)
price_down = -npf.pv(rate=0.04, nper=30, pmt=3.5, fv=100)
duration = (price_down - price_up) / (2 * price * 0.01)

# Find the dollar duration of the bond
dollar_duration = duration * price * 0.01
print("Dollar Duration: ", dollar_duration)

# Find the DV01 of the bond
dv01 = duration * price * 0.0001
print("DV01: ", dv01)
```

### Question 8: Creating a duration neutral portfolio

Hedging is a very important part of working with bonds and bond portfolios. In this exercise, you are going to find the quantity of a bond needed to hedge a portfolio, as well as the dollar amount of this quantity.

Say you own a portfolio of bonds whose combined DV01 is USD 5,000. You decide to hedge this portfolio by selling a fixed amount of the 30 year bond from the previous exercise, which has a price of USD 76.94 and a DV01 of 12.88 cents.

**Instructions**

1. Assign the DV01 of the portfolio and the bond to portfolio_dv01, bond_dv01, respectively, and the bond price to bond_price.
2. Find the number of bonds needed to hedge the portfolio.
3. Find the dollar value of this amount of bonds.

**Pre Code**

```py
# Assign DV01 of portfolio and bond to variables
portfolio_dv01 = ____
bond_dv01 = ____
bond_price = ____

# Calculate quantity of bond to hedge portfolio
hedge_quantity = ____
print("Number of bonds to sell: ", ____)

# Calculate dollar amount of bond to hedge portfolio
hedge_amount = ____
print("Dollar amount to sell: USD", ____)
```

**Ans.**

```py
# Assign DV01 of portfolio and bond to variables
portfolio_dv01 = 5000
bond_dv01 = 0.1288
bond_price = 76.94

# Calculate quantity of bond to hedge portfolio
hedge_quantity = portfolio_dv01 / bond_dv01
print("Number of bonds to sell: ", hedge_quantity)

# Calculate dollar amount of bond to hedge portfolio
hedge_amount = hedge_quantity * bond_price
print("Dollar amount to sell: USD", hedge_amount)
```

### Question 9: Predicting price impacts from duration

Using duration to predict price impacts is very common when managing a large portfolio of bonds, where repricing each bond would be very time consuming. Instead, you can find the dollar duration of the portfolio and use this to predict what will happen to the portfolio as interest rates change.

In this exercise, you will estimate the price change of a bond using duration, then compare this to the actual price of the bond to see how accurate your estimate was.

The bond has a maturity of 5 years, coupon of 7%, yield of 4%, and face value of USD 100. It has a price of USD 113.36 and dollar duration of USD 4.83. You will predict the price change for a 2% decrease in interest rates.

numpy_financial is already imported for you as npf.

**Instructions**

1. Assign the bond price, dollar duration, and yield change to bond_price, dollar_duration, and yield_change, respectively.
2. Calculate the expected price change using dollar duration.
3. Calculate the actual price change by repricing the bond at 2% yields and subtracting its previous price.

**Pre Code**

```py
# Assign bond price, dollar duration, yield change to variables
bond_price = ____
dollar_duration = ____
yield_change = ____

# Predict bond price change using duration
price_prediction = ____ * ____ * ____
print("Predicted Change: USD ", ____)

# Find actual price change and compare
price_actual = -npf.pv(rate=____, nper=____, pmt=____, fv=____) - ____
print("Actual Change: USD ", ____)
print("Estimation Error: USD ", price_prediction - price_actual)
```

**Ans.**

```py
# Assign bond price, dollar duration, yield change to variables
bond_price = 113.36
dollar_duration = 4.83
yield_change = -0.02

# Predict bond price change using duration
price_prediction = -100 * dollar_duration * yield_change
print("Predicted Change: USD ", price_prediction)

# Find actual price change and compare
price_actual = -npf.pv(rate=0.02, nper=5, pmt=7, fv=100) - bond_price
print("Actual Change: USD ", price_actual)
print("Estimation Error: USD ", price_prediction - price_actual)
```
