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


# # Transfer the volume data from demand.csv to EMME's OD matrix
# df = pd.read_csv('demand.csv')
# matrix_data = {}
# for index, row in df.iterrows():
#     origin_zone = row['o_zone_id']
#     destination_zone = row['d_zone_id']
#     volume = row['volume']
#     if origin_zone not in matrix_data:
#         matrix_data[origin_zone] = {}
#     matrix_data[origin_zone][destination_zone] = volume
# matrix_df = pd.DataFrame(matrix_data).fillna(0) 
# matrix_df.to_csv('temp.csv')
# mf1_df = pd.read_csv('mf1.csv', header=None) 
# for index, row in matrix_df.iterrows():
#     origin_zone = index
#     for destination_zone, volume in row.iteritems():
#         mf1_df.at[origin_zone, destination_zone] = volume
# mf1_df.to_csv('mf1.csv', header=False, index=False)  