1. **How to implement GARCH models in Python**
In this lesson, let's learn how to implement GARCH models in Python.

2. **Python "arch" package**
We can implement GARCH models in Python easily with functions predefined in the "arch" package. To import the module, simply state "from arch import arch_model", where arch_model is the function we will use to define GARCH models.

1 Kevin Sheppard. (2019, March 28). bashtage/arch: Release 4.8.1 (Version 4.8.1). Zenodo. http://doi.org/10.5281/zenodo.2613877

3. **Workflow**
There are three steps to develop a GARCH model with the "arch" package. First we specify the model by defining model assumptions. Then we fit the model with data. Last but not least, we use the fitted model to make a forecast. Next up let's learn how to implement each step in Python.

4. **Model specification**
There are mainly three types of assumptions to specify for a GARCH model. The first is the distribution assumption of the residuals, which includes "normal" distribution by default, "t" as Student's t-distribution, "skewt" as skewed Student's t-distribution, and more. The second is the mean model assumption. Specify "constant" mean by default which are common for most of the liquid financial asset returns. Other options include "zero" for zero mean, "AR" for autoregressive mean, and more. Last specify the volatility model to be "GARCH" by default. Other options include "ARCH", "EGARCH", and more. Don't feel overwhelmed by these options. We will discuss them in more details later. Now let's just keep things simple and stick to the default setting. Also we will only fit GARCH(1,1) model, and it is specified by making p equal 1 and q equal 1.

5. **Model fitting**
We can fit the model in a simple line of code with the "fit()" method. Specify "update_freq = n" to display model fitting output after every n iterations. Turn off the display by specifying "disp = 'off'".

6. **Fitted results: parameters**
The GARCH model parameters omega, alpha, beta are estimated using the "maximum likelihood method". It means: the fitting process tries to find parameter values for which the GARCH model is most likely to have generated the observed time series data. We can directly check the parameters by referring to "params" in the fitted model result.

7. **Fitted results: summary**
We can print out the model fitting summary. The results clearly lay out information in sections that correspond to the model assumptions. We can also find the model parameters in the lower left under the "Volatility Model" section.

8. **Fitted results: plots**
We can plot the fitted model results. By default it will show model estimated standardized residuals and conditional volatility. Don't worry about the meaning of "standardized residuals", we will learn more about it in later lessons.

9. **Model forecasting**
Last but not least, we can use "forecast()" to make volatility predictions with the fitted model. Specify "horizon = n" to perform a n-period forecast. We can check the forecast result by "variance". The value in the column "h-dot-1" is the 1-step ahead forecast, while value in "h-dot-5" is the 5-step ahead forecast. The output is aligned so that the "Date" column is the final data used to generate the forecast. That is: h-dot-1 value in row "2019-10-10" is the 1-step ahead forecast made using data up to and including that date.

10. **Let's practice!**
Now it's your turn. Happy practice!

