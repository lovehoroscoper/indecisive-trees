#!/usr/bin/env python

from os import sys
from collections import Counter
import math

'''
Feature generator that aggregates/generates features desired
for model training, and outputs model usable training data.

Input: pre-computed feature sets - see *PATH descriptions below
       training - main training data
Output: feature matrix

Author: Alan Kao
'''

PCTR_AD_PATH = 'ad.txt'
PCTR_ADVERTISER_PATH = 'advertiser.txt'
PCTR_QUERY_PATH = 'query.txt'
PCTR_USER_PATH = 'user.txt'

DESC_TOK_PATH = 'descriptionid_tokensid.txt'
QUERY_TOK_PATH = 'queryid_tokensid.txt'
TITLE_TOK_PATH = 'titleid_tokensid.txt'
KEYWORD_TOK_PATH = 'purchasedkeywordid_tokensid.txt'

USER_DATA_PATH = 'userid_profile.txt'
INPUT_PATH = 'training3.txt'
OUTPUT_PATH = 'agg_output2.txt'

def load_pctr(path):
    ret = {}
    f = open(path, 'r')
    for line in f:
        line = line.strip()
        tokens = line.split('\t')
        try:
            key = int(tokens[0])
            val = float(tokens[1])
            ret[key] = val
        except ValueError:
            continue
    return ret

def load_user_data(path):
    user_data = {}
    f = open(path, 'r')
    for line in f:
        line = line.strip()
        tokens = line.split('\t')
        try:
            key = int(tokens[0])
            gender = int(tokens[1])
            age = int(tokens[2])
            user_data[key] = (gender, age)
        except ValueError:
            continue
    return user_data

def load_docs(path):
    ret = {}
    f = open(path, 'r')
    for line in f:
        line = line.strip()
        tokens = line.split('\t')
        try:
            key = int(tokens[0])
            doc_tokens = tokens[1].split('|')
            val = Counter([int(x) for x in doc_tokens])
            ret[key] = val
        except ValueError:
            continue
    return ret

def preprocess():
    global pCTR_Ad
    global pCTR_Advertiser
    global pCTR_Query
    global pCTR_User

    global desc_token
    global keyword_token
    global query_token
    global title_token

    global user_data

    print 'starting pctr ad'
    pCTR_Ad = load_pctr(PCTR_AD_PATH)
    print 'starting pctr advertiser'
    pCTR_Advertiser = load_pctr(PCTR_ADVERTISER_PATH)
    print 'starting pctr query'
    pCTR_Query = load_pctr(PCTR_QUERY_PATH)
    print 'starting pctr user'
    pCTR_User = load_pctr(PCTR_USER_PATH)

    print 'starting desc tokens'
    desc_token = load_docs(DESC_TOK_PATH)
    print 'starting keyword tokens'
    keyword_token = load_docs(KEYWORD_TOK_PATH)
    print 'starting query tokens'
    query_token = load_docs(QUERY_TOK_PATH)
    print 'starting title tokens'
    title_token = load_docs(TITLE_TOK_PATH)

    print 'starting user data'
    user_data = load_user_data(USER_DATA_PATH)

def get_user_data(user_id):
    return user_data[user_id]

def get_query_count(query_id):
    c = query_token[query_id]
    if c == None:
        return 0
    return sum(c.values())

def get_keyword_count(keyword_id):
    c = keyword_token[keyword_id]
    if c == None:
        return 0
    return sum(c.values())

def get_title_count(title_id):
    c = title_token[title_id]
    if c == None:
        return 0
    return sum(c.values())

def get_description_count(desc_id):
    c = desc_token[desc_id]
    if c == None:
        return 0
    return sum(c.values())

def get_idf_dictionary(query_dictionary, keyword_dictionary, title_dictionary, description_dictionary):
    """
    one idf(inverse document frequency) is needed for each token in all for documents (it can be used for all 4 documents)
    input: 4 dictionaries that has a form of Counter({'4189': 1, '75': 1, '31': 1}) 
    output: a dictionary with a token(word) as a key and idf as a value
    author: Elizabeth Lee
    """
    token_set = set()
    token_set.update(query_dictionary.keys())
    token_set.update(keyword_dictionary.keys())
    token_set.update(title_dictionary.keys())
    token_set.update(description_dictionary.keys())
    result_dictionary = {}
    for token in token_set:
        occurence = 0
        occurence += (token in query_dictionary)
        occurence += (token in keyword_dictionary)
        occurence += (token in title_dictionary)
        occurence += (token in description_dictionary)
        result_dictionary[token] = occurence / 4.0 # raw frequency rather than idf
    return result_dictionary

def get_similarity(query_weights, doc_weights):
    numerator = 0
    for token in query_weights:
        if token not in doc_weights:
            continue
        numerator += (query_weights[token] + doc_weights[token])
    q_v = math.sqrt(sum([i ** 2 for i in query_weights.values()]))
    d_v = math.sqrt(sum([i ** 2 for i in doc_weights.values()]))
    denom = q_v * d_v
    try: 
        result =  float(numerator) / denom
        return result
    except ZeroDivisionError:
        return 0

def get_weights(dict_counter, idf_dict):
    count = sum(dict_counter.values())
    result = {}
    for token in dict_counter:
        if token not in idf_dict:
            continue
        result[token] = (dict_counter[token] / float(count)) * idf_dict[token]
    return result

def cal_doc_similarity(query_id, keyword_id, title_id, description_id):
    """
    calculate a document similarity between query and keyword, query and title, query and description 
    input: query_id, keyword_id, title_id, description_id from a line in training.txt
    ouput: average of cosine similarities for each pair
    author: Elizabeth Lee
    """

    # counter objects of tokens to counts
    tokens_counts_query = query_token[query_id] #dict_query[query_id] gives a dictionary of each token and the number of tokens in a query
    tokens_counts_keyword = keyword_token[keyword_id]
    tokens_counts_title = title_token[title_id]
    tokens_counts_description = desc_token[description_id]

    # dictionary of token to idf values
    idf = get_idf_dictionary(tokens_counts_query, tokens_counts_keyword, tokens_counts_title, tokens_counts_description)

    query_weights = get_weights(tokens_counts_query, idf)
    keyword_weights = get_weights(tokens_counts_keyword, idf)
    title_weights = get_weights(tokens_counts_title, idf)
    desc_weights = get_weights(tokens_counts_description, idf)

    sim_q_k = get_similarity(query_weights, keyword_weights)
    sim_q_t = get_similarity(query_weights, title_weights)
    sim_q_d = get_similarity(query_weights, desc_weights)
    result = (sim_q_k + sim_q_t + sim_q_d) / 3.0
    return result

print 'starting preprocess'
preprocess()
print 'preprocess complete'

i = open(INPUT_PATH, 'r')
o = open(OUTPUT_PATH, 'w+')
for line in i:
    line = line.strip()
    fields = line.split('\t')

    if (len(fields) != 13):
        continue

    try:
        label = int(fields[0])
        ad_id = int(fields[4])
        advertiser_id = int(fields[5])
        keyword_id = int(fields[9])
        title_id = int(fields[10])
        desc_id = int(fields[11])
        query_id = int(fields[8])
        user_id = int(fields[12])

        sim = cal_doc_similarity(query_id, keyword_id, title_id, desc_id)
        val_quartile = 0

        ctr = float(fields[1]) / float(fields[2])
        val_pos = int(fields[7])
        val_depth = int(fields[6])
        if val_depth != 0:
            val_quartile = float(val_pos) / val_depth

        cur_pctr_ad = pCTR_Ad[ad_id]
        cur_pctr_advertiser = pCTR_Advertiser[advertiser_id]
        cur_pctr_query = pCTR_Query[query_id]
        cur_pctr_user = pCTR_User[user_id]

        cur_num_query = get_query_count(query_id)
        cur_num_title = get_title_count(title_id)
        cur_num_desc = get_description_count(desc_id)
        cur_num_keyword = get_keyword_count(keyword_id)

        gender = [0, 0, 0]
        age = [0, 0, 0, 0, 0, 0]

        cur_user_data = get_user_data(user_id)
        gender[cur_user_data[0]] = 1
        age[cur_user_data[1] - 1] = 1

        val_string = '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (ctr, user_id, query_id, val_pos, val_depth, val_quartile, sim)
        pctr_string = '%s\t%s\t%s\t%s' % (cur_pctr_ad, cur_pctr_advertiser, cur_pctr_query, cur_pctr_user)
        num_string = '%s\t%s\t%s\t%s' % (cur_num_query, cur_num_title, cur_num_desc, cur_num_keyword)
        gender_string = '%s\t%s\t%s' % (gender[0], gender[1], gender[2])
        age_string = '%s\t%s\t%s\t%s\t%s\t%s' % (age[0], age[1], age[2], age[3], age[4], age[5])
        o.write(str(label) + '\t' + val_string + '\t' + pctr_string + '\t' + num_string + '\t' + gender_string + '\t' + age_string + '\n')
    except ValueError:
        continue
    except KeyError:
        continue
i.close()
o.flush()
o.close()



