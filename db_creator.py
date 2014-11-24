import time
import bsddb
PATH = '/Users/Alan_Work/Desktop/Stat 157/indecisive-trees/'
def make_db(src_path, dst_path):
	f = open(src_path, 'r')
	db = bsddb.btopen(dst_path, 'c')
	for line in f:
		line = line.strip()
		tokens = line.split('\t')
		db[tokens[0]] = tokens[1]
	db.sync()

make_db(PATH + 'pCTR_Query/query.txt', PATH + 'pCTR_Query/pctr_query.db')
make_db(PATH + 'pCTR_Advertiser/advertiser.txt', PATH + 'pCTR_Advertiser/pctr_advertiser.db')
make_db(PATH + 'pCTR_Ad/ad.txt', PATH + 'pCTR_Ad/pctr_ad.db')

make_db(PATH + 'token_docs/descriptionid_tokensid.txt', PATH + 'token_docs/desc.db')
make_db(PATH + 'token_docs/purchasedkeywordid_tokensid.txt', PATH + 'token_docs/keyword.db')
make_db(PATH + 'token_docs/queryid_tokensid.txt', PATH + 'token_docs/query.db')
make_db(PATH + 'token_docs/titleid_tokensid.txt', PATH + 'token_docs/title.db')
