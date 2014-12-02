Statistics 157: Indecisive Trees
================

## Final Project

### Instructions
0. Run PCTR map reduce code to generate the PCTR datasets.

1. Pipe training.txt (or a dataset with identical structure) into instance_sampler.py and pipe out the results into the desired location. You can also tweak the sampling rates via the global variable PERCENTAGE. This step produces the sampled dataset.

2. Set up feature_generator.py by filling in all global variables with the correct path. Persisting dictionaries is memory-intensive, so if you are paging to disk constantly, you likely have insufficient memory to run feature_generator.py. This step produces the raw matrix.

3. This is an optional step, but it is recommended that data_validator.py is run on the output from (2) to ensure that the raw matrix is not corrupted.

4. Shuffle the matrix from (3) (or (2)) using the Unix tool 'shuf'.

5. Run data_transformer.py over the result from (3) (or (2)). This will create the training features, training labels, validation features, and validation labels, as well as normalize all features. All datasets created in this step will be pickled (persisted python objects).

6. Execute model.py in the same directory as the data sets produced in (5). model.py will grid search over hyperparameter C, which can be adjusted for better results. It will then create a model with the best C (assessed by the model with the highest validation auc) and pickle it.

7. To cross validate, repeat steps (4), (5), and (6) and average the results. It is also simple to split the result from (4) into discrete chunks to run crossvalidation on (via the unix tool 'head').

### Results
Best CV AUC: 0.955342265923

Best CV Score: 0.884433622533

### Notes
Output from (2), (3) and (6) can be found online in Alan Kao's S3 directory, under the folder "Final Projects". It is also recommended that the individual file descriptions/code be read for further details.
