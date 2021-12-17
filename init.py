import sys
import json
import os
import os.path
from os import path
from datetime import date

def create_makefile(project_name, binary_name):
    file = open("Makefile", "w+")
    file.close()

def create_repository(binary_name, project_name, config):
    already_here = 0
    for directory in config:
        if (directory != "." and path.isdir(directory) == False):
            already_here += 1;
            os.mkdir(str(directory))
        for files in config[directory]:
            paths = str(directory) + "/" + str(files)
            if (path.isfile(paths) == False):
                already_here += 1
                if (".h" in files):
                    paths = str(directory) + "/" + str(project_name) + ".h"
                file = open(paths, "w+")
                if (files != "Makefile"):
                    file.write("/* \n")
                    file.write("** EPITECH PROJECT, " + str(date.today().year) + "\n")
                    file.write("** " + str(project_name) + "\n")
                    file.write("** File description:\n")
                    file.write("** simple_description\n*/\n\ninclude \"" + project_name + ".h\"\n")
                file.close()
    if (already_here == 0):
        print("Files and folders already here")
    else:
        print("Generation finished")
    print("Adding Makefile")
    create_makefile(project_name, binary_name)

def main():
    if len(sys.argv) == 1:
        path = os.path.expanduser('~')
        for line in open(path + "/init_scripts/sources/help.txt"):
            print(line)
    elif len(sys.argv) == 3:
        binary_name = sys.argv[2]
        project_name = sys.argv[1]
        sum = ""
        path = os.path.expanduser('~')
        for line in open(path + "/init_scripts/sources/config.json"):
            sum += (line.replace("\n", "")).replace(" ", "")
        config = json.loads(sum)
        print("Configuration loaded successfully")
        create_repository(binary_name, project_name, config)
    else:
        print("Error:", len(sys.argv), "arguments given but expected 3")

main()
