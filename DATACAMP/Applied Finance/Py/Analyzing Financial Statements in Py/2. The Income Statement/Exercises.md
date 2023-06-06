### Question 1: Compute net income

One of the uses of an income statement is to determine how much profit (also called net income) the company is making. In this exercise, you will compute the net income of a company.

In this exercise, total_revenue, depreciation, and cost_of_goods_sold have already been loaded for you. You will compute the income before taxes using these items. Then, assuming a tax rate of 5%, you will compute the net income, i.e., the income after taxes.

**Instructions**

1. Compute the income before taxes.
2. Assuming a tax rate of 5%, compute the net income.

**Pre Code**

```py
depreciation = 260
total_revenue = 3640
cost_of_goods_sold = 460

# Compute income before taxes
income_before_taxes = ____

# Compute income before taxes
net_income = ____

print(net_income)
```

**Ans.**

```py
depreciation = 260
total_revenue = 3640
cost_of_goods_sold = 460

# Compute income before taxes
income_before_taxes = total_revenue - depreciation - cost_of_goods_sold

# Compute income before taxes
net_income = income_before_taxes - (5/100) * income_before_taxes

print(net_income)
```

### Question 2: Computing ratios from the income statement

The gross and operating margins are commonly used to see how efficiently a company uses its assets to earn money. In this exercise, you will compute the average gross margin and operating margin by industry.

The DataFrame income_statement has already been loaded for you, and pandas have also been loaded with the alias pd.

**Instructions 1/2**

1. Print the columns of income_statement to view the columns you can use to compute the gross and operating margin.

**Pre Code**

```py
# Check the columns of the income statement
print(income_statement.____)
```

**Ans.**

```py
# Check the columns of the income statement
print(income_statement.columns)
```

**Instructions 2/2**

1. Compute the gross margin.
2. Compute the operating margin.
3. Use .groupby() to return the average gross margin and operating margin by industry (provided in the comp_type column).

**Pre Code**

```py
# Compute the gross margin
income_statement["gross_margin"] = ____

# Compute the operating margin
income_statement["operating_margin"] = ____

# Calculate mean gross margin and operating margin by industry
average_ratio = ____

print(average_ratio)
```

**Ans.**

```py
# Compute the gross margin
income_statement["gross_margin"] = (income_statement["Total Revenue"] - income_statement["Cost Of Revenue"])/income_statement["Total Revenue"]

# Compute the operating margin
income_statement["operating_margin"] = (income_statement["Total Revenue"] - income_statement["Total Operating Expenses"])/income_statement["Total Revenue"]

# Calculate mean gross margin and operating margin by industry
average_ratio = income_statement.groupby("comp_type")[["gross_margin", "operating_margin"]].mean()
print(average_ratio)
```

### Question 3: Updating the user-defined function
User-defined functions are a great way of reducing repetitive work. The function defined in the video is provided below:

```py
def compute_ratio(df, numerator, denominator,
                  ratio_name):
    df[ratio_name] = df[numerator] / df[denominator]
    return df
```

Notice that the function we defined cannot directly compute ratios that require adding or subtracting values in the numerator and denominator, such as the operating or the gross margin ratio.

In this exercise, you will update this function so that it can be used to compute ratios that involve addition in the numerator and denominator.

You will use a pandas function called .sum(), which can sum over an axis in the DataFrame. An axis of 0 means rows, so it would sum up values over the rows and return one value for each column. An axis of 1 means columns, so it would sum up values from different columns in df and return one value for each row. You can think of df.sum(axis=1) as being equivalent to df[column_1] + ... + df[column_n]. The default axis in pd.sum() is 0. 

**Instructions 1/3**

1. Update the function compute_ratio to take a list of numerator column names and sum them up so that one value is returned for each row; do the same for a list of denominator column names.

**Pre Code**

```py
# Update the function
def compute_ratio(df, numerator, denominator, ratio_name):
    df[ratio_name] = df[numerator]____ / df[denominator]____
    return df
```

**Ans.**

```py
# Update the function
def compute_ratio(df, numerator, denominator, ratio_name):
    df[ratio_name] = df[numerator].sum(axis=1) / df[denominator].sum(axis=1)
    return df
```

**Instructions 2/3**

1. Print the columns of the DataFrame balance_sheet to see if you can compute the current ratio with the given columns.

**Pre Code**

```py
def compute_ratio(df, numerator, denominator, ratio_name):
    df[ratio_name] = df[numerator].sum(axis=1) / df[denominator].sum(axis=1)
    return df

# Check the columns of balance_sheet
print(balance_sheet____)
```

**Ans.**

```py
def compute_ratio(df, numerator, denominator, ratio_name):
    df[ratio_name] = df[numerator].sum(axis=1) / df[denominator].sum(axis=1)
    return df

# Check the columns of balance_sheet
print(balance_sheet.columns)
```

**Instructions 3/3**

1. Compute a column called current_ratio with the function compute_ratio using the columns provided in balance_sheet.

**Pre Code**

```py
def compute_ratio(df, numerator, denominator, ratio_name):
    df[ratio_name] = df[numerator].sum(axis=1) / df[denominator].sum(axis=1)
    return df

print(balance_sheet.columns)

# Use compute_ratio to compute the current ratio
balance_sheet = ____

print(balance_sheet)
```

**Ans.**

```py
def compute_ratio(df, numerator, denominator, ratio_name):
    df[ratio_name] = df[numerator].sum(axis=1) / df[denominator].sum(axis=1)
    return df

print(balance_sheet.columns)

# Use compute_ratio to compute the current ratio
balance_sheet = compute_ratio(balance_sheet, ["Inventory", "Short Term Investments"], ["Accounts Payable"], "current_ratio")

print(balance_sheet)
```

### Question 4: Updating user-defined function to do subtraction

The function you worked on in the previous exercise cannot do subtraction. Have a look at this function:

```py
def compute_ratio(df, numerator, denominator, ratio_name, 
                  addition_in_numerator = True,
                  addition_in_denominator = True):
  numerator_of_ratio = np.where(addition_in_numerator,
                             df[numerator].sum(axis=1), 
                             df[numerator[0]] - df[numerator[1:]].sum(
                               axis=1))
  denominator_of_ratio = np.where(addition_in_denominator, 
                               df[denominator].sum(axis=1), 
                               df[denominator[0]] - df[denominator[1:]].sum(axis=1))
  df[ratio_name] = numerator_of_ratio/denominator_of_ratio
  return df
```

This function can deal with addition and subtraction in numerators and denominators of financial ratios. Notice that the function uses np.where. This is a function from the package NumPy. np.where checks if the first argument is True; if so, it returns the second argument, else it returns the third. For example, in the above, we have:

```py
np.where(addition_in_numerator,
                             df[numerator].sum(axis=1), 
                             df[numerator[0]] - df[numerator[1:]].sum(
                               axis=1))
If addition_in_numerator is true, np.where will return df[numerator].sum(axis=1), else it will return df[numerator[0]] - df[numerator[1:]].sum(axis=1).
```

In this exercise, the balance_sheet DataFrame, along with pandas and NumPy aspd and np, respectively, have been loaded for you. Use these to determine which of the following statements is correct.

1. The function subtracts random columns from the list of columns in numerator and denominator
2. The function cannot handle cases where we want to add values in the numerator while subtracting values in the denominator for the ratio we want to compute.
3. The function subtracts the sum of the rest of the columns named in the denominator and numerator from the first column.
4. The function does not append the computed ratio in the returned DataFrame. 

**Ans.** 3

### Question 5: Computing ratios with user-defined function

In this exercise, you'll use the function from the last exercise to compute financial ratios. Recall that the function is:

```py
def compute_ratio(df, numerator, denominator, ratio_name, 
                  addition_in_numerator = True,
                  addition_in_denominator = True):
  numerator_of_ratio = np.where(addition_in_numerator,
                             df[numerator].sum(axis=1), 
                             df[numerator[0]] - df[numerator[1:]].sum(
                               axis=1))
  denominator_of_ratio = np.where(addition_in_denominator, 
                               df[denominator].sum(axis=1), 
                               df[denominator[0]] - df[denominator[1:]].sum(axis=1))
  df[ratio_name] = numerator_of_ratio/denominator_of_ratio
  return df
```

The pandas DataFrame merged_dat is loaded for you, which you will use to compute financial ratios using the function compute_ratio.

**Instructions 1/2**

1. Print the columns of merged_dat to verify if you can compute gross margin and asset turnover ratio.

**Pre Code**

```py
# Print the columns of merged_dat
print(merged_dat____)
```

**Ans.**

```py
# Print the columns of merged_dat
print(merged_dat.columns)
```

**Instructions  2/2**

1. Compute gross margin using the function compute_ratio.
2. Compute the asset turnover ratio using the function compute_ratio.

**Pre Code**

```py
print(merged_dat.columns)

# Compute gross margin using compute_ratio
merged_dat = compute_ratio(____, ratio_name="gross_margin")

# Compute asset turnover ratio using compute_ratio
merged_dat = compute_ratio(____, ratio_name="asset_turnover")

print(merged_dat.head())
```

**Ans.**

```py
# Print the columns of merged_dat
print(merged_dat.columns)

# Compute gross margin using compute_ratio
merged_dat = compute_ratio(merged_dat, numerator=["Total Revenue", "Cost Of Revenue"], denominator=["Total Revenue"], addition_in_numerator=False, ratio_name="gross_margin")

# Compute asset turnover ratio using compute_ratio
merged_dat = compute_ratio(merged_dat, numerator=["Total Revenue"], denominator=["Total Assets"], ratio_name="asset_turnover")

print(merged_dat.head())
```

### Question 6: Computing multiple ratios with the user-defined function

Let's have a look at the function you saw in the last two exercises.

```py
def compute_ratio(df, numerator, denominator, ratio_name, 
                  addition_in_numerator = True,
                  addition_in_denominator = True):
  ratio_numerator = np.where(addition_in_numerator,
                             df[numerator].sum(axis=1), 
                             df[numerator[0]] - df[numerator[1:]].sum(
                               axis=1))
  ratio_denominator = np.where(addition_in_denominator, 
                               df[denominator].sum(axis=1), 
                               df[denominator[0]] - df[denominator[1:]].sum(axis=1))
  df[ratio_name] = ratio_numerator/ratio_denominator
  return df
```

Recall that in the previous exercise, we used the function to compute ratios. Still, it was not more efficient nor did it involve less coding to compute the ratios using this function. In this exercise, you'll see how the function can be used to compute many ratios in a loop. This will make computing multiple ratios more efficient and involve less coding.

**Instructions 1/3**

1. Let's start off by checking the columns in the DataFrame merged_dat.

**Pre Code**

```py
# Print the columns 
print(merged_dat.____)
```

**Ans.**

```py
# Print the columns 
print(merged_dat.columns)
```

**Instructions 2/3**

1. Have a look at the ratios and the order in which they appear in list_of_ratio_names and fill up the list_of_numerators, list_of_denominators, list_addition_in_numerator and list_addition_in_denominator accordingly.

**Pre Code**

```py
# Print the columns 
print(merged_dat.columns)

list_of_ratio_names = ["asset_turnover", "gross_margin", "current_ratio"]

# Fill in the right values
list_of_numerators = [["Total Revenue"], [____], [____]]
list_of_denominators = [[____], ["Total Revenue"], [____]]

list_addition_in_numerator = [____]
list_addition_in_denominator = [____]
```

**Ans.**

```py
# Print the columns 
print(merged_dat.columns)

list_of_ratio_names = ["asset_turnover", "gross_margin", "current_ratio"]

# Fill in the right values
list_of_numerators = [["Total Revenue"],
  					  ["Total Revenue", "Cost Of Revenue"],
  					  ["Total Current Assets"]]
list_of_denominators = [["Total Assets"],
                      ["Total Revenue"],
                      ["Total Current Liabilities"]]

list_addition_in_numerator = [True, False, True]
list_addition_in_denominator = [True, True, True]
```

**Instructions 3/3**

1. Fill in the correct function to loop over multiple lists simultaneously.

**Pre Code**

```py
# Print the columns 
print(merged_dat.columns)

list_of_ratio_names = ["asset_turnover", "gross_margin", "current_ratio"]

list_of_numerators = [["Total Revenue"],
  					  ["Total Revenue", "Cost Of Revenue"],
  					  ["Total Current Assets"]]
list_of_denominators = [["Total Assets"],
                      ["Total Revenue"],
                      ["Total Current Liabilities"]]

list_addition_in_numerator = [True, False, True]
list_addition_in_denominator = [True, True, True]

# Fill in the correct function here
for numerator, denominator, ratio_name, addition_in_numerator, addition_in_denominator in ____(list_of_numerators, list_of_denominators, list_of_ratio_names, list_addition_in_numerator, list_addition_in_denominator):
  
  merged_dat = compute_ratio(merged_dat, numerator, denominator, ratio_name, addition_in_numerator, addition_in_denominator)
  
print(merged_dat[list_of_ratio_names].head())
```

**Ans.**

```py
# Print the columns 
print(merged_dat.columns)

list_of_ratio_names = ["asset_turnover", "gross_margin", "current_ratio"]

list_of_numerators = [["Total Revenue"],
  					  ["Total Revenue", "Cost Of Revenue"],
  					  ["Total Current Assets"]]
list_of_denominators = [["Total Assets"],
                      ["Total Revenue"],
                      ["Total Current Liabilities"]]

list_addition_in_numerator = [True, False, True]
list_addition_in_denominator = [True, True, True]

# Fill in the correct function here
for numerator, denominator, ratio_name, addition_in_numerator, addition_in_denominator in zip(list_of_numerators, list_of_denominators, list_of_ratio_names, list_addition_in_numerator, list_addition_in_denominator):
  
  merged_dat = compute_ratio(merged_dat, numerator, denominator, ratio_name, addition_in_numerator, addition_in_denominator)

print(merged_dat[list_of_ratio_names].head())
```

### Question 7: Plotting ratios

The gross margin ratio is an important profitability ratio that assesses a company's ability to earn profits from its sales. The asset turnover ratio is an important efficiency ratio that measures how efficiently a company is using its assets.

In this exercise, you'll plot and compute the gross margin and asset turnover ratio of Microsoft over time. This will help visually analyze the trend of these ratios for Microsoft: are these ratios constant, improving over time, volatile, or worsening? Let's find out!

Unlike using Seaborn to plot bar plots which we learned in the video, you will be using seaborn to make a line plot. Making a line plot with Seaborn only involves changing the sns.barplot to sns.lineplot. The rest of the arguments remain the same.

A DataFrame called msft has been loaded for you, along with pandas as pd and Seaborn as sns. You can run print(msft.columns) in the console to see the columns to use for this exercise.

**Instructions 1/2**

1. Compute asset turnover ratio.
2. Compute gross margin ratio.

**Pre Code**

```py
# Compute asset turnover ratio
msft["asset_turnover"] = msft[____] / msft[____]

# Compute gross margin ratio
msft["gross_margin"] = (____) / msft[____]
```

**Ans.**

```py
# Compute asset turnover ratio
msft["asset_turnover"] = msft["Total Revenue"] / msft["Total Assets"]

# Compute gross margin ratio
msft["gross_margin"] = (msft["Total Revenue"] - msft["Cost Of Revenue"]) / msft["Total Revenue"]
```

**Instructions 2/2**

1. Use Seaborn to plot the gross margin ratio with Year on the x-axis.
2. Use Seaborn to plot the asset turnover ratio with Year on the x-axis.

**Pre Code**

```py
# Compute asset turnover ratio
msft["asset_turnover"] = msft["Total Assets"] / msft["Total Revenue"]

# Compute gross margin ratio
msft["gross_margin"] = (msft["Total Revenue"] - msft["Cost Of Revenue"]) / msft["Total Revenue"]

# Plot the gross margin ratio over time
gross_margin_plot = sns.lineplot(data= ____, x= ____, y = ____)
gross_margin_plot.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
plt.close()

# Plot the asset turnover ratio over time
asset_turnover_plot = sns.lineplot(data= ____, x= ____, y = ____)
gross_margin_plot.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
plt.close()
```

**Ans.**

```py
# Compute asset turnover ratio
msft["asset_turnover"] = msft["Total Assets"] / msft["Total Revenue"]

# Compute gross margin ratio
msft["gross_margin"] = (msft["Total Revenue"] - msft["Cost Of Revenue"]) / msft["Total Revenue"]

# Plot the gross margin ratio over time
gross_margin_plot = sns.lineplot(data=msft, x="Year", y="gross_margin")
gross_margin_plot.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
plt.close()

# Plot the asset turnover ratio over time
asset_turnover_plot = sns.lineplot(data=msft, x="Year", y="asset_turnover")
asset_turnover_plot.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
plt.close()
```

### Question 8: Plotting ratios in one figure

In this exercise, you'll plot and compute the gross margin and asset turnover ratio of Microsoft over time. But unlike the last exercise, here you will plot it in one figure. This will help visually analyze the trend of these ratios since the ratios are plotted in the same figure.

You will use the pandas .melt() function in this exercise. In the video, the value_vars argument was specified in the function. value_vars refer to the columns we want to unpivot. However if value_vars is not specified, then all the columns which are not id_vars will be taken as value_vars.

Asset turnover and gross margin ratios have been computed for you in the msft DataFrame, provided in the "asset_turnover" and "gross_margin" columns, respectively.

**Instructions**

1. Convert the msft DataFrame from wide to long format.
2. Plot the asset turnover ratio and gross margin ratio in the same plot with Year on the x-axis and add hue over the dimension of Ratio.

**Pre Code**

```py
# Convert the DataFrame from wide to long
msft_melt = msft.melt(id_vars=____, value_vars=____, var_name="Ratio")

# Plot the data
plot = sns.lineplot(data=msft_melt, x=____, y=___, hue=____)
plt.show()

plot.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
```

**Ans.**

```py
# Convert the DataFrame from wide to long
msft_melt = msft.melt(id_vars="Year", value_vars=['gross_margin', 'asset_turnover'], var_name="Ratio")

# Plot the data
plot = sns.lineplot(data=msft_melt, x="Year", y="value", hue="Ratio")
plt.show()

plot.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
```

<hr>