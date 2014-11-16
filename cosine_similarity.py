def vector_length(vector):
    """vector_length({'pennies': 1, 'nickels': 2, 'dimes': 3, 'quarters': 4 })"""
    tot = 0 
    for term, count in vector.items(): 
        tot += count * count 
    return sqrt(tot) 
 
def dot_product(vecA, vecB):
    """dot_product({'pennies': 2, 'nickles', 4}, {'pennies': 1, 'nickles': 2})
        10"""
    tot = 0
    for term in vecA:
        if term in vecB:
            tot += vecA[term] * vecB[term]
    return total
 
def cos_similarity(query, doc):
    """single value between 0 and 1"""
  total = dot_product(query, doc)
  return float(total) / ( vector_length(query) * vector_length(doc) )
