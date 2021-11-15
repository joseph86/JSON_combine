import json
import glob

# set up list for combined json file data and input glob
combined_list = []
input_files = glob.glob("*.json")

# open all json files in the glob and add them to the combined list
for f in input_files:
  with open(f, "r") as current_file:
    combined_list.append(json.load(current_file))
    
#now print the output just to test
#for i in combined_list:
#    print(i)
#    print('\n')

# write combined json file
with open("combined_json_file.json", "w") as fileout:
    json.dump(combined_list, fileout)
