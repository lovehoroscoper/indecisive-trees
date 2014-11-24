import get_similarity_index
import time

start_time = time.time()
query = str(4688625)
keyword = str(202465)
title = str(1172072)
desc = str(973354)
print "result: " + str(get_similarity_index.cal_doc_similarity(query, keyword, title, desc))
print "total time is: " + str(time.time() - start_time)