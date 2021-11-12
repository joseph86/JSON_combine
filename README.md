# JSON_combine
created by Joseph Parish
TLDR: Combine JSON files in a single JSON file. 

All this does at this point is create a single list of JSON objects where each object is one of the JSON files combined. This means that if you have multiple JSON files, each containing a list of objects, the result will be a list of lists. This is fine for my purposes. Others have handled the situation of combining lists in different JSON files into a single list in a single JSON file using list.extend" rather than list.append. 

If I ever encounter a need to do more complex combining of JSON files, I'll come back and modify this.
