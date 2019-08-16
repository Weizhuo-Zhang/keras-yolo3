def generateNewCSV(file_path, output_file_path):
    output_file_path = "test.csv"

    with open(file_path) as input_file:
        output_file = open(output_file_path, 'w')
        title = input_file.readline()
        input_data = input_file.readlines()
        for line in input_data:
            #items = line.strip().replace('[', '').replace(']','').replace('\'','')
            items = line.strip()
#            if '1'==items[-1]:
#                test_file.write("{0}\n".format(items[:-2]))
#            else:
#                train_file.write("{0}\n".format(items[:-2]))
            print(items)
        output_file.close()

label='test'

import pandas as pd
import scipy
from scipy import io

features_struct = scipy.io.loadmat('cars_{0}_annos.mat'.format(label))
features = features_struct['annotations']
features = features.reshape(features.shape[1], features.shape[0])
dfdata = pd.DataFrame(features[:,0])
datapath1 = 'cars_{}.csv'.format(label)
dfdata.to_csv(datapath1, index=False)

output_path = 'cars_{0}_new.csv'.format(label)
generateNewCSV(datapath1, output_path)

