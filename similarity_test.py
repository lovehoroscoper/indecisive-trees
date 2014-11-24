import get_similarity_index

query = str(4688625)
keyword = str(202465)
title = str(1172072)
desc = str(973354)
print str(get_similarity_index.cal_doc_similarity(query, keyword, title, desc))
