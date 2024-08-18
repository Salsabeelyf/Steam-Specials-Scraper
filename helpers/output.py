# Export info into output csv file
import pandas as pd

# export games info to csv file
def export_to_csv(games: list, output_file):
    df = pd.DataFrame(games)
    print(f'Exporting to {output_file} .....')
    df.to_csv(output_file, index=False)