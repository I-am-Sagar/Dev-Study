### Question 1: Match balance sheet items to their class

Assets are used by the business to create positive economic value. Thus assets reap benefits to the business. Liabilities are future burdens that the business needs to pay off. Assets and liabilities can be further broken down:

Current assets refer to the class of assets that usually reap benefits in one year.
Current liabilities are those burdens that must be paid off in one year.
Non-current assets reap benefits over a period of one year
Non-current liabilities can be paid off over a period of one year.
In this exercise, accounts_receivable, accounts_payable, short_term_loans, long_term_loans, inventory, long_term_investments, and property_plant_equipment have already been loaded for you.

You will identify which balance sheet items are current or non-current assets and liabilities. You will then use them to add up balance sheet items within the correct class to get the total current and non-current assets and liabilities.

**Instructions**

1. Add up total current assets.
2. Add up total non-current assets.
3. Add up total current liabilities.
4. Add up total non-current liabilities.

**Pre Code**

```py
accounts_receivable = 1298
accounts_payable = 500
short_term_loans = 3357
long_term_loans = 8000
inventory = 5420
long_term_investments = 7892
property_plant_equipment = 9840

# Add up total current assets
total_current_assets = ____

# Add up total non-current assets
total_non_current_assets = ____

# Add up total current liabilities
total_current_liab = ____

# Add up total non-current liabilities
total_non_current_liab = ____
```

**Ans.**

```py
accounts_receivable = 1298
accounts_payable = 500
short_term_loans = 3357
long_term_loans = 8000
inventory = 5420
long_term_investments = 7892
property_plant_equipment = 9840

# Add up total current assets
total_current_assets = accounts_receivable + inventory

# Add up total non-current assets
total_non_current_assets = long_term_investments + property_plant_equipment

# Add up total current liabilities
total_current_liab = accounts_payable + short_term_loans

# Add up total non-current liabilities
total_non_current_liab = long_term_loans
```

### Question 2: Relation of assets, liabilities, and shareholders' equity

Recall that assets, liabilities, and shareholders' equity are the three main parts of a balance sheet.

Together, their relationship with each other "balances" the balance sheet.

This relationship is helpful to remember when you don't know the value of one of the main parts of a balance sheet! Suppose you have information about a company's assets and shareholders' equity. You can use your knowledge about their relationship to determine the company's liability.

In this exercise, you will practice doing just this!

**Instructions**

1. Compute the total_liabilities using current_assets, non_current_assets, and shareholders_equity.

**Pre Code**

```py
current_assets = 1500
non_current_assets = 3000
shareholders_equity = 1200

# Compute total liabilities
total_liabilities = ____
```

**Ans.**

```py
current_assets = 1500
non_current_assets = 3000
shareholders_equity = 1200

# Compute total liabilities
total_liabilities = current_assets + non_current_assets - shareholders_equity
```

### Question 3: Practice using the main equation of accounting

In this exercise, you'll compute a company's total liabilities using the main accounting equation you've mastered. To do this, you will first have to compute total assets.

accounts_receivable, inventory, long_term_investments and property_plant_equipment are already loaded for you.

You will identify which items of the balance sheet provided are current or non-current assets, compute total assets, and then use the main accounting equation to compute total liabilities.

**Instructions**

1. Add up total current assets.
2. Add up total non-current assets.
3. Compute total assets.
4. Compute total liabilities

**Pre Code**

```py
accounts_receivable = 1356
long_term_investments = 7892
property_plant_equipment = 9840
inventory = 5420
shareholders_equity = 8000

# Add up total current assets
total_current_assets = ____

# Add up total non-current assets
total_non_current_assets = ____

# Compute total assets
total_assets = ___

# Compute total liabilities
total_liabilities = ____
```

**Ans.**

```py
accounts_receivable = 1356
long_term_investments = 7892
property_plant_equipment = 9840
inventory = 5420
shareholders_equity = 8000

# Add up total current assets
total_current_assets = accounts_receivable + inventory

# Add up total non-current assets
total_non_current_assets = long_term_investments + property_plant_equipment

# Compute total assets
total_assets = total_current_assets + total_non_current_assets

# Compute total liabilities
total_liabilities = total_assets - shareholders_equity
```

### Question 4: Match the ratio to its family 

Recall that financial ratios belong to different families. In this exercise, you'll practice matching the financial ratio to the family to which it belongs - liquidity ratios, leverage ratios, or solvency ratios.

**Instructions**

1. Match the financial ratio to the family it belongs to.

**Ans.**

**Leverage Ratio**
* Debt to Equity Ratio
* Equity Multiplier Ratio

**Liquidity Ratio**
* Current Ratio

**Solvency Ratio**
* Debt to Assets Ratio

### Question 5: Compute the current ratio

Recall that the current ratio is a liquidity ratio that measures a company's ability to meet its short-term financial burdens.

In this exercise, some items from the balance sheet have been defined for you as variables. You will assess these items and use them to compute the current ratio.

**Instructions**

1. Compute the current ratio using the information provided.

**Pre Code**

```py
accounts_receivable = 1298
accounts_payable = 500
short_term_loans = 3357
long_term_loans = 8000
inventory = 5420
long_term_investments = 7892
property_plant_equipment = 9840

# Compute the current ratio
current_ratio = ____
print(current_ratio)
```

**Ans.**

```py
accounts_receivable = 1298
accounts_payable = 500
short_term_loans = 3357
long_term_loans = 8000
inventory = 5420
long_term_investments = 7892
property_plant_equipment = 9840

# Compute the current ratio
current_ratio = (accounts_receivable + inventory) / (accounts_payable + short_term_loans)
print(current_ratio)
```

### Question 6: Leverage ratios

Leverage ratios are a measure of how much equity and debt is used by the company in running its operations. Running a company with too much debt might sound bad initially, but if it makes enough cash inflows (more on this in the third chapter) to pay off its debts, having a lot of debt is not necessarily bad. Similarly, having too much equity is not necessarily as beneficial as one might think. It might be inefficient because a company could be borrowing more money to grow its operations.

In this exercise, you'll compute the debt-to-equity and equity multiplier ratios. Relevant items from the balance sheet have already been defined for you as variables.

You will first use these to compute total assets, liabilities, and shareholders' equity. You'll then use these values to compute the debt-to-equity and equity multiplier ratios.

**Instructions 1/2**

1. Compute total assets.
2. Compute total liabilities.
3. Compute total shareholders' equity.

**Pre Code**

```py
accounts_receivable = 1298
accounts_payable = 500
short_term_loans = 3357
long_term_loans = 8000
inventory = 5420
long_term_investments = 7892
property_plant_equipment = 9840

# Compute total assets
total_assets = ____

# Compute total liabilities
total_liabilities = ____

# Compute total shareholders' equity
shareholders_equity = ____
```

**Ans.**

```py
accounts_receivable = 1298
accounts_payable = 500
short_term_loans = 3357
long_term_loans = 8000
inventory = 5420
long_term_investments = 7892
property_plant_equipment = 9840

# Compute total assets
total_assets = accounts_receivable + inventory + long_term_investments + property_plant_equipment

# Compute total liabilities
total_liabilities = accounts_payable + short_term_loans + long_term_loans

# Compute total shareholders' equity
shareholders_equity = total_assets - total_liabilities
```

**Instructions 2/2**

1. Compute debt-to-equity ratio.
2. Compute equity multiplier ratio.

**Pre Code**

```py
total_assets = 24450
total_liabilities = 11857
shareholders_equity = 12593

# Compute debt-to-equity ratio
debt_to_equity = ____
# Compute equity multiplier ratio
equity_multiplier = ____

print(f"Debt-to-equity ratio: {debt_to_equity}")
print(f"Equity multiplier ratio: {equity_multiplier}")
```

**Ans.**

```py
total_assets = 24450
total_liabilities = 11857
shareholders_equity = 12593

# Compute debt-to-equity ratio
debt_to_equity = total_liabilities / shareholders_equity
# Compute equity multiplier ratio
equity_multiplier = total_assets / shareholders_equity

print(f"Debt-to-equity ratio: {debt_to_equity}")
print(f"Equity multiplier ratio: {equity_multiplier}")
```

### Question 7: Compute current and debt-to-equity ratios

You just learned about liquidity ratios. In this exercise, you'll compute the current ratio, a liquidity ratio, to assess the company's assets to meet its short-term commitments. You'll also compute the debt-to-equity ratio, a commonly used leverage ratio, to see whether a company runs its operations using more debt or its "own" funds.

A pandas DataFrame balance_sheet has been loaded for you. pandas with alias pd has been loaded for you.

**Instructions 1/2**

1. View the columns of balance_sheet and assess whether the columns needed to compute the current ratio and debt-to-equity ratios are present.

**Pre Code**

```py
# Print the columns in df_bal_sheet
print(balance_sheet____)
```

**Ans.**
```py
print(balance_sheet.columns)
```

**Instruction 2/2**

1. Compute the current ratio.
2. Compute the debt-to-equity ratio.

**Pre Code**

```py
# Print the columns in df_bal_sheet
print(balance_sheet.columns)

# Compute the current ratio
balance_sheet["current_ratio"] = balance_sheet[____] / balance_sheet[____]

# Compute debt-to-equity ratio
balance_sheet["debt_to_equity"] = balance_sheet[____] / balance_sheet[____]
```

**Ans.**

```py
# Print the columns in df_bal_sheet
print(balance_sheet.columns)

# Compute the current ratio
balance_sheet["current_ratio"] = balance_sheet["Total Current Assets"] / balance_sheet["Total Current Liabilities"]

# Compute debt-to-equity ratio
balance_sheet["debt_to_equity"] = balance_sheet["Total Liab"] / balance_sheet["Total Stockholder Equity"]
```

### Question 8: Compute relative difference by industry

Computing the relative difference between a company's ratio and its industry average is an excellent way to see if a company is at par with its peers. In this exercise, you'll practice computing the relative difference of the equity multiplier ratio of various FMCG companies from their industry average.

A pandas DataFrame balance_sheet has been loaded for you. pandas has been loaded for you under the alias pd. You can call balance_sheet.columns in the console to assess which columns you can use for the exercise.

**Instructions**

1. Subset the entries in balance_sheet to get only fmcg companies in the column "comp_type" of balance_sheet.
2. Add a column in fcmg where you compute the equity multiplier ratio.
3. Add a column to fmcg where you compute the average yearly equity multiplier ratio.
4. Add a column to fmcg where you compute the relative difference of the company's equity multiplier ratio with its industry average.

**Pre Code**

```py
# Subset the fmcg companies
fmcg = balance_sheet.____[____]

# Compute equity multiplier ratio
fmcg["equity_multiplier_ratio"] = ____

# Compute average equity multiplier ratio by year
fmcg["average_equity_multiplier_ratio"] = fmcg.____(____)[____].____(____)

# Compute the relative difference
fmcg["relative_difference"] = ____

print(fmcg[["Year", "company", "relative_difference"]])
```

**Ans.**

```py
# Subset the fmcg companies
fmcg = balance_sheet.loc[balance_sheet["comp_type"]=="fmcg"]

# Compute equity multiplier ratio
fmcg["equity_multiplier_ratio"] = fmcg["Total Assets"] / fmcg["Total Stockholder Equity"]

# Compute average equity multiplier ratio by year
fmcg["average_equity_multiplier_ratio"] = fmcg.groupby("Year")["equity_multiplier_ratio"].transform("mean")

# Compute the relative difference
fmcg["relative_difference"] = (fmcg["equity_multiplier_ratio"] / fmcg["average_equity_multiplier_ratio"]) - 1

print(fmcg[["Year", "company", "relative_difference"]])
```

### Question 9: Compute ratios by industry

In this exercise, you will assess how the current ratio and debt-to-equity ratio of Tech and FMCG companies are different on average and over time.

An industry's ratio, on average gives us an overall idea of the industry's financial condition. On the other hand, an industry's ratio over timehelps us understand its trends: is the ratio relatively stable or fluctuating over time? Is it improving or worsening?

balance_sheet has been loaded for you as a pandas DataFrame. The current ratio is provided in a column called curr_ratio, and the debt-to-equity ratio is provided in a column called debt_to_equity. pandas has been loaded with the alias pd.

**Instructions**

1. Select those companies whose column comp_type is tech or fmcg.
2. Use .groupby() to compute the average current ratio and debt-to-equity ratio grouped by company type (denoted by the column "comp_type").
3. Use .groupby() to compute the average current ratio and debt-to-equity ratio by both "comp_type" and "Year".

**Pre Code**

```py
# Choose the tech and fmcg companies
tech_fmcg = balance_sheet.loc[balance_sheet[____].isin(____)]

# Compute the average debt-to-equity ratio and current ratio by industry
groupby_industry = tech_fmcg.____(____)[["current_ratio", "debt_to_equity"]].____

# Compute the average debt-to-equity ratio and current ratio by industry and over time
groupby_industry_time = tech_fmcg.____(____)[["current_ratio", "debt_to_equity"]].____

print(groupby_industry)
print(groupby_industry_time)
```

**Ans.**

```py
# Choose the tech and fmcg companies
tech_fmcg = balance_sheet.loc[balance_sheet['comp_type'].isin(["tech", "fmcg"])]

# Compute the average debt-to-equity ratio and current ratio by industry
groupby_industry = tech_fmcg.groupby("comp_type")[["current_ratio", "debt_to_equity"]].mean()

# Compute the average debt-to-equity ratio and current ratio by industry and over time
groupby_industry_time = tech_fmcg.groupby(["comp_type", "Year"])[["current_ratio", "debt_to_equity"]].mean()

print(groupby_industry)
print(groupby_industry_time)
```

<hr>

