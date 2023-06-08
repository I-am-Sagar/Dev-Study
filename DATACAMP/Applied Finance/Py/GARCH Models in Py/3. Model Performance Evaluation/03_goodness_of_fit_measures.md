1. **Goodness of fit measures**
In this lesson, we will discuss the concept "goodness of fit", and how to measure it.

2. **Goodness of fit**
As the name suggests, "goodness of fit" describes how well a model fits a set of observations. Measures of goodness of fit typically summarize the discrepancies between observed values and the values estimated by the model. There are many methods to measure the "goodness of fit". Specifically, we will discuss the maximum likelihood method and information criteria.

3. **Maximum likelihood**
GARCH models use the "maximum likelihood method" to estimate parameters. Maximum likelihood estimation is a method of estimating model parameters by maximizing the likelihood function, so that it maximizes the probability, or the likelihood, of getting the data we have observed under the assumed model.

4. **Log-likelihood in Python**
GARCH model log-likelihood values can be reviewed in the model summary. We can also get the value directly using "loglikelihood".

5. **Overfitting**
Overfitting happens when a model learns the details and noises in the training data, or in-sample data, to the extent that it negatively impacts the performance of the model on new data, or out-of-sample data. In other words, noise or random fluctuations in the in-sample data is picked up and learned as patterns by the model, which does not apply to new information. Overfitting usually results from making an overly complex model to explain idiosyncrasies in the data under study.

6. **Information criteria**
Information criteria intend to measure the trade-off between goodness of fit and model complexity. When fitting models, it is possible to increase the likelihood by adding parameters, but doing so may result in overfitting. Information criteria consider the model likelihood, but also add penalties for model complexity. A model with more parameters will have higher information criteria score given the same likelihood values. AIC and BIC are two commonly used information criteria. AIC stands for "Akaike information criterion", and is named after statistician Akaike who formulated it. BIC stands for "Bayesian information criterion", and is quite similar to AIC. They are both used under the context of model selection, and the models with relatively lower AIC or BIC scores are preferred.

7. **AIC vs. BIC**
What is the difference between AIC and BIC, you may ask. In general, their results agree with each other, and models with the lowest AIC or BIC are preferred. The main difference between AIC and BIC is the size of the penalty for model complexity. BIC imposes bigger penalties on models with more parameters, and leads to choosing more parsimonious models than does AIC.

8. **AIC/BIC in Python**
GARCH model AIC and BIC values can be reviewed in the model summary. We can also get them directly using “aic” and “bic” respectively.

9. **Let's practice!**
Now let's practice of what you have just learned!