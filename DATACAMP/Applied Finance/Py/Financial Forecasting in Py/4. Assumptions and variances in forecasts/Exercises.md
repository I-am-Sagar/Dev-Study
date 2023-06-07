### Question 1: Weighted probability

Txs Tools, a company selling hardware tools, is looking to expand out of their home market A into Market B. They have done some market research, and have received the following numeric probabilities:

| Sales Level (USD)	| Probability (%) | 
| --- | --- |
| 0	| 5 |
| 200 |	10 |
| 300 |	40 |
| 500 |	20 |
| 800 |	25 |

Txs Tools will only be motivated to expand if they can have reasonable assurance that they will achieve sales of 400 or more. To manage the different forecast sales probabilities, Txs Tools have asked you to calculate the weighted probability.

**Instructions**

1. Calculate weighted probability for the sales level of Txs tools based on the probability table by creating a combined sales_probability list with pair values as a string separated by a pipe character |.
2. Create a loop iterating over the list to give the a weighted probability.
    * The for loop should iterate through each pair in the list and split the parts by specifying the character that separates the pairs.
3. Print the result.

**Pre Code**

```py
# Create the combined list for sales and probability
sales_probability = ['0|0.05', ____, ____, ____, ____] 
weighted_probability = 0

# Create a for loop to calculate the weighted probability
for ____ in sales_probability:
    parts = pair.____('____')
    weighted_probability += ____(parts[0]) * ____(parts[1])

# Print the weighted probability result
print("The weighted probability is {}.".format(____))
```

**Ans.**

```py
# Create the combined list for sales and probability
sales_probability = ['0|0.05', '200|0.1', '300|0.4', '500|0.2', '800|0.25'] 
weighted_probability = 0

# Create a for loop to calculate the weighted probability
for pair in sales_probability:
    parts = pair.split('|')
    weighted_probability += float(parts[0]) * float(parts[1])

# Print the weighted probability result
print("The weighted probability is {}.".format(weighted_probability))
```

### Question 2: Market sentiment

Txs Tools has forecast sales of 500 in January, with an expected increase of 5% per month for the rest of the quarter.

However, this is dependent on the market sentiment. Based on historical trends, the following information has been provided:

If the market sentiment drops below 0.6 then the sales will only be realized at an increase of 2% per month.
If market sentiment increases above 0.8. then sales are expected to increase by 7%

**Instructions 1/2**

1. Define a computevariance() function with the arguments amount, sentiment.
2. Create an if statement to define the steps when sentiment drops below 0.6, elif if it is above 0.8, and else for when neither condition is met.

**Pre Code**

```py
# Create the computevariance function
def ____(amount, sentiment):
 if (____ < 0.6):
  res = amount + (amount * ____)
 elif (sentiment > 0.8):
  res = ____ + (____ * 0.07)
 else:
  res = amount + (amount * 0.05)
 return res
```

**Ans.**

```py
# Create the computevariance function
def computevariance(amount, sentiment):
 if (sentiment < 0.6):
  res = amount + (amount * 0.02)
 elif (sentiment > 0.8):
  res = amount + (amount * 0.07)
 else:
  res = amount + (amount * 0.05)
 return res
```

**Instructions 2/2**

1. Create variables jan,feb,mar based on the computevariance() if the sentiment for jan is 0.5, feb is 0.65 and mar is 0.85.
2. Print the results.

**Pre Code**

```py
# Create the computevariance function
def computevariance(amount, sentiment):
 if (sentiment < 0.6):
  res = amount + (amount * 0.02)
 elif (sentiment > 0.8):
  res = amount + (amount * 0.07)
 else:
  res = amount + (amount * 0.05)
 return res

# Compute the variance for jan, feb and mar
jan = ____(500, 0.5)
feb = computevariance(____, 0.65)
____ = computevariance(500, ____)

print("The forecast sales considering variance due to market sentiment is {} for Jan, {} for Feb, and {} for Mar.".format(____, ____, ____))
```

**Ans.**

```py
# Create the computevariance function
def computevariance(amount, sentiment):
 if (sentiment < 0.6):
  res = amount + (amount * 0.02)
 elif (sentiment > 0.8):
  res = amount + (amount * 0.07)
 else:
  res = amount + (amount * 0.05)
 return res

# Compute the variance for jan, feb and mar
jan = computevariance(500, 0.5)
feb = computevariance(500, 0.65)
mar = computevariance(500, 0.85)

print("The forecast sales considering variance due to market sentiment is {} for Jan, {} for Feb, and {} for Mar.".format(jan, feb, mar))
```

### Question 3: Assigning dependencies for sales and COGS

Txs Tools have built a monthly forecast for their gross profit. This will rely on dependencies for Sales and COGS.

Set the dependencies for sales and cogs based on the information below:
* Sales dependency sales_dep: The sale price is the net price after 1 USD commission. Commissions paid increase from 1 USD per unit to 2 USD per unit for every unit above 350 units sold.
* Cost dependency cost_dep: When sales per unit increase above 500 units, an additional production line needs to be used, causing an increase in the cost per unit above 500 of 2 USD per unit.

The baseline sale price per unit (base_sales_price) is 15 USD and the baseline cost per unit (base_cost_price) is 7 USD.

**Instructions 1/2**

1. Set the dependency calculations to sales_dep such that the first 350 sales are calculated at the base_sales_price, and the remaining sales are calculated with the increased commission.
2. Print sales_dep.

**Pre Code**

```py
# Set the Sales Dependency
if sales >= 350:
    sales_dep = (350 * ____) + ((sales - 350) * (____ - 1))
else:
    ____ = sales * base_sales_price

# Print the results
print("The sales dependency is {} USD.".format(____))
```

**Ans.**

```py
# Set the Sales Dependency
if sales >= 350:
    sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
else:
    sales_dep = sales * base_sales_price

# Print the results
print("The sales dependency is {} USD.".format(sales_dep))
```

**Instructions 2/2**

1. Set the dependency calculations to cost_dep such that the first 500 sales are calculated at the base_cost_price, and any additional sales are calculated with the increased production costs.
2. Print cost_dep.

**Pre Code**

```py
# Set the Cost Dependency
if sales >= 500:
    cost_dep = (____ * base_cost_price) + ((sales - 500) * (base_cost_price + ____))
else:
    cost_dep = ____ * base_cost_price
    
# Print the results
print("The cost dependency is {} USD.".format(____))
```

**Ans.**

```py
# Set the Cost Dependency
if sales >= 500:
    cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
else:
    cost_dep = sales * base_cost_price

# Print the results
print("The cost dependency is {} USD.".format(cost_dep))
```

### Question 4: Building a sensitivity analysis for gross profit

Txs Tools is now ready to use these dependencies in the gross profit forecast.

The following forecast unit sales have been provided:

Jul = 700 Aug = 350 Sep = 650

The dependencies for sales and cogs are based on the following:
* Sales dependency sales_dep: The sale price is the net price after 1 USD commission. Commissions paid increase from 1 USD per unit to 2 USD per unit for every unit above 350 units sold.
* Cost dependency cost_dep: When sales per unit increase above 500 units, an additional production line needs to be used, causing an increase in the cost per unit above 500 of 2 USD per unit.

The basic cost price base_cost_price = 7 and basic sales price base_sales_price = 15 has already been set.

**Instructions 1/2**

1. Create a list sales_usd for the sales unit values for Jul - Sep.

**Pre Code**

```py
# Create the sales_usd list
sales_usd = [____, ____, ____]
```

**Ans.**

```py
# Create the sales_usd list
sales_usd = [700, 350, 650]
```

**Instructions 2/2**

1. Looping through the dependency calculations, calculate the forecast gross profit forecast_gross_profit from July to September.
    * For sales_dep, the first 350 sales should be calculated at the base_sales_price, and any further sales calculated with the commission subtracted from base_sales_price.
    * For cost_dep, the first 500 sales should be calculated at the base_cost_price, and any further sales calculated with the increased production costs added to base_cost_price.

**Pre Code**

```py
# Create the sales_usd list
sales_usd = [700, 350, 650]

# Create the if statement to calculate the forecast_gross_profit
for sales in sales_usd:
    if sales > ____:
        sales_dep = (____ * base_sales_price) + ((sales - 350) * (____ - 1))
    else:
        sales_dep = sales * ____
    if sales > ____:
        cost_dep = (____ * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
    else:
        cost_dep = sales * ____
    forecast_gross_profit = sales_dep - ____

    # Print the result
    print("The gross profit forecast for a sale unit value of {} is {} USD.".format(sales, forecast_gross_profit))
```

**Ans.**

```py
# Create the sales_usd list
sales_usd = [700, 350, 650]

# Create the if statement to calculate the forecast_gross_profit
for sales in sales_usd:
    if sales > 350:
        sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
    else:
        sales_dep = sales * base_sales_price
    if sales > 500:
        cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
    else:
        cost_dep = sales * base_cost_price
    forecast_gross_profit = sales_dep - cost_dep

    # Print the result
    print("The gross profit forecast for a sale unit value of {} is {} USD.".format(sales, forecast_gross_profit))
```

### Question 5: Assigning dependencies for expenses

Txs Tools wants to assign a dependency for its operating expenses, particularly admin salaries.

The conditions are as follows:

* Admin expenses increase in July and August (Jul and Aug) as temporary workers need to be hired to cover the summer holiday.
* The increase is based on the number of employees taking holidays during that time. For the current year, the value for August is emp_leave = 6 (6 employees expected to take leave).
* The cost is 80 USD per temp employee hired.

**Instructions**

1. Using an if statement, calculate the dependency for the admin expenses admin_dep for August only by using a calculation that multiplies the employees expected to take leave (using the variable emp_leave) by the USD rate per employee.
2. Print the resultant variable you have calculated.

**Pre Code**

```py
# Set the admin dependency
if emp_leave > 0:
    admin_dep = ____ * ____

# Print the results
print("The admin dependency for August is {} USD.".format(____))
```

**Ans.**

```py
# Set the admin dependency
if emp_leave > 0:
    admin_dep = emp_leave * 80

# Print the results
print("The admin dependency for August is {} USD.".format(admin_dep))
```

### Question 6: Build a sensitivity analysis for the net profit

Txs Tools has provided the following forecast admin cost in USD based on full-time employees:

Jul = 1500 Aug = 1500 Sep = 1500

Build the forecast net profit forecast_net_profit when emp_leave = [6, 6, 0] and the cost per temp employee is 80 USD.

In addition to emp_leave and admin_usd, forecast gross profit has already been provided for you as forecast_gross_profit.

**Instructions**

1. Create an index variable and initialize this index to 0.
2. Create the dependency by looping through the admin_usd list, using your index to access the correct month in your lists.
    * Set the number of temporary employees (temp) by referencing your emp_leave list at the current index
    * If there are temporary employees, your admin dependencies (admin_dep) should reflect the additional cost of the temporary employees (plus the standard admin costs)
    * Else, admin_dep should reflect the standard admin costs.
3. Calculate forecast_net_profit as forecast_gross_profit (at the index) minus the calculated admin_dep.
4. Print the forecast_net_profit.

**Pre Code**

```py
admin_usd = [1500, 1500, 1500]
emp_leave = [6, 6, 0]
forecast_gross_profit = [4850, 2800, 4600]
index = ____

for admin in admin_usd:
    temp = ____[index]
    if temp > 0:
        admin_dep = ____ * 80 + admin
    else: 
         admin_dep = ____ 
    forecast_net_profit = forecast_gross_profit[____] - ____
    print(forecast_net_profit)
    index += 1
print("The forecast net profit is:")
```

**Ans.**

```py
admin_usd = [1500, 1500, 1500]
emp_leave = [6, 6, 0]
forecast_gross_profit = [4850, 2800, 4600]
index = 0

for admin in admin_usd:
    temp = emp_leave[index]
    if temp > 0:
        admin_dep = temp * 80 + admin
    else: 
        admin_dep = admin 
    forecast_net_profit = forecast_gross_profit[index] - admin_dep
    print(forecast_net_profit)
    index += 1    
print("The forecast net profit is:")
```

### Question 7: Building an alternate forecast
We will now build an alternative forecast for Txs Tools. The new quarter forecast is based off actual data for Jul - Aug as well as adjusted forecast data for September. The data (units sold) is as follows:

Jul = 700
Aug = 220
Sep = 520

The dependencies calculations have already been completed from the previous exercise. The following information applies:

base_cost_price = 7
base_sales_price = 15

**Instructions 1/3**

1. Create a dependencies() function for sales and costs with the arguments base_cost_price,base_sales_price, and sales_usd. Pass the arguments into the function in this order.
2. Create the res list that will generate the forecast list.
3. Have dependencies() return the resulting new quarter alternate forecast list.

**Pre Code**

```py
def ____(____, ____, ____):
    res = []
    for sales in sales_usd:
        if sales >= 350:
            sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
        else:
            sales_dep = sales * base_sales_price
        if sales >= 500:
            cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
        else:
            cost_dep = sales * base_cost_price
        res.append(sales_dep - cost_dep)
    return ____
```

**Ans.**

```py
def dependencies(base_cost_price, base_sales_price, sales_usd):
    res = []
    for sales in sales_usd:
        if sales >= 350:
            sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
        else:
            sales_dep = sales * base_sales_price
        if sales >= 500:
            cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
        else:
            cost_dep = sales * base_cost_price
        res.append(sales_dep - cost_dep)
    return res
```

**Instructions 2/3**

1. Create scenario forecast1 for the original forecast.

**Pre Code**

```py
def dependencies(base_cost_price, base_sales_price, sales_usd):
    res = []
    for sales in sales_usd:
        if sales >= 350:
            sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
        else:
            sales_dep = sales * base_sales_price
        if sales >= 500:
            cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
        else:
            cost_dep = sales * base_cost_price
        res.append(sales_dep - cost_dep)
    return res

____ = dependencies(7, 15, [700, 350, 650])
```

**Ans.**

```py
def dependencies(base_cost_price, base_sales_price, sales_usd):
    res = []
    for sales in sales_usd:
        if sales >= 350:
            sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
        else:
            sales_dep = sales * base_sales_price
        if sales >= 500:
            cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
        else:
            cost_dep = sales * base_cost_price
        res.append(sales_dep - cost_dep)
    return res

forecast1 = dependencies(7, 15, [700, 350, 650])
```

**Instructions 3/3**

1. Create scenario forecast2 for the alternative forecast. Use the data provided above to calculate the alternative forecast.

**Pre Code**

```py
def dependencies(base_cost_price, base_sales_price, sales_usd):
    res = []
    for sales in sales_usd:
        if sales >= 350:
            sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
        else:
            sales_dep = sales * base_sales_price
        if sales >= 500:
            cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
        else:
            cost_dep = sales * base_cost_price
        res.append(sales_dep - cost_dep)
    return res

forecast1 = dependencies(7, 15, [700, 350, 650])
forecast2 = dependencies(____, ____, [____, ____, ____])

print("The original forecast scenario is {}:".format(forecast1))
print("The alternative forecast scenario is {}:".format(forecast2))
```

**Ans.**

```py
def dependencies(base_cost_price, base_sales_price, sales_usd):
    res = []
    for sales in sales_usd:
        if sales >= 350:
            sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
        else:
            sales_dep = sales * base_sales_price
        if sales >= 500:
            cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
        else:
            cost_dep = sales * base_cost_price
        res.append(sales_dep - cost_dep)
    return res

forecast1 = dependencies(7, 15, [700, 350, 650])
forecast2 = dependencies(7, 15, [700, 220, 520])

print("The original forecast scenario is {}:".format(forecast1))
print("The alternative forecast scenario is {}:".format(forecast2))
```

### Question 8: Building a gap analysis between forecasts

Txs Tools now has two forecasts, the original forecast forecast1 and the adjusted forecast forecast2.

The dependencies have already been defined as def dependencies(base_cost_price, base_sales_price, sales_usd), where base_cost_price = 7 and base_sales_price = 15, with forecast2 based off the following adjusted sales unit values:

Jul = 700
Aug = 220
Sep = 520
In this exercise, we will look at how to use a for loop to cycle between two different lists, forecast1 and forecast2 and calculate the difference ("gap") using an incremented index. It is possible to do this simultaneously as both lists have the same length.

**Instructions**

1. Complete the code for the adjustment forecast and original forecast with the required variables.
2. Use an index (setting index to start at 0) to loop through your forecast2 list and print the result of the difference between the forecast2 minus forecast1.
3. Use the .format method as part of the print statement in order to print the result, and increment your index by 1.

**Pre Code**

```py
# Set the two results
forecast1 = ____(7, 15, [700, 350, 650])
forecast2 = dependencies(____, ____, [____, ____, ____])

# Create an index and the gap analysis for the forecast
index = ____
for ____ in forecast2:
    print("The gap between forecasts is {}".____(value - ____[index]))
    ____ += 1
```

**Ans.**

```py
# Set the two results
forecast1 = dependencies(7, 15, [700, 350, 650])
forecast2 = dependencies(7, 15, [700, 220, 520])

# Create an index and the gap analysis for the forecast
index = 0
for value in forecast2:
    print("The gap between forecasts is {}".format(value - forecast1[index]))
    index += 1
```

### Question 9: Setting dependencies for Netflix

Netflix has compiled a forecast up to the 2019 financial year netflix_f_is, and has based the sales figures in 2019 on the following dependency:

Number of active subscriptions, which are based on the success of Netflix original shows.
For 2019, the success of original shows (critical and commercial acclaim) are estimated at 78%. The total amount of subscribers per percentage point is 500, and set to the variable n_subscribers_per_pp (i.e there is a calculated correlation between show success and number of subscribers).

In this exercise, we will calculate how dependent sales are on the number of subscribers in the forecast, which we will use in the next exercise.

The Netflix forecast, netflix_f_iscan be printed in the shell.

**Instructions 1/3**

1. Print netflix_f_is in the shell and choose the metric that represents the sales row for the sales_metric filter list.
2. Filter the data for rows using the using the .isin() method where metric is in sales_metric and assign the result to filtered_netflix_f_is.
3. Select the 2019 forecast column, "2019 fc", from filtered_netflix_f_is, and use iloc[0] to extract the zeroth value, and assign the result to forecast1
4. Print forecast1.

**Pre Code**

```py
# Create a filter to select the sales row from the netflix_f_is dataset
sales_metric = [____]

# Filter for rows containing the Sales metric
filtered_netflix_f_is = ____[netflix_f_is.metric.isin(____)]

# Extract the 2019 Sales forecast value
forecast1 = netflix_f_is[____].____[0]

# Print the resulting forecast
print("The sales forecast is {}.".format(____))
```

**Ans.**

```py
# Create a filter to select the sales row from the netflix_f_is dataset
sales_metric = ['Sales']

# Filter for rows containing the Sales metric
filtered_netflix_f_is = netflix_f_is[netflix_f_is.metric.isin(sales_metric)]

# Extract the 2019 Sales forecast value
forecast1 = filtered_netflix_f_is["2019 fc"].iloc[0]

# Print the resulting forecast
print("The sales forecast is {}.".format(forecast1))
```

**Instructions 2/3**

1. Set the variable for the pct_success level at 78% (this has been done for you).
2. Calculate the subscriber base dependency the Netflix Forecast was based on. That is, calculate the number of subscribers per percentage point multiplied by the percentage of successes.

**Pre Code**

```py
# Set the success percentage to 78%
pct_success = 0.78

# Calculate the dependency for the subscriber base
n_subscribers = ____ * ____

# See the result
print("The dependency for the subscriber base is {}.".format(n_subscribers))
```

**Ans.**

```py
# Set the success percentage to 78%
pct_success = 0.78

# Calculate the dependency for the subscriber base
n_subscribers = n_subscribers_per_pp * pct_success

# See the result
print("The forecast depends on a subscription base of {}.".format(n_subscribers))
```

**Instructions 3/3**

1. Calculate the ratio between forecast 2019 sales (forecast1 and the number of subscribers n_subscribers, assigning the result to sales_subs_ratio.

**Pre Code**

```py
# From previous steps
sales_metric = ['Sales']
filtered_netflix_f_is = netflix_f_is[netflix_f_is.metric.isin(sales_metric)]
forecast1 = filtered_netflix_f_is["2019 fc"].iloc[0]
pct_success = 0.78
n_subscribers = n_subscribers_per_pp * pct_success

# Calculate the ratio between forecast sales and subscribers
sales_subs_ratio = ____ / ____

# See the result
print("The ratio between subscribers and sales is 1 subscriber equals ${:.2f}.".format(sales_subs_ratio))
```

**Ans.**

```py
# From previous steps
sales_metric = ['Sales']
filtered_netflix_f_is = netflix_f_is[netflix_f_is.metric.isin(sales_metric)]
forecast1 = filtered_netflix_f_is["2019 fc"].iloc[0]
pct_success = 0.78
n_subscribers = n_subscribers_per_pp * pct_success

# Calculate the ratio between forecast sales and subscribers
sales_subs_ratio = forecast1 / n_subscribers

# See the result
print("The ratio between subscribers and sales is 1 subscriber equals ${:.2f}.".format(sales_subs_ratio))
```

### Question 10: Calculating an alternative forecast for Netflix

The original assumptions are as follows: the total amount of subscribers at a 78% success rate results in 39,000 subscribers. We used this to build the forecast numbers.

However, the success rate for 2019 has been recalculated to have a probability of 65%, and the management has asked us to make an adjusted forecast based on this value.

The ratio between the subscribers and sales is 1 subscriber to 0.46 USD sales, set to variable sales_subs_ratio. In addition, the variables for number of subscribers per percentage point (n_subscribers_per_pp) and our prior calculation of forecast1 have also been set.

**Instructions 1/2**

1. Set the percentage of successes to 65% (as a whole number, not a fraction).
2. Calculate the new number of subscribers in the dependency as the product of the number of subscribers per percentage point times the percentage of successes.
3. Calculate the new forecast, forecast2, as the new number of subscribers times the sales to subscriptions ratio.

**Pre Code**

```py
# Set the proportion of successes to 65%
pct_success2 = ____

# Calculate the number of subscribers
n_subscribers2 = ___

# Calculate the new forecast
forecast2 = ____ * ____
```

**Ans.**

```py
# Set the proportion of successes to 65%
pct_success2 = 65

# Calculate the number of subscribers
n_subscribers2 = n_subscribers_per_pp * pct_success2

# Calculate the new forecast
forecast2 = n_subscribers2 * sales_subs_ratio
```

**Instructions 2/2**

1. Insert a new column to filtered_netflix_f_is named "AltForecast" after the last column, containing the value forecast2.
    * Use the len() function to count the number of items in the list and ensure the value of forecast2 is inserted in the last position at the end of filtered_netflix_f_is
2. Use a similar approach to insert another column named "Gap" after the last column, containing the value forecast1 minus forecast2.


**Pre Code**

```py
# From previous step
pct_success2 = 65
n_subscribers2 = n_subscribers_per_pp * pct_success2
forecast2 = n_subscribers2 * sales_subs_ratio

# Insert a column named AltForecast, containing forecast2
filtered_netflix_f_is.insert(len(filtered_netflix_f_is.columns), '____', ____)

# Insert a column named Gap, containing the difference
____

# See the result
print(filtered_netflix_f_is)
```

**Ans.**

```py
# From previous step
pct_success2 = 65
n_subscribers2 = n_subscribers_per_pp * pct_success2
forecast2 = n_subscribers2 * sales_subs_ratio

# Insert a column named AltForecast, containing forecast2
filtered_netflix_f_is.insert(len(filtered_netflix_f_is.columns), 'AltForecast', forecast2)

# Insert a column named Gap, containing the difference
filtered_netflix_f_is.insert(len(filtered_netflix_f_is.columns), 'Gap', forecast1 - forecast2)

# See the result
print(filtered_netflix_f_is)
```

<hr>