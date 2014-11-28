from collections import Counter
import linecache
import math

def get_counter(mem_file, file_id):
    line = linecache.getline(mem_file, file_id + 1)
    line = line.strip()
    file_id, token_list = line.split("\t")
    token_list = token_list.split("|")
    #maybe do some checking with ids here
    return Counter(token_list)

def get_query_count(query_id):
    c = get_counter(m_query, query_id)
    return sum(c.values())

def get_keyword_count(keyword_id):
    c = get_counter(m_keyword, keyword_id)
    return sum(c.values())

def get_title_count(title_id):
    c = get_counter(m_title, title_id)
    return sum(c.values())

def get_description_count(desc_id):
    c = get_counter(m_description, desc_id)
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
        result_dictionary[token] = math.log(float(4)/occurence)
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
    return float(numerator) / denom

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
    m_query = "querydb"
    m_keyword = "purchasedkeywordid_tokensid.txt"
    m_title = "titleid_tokensid.txt"
    m_description = "descriptionid_tokensid.txt"

    # counter objects of tokens to counts
    tokens_counts_query = get_counter(m_query, query_id) #dict_query[query_id] gives a dictionary of each token and the number of tokens in a query
    tokens_counts_keyword = get_counter(m_keyword, keyword_id)
    tokens_counts_title = get_counter(m_title, title_id)
    tokens_counts_description = get_counter(m_description, description_id)

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

