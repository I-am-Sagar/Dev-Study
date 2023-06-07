1. **Logistic regression for probability of default**
Now that we've removed both outliers and missing data from out data set, we can begin modeling to predict the probability of default.

2. **Probability of default**
Recall that the probability of default is the likelihood that someone will fail to repay a loan. This is expressed as a probability which is a value between zero and one. These probabilities are associated with our loan status column where a 1 is a default, and a 0 is a non default.

3. **Probability of default**
The resulting predictions give us probabilities of default. The closer the value is to 1, the higher the probability of the loan being a default.

4. **Predicting probabilities**
To get these probabilities, we train machine learning models on our credit data columns, known as features, so the models learn how to use the data to predict the probabilities. These types of models are known as classification models, where the class is default or non-default. In the industry, two models are used frequently. These are logistic regressions, and decision trees. Both of these models can predict the probability of default, and tell us how important each column is for predictions.

5. **Logistic regression**
The logistic regression is like a linear regression but only produces a value between 0 and 1. Notice that the equation for the linear regression is actually part of the logistic regression. Logistic regressions perform better on data when what determines a default or non-default can vary greatly. Think about the y-intercept here, which is the log odds of non-default. This as another way of expressing the overall probability of non-default.

6. **Training a logistic regression**
In this course, we use the logistic regression within scikit learn. The use of the model is easy. Like any function, you can pass in parameters or not. The solver parameter is an optimizer, just like the solver in Excel. LBFGS is the default. To train the model, we call the fit method on it. Within the method, we have to provide the model with training columns and training labels. We use ravel from numpy to make the labels a one-dimensional array instead of a data frame. In our credit data, the training columns are every column except the loan status. The loan status contains the labels.

7. **Training and testing**
Generally, in machine learning, we split our entire data set into two individual data sets.

8. **Training and testing**
They are the training set and the test set. We use the majority of the data to train our models, so they learn as much as possible from the data. Our test set is used to see how our model reacts to new data that it has not seen before. This is like students learning in school. They will learn facts from one subject, and be tested on different facts from that same subject. This way, we can asses their mastery of the topic.

9. **Creating the training and test sets**
The first thing we do is separate our data into training columns and labels. Here, we have assigned those as X and Y. With that done, we use the test train split function within the sci-kit learn package. Let's have a look at the code. Remember how I said we need training columns and labels for our model? We need these for both the training set and the test set, which are all easily created with one line of code. Within this function, we set the percentage of the data to be used as a test set, and a number used as a random seed for reproducibility.

10. **Let's practice!**
Now that we've learned how to use a logistic regression to predict the probability of default, let's jump right into some programming exercises!