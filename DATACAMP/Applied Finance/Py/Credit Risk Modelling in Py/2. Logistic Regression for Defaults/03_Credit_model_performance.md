1. **Credit model performance**
We saw predictions for probability of default against true values for loan status, but how do we analyze the performance of our model?

2. **Model accuracy scoring**
The easiest way to analyze performance is with accuracy. Accuracy is the number of correct predictions divided by the total number of predictions. One way to check this is to use the score method within scikit-learn on the logistic regression. This is used on the trained model and returns the average accuracy for the test set. Using the score method will display this accuracy as a percentage. In this example, it tells us that 81 percent of the loans were predicted correctly.

3. **ROC curve charts**
R-O-C charts are a great way to visualize the performance of our model. They plot the true positive rate, the percentage of correctly predicted defaults, against the false positive rate, the percentage of incorrectly predicted defaults. Using the roc_curve function in scikit-learn, we create these two values and the thresholds all at once. From there, we use a normal line plot to see the results. The dotted blue line represents a random prediction and the orange line represents our model's predictions.

4. **Analyzing ROC charts**
R-O-C charts are interpreted by looking at how far away the model's curve gets from the dotted blue line shown here, which represents the random prediction. This movement away from the line is called lift. The more lift we have, the larger the area under the curve gets. The A-U-C is the calculated area between the curve and the random prediction. This is a direct indicator of how well our model makes predictions.

5. **Default thresholds**
To analyze performance further, we need to decide what probability range is a default, and what is a non-default. Let's say that we decide any probability over 0.5 is a default, and anything below that is a non-default. What this means is that we will assign a new loan_status to these loans based on their probability of default and the threshold. Once we have this, we can further check the model's performance.

6. **Setting the threshold**
Once the threshold is defined, we need to relabel our loans based on that threshold. For that, we will first need to create a variable to store the predicted probabilities. Then we can create a data frame from the second column which contains the probabilities of default. Then we apply a quick function to assign a value of 1 if the probability of default is above our threshold of 0.5. The lambda is there just to tell Python that we want to use a one-time function without defining it. The result of this is a data frame with new values for loan status based on our threshold.

7. **Credit classification reports**
Another really useful function for evaluating our models is the classification report function within scikit-learn. This will show us several different evaluation metrics all at once! We use this function to evaluate our model using our true values for loan status stored in the y_test set, and our predicted loan status values from our logistic regression and the threshold we set. There are 2 really useful metrics in this table, and they are the precision and recall. For now, let's focus on recall.

8. **Selecting classification metrics**
Sometimes after generating the report, you want to select or store specific values from within the report. To do this, you can use the precision recall fscore support function within sci-kit learn. With this function, we can get the recall for defaults from by subsetting the report the way we would any array. Here we select the second value from the second set.

9. **Let's practice!**
Now that we've talked about model accuracy, recall, and AUC scores let's put it all into practice with code!