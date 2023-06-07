1. **Credit strategy and minimum expected loss**
We've looked at acceptance rates to calculate thresholds and we calculated bad rates to see how many defaults are accepted. Now, let's talk about how we test many different acceptance rates and how we can estimate total expected loss.

2. **Selecting acceptance rates**
Previously, we selected an acceptance rate of 85%. What if we don't know what values to set? To discover the bad rate an impact of each acceptance rate we could calculate all the values manually, or we could calculate them automatically and create a table. This table is referred to as the strategy table because we can choose our acceptance rate based on our overall strategy for the loan portfolio.

3. **Setting up the strategy table**
Before we begin calculating all the values for the strategy table, we first set up objects to store the values. Here, we create a list of all the acceptance rates to test. We also have two empty lists to store the thresholds and bad rates.

4. **Calculating the table values**
To create the table, we use a for loop to perform all of the calculations automatically and store the results. So, for each acceptance rate we define, we calculate the threshold, store it for later, apply it to the loans, create a subset called accepted loans, and then calculate and store the bad rate.

5. **Strategy table interpretation**
Once the for loop completes we can create a data frame for the strategy table which contains the values from each of the lists we made before. If we decided on an acceptance rate of 90%, then here we can see the threshold and bad rate for that acceptance rate. We accept only 90% of new loans, and reject the top 10% which gives us a threshold of 0.947. If we assume our test set loans are new loans not seen before, then we have an estimated bad rate of 13%.

6. **Adding accepted loans**
To make the strategy table more useful, we are going to add a few columns. The first is the number of accepted loans. This shows us how many new loans we accept for each acceptance rate.

7. **Adding average loan amount**
Next, we add an average loan value that we will use later. This is just the average loan amount from the test set.

8. **Estimating portfolio value**
Finally, the estimated value is difference between the average value of the accepted non-defaults minus the average value of accepted defaults. Remember, the accepted defaults is represented as a percentage which is the bad rate. Here, I assume each default in our accepted loans is a loss of the average amount of all loans. This gives a rough estimate for the portfolio value at each acceptance rate. So, if I choose an acceptance rate of 95% then my bad rate is 17.7%. If my acceptance rate is 85% then my bad rate is 9%. There is a trade-off between acceptance and bad rate. With this new table, we can estimate the difference.

9. **Total expected loss**
The final way we will measure the financial impact of our predictions is with total expected loss. This represents how much we expect to lose on loan defaults given their probability of default. We will take the product of the probability of default, loss given default, and exposure at default for each loan, and sum it. Within our predictions data frame we will use the probability of default from prob_default, the exposure will be assumed as the total loan value, and the loss given default will be 1 for a total loss on the loan.

10. **Let's practice!**
Now that we've figured out how to create the strategy table and calculate total expected loss for the portfolio, let's finish strong with our final set of coding exercises!