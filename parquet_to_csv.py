### script to convert parquet files in model_output directory into CSV

import os
import pandas as pd

cwd = os.getcwd()
model_output_path = os.path.join(cwd, 'model_output', 'state5_None')

for filename in os.listdir(model_output_path):
	if filename.endswith('.parquet'):
		df = pd.read_parquet(os.path.join(model_output_path, filename))
		df.to_csv(os.path.join(model_output_path, filename.replace('parquet', 'csv')))