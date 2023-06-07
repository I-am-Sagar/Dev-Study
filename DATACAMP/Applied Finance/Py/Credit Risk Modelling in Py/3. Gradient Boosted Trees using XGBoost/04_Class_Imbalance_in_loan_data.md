1. **Class imbalance in loan data**
We just used cross-validation to check the robustness of our model. Let's talk more about how the data impacts the robustness of the model.

2. **Not enough defaults in the data**
In our credit data, the values for loan status are our classes. By looking at the value counts, we see that the number of defaults and non-defaults is not equal. In the training data, the defaults account for 22%. So, there are far more non-defaults than defaults. This is class imbalance, which is a problem.

3. **Model loss function**
Our tree models use a loss function called log-loss. Our model will want to predict both classes accurately as this leads to an overall better score. Here, we have one default and one non-default. Each has a predicted probability far away from the actual loan status. With the log-loss function, both result in the same value. So, for our model each is equally bad. The problem is, for loans, a default predicted to be a non-default is much more costly.

4. **The cost of imbalance**
Let's say we have two loans for a thousand dollars each. One is a non-default predicted as default, and the other is a default predicted as non-default. Here, each has a potential profit of 10 dollars. If we deny a loan because we think it's a default when it isn't, we miss out on 10 dollars. If we accept a loan because we think it's a non-default when it is a default, we could lose a thousand dollars. For the model, each of these is equally bad. For our portfolio, that is definitely not the case.

5. **Causes of imbalance**
What causes class imbalance can be several different things. One is there might be some issues with the data itself. Maybe the training data was not sampled correctly. For us, the imbalance is perfectly normal. People have incentives to not default on loans. One example is the less often they default, their credit rating goes up and they are able to purchase more things.

6. **Dealing with class imbalance**
So, how can we deal with class imbalance? One way is to gather more data. However, if it remains normal for people to not default on loans, it's unlikely that the percentage of defaults will change. Another way is to penalize the classification differently. This would have models weight inaccurately predicted defaults more. However, this can require frequent model parameter tuning and maintenance for the life of the model. We will use the simplest method, which is to sample the training data differently.

7. **Undersampling strategy**
The type of sampling we are going to perform is called undersampling. What we will do is take a random sample of non-defaults and combine it with our defaults. Imagine we have 100 loans where 80% are non-defaults. We will randomly sample only 20 of our non-defaults, and combine that with our set of 20 defaults. With this, we have a balanced training set of 20 defaults and 20 non-defaults.

8. **Combining the split data sets**
So here is the way we undersample our training data. First we concatenate our X and y training sets because we separated them for our model, but now we need to change the training data as a whole. Then we store the counts for defaults and non-defaults. After that, we create two new data sets. One with only defaults and one with only non-defaults.

9. **Undersampling the non-defaults**
With that done, we randomly sample our non-defaults to be the same number of loans as our defaults. Then, we concatenate the two data sets together, and we have a balanced training set!

10. **Let's practice!**
So we've learned why class imbalance is a problem, and an easy way to correct it. Let's get to coding!