# Import modules
import osm2gmns as og
import pandas as pd
import grid2demand as gd


# # Download OSM map, if applicable
# og.downloadOSMData(3444656, 'asu.osm')


# Produce routable network along with POIs
net = og.getNetFromFile('asu.osm', 
                        network_types=('auto'), 
                        POI=True,
                        strict_mode=True, 
                        min_nodes=10,
                        default_lanes=True, 
                        default_speed=True, 
                        default_capacity=True, 
                        start_node_id=1, 
                        start_link_id=1)
default_lanes_dict = {'motorway': 4, 'trunk': 3, 'primary': 3, 'secondary': 2, 'tertiary': 2,
                      'residential': 1, 'service': 1, 'cycleway':1, 'footway':1, 'track':1,
                      'unclassified': 1, 'connector': 2}
default_speed_dict = {'motorway': 120, 'trunk': 100, 'primary': 80, 'secondary': 60, 'tertiary': 40,
                      'residential': 30, 'service': 30, 'cycleway':5, 'footway':5, 'track':30,
                      'unclassified': 30, 'connector':120}
default_capacity_dict = {'motorway': 2300, 'trunk': 2200, 'primary': 1800, 'secondary': 1600, 'tertiary': 1200,
                      'residential': 1000, 'service': 800, 'cycleway':800, 'footway':800, 'track':800,
                      'unclassified': 800, 'connector':9999}
og.connectPOIWithNet(net)
og.generateNodeActivityInfo(net)
og.outputNetToCSV(net)


# # Produce cell grids
# net = gd.ReadNetworkFiles('')
# zone = gd.PartitionGrid(number_of_x_blocks=5, number_of_y_blocks=5, latitude=30)
# triprate = gd.GetPoiTripRate(trip_rate_folder='',trip_purpose=1)
# nodedemand = gd.GetNodeDemand()
# accessibility = gd.ProduceAccessMatrix(latitude=30, accessibility_folder='')
# demand = gd.RunGravityModel(trip_purpose=1, a=None, b=None, c=None)
# demand = gd.GenerateAgentBasedDemand()


# # Modify the allowed_users (modes) in the link file to better-fit EMME's requirement
# df = pd.read_csv('link.csv')
# df['allowed_uses'] = df['allowed_uses'].str.replace('auto','a')
# df['allowed_uses'] = df['allowed_uses'].str.replace('walk','')
# df['allowed_uses'] = df['allowed_uses'].str.replace('bike','')
# df['allowed_uses'] = df['allowed_uses'].str.replace(';','')
# df = df[df['link_type_name'] != 'connector']
# df.to_csv('link.csv', index=False)


# # Modify to remove POI nodes and add a is_zone column in the node file to better-fit EMME's requirement
# df = pd.read_csv('node.csv')
# df = df[df['activity_type'] != 'poi']
# df['node_type'] = df['node_type'].fillna(df['activity_type'])
# df.drop(columns=['activity_type'], inplace=True)
# df['is_zone'] = df['node_type'].str.contains('centroid')
# df.to_csv('node.csv', index=False)

