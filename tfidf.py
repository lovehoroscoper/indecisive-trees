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

