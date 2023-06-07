1. **Model discrimination and impact**
We've looked at some ways to evaluate our logistic regression. Let's talk more about thresholds and their impact on portfolio performance.

2. **Confusion matrices**
Another way to analyze our model's performance is with the confusion matrix. These will show us all our correct and incorrect predictions for loan status. The confusion matrix has four sections: true positives, false positives, false negatives, and true negatives. We've looked at recall for defaults within classification reports. That formula and where it resides in the confusion matrix are shown here.

3. **Default recall for loan status**
The definition of default recall, also called sensitivity, is the proportion of actual positives correctly predicted. Before, we retrieved this value from the classification report without understanding how it's calculated. Recall is found by taking the number of true defaults and dividing it by the sum of true defaults and defaults predicted as non-default.

4. **Recall portfolio impact**
Let's look at the recall for defaults highlighted in red in a classification report. This is an example of a report from an under-performing Logistic Regression model. Here, the proportion of true defaults predicted by our model was only 4 percent.

5. **Recall portfolio impact**
Imagine that we have 50 thousand loans in our portfolio, and they each have a total loan amount of 50 dollars. As seen in the classification report, this model has a default recall of 4 percent. So, that means we correctly predicted 4 percent of defaults, and incorrectly predicted 96 percent of defaults. If all of our true default loans defaulted right now, our estimated loss from the portfolio would be 2.4 million dollars! This loss would be something we didn't plan for, and would be unexpected.

6. **Recall, precision, and accuracy**
When it comes to metrics like recall, precision, and accuracy, it can be challenging to find an optimum number for all three as a target. Have a look at this example graph of a logistic regression model on the credit data. The blue line, which is default recall, starts out really high. This is because if we predict all loans to be a default, we definitely predict all of our defaults correctly! You can also see that when default recall is high, more often than not non-default recall is low. Initially, we have to make a determination about what scores for each are good enough in order to set a baseline for performance.

7. **Let's practice!**
Now that you've learned about confusion matrices and the impact of metrics like recall on the portfolio, go ahead and test these ideas out in the programming exercises!