import sys
import json

##def create_makefile(config, project_name, binary_name):

def create_repository(binary_name, project_name, config):
    

def main():
    if len(sys.argv) == 1:
        for line in open("sources/help.txt"):
            print(line)
    elif len(sys.argv) == 3:
        try:
            binary_name = sys.argv[2]
            project_name = sys.argv[1]
            sum = ""
            for line in open("sources/config.json"):
                sum += (line.replace("\n", "")).replace(" ", "")
            config = json.loads(sum)
            print("Configuration loaded successfully")
            create_repository(binary_name, project_name, config)
        except:
            print("Configuration not found")
            print("Configuration should be in 'sources' directory and named 'config.json'")
    else:
        if (4 - len(sys.argv) > 0):
            print("Error:", len(sys.argv), "arguments given but expected 4")
        else:
            print("Error:", len(sys.argv) - 3, "arguments given but expected 4")

main()