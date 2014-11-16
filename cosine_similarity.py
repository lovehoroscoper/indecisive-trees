def vector_length(vector): 
    tot = 0 
    for term, count in vector.items(): 
        tot += count * count 
    return sqrt(tot) 
 
def dot_product(vecA, vecB):
    tot = 0
    for term in vecA:
        if term in vecB:
            tot += vecA[term] * vecB[term]
    return total
 
def cos_similarity(query, doc):
  total = dot_product(query, doc)
  return float(total) / ( vector_length(query) * vector_length(doc) )
