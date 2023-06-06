1. **Financial ratios from the cash flow statement**
In this video, we will learn how to read JSON files into python. We we will also learn about financial ratios from the cash flow statement and how to impute missing values.

2. **Reading in JSON data**
Data from the wild comes in many formats - not just in spreadsheets, so we should know how to read different data formats into Python. JSON is a common format companies share their financial data in. JSON files can be read into Python using pandas. The code is very similar to reading in Excel files using pandas.

3. **Cash flow to net income ratio**
Now, on to some ratios from the cash flow statement. Cash flow to net income ratio is the proportion of cash from operating activities to the net income of the business. Cash flow from operating activities is the cash generated from the core activities of the business. A high ratio implies that the business generates a sizable amount of its net income from its core activities in cash.

4. **Operating cash flow ratio**
Next, let's talk about operating cash flow ratio. This is the proportion of cash flow generated from operating activities to current liabilities. Recall that current liabilities are the short-term obligations of the business, thus this ratio tells us how many times the business can pay off its short-term obligations using the cash it generates from the core of its business. A ratio of more than one implies a business can meet its short term obligations.

5. **Imputing missing values**
Nobody likes to have missing data, but it is something very common when we collect data from the wild. If a company is missing data to compute a ratio, we can use the non-missing data to impute it.

6. **Imputing missing values**
The DataFrame here has missing values in the "Total Current Liabilities" column. The missing value can be imputed by using the average of the non-missing values per company.

7. **Imputing missing values**
We can use the code shown to impute and fill in the missing values. We use the transform function of pandas which we covered earlier to create our imputations. The pandas function of fillna is used to fill in the missing values. We can use groupby not only over the company but over any dimension we want to impute missing values over. However, imputing missing values for companies might result in us computing optimistic ratios with the imputed values if the industry or year used to make the imputation has performed extremely well, but not the company whose missing values we are imputing. We can overcome this problem by using percentiles.

8. **Imputing missing values with percentiles**
Using, say, a 70th percentile worse value as an imputation would yield more conservative results. Using conservative values to compute ratios is safer if the ratio is used for future decision-making. For example, consider the decision to invest in a company. We can use the code shown to impute and fill in missing values using percentiles. np-dot-nanqunatile is used, where the first argument is the array over which we want to compute a percentile, and the second argument is the percentile we want to compute, which is a number between 0 and 1. To compute the 70th percentile of non-missing data, we pass 0-point-seven as the second argument. The lambda used here is like the "def" we use to make functions. So, in this case, lambda is just like a function which takes the argument x, which is "Total Current Liabilities", passes it though the np-dot-nanqunatile to compute its 70th percentile of non-missing data. You can check out pythons documentation to see what the lambda function does in more detail.

9. **Let's practice!**
Now let's practice with some exercises!