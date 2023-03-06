import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

import pandas as pd


class StockReturnForecaster:
    def __init__(self, data):
        self.data = data
        self.regressor = LinearRegression()
        self.features = None
        self.target = None
        self.model = None

    def preprocess_data(self):
        # handling missing values
        self.data.fillna(method='ffill', inplace=True)
        self.data.fillna(method='bfill', inplace=True)

        # scaling
        self.data = (self.data - self.data.mean()) / self.data.std()

    def extract_features(self):
        # calculate returns
        self.data['returns'] = self.data['price'].pct_change()
        self.data.dropna(inplace=True)

        # moving averages
        self.data['ma_5'] = self.data['price'].rolling(window=5).mean()
        self.data['ma_10'] = self.data['price'].rolling(window=10).mean()
        self.data.dropna(inplace=True)

        self.features = self.data[['ma_5', 'ma_10']]
        self.target = self.data['returns']

    def fit_model(self):
        self.regressor.fit(self.features, self.target)

    def predict(self, new_data):
        return self.regressor.predict(new_data)

    def evaluate_model(self, test_features, test_target):
        # calculate R^2 score
        r2_score = self.regressor.score(test_features, test_target)
        print("R^2 Score: ", r2_score)

    def plot_prediction(self, new_data, predicted_values):
        import matplotlib.pyplot as plt
        plt.plot(new_data.index, predicted_values, label='Predicted Returns')
        plt.plot(new_data.index, new_data['returns'], label='True Returns')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    # load data
    data = pd.read_csv("stock_data.csv")

    # create instance of the class
    forecaster = StockReturnForecaster(data)

    # preprocess data
    forecaster.preprocess_data()

    # extract features
    forecaster.extract_features()

    # split data into training and testing sets
    training_features = forecaster.features[:-100]
    training_target = forecaster.target[:-100]
    test_features = forecaster.features[-100:]
    test_target = forecaster.target[-100:]

    # fit model on training data
    forecaster.fit_model()

    # evaluate model on test data
    forecaster.evaluate_model(test_features, test_target)

    # predict returns for next 30 days
    new_data = data[-30:]
    predicted_values = forecaster.predict(new_data[['ma_5', 'ma_10']])

    # plot prediction
    forecaster.plot_prediction(new_data, predicted_values)
