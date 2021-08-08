import schedule
import scrap_images
import argparse
import time
import yaml
import sys

def scheduler():
    schedule.every(1).minutes.do(scrap_images.search_and_download, search_term=args['search_item'],\
                  driver_path=args['driver_path'],number_images=args['number_images'])
    while True:
        schedule.run_pending()
        time.sleep(1)
    return


def parse_argument():
    # Argument parser for reading yaml file
    parser = argparse.ArgumentParser(description='Schedule image scrapping')
    # address of the yaml file
    parser.add_argument('--params_file', type=str,
                    help='Parameter file name in yaml format')
    args = parser.parse_args()
    try:
        # to load the contents of the yaml file in dictionary format
        params = yaml.load(open(args.params_file), Loader=yaml.FullLoader)
    except:
        print(f'Error loading parameter file: {args.params_file}.')
        sys.exit(1)
    return params
    

if __name__ == '__main__':
    
    start = time.time()
    args = parse_argument()
    scheduler()
               
    print("Total minutes: {}/{}".format((time.time() - start)/60))