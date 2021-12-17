import sys
import json
import os
import os.path
from os import path
from datetime import date

def create_main(project_name, binary_name, config):
    for directory in config:
        for files in config[directory]:
            if files == "main.c":
                file = open(directory + "/" + files, "w+")
                file.write("/* \n")
                file.write("** EPITECH PROJECT, " + str(date.today().year) + "\n")
                file.write("** " + str(project_name) + "\n")
                file.write("** File description:\n")
                file.write("** simple_description\n*/\n\n#include \"" + project_name + ".h\"\n\n")
                file.write("int main(int argc, char **argv)\n{\n    return (0);\n}\n")

def create_include(project_name, binary_name, config):
    h_name = project_name.upper() + "_H_"
    file = open("include/" + project_name + ".h", "w+")
    file.write("/* \n")
    file.write("** EPITECH PROJECT, " + str(date.today().year) + "\n")
    file.write("** " + str(project_name) + "\n")
    file.write("** File description:\n")
    file.write("** simple_description\n*/\n")
    file.write("\n#ifndef\t" + h_name + "\n")
    file.write("\t#define\t" + h_name + "\n\n")
    file.write("#endif\t/* " + h_name + " */\n")
    file.close()

def create_makefile(project_name, binary_name, config):
    file_nbr = 0
    i = 0
    file = open("Makefile", "w+")
    file.write("## \n")
    file.write("## EPITECH PROJECT, " + str(date.today().year) + "\n")
    file.write("## " + str(project_name) + "\n")
    file.write("## File description:\n")
    file.write("## simple_description\n##\n\n")
    file.write("SRC\t=")
    for directory in config:
        i += 1
        if file_nbr == 0 and i + 1 != len(config):
            file.write("\t$(wildcard " + directory + "/*.c)")
            file_nbr += 1
        elif directory != "include" and directory != "." and ("test" in directory) != True and i + 1 != len(config):
            file.write("\t\\\n")
            file.write("\t\t$(wildcard " + directory + "/*.c)\t")
        elif directory != "include" and directory != "." and ("test" in directory) != True and i + 1 == len(config):
            file.write("\t\\\n")
            file.write("\t\t$(wildcard " + directory + "/*.c)")
    file.write(" main.c\n\n")
    file.write("SRCD\t=")
    i = 0
    file_nbr = 0
    for directory in config:
        i += 1
        if file_nbr == 0 and i + 1 <= len(config):
            file.write("\t$(wildcard " + directory + "/*.c)\t\\\n")
            file_nbr += 1
        elif directory != "include" and directory != "." and i + 1 != len(config):
            file.write("\t\t$(wildcard " + directory + "/*.c)\t\\\n")
        elif directory != "include" and directory != "." and i + 1 == len(config):
            file.write("\t\t$(wildcard " + directory + "/*.c)\n")
    file.write("\n")
    file.write("OBJ\t=\t$(SRC:.c=.o)\n\n")
    file.write("CFLAGS\t=\t-I./include/\n\n")
    file.write("NAME\t=\t" + binary_name + "\n\n")
    file.write("all:\t$(NAME)\n\n$(NAME):\t$(OBJ)\n\tgcc -o $(NAME) $(OBJ) $(CFLAGS)\n\n")
    file.write("clean:\n\trm -f $(OBJ)\n\n")
    file.write("fclean:\tclean\n\trm -f $(NAME)\n\nre:\tfclean\tall\n")
    file.write("\nunit_tests:\tfclean\t" + binary_name + "\n\tgcc -o unit_tests $(SRCD) $(CFLAGS) --coverage -lcriterion\n\ntests_run:\tunit_tests\n\t./unit_tests\n")
    file.close()

def create_repository(binary_name, project_name, config):
    already_here = 0
    for directory in config:
        if (directory != "." and path.isdir(directory) == False):
            already_here += 1;
            os.mkdir(str(directory))
        for files in config[directory]:
            paths = str(directory) + "/" + str(files)
            if (".h" in files):
                paths = str(directory) + "/" + str(project_name) + ".h"
            if (path.isfile(paths) == False):
                already_here += 1;
                file = open(paths, "w+")
                if (files != "Makefile" and (".h" in files) != True and files != "main.c"):
                    file.write("/* \n")
                    file.write("** EPITECH PROJECT, " + str(date.today().year) + "\n")
                    file.write("** " + str(project_name) + "\n")
                    file.write("** File description:\n")
                    file.write("** simple_description\n*/\n\n#include \"" + project_name + ".h\"\n")
                file.close()
    if (already_here == 0):
        print("=> Files and folders already here")
    else:
        print("=> Generation finished")
    print("=> Adding Makefile")
    create_makefile(project_name, binary_name, config)
    print("=> Writing include")
    create_include(project_name, binary_name, config)
    print("=> Initializing main")
    create_main(project_name, binary_name, config)

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
        print("=> Configuration loaded successfully")
        create_repository(binary_name, project_name, config)
    else:
        print("=> Error:", len(sys.argv) - 1, "arguments given but expected 2")

main()
