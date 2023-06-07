1. **Predicting the probability of default**
So far, we've trained a logistic regression on our credit data, and looked some attributes of the model. Now, let's discuss the structure of the model and how to create predictions.

2. **Logistic regression coefficients**
In the previous exercise, we saw the following intercept and coefficients for our model. These coefficients the importance of each column. These values are part of the logistic regression formula that calculates the probability of default which we see here. Each coefficient is multiplied by the values in the column, and then added together along with the intercept. Then, 1 is divided by the sum of 1 and e to the negative power of our intercept coefficient sums. The result is the probability of default.

3. **Interpreting coefficients**
Consider employment length as an example. I've already calculated the intercept and coefficient for a logistic regression using this one column. What this coefficient tells us is the log odds for non-default. This means that for every 1 year increase in employment length, the person is less likely to default by a factor of the coefficient.

4. **Interpreting coefficients**
Let's say we have 3 values for employment length, and we want to know how this affects our probability of default by looking at the coefficients. What we see here is that the higher a person's employment length is, the less likely they are to default.

5. **Using non-numeric columns**
Since we're talking about numbers, it's worth mentioning that so far we have only used numeric columns to train out models. Our data also contains non-numeric columns like loan intent, which uses words to describe how the person plans to use the money we lend them. In Python, unlike R, machine learning models do not know how to use these non-numeric values. So, we have to perform an operation called one-hot encoding before we can use them.

6. **One-hot encoding**
One-hot encoding sounds complicated, but it's really simple. The main idea is to represent a string with a numeric value. Here is how it works. Let's think about the loan intent column where each loan has it's own intent value as a string. This sample has education, medical, and venture.

7. **One-hot encoding**
With one-hot encoding, we get a new set of columns where each value from loan intent is now it's own column. Each new column is created by separating out the loans with each intent value and making the new column's value a 0 or 1. For example, if the loan intent was education, it is now represented with a 1 in the loan intent education column. This way, there is one hot value.

8. **Get dummies**
To one-hot encode our string columns, we use the get dummies function within pandas. First, we separate the numeric and non-numeric columns from the data into two sets. Then we use the get dummies function to one-hot encode only the non-numeric columns. We union the two sets and the result is a full data set that's ready for machine learning!

9. **Predicting the future, probably**
Once our model is trained, we use the predict proba method on test data to make predictions. This creates a set of probabilities for non-default and default. Notice the output is a series of numbers between 0 and 1. We have two for each loan. The first number is the probability of non-default, and the second number is the probability of default.

10. **Let's practice!**
We've discussed the model coefficients and one-hot encoding, so let's predict loan defaults with code!