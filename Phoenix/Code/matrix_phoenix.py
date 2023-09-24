# Import modules
import pandas as pd


# Transfer production and attraction from zone.csv to origin and destination matrix
zone_df = pd.read_csv('zone.csv')
mo1_df = pd.read_csv('mo1.csv')
md1_df = pd.read_csv('md1.csv')
mo1_df['value'] = zone_df['total_production']
md1_df['value'] = zone_df['total_attraction']
mo1_df.to_csv('mo1.csv', index=False)
md1_df.to_csv('md1.csv', index=False)


# Multiply one of them by a factor to equilize production and attraction (EMME's requirement)
mo1_df = pd.read_csv('mo1.csv')
md1_df = pd.read_csv('md1.csv')
sum_mo1 = mo1_df['value'].sum()
sum_md1 = md1_df['value'].sum()
factor = sum_mo1 / sum_md1
md1_df['value'] = md1_df['value'] * factor
md1_df.to_csv('md1.csv', index=False)