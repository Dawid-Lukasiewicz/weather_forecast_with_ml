# import ridge regression model
from sklearn.linear_model import Ridge
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

