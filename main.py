from etl.etl import *
import logging
logging.basicConfig(filename='logs/record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

if __name__ == '__main__':
    logging.info("extracting data from excel file")
    data = extract(pat)
    logging.info("applying transformations")
    data2 = transform(data)
    logging.info('Loading the data into warehouse')
    load(data2)
