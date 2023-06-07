### Question 1: Predicted vs. actual prices I

Plotting the predicted prices of bonds for different levels of yields using duration, then comparing these predicted prices to the actual prices of the bond is a great way of visualizing the accuracy of duration.

In this exercise, you will begin by finding the duration of the bond, as well as the price of the bond at different yield levels. In the next exercise, you will find the predicted price from duration and plot the difference.

The bond you will consider is a 10 year bond paying an annual coupon of 5% and a yield to maturity of 5%.

numpy, numpy_financial, pandas, and matplotlib have already been imported for you as np, npf, pd, and plt, respectively.

**Instructions**

1. Find the duration and dollar duration of the bond.
2. Create an array of bond yields from 0 to 10 in increments of 0.1 and convert this array to a pandas DataFrame called bond_yield.
3. Add the column price containing the bond price for each level of yield.

**Pre Code**

```py
# Price a 10 year bond with 5% coupon and 5% yield, reprice at higher and lower yields
price = ____
price_up = ____
price_down = ____

# Find the duration and dollar duration of the bond
duration = ____
dollar_duration = ____ * ____ * ____

# Create an array of yields from 0 to 10 in steps of 0.1, convert to DataFrame
bond_yields = np.arange(____, ____, ____)
bond = pd.DataFrame(____, columns=['bond_yield'])

# Add a column called price with the bond price for each yield level
bond['price'] = -npf.pv(rate=bond['bond_yield'] / 100, ____, ____, ____)
```

**Ans.**

```py
# Price a 10 year bond with 5% coupon and 5% yield, reprice at higher and lower yields
price = -npf.pv(rate=0.05, nper=10, pmt=5, fv=100)
price_up = -npf.pv(rate=0.06, nper=10, pmt=5, fv=100)
price_down = -npf.pv(rate=0.04, nper=10, pmt=5, fv=100)

# Find the duration and dollar duration of the bond
duration = (price_down - price_up) / (2 * price * 0.01)
dollar_duration = duration * price * 0.01

# Create an array of yields from 0 to 10 in steps of 0.1, convert to DataFrame
bond_yields = np.arange(0, 10, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add a column called price with the bond price for each yield level
bond['price'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=10, pmt=5, fv=100)
```

### Question 2: Predicted vs. actual prices II

Plotting the predicted prices of bonds for different levels of yields using duration, then comparing these predicted prices to the actual prices of the bond is a great way of visualizing the accuracy of duration.

In the previous exercise, you found the duration of the bond, and created a DataFrame with the actual bond prices at each level of yield. In this exercise, you will add columns to this DataFrame containing the predicted bond prices using duration, then plot the difference between the predicted price and the actual price.

numpy, numpy_financial, pandas, and matplotlib have already been imported for you as np, npf, pd, and plt, respectively, as well as the code from the previous exercise.

**Instructions**

1. Add the column yield_change with the current yield minus original yield.
2. Add the column price_change with the predicted bond price change using dollar duration.
3. Add the column predicted_price combining the original bond price with the price change.
4. Add a plot of bond yields against actual prices and against predicted prices on the same axes, and show the plot.

**Pre Code**

```py
# Add a column called yield_change with the current yield minus original yield
bond['yield_change'] = (bond['bond_yield'] - ____)

# Find the predicted bond price change using dollar duration then find predicted price
bond['price_change'] = -100 * ____ * bond['yield_change'] / 100
bond['predicted_price'] = ____ + bond['price_change'] 

# Plot bond yields against predicted and actual prices, add labels, legend, and display
plt.plot(bond['bond_yield'], bond['price'])
plt.plot(____, ____)
plt.xlabel('Yield (%)')
plt.ylabel('Price (USD)')
plt.legend(["Actual Price", "Predicted Price"])
____
```

**Ans.**

```py
# Add a column called yield_change with the current yield minus original yield
bond['yield_change'] = (bond['bond_yield'] - 5)

# Find the predicted bond price change using dollar duration then find predicted price
bond['price_change'] = -100 * dollar_duration * bond['yield_change'] / 100
bond['predicted_price'] = price + bond['price_change'] 

# Plot bond yields against predicted and actual prices, add labels, legend, and display
plt.plot(bond['bond_yield'], bond['price'])
plt.plot(bond['bond_yield'], bond['predicted_price'])
plt.xlabel('Yield (%)')
plt.ylabel('Price (USD)')
plt.legend(["Actual Price", "Predicted Price"])
plt.show()
```

### Question 3: Finding the convexity of a bond

Calculating the convexity of a bond is an important step in predicting bond price changes and measuring the interest rate risk of a portfolio in a more comprehensive way.

In this exercise, you are going to find the convexity of a 20 year bond that pays a 6% annual coupon, has a yield to maturity of 5%, and face value of USD 100.

**Instructions**

1. Find the price of a 20 year bond with 6% coupon and 5% yield
2. Find the price of the same bond for a 1% higher and 1% lower level of yields.
3. Find the convexity of the bond and print the result.

**Pre Code**

```py
# Find the price of a 20 year bond with 6% coupon and 5% yield
price = ____

# Find the price of the same bond for a 1% higher and 1% lower level of yields
price_up = ____
price_down = ____

# Find the convexity of the bond and print the result
convexity = ____
print("Convexity: ", ____)
```

**Ans.**

```py
# Find the price of a 20 year bond with 6% coupon and 5% yield
price = -npf.pv(rate=0.05, nper=20, pmt=6, fv=100)

# Find the price of the same bond for a 1% higher and 1% lower level of yields
price_up = -npf.pv(rate=0.06, nper=20, pmt=6, fv=100)
price_down = -npf.pv(rate=0.04, nper=20, pmt=6, fv=100)

# Find the convexity of the bond and print the result
convexity = (price_down + price_up - 2 * price) / (price * 0.01 ** 2)
print("Convexity: ", convexity)
```

### Question 4: The bond with the highest convexity

By knowing how convexity changes with respect to maturity, coupon rate, and level of yield, you can sometimes tell which bond has the highest convexity without having to directly calculate it.

Which of the following bonds below has the highest convexity?

1. 20 year zero coupon bond with 3% yield
2. 10 year 5% coupon bond with 5% yield
3. 10 year 5% coupon bond with 3% yield
4. 10 year 2% coupon bond with 3% yield

**Ans.** 1

### Question 5: Comparing the convexity of two bonds directly

You can also investigate the influence of factors on bond convexity by pricing-up two bonds that vary only in this factor and then calculating the convexity of each bond directly.

In this exercise, you will find the convexity of two bonds; both will be 5 year bonds with a yield of 3% and face value of USD 100, but the first bond will pay a 1% coupon and the second bond will pay a 10% coupon.

numpy_financial has already been imported for you as npf.

**Instructions 1/2**

1. Find and print the convexity of a five year bond with a face value of USD 100, annual coupon of 1%, and yield of 3%.

**Pre Code**

```py
# Find the price of a 5 year bond with 3% yield and 1% coupon
price_1 = ____

# Shift yields up and down 1% and reprice
price_up_1 = ____
price_down_1 = ____

# Find convexity of the bond and print the result
convexity_1 = ____
print("Low Coupon Bond Convexity: ", ____)
```

**Ans.**

```py
# Find the price of a 5 year bond with 3% yield and 1% coupon
price_1 = -npf.pv(rate=0.03, nper=5, pmt=1, fv=100)

# Shift yields up and down 1% and reprice
price_up_1 = -npf.pv(rate=0.04, nper=5, pmt=1, fv=100)
price_down_1 = -npf.pv(rate=0.02, nper=5, pmt=1, fv=100)

# Find convexity of the bond and print the result
convexity_1 = (price_down_1 + price_up_1 - 2 * price_1) / (price_1 * 0.01 ** 2)
print("Low Coupon Bond Convexity: ", convexity_1)
```

**Instructions 2/2**

1. Find and print the convexity of a five year bond with a face value of USD 100, annual coupon of 10%, and yield of 3%.

**Pre Code**

```py
# Find the price of a 5 year bond with 3% yield and 10% coupon
price_2 = ____

# Shift yields up and down 1% and reprice
price_up_2 = ____
price_down_2 = ____

# Find convexity of the bond and print the result
convexity_2 = ____
print("High Coupon Bond Convexity: ", ____)
```

**Ans.**

```py
# Find the price of a 5 year bond with 3% yield and 10% coupon
price_2 = -npf.pv(rate=0.03, nper=5, pmt=10, fv=100)

# Shift yields up and down 1% and reprice
price_up_2 = -npf.pv(rate=0.04, nper=5, pmt=10, fv=100)
price_down_2 = -npf.pv(rate=0.02, nper=5, pmt=10, fv=100)

# Find convexity of the bond and print the result
convexity_2 = (price_down_2 + price_up_2 - 2 * price_2) / (price_2 * 0.01 ** 2)
print("High Coupon Bond Convexity: ", convexity_2)
```

### Question 6: Using the curvature of the price/yield line

In addition to using the steepness of the price/yield line to estimate the duration of a bond, you can also use its curvature to estimate the convexity of a bond.

In this exercise, you are going to plot a price/yield graph of two bonds in order to see which bond has the greatest convexity. Both bonds will pay a 5% annual coupon, have a 5% yield and a face value of USD 100, but the first bond will be a 5 year bond, and the second a 20 year bond.

numpy, numpy_financial, pandas, and matplotlib have already been imported for you as np, npf, pd, and plt, respectively.

**Instructions 1/3**

1. Create an array of yields from 0 to 20 in steps of 0.1 using the np.arange() function.
2. Convert this array to a pandas DataFrame with the column title bond_yield.

**Pre Code**

```py
# Create array of yields and convert to pandas DataFrame
bond_yields = ____
bond = ____(____, ____)
```

**Ans.**

```py
# Create array of yields and convert to pandas DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])
```

**Instructions 2/3**

1. Add two columns to your DataFrame, one for each bond.
2. Each bond pays a 5% coupon and has a face value of USD 100, the first bond is a 5 year bond and the second a 20 year bond.

**Pre Code**

```py
# Create array of yields and convert to pandas DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add columns for 5 year and 20 year bonds
bond['price_5y'] = -npf.pv(rate=bond['____'] / 100, nper=____, pmt=____, fv=____)
bond['price_20y'] = ____
```

**Ans.**

```py
# Create array of yields and convert to pandas DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add columns for 5 year and 20 year bonds
bond['price_5y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=5, pmt=5, fv=100)
bond['price_20y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=5, fv=100)
```

**Instructions 3/3**

1. Add each bond to the plot using the plt.plot() function.
2. Add a legend with the labels "5 Year Bond" and "20 Year Bond".
3. Show the plot.

**Pre Code**

```py
# Create array of yields and convert to pandas DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add columns for 5 year and 20 year bonds
bond['price_5y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=5, pmt=5, fv=100)
bond['price_20y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=5, fv=100)

# Create plot for bond bonds, add labels to axes, legend, and display
plt.plot(bond['bond_yield'], bond['____'])
plt.plot(bond['bond_yield'], bond['____'])
plt.xlabel('Yield (%)')
plt.ylabel('Price (USD)')
plt.legend(["____", "____"])
____
```

**Ans.**

```py
# Create array of yields and convert to pandas DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add columns for 5 year and 20 year bonds
bond['price_5y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=5, pmt=5, fv=100)
bond['price_20y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=5, fv=100)

# Create plot for bond bonds, add labels to axes, legend, and display
plt.plot(bond['bond_yield'], bond['price_5y'])
plt.plot(bond['bond_yield'], bond['price_20y'])
plt.xlabel('Yield (%)')
plt.ylabel('Price (USD)')
plt.legend(["5 Year Bond", "20 Year Bond"])
plt.show()
```

### Question 7: Plotting convexity vs. the factor

Another way to check what effect a certain factor has on bond convexity is to directly plot a graph of this factor against the bond's convexity.

In this exercise, you will price a 20 year bond with a 6% coupon and face value of USD 100, then find the convexity of this bond for different levels of yields.

numpy, numpy_financial, pandas, and matplotlib have already been imported for you as np, npf, pd, and plt, respectively.

**Instructions**

1. Create an array of bond yields from 0 to 20 in increments of 0.1 and convert to a pandas DataFrame.
2. Find the price of the bond, shift the yields up and down and reprice, then calculate the convexity of the bond.
3. Plot a graph of bond yields on the x-axis against convexity on the y-axis.

**Pre Code**

```py
# Create array of bond yields and covert to pandas DataFrame
bond_yields = np.arange(____, ____, ____)
bond = pd.DataFrame(____, columns=['bond_yield'])

# Find price of bond, reprice for higher and lower yields, calculate convexity
bond['price'] = -npf.pv(rate=bond['____'] / 100, nper=____, pmt=____, fv=____)
bond['price_up'] = ____
bond['price_down'] = ____
bond['convexity'] = (bond['____'] + bond['____'] - 2 * bond['____']) / (bond['____'] * 0.01 ** 2)

# Create plot of bond yields against convexity, add labels to axes, display plot
plt.plot(bond['____'], bond['____'])
plt.xlabel('Yield (%)')
plt.ylabel('Convexity')
____
```

**Ans.**

```py
# Create array of bond yields and covert to pandas DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Find price of bond, reprice for higher and lower yields, calculate convexity
bond['price'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=6, fv=100)
bond['price_up'] = -npf.pv(rate=bond['bond_yield'] / 100 + 0.01, nper=20, pmt=6, fv=100)
bond['price_down'] = -npf.pv(rate=bond['bond_yield'] / 100 - 0.01, nper=20, pmt=6, fv=100)
bond['convexity'] = (bond['price_down'] + bond['price_up'] - 2 * bond['price']) / (bond['price'] * 0.01 ** 2)

# Create plot of bond yields against convexity, add labels to axes, display plot
plt.plot(bond['bond_yield'], bond['convexity'])
plt.xlabel('Yield (%)')
plt.ylabel('Convexity')
plt.show()
```

### Question 8: Dollar convexity

Calculating the dollar convexity of a bond is an important first step in using convexity to predict bond prices. In this exercise, you are going to calculate the dollar convexity of a 10 year bond paying a 2% coupon, with a yield of 3% and face value of USD 100.

**Instructions**

1. Find the dollar convexity of a 10 year bond with a 2% annual coupon and 3% yield and print the result.

**Pre Code**

```py
# Find price of a 10 year bond with 2% coupon and 3% yield, shift yields, and reprice
price = ____
price_up = ____
price_down = ____

# Calculate convexity of the bond
convexity = ____

# Calculate dollar convexity and print the result
dollar_convexity = ____
print("Dollar convexity: ", ____)
```

**Ans.**

```py
# Find price of a 10 year bond with 2% coupon and 3% yield, shift yields, and reprice
price = -npf.pv(rate=0.03, nper=10, pmt=2, fv=100)
price_up = -npf.pv(rate=0.04, nper=10, pmt=2, fv=100)
price_down = -npf.pv(rate=0.02, nper=10, pmt=2, fv=100)

# Calculate convexity of the bond
convexity = (price_down + price_up - 2 * price) / (price * 0.01 ** 2)

# Calculate dollar convexity and print the result
dollar_convexity = convexity * price * 0.01 ** 2
print("Dollar convexity: ", dollar_convexity)
```

### Question 9: Convexity adjustment

Finding the convexity adjustment of a bond is the next step in using both duration and convexity to predict changes in bond prices. In this exercise, you are going to calculate the convexity adjustment for a 10 year zero coupon bond with a yield of 5% and face value of USD 100.

**Instructions**

1. Find the convexity adjustment for a 10 year zero coupon bond and print the result.

**Pre Code**

```py
# Find price of 10 year zero coupon bond with a 5% yield, shift yields, and reprice
price = ____
price_up = ____
price_down = ____

# Calculate convexity and dollar convexity of the bond
convexity = ____
dollar_convexity = ____

# Find the convexity adjustment and print the result
convexity_adjustment = ____
print("Convexity adjustment: ", ____)
```

**Ans.**

```py
# Find price of 10 year zero coupon bond with a 5% yield, shift yields, and reprice
price = -npf.pv(rate=0.05, nper=10, pmt=0, fv=100)
price_up = -npf.pv(rate=0.06, nper=10, pmt=0, fv=100)
price_down = -npf.pv(rate=0.04, nper=10, pmt=0, fv=100)

# Calculate convexity and dollar convexity of the bond
convexity = (price_down + price_up - 2 * price) / (price * 0.01 ** 2)
dollar_convexity = convexity * price * 0.01 ** 2

# Find the convexity adjustment and print the result
convexity_adjustment = 0.5 * dollar_convexity * 100 ** 2 * 0.01 ** 2
print("Convexity adjustment: ", convexity_adjustment)
```

### Question 10: Combining duration and convexity

Now let's combine everything you have learned in the last few chapters by using both duration and convexity to predict bond price changes. Take a 7 year bond that pays an annual coupon of 3% and has a yield to maturity of 4%.

**Instructions 1/4**

1. Find the price of a 7 year bond that pays an annual coupon of 3% and has a yield to maturity of 4%, then shift the yields up and down 1% and reprice.

**Pre Code**

```py
# Find the price of 7 year bond with 3% coupon and 4% yield, shift yields and reprice
price = ____
price_up = ____
price_down = ____
```

**Ans.**

```py
# Find the price of 7 year bond with 3% coupon and 4% yield, shift yields and reprice
price = -npf.pv(rate=0.04, nper=7, pmt=3, fv=100)
price_up = -npf.pv(rate=0.05, nper=7, pmt=3, fv=100)
price_down = -npf.pv(rate=0.03, nper=7, pmt=3, fv=100)
```

**Instructions 2/4**

1. Find the duration of the bond.
2. Find the dollar duration of the bond.

**Pre Code**

```py
# Find the price of 7 year bond with 3% coupon and 4% yield, shift yields and reprice
price = -npf.pv(rate=0.04, nper=7, pmt=3, fv=100)
price_up = -npf.pv(rate=0.05, nper=7, pmt=3, fv=100)
price_down = -npf.pv(rate=0.03, nper=7, pmt=3, fv=100)

# Find duration and dollar duration of the bond
duration = ____
dollar_duration = ____
```

**Ans.**

```py
# Find the price of 7 year bond with 3% coupon and 4% yield, shift yields and reprice
price = -npf.pv(rate=0.04, nper=7, pmt=3, fv=100)
price_up = -npf.pv(rate=0.05, nper=7, pmt=3, fv=100)
price_down = -npf.pv(rate=0.03, nper=7, pmt=3, fv=100)

# Find duration and dollar duration of the bond
duration = (price_down - price_up) / (2 * price * 0.01)
dollar_duration = duration * price * 0.01
```

**Instructions 3/4**

1. Find the convexity, dollar convexity, and convexity adjustment for the bond.

**Pre Code**

```py
# Find the price of 7 year bond with 3% coupon and 4% yield, shift yields and reprice
price = -npf.pv(rate=0.04, nper=7, pmt=3, fv=100)
price_up = -npf.pv(rate=0.05, nper=7, pmt=3, fv=100)
price_down = -npf.pv(rate=0.03, nper=7, pmt=3, fv=100)

# Find duration and dollar duration of the bond
duration = (price_down - price_up) / (2 * price * 0.01)
dollar_duration = duration * price * 0.01

# Find convexity, dollar convexity and convexity adjustment
convexity = ____
dollar_convexity = ____
convexity_adjustment = ____
```

**Ans.**

```py
# Find the price of 7 year bond with 3% coupon and 4% yield, shift yields and reprice
price = -npf.pv(rate=0.04, nper=7, pmt=3, fv=100)
price_up = -npf.pv(rate=0.05, nper=7, pmt=3, fv=100)
price_down = -npf.pv(rate=0.03, nper=7, pmt=3, fv=100)

# Find duration and dollar duration of the bond
duration = (price_down - price_up) / (2 * price * 0.01)
dollar_duration = duration * price * 0.01

# Find convexity, dollar convexity and convexity adjustment
convexity = (price_down + price_up - 2 * price) / (price * 0.01 ** 2)
dollar_convexity = convexity * price * 0.01 ** 2
convexity_adjustment = 0.5 * dollar_convexity * 100 ** 2 * 0.01 ** 2
```

**Instructions 4/4**

1. Predict the bond price change for a 1% change in yields.

**Pre Code**

```py
# Find the price of 7 year bond with 3% coupon and 4% yield, shift yields and reprice
price = -npf.pv(rate=0.04, nper=7, pmt=3, fv=100)
price_up = -npf.pv(rate=0.05, nper=7, pmt=3, fv=100)
price_down = -npf.pv(rate=0.03, nper=7, pmt=3, fv=100)

# Find duration and dollar duration of the bond
duration = (price_down - price_up) / (2 * price * 0.01)
dollar_duration = duration * price * 0.01

# Find convexity, dollar convexity and convexity adjustment
convexity = (price_down + price_up - 2 * price) / (price * 0.01 ** 2)
dollar_convexity = convexity * price * 0.01 ** 2
convexity_adjustment = 0.5 * dollar_convexity * 100 ** 2 * 0.01 ** 2

# Combine duration and convexity to predict bond price change
combined_prediction = ____
print("Predicted Price Change: ", ____)
```

**Ans.**

```py
# Find the price of 7 year bond with 3% coupon and 4% yield, shift yields and reprice
price = -npf.pv(rate=0.04, nper=7, pmt=3, fv=100)
price_up = -npf.pv(rate=0.05, nper=7, pmt=3, fv=100)
price_down = -npf.pv(rate=0.03, nper=7, pmt=3, fv=100)

# Find duration and dollar duration of the bond
duration = (price_down - price_up) / (2 * price * 0.01)
dollar_duration = duration * price * 0.01

# Find convexity, dollar convexity and convexity adjustment
convexity = (price_down + price_up - 2 * price) / (price * 0.01 ** 2)
dollar_convexity = convexity * price * 0.01 ** 2
convexity_adjustment = 0.5 * dollar_convexity * 100 ** 2 * 0.01 ** 2

# Combine duration and convexity to predict bond price change
combined_prediction = -100 * dollar_duration * 0.01 + convexity_adjustment
print("Predicted Price Change: ", combined_prediction)
```

<hr>