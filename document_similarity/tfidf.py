#counts how many times a word appeared in document
def freq(token, document):
  return document.count(token)

#counts all the words in input document
def wordCount(document):
  return len(document)

#total number of documents that contain certain word
def num_docs_contain(token,documentList):
  count = 0
  for document in documentList:
    if freq(token,document) > 0:
      count += 1
  return count
#tf
def tf(token, document):
  return (freq(token,document) / float(wordCount(document)))
#idf
def idf(token, documentList):
  return math.log(len(documentList) / num_docs_contain(token,documentList))
#tf*idf
def tfidf(token, document, documentList):
  return (tf(token,document) * idf(token,documentList))

def get_tokens(id_val, filename):
    """ Given (ID, filename), return the list of tokens associated with it"""
    id_token_list = [line.strip() for line in open(filename)]
    id_token = id_token_list[int(id_val)]
    token_list = id_token.split()
    tokenlist = token_list[1].split("|")
    return tokenlist
    
def cal_tf_idf(ad_id):
    instance_list = [line.strip() for line in open("instances.txt")]
    for ins in instance_list:
        if ins.split()[3] == ad_id:
            idlist = ins.split()
    tokens_query = get_tokens(idlist[7], 'queryid_tokensid.txt')
    tokens_keyword = get_tokens(idlist[8], "purchasedkeywordid_tokensid.txt")
    tokens_title = get_tokens(idlist[9], "titleid_tokensid.txt")
    tokens_description = get_tokens(idlist[10], "descriptionid_tokensid.txt")
    alltoken = tokens_query + tokens_keyword + tokens_title + tokens_description
    for query in tokens_query:
        dic = {}
        dic[query]= tfidf(query, tokens_query, alltoken)
        print dic
