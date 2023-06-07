### Question 1: Assign cash flow entries to the correct part

Recall that the cash flow statement records cash flows from three main parts:

* Cash from operating activities, focusing on cash flows on the core business.
* Cash from investing activities, showing the cash generated or spent relating to investment activities, e.g., the purchase of assets.
* Cash from financing activities, showing the net flows of cash that are used to fund the company.

In this exercise, you'll assign cash flow entries to one of these three parts.

**Instructions**

1. Drag and drop the cash flow entries to the part of the cash flow statement it belongs to.

**Ans.**

**Operating Activities**
1. Decrease in accounts receivable 
2. Rise in accounts payable
3. Tax on income paid in cash

**Investing Activities**

1. Purchase of Property
2. Sale of Investment

**Financing Activities**

1. Dividends Paid

### Question 2: Compute net cash flow

In the last video, you saw what cash outflows and inflows are. In this exercise, you'll put that knowledge to the test. You'll add and subtract transactions to the net income to compute net cash flow. The exercise has one transaction from each part of the cash flow statement: cash flow from operating, investing, and financing activities.

**Instructions**

1. Correctly add and subtract the net cash inflows and outflows from the net income, filling in the blanks with + or -.

**Pre Code**

```py
net_profit = 1000

decrease_in_accounts_recievable = 20

sale_of_property = 430

dividends_paid = 50

# Fill in the blanks
net_cash_flow = net_profit ____ decrease_in_accounts_recievable ____ sale_of_property ____ dividends_paid
print(net_cash_flow)
```

**Ans.**

```py
net_profit = 1000

decrease_in_accounts_recievable = 20

sale_of_property = 430

dividends_paid = 50

# Fill in the blanks
net_cash_flow = net_profit + decrease_in_accounts_recievable + sale_of_property - dividends_paid
print(net_cash_flow)
```

### Question 3: Merging financial statements

You just learned to read JSON data into Python and compute two ratios from the cash flow statement. Computing the cash flow to net income ratio and operating cash flow ratio not only needs information from a company's cash flow statement, but also the income statement and balance sheet.

In this exercise, you'll practice loading JSON data into Python using pandas and merging it with the income statement and balance sheet data.

pandas has already been loaded for you as pd. The datasets with balance sheet and income statement information are called balance_sheet and income_statement, respectively. These have also been loaded for you.

**Instructions**

1. Begin by reading cash_flow_tech.json as a pandas DataFrame.
2. Merge the income statement with the balance sheet data, calling the result merged_income_statement_balance_sheet; use "Year" and "company" as columns to join on.
3. Merge cash flow data with merged_income_statement_balance_sheet.

**Pre Code**

```py
# Read cash flow data
cash_flow = ____

# Merge income statement data with balance sheet data
____ = pd.____(income_statement, ____, on=____)

# Now merge it with cash flow data
merged_all = pd.____(cash_flow, ____, on=____)
```

**Solution**

```py
# Read cash flow data
cash_flow = pd.read_json("cash_flow_tech.json")

# Merge income statement data with balance sheet data
merged_income_statement_balance_sheet = pd.merge(income_statement, balance_sheet, on=["Year", "company"])

# Now merge it with cash flow data
merged_all = pd.merge(cash_flow, merged_income_statement_balance_sheet, on=["Year", "company"])
```

### Question 4: Compute cash flow statement ratios

In this exercise, you'll compute the operating cash flow ratio and cash flow to net income ratio.

Recall that the operating cash flow ratio tells us how many times a company can pay off its short-term obligations from the cash it generates from the core of its business.

The cash flow to net income ratio gives us an idea of the proportion of cash flows earned from operating activities.

The pandas DataFrame merged_dat has already been loaded for you. It contains information from the cash flow statement, income statement, and balance sheet. pandas has been loaded as pd.

**Instructions 1/3**

1. Check the columns of merged_dat to determine which columns you'll need to calculate the operating cash flow ratio and cash flow to net income ratio.

**Pre Code**

```py
# Check the columns
print(merged_dat____)
```

**Ans.**

```py
# Check the columns
print(merged_dat.columns)
```

**Instructions 2/3**

1. Compute cash flow to net income ratio and add it as a column to merged_dat.
2. Compute the operating cash flow ratio and add it as a column to merged_dat.

**Pre Code**

```py
print(merged_dat.columns)

# Compute cash flow to net income ratio
merged_dat["cash_flow_to_net_income"] = ____

# Compute operating cash flow ratio
merged_dat["operating_cash_flow"] = ____
```

**Ans.**

```py
print(merged_dat.columns)

# Compute cash flow to net income ratio
merged_dat["cash_flow_to_net_income"] = merged_dat["Total Cash From Operating Activities"] / merged_dat["Net Income"]

# Compute operating cash flow ratio
merged_dat["operating_cash_flow"] = merged_dat["Total Cash From Operating Activities"] / merged_dat["Total Current Liabilities"]
```

**Instructions 3/3**

1. Use pivot_table to compute the average cash flow to net income and operating cash flow ratio per Year.

**Pre Code**

```py
print(merged_dat.columns)
merged_dat["cash_flow_to_net_income"] = merged_dat["Total Cash From Operating Activities"] / merged_dat["Net Income"]
merged_dat["operating_cash_flow"] = merged_dat["Total Cash From Operating Activities"] / merged_dat["Total Current Liabilities"]

# Compute the average ratios
average_ratios = merged_dat.pivot_table(___)

print(average_ratios)
```

**Ans.**

```py
print(merged_dat.columns)
merged_dat["cash_flow_to_net_income"] = merged_dat["Total Cash From Operating Activities"] / merged_dat["Net Income"]
merged_dat["operating_cash_flow"] = merged_dat["Total Cash From Operating Activities"] / merged_dat["Total Current Liabilities"]

# Compute the average ratios
average_ratios = merged_dat.pivot_table(index="Year", values = ["cash_flow_to_net_income", "operating_cash_flow"])

print(average_ratios)
```

### Question 5: Imputing and filling in missing values using averages

When you want to do your analysis, you will likely use your own data. Datasets often have some missing values. In this exercise, you'll practice imputing these missing values. Imputing missing values is important as you do not want missing values to be an obstacle in our analysis.

pandas has been loaded with the alias pd and NumPy has been loaded with the alias np. A pandas DataFrame called dataset has been loaded for you. It has the column "Total Current Liabilities", which has some missing values in it.

**Instructions 1/2**

1. Impute the missing values in "Total Current Liabilities" by "company" using the average non-missing value.
2. Impute the missing values in "Total Current Liabilities" by "comp_type" using the average non-missing value.

**Pre Code**

```py
# Impute missing value using average non-missing values by company
impute_by_company = dataset.____

# Impute missing value using average non-missing values by industry
impute_by_comp_type = dataset.____

print(impute_by_company)
print(impute_by_comp_type)
```

**Ans.**

```py
# Impute missing value using average non-missing values by company
impute_by_company = dataset.groupby("company")["Total Current Liabilities"].transform("mean")

# Impute missing value using average non-missing values by industry
impute_by_comp_type = dataset.groupby("comp_type")["Total Current Liabilities"].transform("mean")

print(impute_by_company)
print(impute_by_comp_type)
```

**Instructions 2/2**

1. Fill the missing values in "Total Current Liabilities" by "company" using its average non-missing value.
2. Fill the missing values in "Total Current Liabilities" by "comp_type" using its average non-missing value.

**Pre Code**

```py
impute_by_company = dataset.groupby("company")["Total Current Liabilities"].transform("mean")
impute_by_comp_type = dataset.groupby("comp_type")["Total Current Liabilities"].transform("mean")

# Fill in the missing values with imputation
dataset["current_liab_avg_comp"] = ____

# Fill in the missing values with imputation
dataset["current_liab_avg_comp_type"] = ____

print(dataset)
```

**Ans.**

```py
impute_by_company = dataset.groupby("company")["Total Current Liabilities"].transform("mean")
impute_by_comp_type = dataset.groupby("comp_type")["Total Current Liabilities"].transform("mean")

# Fill in the missing values with imputation
dataset["current_liab_avg_comp"] = dataset["Total Current Liabilities"].fillna(impute_by_company)

# Fill in the missing values with imputation
dataset["current_liab_avg_comp_type"] = dataset["Total Current Liabilities"].fillna(impute_by_comp_type)

print(dataset)
```

### Question 6: Imputing missing values with percentiles

In this exercise, you'll continue to practice imputing missing values. Unlike the previous exercise, however, you will use percentiles in place of averages to compute the imputations. Using percentiles is a great way to get conservative imputations. Imputing missing values in a column using percentiles involves the following underlying steps:

* Remove the missing values from the column of interest.
* Then compute the, say 70th percentile of the numbers from the column you just removed missing values from.
* 70th percentile worst value depends on the column you compute the percentile from:
    * For instance, having a large amount of assets is considered to be a good thing, so a low amount of assets is worse. The 70th percentile worst value of assets is actually just the 30th percentile of assets.
    * Analogously, high amounts of liabilities is considered bad. So a 70th worst value of liabilities is simply its 70th percentile.
* pandas has been loaded with the alias pd and NumPy has been loaded with the alias np. A pandas DataFrame called dataset has been loaded for you. It has the column "Total Current Liabilities", which has some missing values. 

**Instructions 1/2**

1. Impute the missing values in "Total Current Liabilities" by "company" using the 70th percentile non-missing value.
2. Impute the missing values in "Total Current Liabilities" by "comp_type" using the 70th percentile non-missing value.

**Pre Code**

```py
# Impute missing value with 70th percentile non-missing values of company
impute_by_company = ___

# Impute missing value with 70th percentile non-missing values of industry
impute_by_comp_type = ____

print(impute_by_company)
print(impute_by_comp_type)
```

**Ans.**

```py
# Impute missing value with 70th percentile non-missing values of company
impute_by_company = dataset.groupby("company")["Total Current Liabilities"].transform(lambda x: np.nanquantile(x, 0.7))

# Impute missing value with 70th percentile non-missing values of industry
impute_by_comp_type = dataset.groupby("comp_type")["Total Current Liabilities"].transform(lambda x: np.nanquantile(x, 0.7))

print(impute_by_company)
print(impute_by_comp_type)
```

**Instructions 2/2**

1. Fill the missing values in "Total Current Liabilities" by "company" using the 70th percentile non-missing value.
2. Fill the missing values in "Total Current Liabilities" by "comp_type" using the 70th percentile non-missing value.

**Pre Code**

```py
# Impute missing value with average non-missing values of company
impute_by_company = dataset.groupby("company")["Total Current Liabilities"].transform(lambda x: np.nanquantile(x, 0.7))

# Impute missing value with average non-missing values of industry
impute_by_comp_type = dataset.groupby("comp_type")["Total Current Liabilities"].transform(lambda x: np.nanquantile(x, 0.7))

# Fill in the missing values using imputation
dataset["current_liab_quant_comp"] = ----

# Fill in the missing values using imputation
dataset["current_liab_quant_comp_type"] = ____

print(dataset)
```

**Ans.**

```py
# Impute missing value with 70th percentile non-missing values of company
impute_by_company = dataset.groupby("company")["Total Current Liabilities"].transform(lambda x: np.nanquantile(x, 0.7))

# Impute missing value with 70th percentile non-missing values of industry
impute_by_comp_type = dataset.groupby("comp_type")["Total Current Liabilities"].transform(lambda x: np.nanquantile(x, 0.7))

# Fill in the missing values using imputation
dataset["current_liab_quant_comp"] = dataset["Total Current Liabilities"].fillna(impute_by_company)

# Fill in the missing values using imputation
dataset["current_liab_quant_comp_type"] = dataset["Total Current Liabilities"].fillna(impute_by_comp_type)

print(dataset)
```

### Question 7: Merging financial statements and filling missing values

You just learned about cash flow to net income and operating cash flow ratio. Recall that net income is not entirely earned in cash, and the cash flow to net income ratio tells us the rate of net income earned in cash. The operating cash flow ratio tells us whether the company has enough cash to meet its short-term commitments.

In this exercise, you'll compute both of these ratios for Apple and Microsoft and then plot them. A side-by-side plot of ratios of companies in the same industry helps visualize their differences.

You will usually get only some of the necessary information from different financial statements in any one DataFrame. You will likely get it from different sources and have to merge them. In addition, data from the wild often has missing values. This exercise involves filling in NaNs and merging DataFrames.

A pandas DataFrame dataset has been loaded for you. It contains information about Microsoft and Apple's income statements and balance sheets. Another pandas DataFrame cash_flow_statement has also been loaded for you. This has some of Apple and Microsoft's cash flow information.

**Instructions 1/3**

1. Check the columns of dataset and cash_flow_statement, and see which columns they should be merged on.

**Pre Code**

```py
# Check the columns of dataset and cash_flow_statement
print(dataset.____)
print(cash_flow_statement.____)
```

**Ans.**

```py
# Check the columns of dataset and cash_flow_statement
print(dataset.columns)
print(cash_flow_statement.columns)
```

**Instructions 2/3**

1. Merge dataset and cash_flow_statement on the keywords "Year" and "company".
2. The column Total Current Liabilities has NaN values; fill them with the average Total Current Liabilities of all companies.

**Pre Code**

```py
# Check the columns of dataset and cash_flow_statement
print(dataset.columns)
print(cash_flow_statement.columns)

# Merge dataset with cash_flow_statement with the mean
merged_dat = pd.merge(____, ____, on=____)

# Fill in the NaN values in Total Current Liabilities
merged_dat["Total Current Liabilities"] = merged_dat["Total Current Liabilities"].fillna(____)
```

**Ans.**

```py
# Check the columns of the dataset and cash_flow_statement
print(dataset.columns)
print(cash_flow_statement.columns)

# Merge dataset with cash_flow_statement with the mean
merged_dat = pd.merge(dataset, cash_flow_statement, on=["Year", "company"])

# Fill in the NaN values in Total Current Liabilities
merged_dat["Total Current Liabilities"] = merged_dat["Total Current Liabilities"].fillna(merged_dat["Total Current Liabilities"].mean())
```

**Instructions 3/3**

1. Compute the operating cash flow ratio.

**Pre Code**

```py
# Merge dataset with cash_flow_statement
merged_dat = pd.merge(dataset, cash_flow_statement, on=["Year", "company"])

# Fill in the NaN values in Total Current Liabilities with the mean
merged_dat["Total Current Liabilities"] = merged_dat["Total Current Liabilities"].fillna(merged_dat["Total Current Liabilities"].mean())

# Compute operating cash flow ratio
merged_dat["operating_cash_flow"] = merged_dat[____] / merged_dat[____]

print(merged_dat[["Year", "company", "operating_cash_flow"]])
```

**Ans.**

```py
# Merge dataset with cash_flow_statement
merged_dat = pd.merge(dataset, cash_flow_statement, on=["Year", "company"])

# Fill in the NaN values in Total Current Liabilities with the mean
merged_dat["Total Current Liabilities"] = merged_dat["Total Current Liabilities"].fillna(merged_dat["Total Current Liabilities"].mean())

# Compute operating cash flow ratio
merged_dat["operating_cash_flow"] = merged_dat["Total Cash From Operating Activities"] / merged_dat["Total Current Liabilities"]

print(merged_dat[["Year", "company", "operating_cash_flow"]])
```

### Question 8: Plotting cash flow ratios

Sometimes, you might want to plot several line plots in one image. However, having too many lines in one plot will make it challenging to read. Making separate facets for every line is more elegant: the figure will look neat and more interpretable.

A pandas DataFrame plot_df has already been loaded for you. It has the columns "Year", "company","cash_flow_to_net_income" and "operating_cash_flow". Seaborn has been loaded with the alias sns.

**Instructions**

1. Melt plot_dfto prepare it for plotting.
2. Use sns.relplot() to make a line plot of the cash flow to net income and operating cash flow ratio of Apple and Microsoft over time, with hue over the dimension of "Ratio".

**Pre Code**

```py
# Melt the DataFrame to prepare for plotting
melt_data = plot_df.melt(____, var_name="Ratio")

# Plot your melted DataFrame
sns.relplot(data=____, x=____, y=____, col=____, kind=____, hue=____)

plt.show()
```

**Ans.**

```py
# Melt the DataFrame to prepare for plotting
melt_data = plot_df.melt(id_vars = ["Year","company"], value_vars=["cash_flow_to_net_income", "operating_cash_flow"], var_name="Ratio")

# Plot your melted DataFrame
sns.relplot(data = melt_data, x="Year", y="value", col="company", kind="line",
            hue='Ratio')

plt.show()
```

<hr>