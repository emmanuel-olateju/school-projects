import glob 
import os
import pandas as pd
import shutil 

DRY_RUN_SIGNALS_PATH = './dry-run-signals-03-15-2021'
OUTPUT = './output'
DRY_RUN_SIGNALS = glob.glob(f'{DRY_RUN_SIGNALS_PATH}/*.txt')

for txtfile in DRY_RUN_SIGNALS:
    csvfile = pd.read_csv(txtfile)
    csvfile.to_csv(os.path.join(OUTPUT,txtfile.split('\\')[-1].split('.')[0]+'.csv'), index=False)


