def main():
    generateTrainTestSet()

def generateNewClassNameCSV():
    file_path = "class_name.csv"
    output_file_path = "class_name_labels.csv"

    with open(file_path) as input_file:
        output_file = open(output_file_path, 'w')
        input_data = input_file.readlines()
        for line in input_data:
            items = line.strip()
            output_file.write("{0}\n".format(items[:-2]))
        output_file.close()

def generateTrainTestSet():
    file_path = "annotations.csv"
    train_output_file_path = "train.csv"
    test_output_file_path = "test.csv"

    with open(file_path) as input_file:
        train_file = open(train_output_file_path, 'w')
        test_file = open(test_output_file_path, 'w')
        title = input_file.readline()
        input_data = input_file.readlines()
        for line in input_data:
            items = line.strip().replace('[', '').replace(']','').replace('\'','')
            if '1'==items[-1]:
                test_file.write("{0}\n".format(items[:-2]))
            else:
                train_file.write("{0}\n".format(items[:-2]))
#            print(items[:-2])

        train_file.close()
        test_file.close()


if "__main__" == __name__:
    main()
