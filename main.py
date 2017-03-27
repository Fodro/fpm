# Copyright 2017 Fodro
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

from func import *  # import functions from func.py

members = list()  # create empty list
infile = 'member_list.json'  # set json file to save
# print some information about program
print("Fodro's projects manager (FPM) version 0.1")
print("Written by Fodro <feodor.tomilov@gmail>")
while True:  # create main cycle
    cmd = input(":")  # setup command line
    if cmd == 'exit':  # setup exit
        break
    elif cmd == 'add':  # add project
        member = create_member()  # call function create_member()
        members.append(member)  # append dictionary "member" to list "members"
        save_by_json(infile, members)  # save list "members" to json file
    elif cmd == 'list':  # print list of projects
        list_members(infile)  # call list_members function
    elif cmd == 'del':  # delete member from file
        del_member(infile, members)
    elif cmd == 'help':
        print("exit - exit program\nadd - add project\nlist - print list of projects")
        print("del - delete project\nhelp - print list of commands")
    else:
        print("Error: command not found. Type help to print list of commands")
