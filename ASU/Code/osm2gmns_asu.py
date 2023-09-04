# Import modules
import osm2gmns as og
import pandas as pd
import grid2demand as gd

# # Download OSM map, if applicable
# # og.downloadOSMData(3444656, 'asu.osm')

# # Produce routable network along with POIs
# net = og.getNetFromFile('asu.osm', 
#                         network_types=('auto','bike','walk'), 
#                         POI=True,
#                         strict_mode=True, 
#                         default_lanes=True, 
#                         default_speed=True, 
#                         default_capacity=True, 
#                         start_node_id=1, 
#                         start_link_id=1)
# default_lanes_dict = {'motorway': 4, 'trunk': 3, 'primary': 3, 'secondary': 2, 'tertiary': 2,
#                       'residential': 1, 'service': 1, 'cycleway':1, 'footway':1, 'track':1,
#                       'unclassified': 1, 'connector': 2}
# default_speed_dict = {'motorway': 120, 'trunk': 100, 'primary': 80, 'secondary': 60, 'tertiary': 40,
#                       'residential': 30, 'service': 30, 'cycleway':5, 'footway':5, 'track':30,
#                       'unclassified': 30, 'connector':120}
# default_capacity_dict = {'motorway': 2300, 'trunk': 2200, 'primary': 1800, 'secondary': 1600, 'tertiary': 1200,
#                       'residential': 1000, 'service': 800, 'cycleway':800, 'footway':800, 'track':800,
#                       'unclassified': 800, 'connector':9999}
# og.outputNetToCSV(net)

# # Modify the allowed_users (modes) in the link file to better-fit EMME's requirement
# df = pd.read_csv('link.csv')
# word_to_letter = {
#     'auto':'a',
#     'walk':'w',
#     'bike':'b'}

# df['allowed_uses'] = df['allowed_uses'].str.replace('|'.join(word_to_letter.keys()), 
#                                                     lambda x: word_to_letter[x.group()], regex=True)
# df['allowed_uses'] = df['allowed_uses'].str.replace(';', '')
# df.to_csv('link.csv', index=False)

# Produce cell grids
net = gd.ReadNetworkFiles(input_folder='C:\\Users\\aditr\\OneDrive\\Desktop\\ASU\\Modeling\\ASU\\Code')
zone = gd.PartitionGrid(number_of_x_blocks=5, number_of_y_blocks=5)

