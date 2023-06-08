1. **GARCH model backtesting**
In this lesson, let's see how we can use backtesting as a handy tool to assess model performance, and how to quantify and compare backtesting results.

2. **Backtesting**
Backtesting is a method to assess the quality of a model forecast. We compare the model predicted results with the actual historical data to see how close they are. A satisfactory backtesting result will give us more confidence in the reliability of model predictions.

3. **In-sample vs. out-of-sample**
Typically we can separate all the historical data we have at hand into two parts. The so-called “in-sample” data is used for modeling fitting, and the “out-of-sample” data is reserved for backtesting to evaluate model performance.

4. **MAE**
We can use MAE to measure backtesting results. MAE stands for "Mean Absolute Error". As shown in its equation, it is the average of the absolute errors between predictions and the actual data. Relatively, the smaller the MAE, the better the model performance.

5. **MSE**
Another measure of backtesting results is MSE, which stands for "Mean Squared Error". It is the average squared difference between the estimated values and the actual values. We want to minimize prediction errors. So similar to the MAE, the smaller the MSE, the better the model performance.

6. **Calculate MAE, MSE in Python**
We can easily calculate prediction errors with pre-defined functions in the "sklearn.metrics" package. Call "mean_absolute_error()" to calculate MAE, and "mean_squared_error()" to calculate MSE. Pass the actual data and model predictions as parameters.

7. **Let's practice!**
Now it's your turn. Happy practice!

