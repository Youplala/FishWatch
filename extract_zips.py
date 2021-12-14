import os
import zipfile
import pandas as pd
from datetime import datetime

cwd = os.getcwd()
input = os.path.join(os.getcwd(), 'carriers_data')
extract_path = os.path.join(cwd, 'extracted')
if not os.path.exists(extract_path):
    os.mkdir(extract_path)
for filename in os.listdir(input):
    path = os.path.join(input, filename)
    file = path.replace('.zip', '')
    with zipfile.ZipFile(path, 'r') as zip_ref:
        a = os.path.join(extract_path, filename.replace('.zip', ''))
        zip_ref.extractall(a)

final = pd.DataFrame()
for folder in os.listdir(extract_path):
    folderpath = os.path.join(extract_path, folder)
    for file in os.listdir(folderpath):
        if file.endswith('encounter.zip'):
            path = os.path.join(extract_path, folder, file)
            with zipfile.ZipFile(path, 'r') as zip_ref:
                a = os.path.join(extract_path, folder, file.replace('.zip', ''))
                zip_ref.extractall(a)
            print(f"Unzipping {file} from {folder}")
            csvpath = os.path.join(extract_path, folder, file.replace('.zip', ''), 'data/csv', 'encounter.csv')
            df = pd.read_csv(csvpath)
            df['date'] = datetime.strptime(folder.split('v')[-1], '%Y%m%d')
            final = final.append(df)

final.to_csv('final.csv')