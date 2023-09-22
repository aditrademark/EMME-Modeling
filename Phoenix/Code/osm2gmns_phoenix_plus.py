import osm2gmns as og
import pandas as pd
import grid2demand as gd
import multiprocessing

# Define a function for parallel processing
def process_data(filename):
    net = og.getNetFromFile(
        filename,
        network_types=('auto'),
        link_types=('motorway', 'trunk'),
        POI=True,
        POI_sampling_ratio=0.001,
        strict_mode=True,
        min_nodes=100,
        default_lanes=True,
        default_speed=True,
        default_capacity=True,
        start_node_id=1,
        start_link_id=1
    )
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

if __name__ == "__main__":
    # Specify the number of CPU cores to use
    num_cores = multiprocessing.cpu_count()
    
    # List of input files (you may need to adapt this)
    input_files = ['phoenix.pbf']
    
    # Create a multiprocessing pool
    pool = multiprocessing.Pool(processes=num_cores)
    
    # Use the pool to process the data in parallel
    pool.map(process_data, input_files)

    # Close the pool to release resources
    pool.close()
    pool.join()
