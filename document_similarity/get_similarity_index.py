from collections import Counter
import math
def get_dictionary_of_id_tokens_and_freq(filename):
    """input takes a file and returns a dictionary with unique id as a key and counter token as values
    author: Elizabeth Lee"""
    result_dict ={}
    for line in open(filename):
        line = line.strip()
        id, token_list = line.split("\t", 1)
        token_list = token_list.split("|")
        result_dict[id] = Counter(token_list)
    return result_dict
dict_query = get_dictionary_of_id_tokens_and_freq('queryid_tokensid.txt')
#output has a form of {'1': Counter({'75': 1, '1545': 1, '31': 1}) : '1' is id value and '75' is token and 1 means how many times this token appeared in a line
#'0': Counter({'12731': 1}), '3': Counter({'518': 1, '1996': 1}),
# '2': Counter({'383': 1}), '4': Counter({'4189': 1, '75': 1, '31': 1})}
dict_keyword = get_dictionary_of_id_tokens_and_freq("purchasedkeywordid_tokensid.txt")
dict_title = get_dictionary_of_id_tokens_and_freq("titleid_tokensid.txt")
dict_description = get_dictionary_of_id_tokens_and_freq("descriptionid_tokensid.txt")
    
def get_idf_dictionary(query_dictionary, keyword_dictionary, title_dictionary, descrioption_dictionary):
    """takes 4 dictionaries that has a form of Counter({'4189': 1, '75': 1, '31': 1}) as input 
    and returns a dictionary with a token(word) as a key and idf as a value
    author: Elizabeth Lee"""
    #one idf is needed for each token in all for documents (it can be used for all 4 documents)
    token_set = set()
    token_set.update(query_dictionary.keys())
    token_set.update(keyword_dictionary.keys())
    token_set.update(title_dictionary.keys())
    token_set.update(description_dictionary.keys())
    result_dictionary = {}
    for token in token_set:
        occurence = 0
        occurence += token in query_dictionary
        occurence += token in keyword_dictionary
        occurence += token in title_dictionary
        occurence += token in description_dictionary
        result_dictionary[token] = math.log(float(4)/occurence)
    return result_dictionary
 def tf(dictionary):
     """calculating term frequency for a dictionary and outputs a term and term frequncy within a dictionary
     Elizabeth Lee"""
    diction = {}
    for tok in dictionary.keys():
        tok_num = dictionary[tok]
        tf = tok_num/float(len(dictionary.keys()))
        diction[tok] = tf
    return diction #{'75': 0.3333333333333333, '1545': 0.3333333333333333, '31': 0.3333333333333333}

def doc_similarity(vec1_dic, vec2_dic):
    """ calculates cosine similarity between two documents takes dictionaries as inputs
    and output a single number
    author : Elizabeth Lee"""
    denom = []
    num = []
    for key in vec1_dic.keys() and vec2_dic.keys():
        denom.append(vec1_dic[key]**2)
        denom.append(vec2_dic[key]**2)        
    for key in vec1_dic.keys():
        if key in vec2_dic.keys():
            num.append(vec1_dic[key]*vec2_dic[key])
    return float(sum(num))/float(sum(denom))
            
def cal_doc_similarity(query_id, keyword_id, title_id, description_id):
    """calculate a document similarity between query and keyword,
    query and title, query and description and returns a average of three
    author: Elizabeth Lee"""
    tokens_counts_query = dict_query[query_id] #dict_query[query_id] gives a dictionary of each token and the number of tokens in a query
    tokens_counts_keyword = dict_keyword[keyword_id] #Counter({'75': 1, '1545': 1, '31': 1})
    tokens_counts_title = dict_title[title_id]
    tokens_counts_description = dict_description[description_id]
    tokens_q = token_counts.query.keys() #['75', '1545', '31']
    tokens_k = token_counts.keyword.keys()
    tokens_t = token_counts.title.keys()
    tokens_d = token_counts.description.keys()
    idf = get_idf_dictionary(tokens_counts_query, tokens_counts_keyword, tokens_counts_title, tokens_counts_description)
    tf_q = tf(tokens_counts_query)
    tf_k = tf(tokens_counts_query)
    tf_t = tf(tokens_counts_query)
    tf_d = tf(tokens_counts_query)#{'75': 0.3333333333333333, '1545': 0.3333333333333333, '31': 0.3333333333333333}
    result_dictionary_q ={} # 'token': tf*idf
    result_dictionary_k ={}
    result_dictionary_t ={}
    result_dictionary_d ={}
    for key in idf.keys() and tf_q.keys():
        result_dictionary_q[key] = idf[key]*tf_q[key]
        result_dictionary_k[key] = idf[key]*tf_k[key]
        result_dictionary_t[key] = idf[key]*tf_t[key]
        result_dictionary_d[key] = idf[key]*tfd[key]
        return result_dictionary
    sim_q_k = doc_similarity(result_dictionary_q, result_dictionary_k)
    sim_q_t = doc_similarity(result_dictionary_q, result_dictionary_t)
    sim_q_d = doc_similarity(result_dictionary_q, result_dictionary_d)
    return (sim_q_k + sim_q_t + sim_q_d) / 3


