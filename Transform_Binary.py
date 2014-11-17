'''
Author: Alan Kao

Transforms the input instance randomly into a positive or negative
instance based on the ctr rate. This is necessary for the binary
classification model used.

Input: feature matrix [num_samples, num_features] with ctr at column 0
Output: new feature matrix [num_samples, num_features + 1] with binary
        class at column 0
'''

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    ctr = 0
    try:
        ctr = float(fields[0])
    except ValueError:
        continue
    r = random.random()
    if r < ctr:
        print '1\t' + line
    else:
        print '0\t' + line