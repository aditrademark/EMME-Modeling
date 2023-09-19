import path4gmns as pg
import pandas as pd

# df = pd.read_csv('zone.csv')
# df = df.rename(columns={'activity_zone_id': 'zone_id'})
# df.to_csv('zone.csv', index=False)


network = pg.read_network()
pg.read_zones(network)
pg.load_demand(network)


column_gen_num = 20
column_update_num = 10

# path-based UE only
pg.perform_column_generation(column_gen_num, column_update_num, network)

# if you do not want to include geometry info in the output file,
# use pg.output_columns(network, False)
pg.output_columns(network)
pg.output_link_performance(network)
