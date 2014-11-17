from collections import Counter
import math
def get_dictionary_of_id_tokens_and_freq(filename):
    """get a dictionary with id as a key and counter token as values"""
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
    
  def tf(token, document):
    return
    
