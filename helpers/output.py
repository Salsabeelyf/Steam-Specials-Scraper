# Export info into output csv file
import pandas as pd
from datetime import datetime

# export games info to csv file
def export_to_csv(games: list, output_file):
    df = pd.DataFrame(games)
    file_name = f'{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}_{output_file}'
    print(f'Exporting to {file_name} .....')
    df.to_csv(f'{file_name}', index=False)