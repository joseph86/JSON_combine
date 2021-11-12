import json
import glob

# set up list of combined json file data and input glob
combined_json = []
input_files = glob.glob("*.json")

for f in input_files:
  with open(f, "rb") as current_file:
    combined_json.append(json.load(current_file))
    
#now print the output just to test
print(combined_json)
