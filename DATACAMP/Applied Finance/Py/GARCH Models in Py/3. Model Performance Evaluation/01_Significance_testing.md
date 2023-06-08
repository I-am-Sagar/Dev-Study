1. **Significance testing of model parameters**
Hi and welcome back! Previously you have learned how to specify assumptions to define more realistic GARCH models, and how to make better forecasts with the rolling window approach. But how do we measure model performance and choose a better model? You will gain clarity after this chapter.

2. **Do I need this parameter?**
GARCH models can have a lot of parameters, such as omega, alpha, beta for difference lag periods, lambda for GJR-GARCH, EGARCH and so on. A valid question is: do I need this parameter? Is it relevant and help to construct a better model? Or is it so close to zero that can we leave it out? In data science modeling, and in scientific research in general, we should always follow the "KISS" rule, which stands for "keep it simple stupid"!. In other words, choose the parsimonious models over complex models. The principle of parsimony states that the simplest explanation of an event or observation is the preferred one. A parsimonious model can do a good job explaining the data with the minimum number of parameters.

3. **Hypothesis test**
We can use a hypothesis test to help decide whether to keep or drop a model parameter. Hypothesis test is a statistical way to verify a claim, also known as the "null hypothesis or H0, that is made about a population using the sample data. The alternative hypothesis is the one we would accept if the null hypothesis is concluded to be untrue. In our case, the null hypothesis is: a parameter value is 0. If H0 cannot be rejected, we should leave the parameter out of the GARCH model.

4. **Statistical significance**
We can conduct tests of statistical significance to determine whether to accept or reject the null hypothesis. As a general rule, the significance level is commonly set to 0.05, meaning that the probability of observing the results in our data by chance is just 5%.

5. **P-value**
From a statistical significance test, we can obtain the p-value, which is used to compare with the predefined significance level to decide whether to reject or accept the null hypothesis. P-value is the probability value of obtaining the observed results of a test, assuming that the null hypothesis is true. It tells us what the odds are that the results could have happened by chance. The lower the p-value, the more surprising the evidence is, the more ridiculous our null hypothesis looks. In other words, reject the null hypothesis if the p-value is smaller than the specified significance level, such as 5%.

6. **P-value example**
GARCH model p-values can be reviewed in the model summary. We can also get them directly using "pvalues".

7. **T-statistic**
Another measure from the statistical significance test is t-statistics. It is calculated as the estimated parameter value subtracted by its expected mean value, and then divided by its standard error. Since our null hypothesis assumes the parameter mean value is zero, it is simply the estimated parameter divided by the standard error. The absolute value of the t-statistic is a distance measure, that tells us how many standard errors the estimated parameter is away from 0. The larger the distance, the more likely the parameter is not zero. As a rule of thumb, if the t-statistic is larger than 2, we can reject the null hypothesis. In other words, the parameter is not likely to be zero and should be included in the model.

8. **T-statistic example**
The t-statistic can be viewed in the model fitting summary or directly accessed with "tvalues". It can also be calculated as the parameter values divided by their standard errors.

9. **Let's practice!**
Now it's your turn!

