1. **Column selection for credit risk**
We've trained logistic regression models and gradient boosted trees now. But does selecting specific columns affect model performance?

2. **Choosing specific columns**
When we first started working with logistic regression models, we used only a few columns. Now, we've been using all of the columns, but how do we know which are the most important for accurately predicting probability of default? For logistic regression models, we were looking at the coefficient of each column and interpreting that coefficient as a weight or measure of importance. But what do we use for our gradient boosted trees?

3. **Column importances**
The first easy way to tell which columns are important is to check the feature importances using the get booster and get score methods together. For this course we will focus on the weight type, which shows how many times the column appears in all the models' trees. Once we've trained a model, we are able to see the feature importances by calling these two methods in sequence This returns is a dictionary of each column's name with the weight number as shown here.

4. **Column importance interpretation**
These were the importance values we looked at in the last example, but how do we interpret this? In this example, our model created two trees which were gradient boosted. Our column importance for person home ownership was 2, and we can see here that the column appears in both trees. The person home ownership rent is only in one of the trees, so it's column importance is one.

5. **Plotting column importances**
We can also visualize the column importances with the plot importance function in xgboost. We call this function and pass in our model to see a nice visualization of the importances. In this example, our model created 400 trees, and the person_income column was used 315 times across all of them. So, 315 of the 400 trees used person_income.

6. **Choosing training columns**
Once we have the importances for each column, to determine if we want to create a new training set with only select columns. Different combinations of these columns will affect the overall performance Consider this example. We have two training sets. One has loan interest rate and employment length, while the other has these two columns and the loan's percentage of the person's income. In this example, adding another column improves the accuracy, but changes the importance of the other two columns and reduces default recall. Sometimes adding more columns increases accuracy, but it can also make it more difficult for the model to learn and decrease other performance metrics like default recall.

7. **F1 scoring for models**
It can be difficult to use two metrics like accuracy and recall to gauge a model's performance. Fortunately, there is already a defined metric that combines both of these two into one. This metric is the F1 score. This is a combination of both precision and recall. This is useful because it helps us keep recall for loan defaults as an important consideration for any model. The formula, as shown here, is two times the product of the precision and recall divided by their sum. The great thing is that this number already shows up in a classification report. Here, we see the F1-score numbers for both defaults and non-defaults.

8. **Let's practice!**
Now that we've talked about how important different columns are for predictions as well as how to select different columns and why, let's dive into the code again to put these ideas into practice!

