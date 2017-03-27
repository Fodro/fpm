# Copyright 2017 Fodro
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

import json


def create_member():
    """"Create project"""
    name = input("Name? ")  # setup attributes
    time = input("Time? ")
    obj = input("Object? ")
    cash = input("Cash? ")
    member = {  # create dictionary
        'type': '------Project------',
        'name': name,
        'time': time,
        'object': obj,
        'cash': cash

    }
    return member


def save_by_json(infile, member):
    """"Save dictionary from function create_member() to json"""
    member_list = open(infile, mode='w', encoding='utf-8')  # open file in write mode
    json.dump(member, member_list)  # dump list "members"
    member_list.close()  # close file


def list_members(infile):
    """Print list of projects"""
    try:  # except error
        member_list = open(infile, mode='r', encoding='utf-8')  # open file in read mode
        jlist = json.load(member_list)  # load information from json
        for project in jlist:  # create cycle for
            print(str(project['type']))  # print "border" between projects
            print("Name: " + str(project['name']))  # print attributes of project
            print("Time: " + str(project['time']))
            print("Object: " + str(project['object']))
            print("Cash: " + str(project['cash']))
        member_list.close()  # close file
    except FileNotFoundError:  # except FileNotFoundError
        print("Error: file not found")


def del_member(infile, member):
    """Delete project"""
    del_mem = input("Type name of client: ")  # take name of client
    for i in member:  # search project by name of client
        if str(i['name']) == del_mem:
            member.remove(i)
    member_list = open(infile, mode='w', encoding='utf-8')  # rewrite file
    json.dump(member, member_list)
    member_list.close()
