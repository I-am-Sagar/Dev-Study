### Question 1: Calculating gross profit

Gross profit is the amount of money you generated in sales minus the cost of selling those goods (Also know as Cost of Goods Sold or COGS). COGS does not include administration or marketing costs, only costs directly related to production or providing the good or service, so Gross Profit is a good metric to see the core profitability of any product\service.

Gross profit margin is the gross profit expressed as a percentage of sales, which is valuable for analysis and decision making.

As the manager of a factory, you have been asked to check the gross profit forecast for the following year.

**Instructions 1/2**

1. Set sales and cogs variables to 8000 and 5400, respectively.
2. Using the formulas, calculate the gross profit gross_profit and print the gross_profit result.

**Pre Code**

```py
# Set the sales variable to 8000
sales = ____

# Set the cost of goods sold (cogs) variable to 5400
cogs = ____

# Calculate the gross profit (gross_profit)
____ = ____ - ____

# Print the gross profit
print("The gross profit is {}.".format(____))
```

**Ans.**

```py
# Set the sales variable to 8000
sales = 8000

# Set the cost of goods sold (cogs) variable to 5400
cogs = 5400

# Calculate the gross profit (gross_profit)
gross_profit = sales - cogs

# Print the gross profit
print("The gross profit is {}.".format(gross_profit))
```

**Instruction 2/2**

1. Using the formulas, calculate the gross profit margin gross_profit_margin.
2. Print the gross_profit_margin result.

**Pre Code**

```py
# Set the sales variable and cost of goods sold (cogs) variables
sales = 8000
cogs = 5400

# Calculate the gross profit (gross_profit)
gross_profit = sales - cogs

# Print the gross profit
print("The gross profit is {}.".format(gross_profit))

# Calculate the gross profit margin
gross_profit_margin = ____ / ____

# Print the gross profit margin
print("The gross profit margin is {}.".format(____))
```

**Ans.**

```py
# Set the sales variable and cost of goods sold (cogs) variables
sales = 8000
cogs = 5400

# Calculate the gross profit (gross_profit)
gross_profit = sales - cogs

# Print the gross profit
print("The gross profit is {}.".format(gross_profit))

# Calculate the gross profit margin
gross_profit_margin = ____ / ____

# Print the gross profit margin
print("The gross profit margin is {}.".format(____))
```

### Question 2: Calculating net profit

The net profit includes all the other costs (and all other income) that may incur or earn that is not directly related to the product. For example the salary of the accountant who prepares your invoices, the advertising budget, travel expenses, etc.

So, how do we calculate this?

We start by setting a list for all the items that we want to include in the net profit calculation and calling the list "other operating expenses" or "opex". To keep it simple we will not go into any tax or exceptional expenses or income. 

The gross_profit (gross profit) variable has been set for you.

**Instructions**

1. Add the appropriate variables into the opex list: admin, travel, training, marketing, insurance.
2. Print the resultant list.
3. Calculate the net profit as the gross profit minus the total operational expenses.

**Pre Code**

```py
# Create and print the opex list
opex = [____, ____, ____, ____, ____]
print(____)

# Calculate and print net profit
net_profit = ____ - ____
print("The net profit is {}.".format(____))
```

**Ans.**

```py
# Create and print the opex list
opex = [admin, travel, training, marketing, insurance]
print(opex)

# Calculate and print net profit
net_profit = gross_profit - sum(opex)
print("The net profit is {}.".format(net_profit))
```

### Question 3: Elements within net profit & gross profit

To ensure you have a good understanding of the parts of both the gross profit and net profit, have a look at the following scenario. Choose the correct option.

Sal, an accountant at Engineering Co., has to compile the income statement of the factory site.

We already know that Gross Profit is Sales less Cost of Goods sold (cogs) and Net Profit is Gross Profit less Operating Expenses (opex).

Which combination of the following components should she use to ensure that she calculates the gross profit and net profit correctly?

1. cogs : Materials + Accountant Salary, opex : Office & Factory utilities
2. cogs : Materials + Accountant Salary + Office utilities, opex : Factory utilities
3. cogs : Materials + factory utilities, opex : Office utilities + Accountant salary
4. cogs : Materials + factory utilities + Accountant Salary, opex : Office utilities

**Ans.** 3

### Question 4: Calculating sales

To calculate a sales forecast we need to know both the price we wish to sell our product and the number of units we expect to sell. In this example we will have a look at a company T-Z producing and selling T-Shirts.

The company offers its customers two options - a basic shirt or a customized shirt. A T-shirt costs 15 USD for a basic shirt, and 25 USD for a customized one.

T-Z have forecast orders for T-Shirts for delivery next month, and want to use the same sales mix of 60% basic and 40% customized. As this mix is relatively stable, we can calculate an average sales price per unit for T-Z. The variable forecast_units has been set for you.

**Instructions**

1. Set the variables for the basic sales price as salesprice_basic, the extensive customization price as salesprice_custom.
2. Calculate the average sales price for the T-Shirts taking into account the sales mix.
3. Calculate the forecast sales figure sales_USD for next month.
4. Print the total USD sales.

**Pre Code**

```py
# Set variables units sold and sales price of the T-shirts (basic and custom)
____ = ____
salesprice_custom = ____

# Calculate the combined sales price taking into account the sales mix
average_sales_price = (____ * 0.6) + (____ * ____)

# Calculate the total sales for next month
sales_USD = ____ * ____

# Print the total sales
print("Next month's forecast sales figure is {:.2f} USD.".format(____))
```

**Ans.**

```py
# Set variables units sold and sales price of the T-shirts (basic and custom)
salesprice_basic = 15
salesprice_custom = 25

# Calculate the combined sales price taking into account the sales mix
average_sales_price = (salesprice_basic * 0.6) + (salesprice_custom * 0.4)

# Calculate the total sales for next month
sales_USD = average_sales_price * forecast_units

# Print the total sales
print("Next month's forecast sales figure is {:.2f} USD.".format(sales_USD))
```
### Question 5: Forecasting sales with a discount

Sales are often made with special mixes and discounts. Discounts are a great marketing tool and a way to move stock. Let's look again at company T-Z.

T-Z has launched a new range of T-Shirts linked to a celebrity meme for 40 USD per T-Shirt. They have excess stock of Celebshirt1 on their shelves, and in expectation of the release of Celebshirt2 in February, they have announced a 40% discount on Celebshirt1 in February.

For this exercise, prices are in USD, and unit amounts are total units sold in the respective month. The following variables have been defined for you:

sales_price = 40
units_january = 500
units_february = 700

The January sales only include sales of Celebshirt1.

The February sales include sales of Celebshirt1 and Celebshirt2, at a ratio of 45:55.

**Instructions**

1. Forecast the sales for January (without a discount).
2. Forecast the sales for February (discounted: dsales_price).
3. Print the results for sales for January and February.

**Pre Code**

```py
# Forecast the sales of January
sales_january = ____ * ____

# Forecast the discounted price
dsales_price = ____ * 0.6

# Forecast the sales of February
sales_february = (____ * units_february * 0.55) + (dsales_price * ____ * ____)

# Print the forecast sales for January and February
print("The forecast sales for January and February are {} and {} USD respectively.".format(____, ____))
```

**Ans.**

```py
# Forecast the sales of January
sales_january = sales_price * units_january

# Forecast the discounted price
dsales_price = sales_price * 0.6

# Forecast the sales of February
sales_february = (sales_price * units_february * 0.55) + (dsales_price * units_february * 0.45)

# Print the forecast sales for January and February
print("The forecast sales for January and February are {} and {} USD respectively.".format(sales_january, sales_february))
```

### Question 6: Calculating COGS

We assume no closing or opening balances, stock is sold in the same month that it is produced.

Material costs to produce one T-shirt is 8 USD. Labor costs are 2 USD per shirt. As you only use materials and labor to make the shirt, this is known as variable costs. The costs to rent a machine that produces these shirts is 1300 USD per month, regardless of the amount of shirts produced. This is therefore an example of a fixed cost, as fixed costs in COGS are costs directly related to the product but are incurred whether you produce the products or not.

Preloaded variables are printed in the shell.

**Instructions 1/2**

1. Set new variables for Fixed costs and Variable costs using predefined variables
2. Calculate the COGS for January and February.

**Pre Code**

```py
# Set the variables for fixed costs and variable costs
fixed_costs = ____ 
variable_costs_per_unit = ____ + labor_costs_per_unit

# Calculate the cogs for January and February
cogs_jan = (____ * variable_costs_per_unit) + ____
cogs_feb = ____
```

**Ans.**

```py
# Set the variables for fixed costs and variable costs
fixed_costs = machine_rental 
variable_costs_per_unit = material_costs_per_unit + labor_costs_per_unit

# Calculate the cogs for January and February
cogs_jan = (units_jan * variable_costs_per_unit) + fixed_costs
cogs_feb = (units_feb * variable_costs_per_unit) + fixed_costs
```

**Instructions 2/2**

1. Calculate the cost per unit for January and February.
2. Print the January and February COGS.

**Pre Code**

```py
# From previous step
fixed_costs = machine_rental 
variable_costs_per_unit = material_costs_per_unit + labor_costs_per_unit
cogs_jan = (units_jan * variable_costs_per_unit) + fixed_costs
cogs_feb = (units_feb * variable_costs_per_unit) + fixed_costs

# Calculate the unit cost for January and February
unit_cost_jan = ____ / units_jan
____ = ____ / ____

# Print the January and February cost per unit
print("The cost per unit for January and February are {} and {} USD respectively.".format(____, ____))
```

**Ans.**

```py
# From previous step
fixed_costs = machine_rental 
variable_costs_per_unit = material_costs_per_unit + labor_costs_per_unit
cogs_jan = (units_jan * variable_costs_per_unit) + fixed_costs
cogs_feb = (units_feb * variable_costs_per_unit) + fixed_costs

# Calculate the unit cost for January and February
unit_cost_jan = cogs_jan / units_jan
unit_cost_feb = cogs_feb / units_feb

# Print the January and February cost per unit
print("The cost per unit for January and February are {} and {} USD respectively.".format(unit_cost_jan, unit_cost_feb))
```

### Question 7: Calculating the break-even point

Tracking and understanding how cost per unit varies by month is critical, as the COGS influence the gross profit. At a certain point, if we do not make enough sales in the month to cover our costs, we will enter a loss situation.

How do we know we have produced enough units to sell to cover our costs? We do this by using a concept called the break-even point. 

In the last exercise, we calculated a unit cost of 16.5 USD for January and 15.2 USD for February. Keep this in mind when calculating the break-even point.

Predefined variables have been printed to the shell.

**Instructions**

1. Print the variables in the shell to help you construct the formula for the break-even point.
2. Forecast the gross profit for January and February.

**Pre Code**

```py
# Calculate the break-even point (in units) for Wizit
break_even = ____/(____ - ____)

# Print the break even point in units
print("The break even point is {} units.".format(____))

# Forecast the gross profit for January and February
gross_profit_jan = (sales_price*____) - cogs_jan
gross_profit_feb = (____*____) - ____

# Print the gross profit for January and February
print("The gross profit for January and February are {} and {} USD respectively.".format(____, ____))
```

**Ans.**

```py
# Calculate the break-even point (in units) for T-Z
break_even = fixed_costs/(sales_price - variable_costs_per_unit)

# Print the break even point in units
print("The break even point is {} units.".format(break_even))

# Forecast the gross profit for January and February
gross_profit_jan = (sales_price*units_jan) - cogs_jan
gross_profit_feb = (sales_price*units_feb) - cogs_feb

# Print the gross profit for January and February
print("The gross profit for January and February are {} and {} USD respectively.".format(gross_profit_jan, gross_profit_feb))
```

### Question 8: Tesla income statement

The dataset for the Tesla income statement is called income_statement.

This dataset has a final column called Trailing Twelve Months (TTM), which is the most recent 12 months of data available. We will use this to calculate a 2018 forecast for Tesla.

We are only interested in the rows 'Revenue', 'Gross profit', 'Total operating expenses', and 'Net income', so we'll create a filtered income statement to only show these rows. The filtering code uses the following pattern.

```py
dataframe[dataframe.columnname.isin(list_of_categories)]
```

**Instructions**

1. Look at income_statement in the shell.
2. Create a list called interesting_metrics that contains the rows we are interested in as a list.
3. Use the .isin() method to filter the income statement for rows where metric is in interesting_metrics.
4. Look at the result.

**Pre Code**

```py
# Choose some interesting metrics
interesting_metrics = ['____', '____', '____', '____']

# Filter for rows containing these metrics
filtered_income_statement = income_statement[income_statement.____.____(____)]

# See the result
print(filtered_income_statement)
```

**Ans.**

```py
# Choose some interesting metrics
interesting_metrics = ['Revenue', 'Gross profit', 'Total operating expenses', 'Net income']

# Filter for rows containing these metrics
filtered_income_statement = income_statement[income_statement.metric.isin(interesting_metrics)]

# See the result
print(filtered_income_statement)
```

### Question 9: Forecasting profit for Tesla

As in the previous exercise, the dataset for the Tesla income statement is named income_statement. Using what we have learned in the previous exercise, we will now append a new column with 2018 Forecast data, which we will assign the header "Forecast".

For this exercise, we would like to set the filtered_income_statement to only show the row 'Revenue'.

Remember, the TTM column is the most recent 12-month value that we will use for the 2018 forecast. Thus far, we have the following information for 2018:

The market demand analysis predicts the revenue to increase to 13,000 in 2018 due to increased sales of Model 3.

**Instructions**

1. Create a filtered income statement only for the revenue_metric row.
2. Get the number of columns of filtered_income_statement, using the length (len()) of the columns attribute.
3. Insert a new column in filtered_income_statement.
    * Locate it at the end of the row (use n_cols as the location).
    * Use 'Forecast' as the column name.
    * Insert the value 13000.
4. Print the result.

**Pre Code**

```py
revenue_metric = ['Revenue']

# Filter for rows containing the revenue metric
filtered_income_statement = ____[____.____.____(____)]

# Get the number of columns in filtered_income_statement
n_cols = ____(filtered_income_statement.____)

# Insert a column in the correct position containing the column 'Forecast'
filtered_income_statement.insert(____, '____', ___) 

# See the result
print(filtered_income_statement)
```

**Ans.**

```py
revenue_metric = ['Revenue']

# Filter for rows containing the revenue metric
filtered_income_statement = income_statement[income_statement.metric.isin(revenue_metric)]

# Get the number of columns in filtered_income_statement
n_cols = len(filtered_income_statement.columns)

# Insert a column in the correct position containing the column 'Forecast'
filtered_income_statement.insert(n_cols, 'Forecast', 13000) 

# See the result
print(filtered_income_statement)
```

<hr>