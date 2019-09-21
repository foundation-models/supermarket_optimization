import numpy as np

COMMA = ','
NEW_LINE = '\n'
THRESHOLD = 3


class RepeatedTransactions:
    """
    Detail description of file is in
    """

    def __init__(self, sigma, input_file='input.dat', output_file='output.dat'):
        self.sigma = sigma
        self.output_file = output_file
        self.map = {}
        with open(input_file, 'r') as file:
            for line in file:
                # assume numbers are separated with space
                splits = line.split()
                if len(splits) > THRESHOLD:
                    transactions = [int(x) for x in splits]
                    # sort it to create a unique list, as the order is irrelevant to find a match
                    # turn sorted list to tuple otherwise it can;t be used as a key in dict
                    sorted_tuple = tuple(np.sort(transactions))
                    self.map[sorted_tuple] = self.map.get(sorted_tuple, 0) + 1
        print("Number of unique transactions with more than 3 items", len(self.map))

    def record_frequent_transactions(self):
        """
        find frequent tuples and write them to a file
        :return:
        """
        with open(self.output_file, 'w') as file:
            for key, value in self.map.items():
                # sigma is a threshold to consider frequent
                if value > self.sigma:
                    # format per line: <item set size (N)>,
                    #          <co-occurrence frequency>,
                    #                 <item 1 id >, <item 2 id>, ?. <item N id>
                    file.write(str(len(key)))
                    file.write(COMMA)
                    file.write(str(value))
                    file.write(COMMA)
                    file.write(COMMA.join(str(x) for x in key))
                    file.write(NEW_LINE)
        print("Result is written to ", self.output_file)


if __name__ == '__main__':
    """
    # Refer to Readme.md
    provide the results obtained for a value of sigma = 4
    """
    repeated_transactions = RepeatedTransactions(sigma=4, input_file='retail_25k.dat')
    repeated_transactions.record_frequent_transactions()
