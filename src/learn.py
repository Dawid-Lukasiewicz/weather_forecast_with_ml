# import ridge regression model
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
# packages to handle data
import pandas as pd
from pathlib import Path, PurePath

# prepare paths to data
base_path = Path.cwd().parent
data_dir_path = base_path.joinpath(PurePath("data", "NCEI-Oakland_International_airport-standard_units"))
data_file_path = data_dir_path.joinpath("prepared_weather.csv")

# load data to variable with DATE column as index
weather_data = pd.read_csv(data_file_path, index_col="DATE")

# set Ridge's parameter
model = Ridge(alpha=0.2)
# list of columns as inputs
predictors = ["PRECIPITATION", "TMAX", "TMIN"]
# set range for training
train = weather_data.loc[:"2021-12-31"]
# set range for tests
test = weather_data.loc["2022-01-01":]

# fit the training data for max temperature
model.fit(train[predictors], train["TARGET_TMAX"])

# get the prediction from model
predictions = model.predict(test[predictors])
# compare predictions to actual values and get the error value
error = mean_absolute_error(test["TARGET_TMAX"], predictions)
print("Mean absolute error between actual and predictions: ", error)