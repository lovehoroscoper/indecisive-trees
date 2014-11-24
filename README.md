Statistics 157: Indecisive Trees
================

# Final Project

##Folders:
###Complete
* num_Description - contains file with key/value pairs (description id, token count for that description id)
* num_Keyword - contains file with key/value pairs (keyword id, token count for that keyword id)
* num_Query - contains file with key/value pairs (query id, token count for that query id)
* num_Title - contains file with key/value pairs (title id, token count for that title id)
* pCTR_Ad - contains mapper/reducer that generates a file with key/value pairs (ad id, pCTR for that ad id)
* pCTR_Advertiser - contains mapper/reducer that generates a file with key/value pairs (advertiser id, pCTR for that advertiser id)
* pCTR_Query - contains mapper/reducer that generates a file with key/value pairs (query id, pCTR for that query id)
* pCTR_User - contains mapper/reducer that generates a file with key/value pairs (user id, pCTR for that user id)
* token_counter - python script to generate the key value pairs for all the token count datasets (num_*)
* aggregator.py - takes a list of instances and aggregates all the datasets generated above to convert into the preliminary data matrix with the engineered features

###TODO
* conversion script to turn the final data files above into a usable format for LIBLINEAR
* script to compute tf-idf document similarity and their resulting output