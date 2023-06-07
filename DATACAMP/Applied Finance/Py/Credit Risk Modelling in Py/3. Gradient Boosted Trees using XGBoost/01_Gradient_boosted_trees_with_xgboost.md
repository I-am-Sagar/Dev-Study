1. **Gradient boosted trees with XGBoost**
We've used many different ways to experiment with a logistic regression for probability of default. Now, let's have a look at gradient boosted decision trees using XGBoost.

2. **Decision trees**
So what is a decision tree? They are machine learning models which use decisions as steps in a process to eventually identify our loan status. While they produce predictions similar to logistic regressions, they are not structured the same way. Here is an example of a simple decision tree. The first box, or node, has decided to split the data into two groups. Those with an employment length above 10, and those below. Then it uses loan intent medical the same way. The results of these splits are yes and no decisions that eventually lead to a predicted loan status of default or non-default.

3. **Decision trees for loan status**
Let's have a look at a simple example of a decision tree on the loan data when what we are predicting is still defaults. Here, we have a red dot for each default, and a green dot for each non-default. The red shaded area is what our model predicted as default. While it predicted all of the defaults correctly, it predicted two non-defaults as default.

4. **Decision tree impact**
What are the consequences of this? Let's say both of these loans were worth 1500 and 1200 at the time we predicted their status. Then, maybe we decide to sell off all debt we think is likely to default for 250 per loan. As a result of the model, our loss is 2200 dollars for just two loans!

5. **A forest of trees**
XGBoost doesn't use just one decision tree though, but a large number of them in what's known as an ensemble through a method called gradient boosting. Each tree in the ensemble is like the one we just saw, and is a weak predictor. Have a look at this example. The first two boxes on the left represent two different individual models. Each of them predicts the defaults, but they also predict some non-defaults as defaults. However, when we use gradient boosting with XGBoost, we get the box on the right which combines the two weak models. In this example, the boosted model predicts all of the loans correctly.

6. **Creating and training trees**
The trees we will use are available within the xgboost package, and they train similar to logistic regression models. Here, we can see that the gradient boosted tree is created using the XGBClassifier function. Next, fit is called on the model the same as before and with the same training data.

7. **Default predictions with XGBoost**
These models predict the same way as the logistic regression do. We can use predict_proba to predict probabilities of default. The predict method gives us a value of 0 or 1 for loan status. The predict_proba method returns an array of probabilities for default and non-default. The predict method returns an array of the loan status.

8. **Hyperparameters of gradient boosted trees**
The models have parameters that are like settings that affect how a model learns. These settings are called hyperparameters. Hyperparameters cannot be learned from data; they have to be set by us. Let's look at a few of these hyperparameters. The learning rate tells the model how quickly it should learn in each step of the ensemble. The smaller the value, the more conservative it is at each step. The max depth tells the model how deep each tree can go. Keeping this value low ensures the model is not too complex.

9. **Let's practice!**
Now that we've learned about gradient boosted trees and how to use them for loan defaults, it's time for some programming fun!