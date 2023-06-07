1. **Cross validation for credit models**
As we select different hyperparameters and columns for our models, how do we know how they will perform over time? This is where we use cross validation to test our models to see how they might perform after we implement them.

2. **Cross validation basics**
But what is cross validation? Simply put, it is a method for training and testing a model multiple times on the same data. We cannot create more loan data to help us develop our model, but we can use cross validation to simulate how our model will perform on new loan data before it comes in. Within XGBoost, to use cross validation you need to create a specialized object called dmatrix, which is just a different way of storing the training data. We also need to use early stopping to keep the models robust. This tells cross validation to stop when the score of the model has not improved after a set number of iterations.

3. **How cross validation works**
Here's how cross validation works. What we do is take the entire set of training data and create pieces, called folds, from it. All but one of the folds are used for training, and the remaining fold is used as a kind of miniature test set. Once testing on all folds is completed, the model is tested against the actual test set. We've created 5 folds. Now what happens is the model is trained on 4 of the folds, and tested against the final fold. This process repeats through 5 splits so that each fold is used for testing at least once. Once this is done, the parameters are averaged across each training session and then the model is finally tested against the original test set.

https://scikit-learn.org/stable/modules/cross_validation.html

4. **Setting up cross validation within XGBoost**
Here is how we use cross validation from within xgboost. First, we set the number of folds. Then, we set the number of iterations we will allow before the simulations stop. Next, we create a dictionary of parameters. The binary logistic parameter we created tells xgboost that we want to predict a 0 or 1 for loan status. The performance metric here is the area under the curve. This is the same metric we used on the logistic regression models.

5. **Using cross validation within XGBoost**
After creating the dictionary of parameters, we transform our training data into the specialized dmatrix object for xgboost. Last, we call the cv function and pass in the data long with all the parameters dictionary.

6. **The results of cross validation**
What the cv function produces is a data frame of training and test AUC scores for our model. Think of this as a scenario analysis where we want to see how our model would perform as new loans come in. Here we see that the auc for the test and train set improves as the model trains on each fold. This suggests that the performance will be stable.

7. **Cross validation scoring**
Within scikit-learn there is another helpful function that combines cross validation, and the accuracy scoring metrics we've seen so far. This is the cross val score function. This is used to automatically perform cross validation with data splitting, model training, and scoring all at once! This function comes from the model selection module and is used like this. We first pass in the model, the training data, the training labels, and then the number of folds for cross validation. There are other ways to use this, but when cv is a number, it automatically uses folds. The result is an array of scores for each iteration of training and scoring.

8. **Let's practice!**
We've learned a lot about model scoring and testing to further validate our models to ensure their performance and success. Let's do some quick programming exercises to reinforce our new knowledge!