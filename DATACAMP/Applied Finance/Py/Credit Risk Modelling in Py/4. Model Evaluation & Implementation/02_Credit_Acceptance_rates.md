1. **Credit acceptance rates**
We've compared our two models and decided to proceed with the gradient boosted tree. It's time to begin implementing our model and the predicted probabilities of default.

2. **Thresholds and loan status**
Until now, we've used guesses and simple checks to set threshold values for determining the loan status based on the predicted probability of default. With those values, we used code like this to set a new loan status based on the probability and threshold. These new values of loan status impact the performance metrics of our model as well as the estimated financial impact on the portfolio. If we have three loans with these probabilities of default, those above the threshold are considered defaults and those below are considered non-defaults.

3. **Thresholds and acceptance rate**
Our models have already predicted the probabilities of default, and we can use these probabilities to calculate the threshold. Because the threshold is used to determine what is a default or non-default, it can also be used to approve or deny new loans as they come in. For example purposes, let's assume our test set is a fresh batch of new loans. Before we calculate the threshold, we need to understand a concept known as acceptance rate. This is a percentage of new loans that we accept with the goal of keeping the number of defaults in a portfolio below a certain number.

4. **Understanding acceptance rate**
Here's an example using our test data. If we want to accept 85% of all loans with the lowest probabilities of default, then our acceptance rate is 85%. This means we reject 15% of all loans with the highest probabilities of default. Instead of setting a threshold value, we want to calculate it to separate the loans we accept using our acceptance rate from the loans we reject. This value will not be the same 85% that we used as an acceptance rate.

5. **Calculating the threshold**
In order to calculate this threshold we need to use the quantile function from numpy. This uses our array of probabilities of default and the acceptance rate to determine what value separates our accepted loans from rejected loans. In our example, the threshold is 0.804. This means that all of our new loans with a probability of default below 80% are accepted, and all probabilities above that are rejected.

6. **Implementing the calculated threshold**
Reassigning loan status values is done the same way as before. We apply a one-time function to our data frame using our new threshold value.

7. **Bad Rate**
Even though we've calculated an acceptance rate for our loans and set a threshold, there will still be some defaults in our accepted loans. These are often in probability ranges where our model was not well-calibrated. For our example, we accepted 85% of the loans, but not all of them are non-defaults as we might wish. The bad rate is the percentage of accepted loans which are actually defaults. So, our bad rate is a percentage of the 10,016 accepted loans.

8. **Bad rate calculation**
The calculation for the bad rate is the number of defaults in our accepted loans divided by the total number of accepted loans. In Python, we use the sum function from numpy to count the number of defaults, and the count method to get the total number of accepted loans. The reason this method works is because our non-defaults are zero and defaults are one, the sum is mathematically the same as the count of defaults. This divided by the count of rows in the data frame gives us our bad rate!

9. **Let's practice!**
So, we've talked about acceptance rates, bad rates, and how to apply them to the data. Time for some Python exercises!