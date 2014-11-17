#!/usr/bin/env python

'''
Aggregator that takes all pre-computed features and
transforms the input training data into the desired
feature matrix. Intended to be the reducer, but
currently runs locally.

Input: training set
Output: feature matrix

Author: Alan Kao
'''

PCTR_AD_PATH = ''
PCTR_ADVERTISER_PATH = ''
PCTR_QUERY_PATH = ''
PCTR_USER_PATH = ''

NUM_QUERY_PATH =  ''
NUM_TITLE_PATH =  ''
NUM_DESC_PATH =  ''
NUM_KEYWORD_PATH =  ''

USER_DATA_PATH = ''

pCTR_Ad = {}
pCTR_Advertiser = {}
pCTR_Query = {}
pCTR_User = {}

num_query = {}
num_title = {}
num_desc = {}
num_keyword = {}

user_data = {}

def load_dict(path):
	ret = {}
	f = open(path, 'r')
	for line in f:
		line = line.strip()
		tokens = line.split('\t')
		val = 0
		try:
			val = float(tokens[1])
		except ValueError:
			continue
		ret[tokens[0]] = val
	return ret

def load_user_data():
	f = open(USER_DATA_PATH, 'r')
	for line in f:
		line = line.strip()
		tokens = line.split('\t')
		gender = 0
		age = 0
		try:
			gender = float(tokens[1])
			age = float(tokens[2])
		except ValueError:
			continue
		user_data[tokens[0]] = (gender, age)
	return user_data


def preprocess():
	pCTR_Ad = load_dict(PCTR_AD_PATH)
	pCTR_Advertiser = load_dict(PCTR_ADVERTISER_PATH)
	pCTR_Query = load_dict(PCTR_QUERY_PATH)
	pCTR_User = load_dict(PCTR_USER_PATH)

	num_query = load_dict(NUM_QUERY_PATH)
	num_title = load_dict(NUM_TITLE_PATH)
	num_desc = load_dict(NUM_DESC_PATH)
	num_keyword = load_dict(NUM_KEYWORD_PATH)

	load_user_data()

preprocess()

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')

    if (len(fields) != 12):
    	continue
    ad_id = fields[3]
    advertiser_id = fields[4]
    keyword_id = fields[8]
    title_id = fields[9]
    desc_id = fields[10]
    query_id = fields[7]
    user_id = fields[11]

    ctr = 0
    val_user = 0
    val_query = 0
    val_pos = 0
    val_depth = 0
    val_quartile = 0

    try:
    	ctr = float(fields[0]) / float(fields[1])
    	val_user = int(user_id)
    	val_query = int(query_id)
    	val_pos = int(fields[6])
    	val_depth = int[fields[5]]
    	if val_depth != 0:
    		val_quartile = float(val_pos) / val_depth
    except ValueError:
    	continue

    cur_pctr_ad = 0
    cur_pctr_advertiser = 0
    cur_pctr_query = 0
    cur_pctr_user = 0

    try:
    	cur_pctr_ad = pCTR_Ad[ad_id]
    	cur_pctr_advertiser = pCTR_Advertiser[advertiser_id]
    	cur_pctr_query = pCTR_Query[query_id]
    	cur_pctr_user = pCTR_User[user_id]
    except KeyError:
    	continue

    cur_num_query = 0
    cur_num_title = 0
    cur_num_desc = 0
    cur_num_keyword = 0

    try:
    	cur_num_query = num_query[query_id]
    	cur_num_title = num_title[title_id]
    	cur_num_desc = num_desc[desc_id]
    	cur_num_keyword = num_keyword[keyword_id]
    except KeyError:
    	continue

    gender = [0, 0, 0]
    age = [0, 0, 0, 0, 0, 0]

    try:
    	cur_user_data = user_data[user_id]
    	gender[cur_user_data[0]] = 1
    	age[cur_user_data[1]] = 1

    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (ctr, val_user, val_query, val_pos, val_depth, val_quartile, \
    	cur_pctr_ad, cur_pctr_advertiser, cur_pctr_query, cur_pctr_user, cur_num_query, cur_num_title, cur_num_desc, cur_num_keyword \
    	gender[0], gender[1], gender[2], age[0], age[1], age[2], age[3], age[4], age[5])


