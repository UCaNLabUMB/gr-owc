#!/usr/bin/env python3
#Coded by Christopher Onwuchekwa
#Umass Boston, MA,USA

#Patch Notes: Small Edits update with latest Features,

import argparse
import contextlib
import xmlrpc.client
from xmlrpc.client import ServerProxy
import sys
import time

server_list = ['http://' + '10.1.1.2' + ':8080',  'http://' + '10.1.1.3' + ':8080',  'http://' + '10.1.1.4' + ':8080']


def add_server_connection(server_url):
    server_list.append(ServerProxy(server_url))
    print(f"Added server {server_url} to server list.")


def set_fn(file_name, server):
    """Sets the file name on the XML-RPC server"""
    server.set_fn(file_name)
    time.sleep(2)

def remove_server(server_list, server_str):
    """Remove a server from the server_list based on its string representation"""
    for server in server_list:
        if str(server) == server_str:
            server_list.remove(server)
            print(f"Removed server: {server_str}")
            return
    print(f"Server not found: {server_str}")


def set_my_select_1(myselect, server):
    """Sets the carriers in use on the XML-RPC server tx"""
    server.set_my_select_1(myselect)
    # Wait 2 seconds after setting the carriers
    time.sleep(1)

def set_my_select_2(myselect_2, server):
    """Sets the carriers in use on the XML-RPC server rx"""
    server.set_my_select_2(myselect_2)
    # Wait 2 seconds after setting the carriers
    time.sleep(1)
    
def set_filter_lf(filter_lf,server):
    """Sets the  lower filter on the XML-RPC server"""
    server.set_filter_lf(filter_lf)
    time.sleep(1)
    
def set_filter_hf(filter_hf,server):
    """Sets the higer filter on the XML-RPC server"""
    server.set_filter_hf(filter_hf)
    time.sleep(1)                   

def set_f_sig(f_sig, server):
    """Sets the signal in meg on the XML-RPC server"""
    server.set_f_sig(f_sig)
    # Wait 5 seconds after setting the sample rate
    time.sleep(1)
def set_f_sig2(f_sig2, server):
    """Sets the signal in meg on the XML-RPC server"""
    server.set_f_sig(f_sig2)
    # Wait 5 seconds after setting the sample rate
    time.sleep(1)
    
def set_config_param(command, params, servers=None):
    """Sets the given parameter on the XML-RPC servers"""

    # Define the command functions
    
    # Check if the command is 'add_server_connection'
    if command == 'add_server_connection':
        # Call the function without specifying any servers
        command_functions[command](*params)
        return
    
    # Send command to all servers if no server is specified
    if servers is None:
        servers = server_list

    # Send command to the specified servers
    for server_url in servers:
        try:
            # Create an XML-RPC server object from the URL
            server = xmlrpc.client.ServerProxy(server_url)

            # Call the appropriate command function on the server
            if command in command_functions:
                command_functions[command](*params, server)
                print(f"Command '{command}' sent successfully to {server_url}")  
            else:
                raise ValueError(f"Invalid command: {command}")
            

        except ConnectionError as e:
            print(f"Error connecting to the server: {e}")

        except Exception as e:
            print(f"Error: {e}")


command_functions = {
    'set_my_select_1': set_my_select_1, #selection carriers in tx 0 = low 1 = high 2 = mixed
    'set_my_select_2': set_my_select_2, #selection carries in rx. tx 0 = low 1 = high 2 = mixed
    'set_filter_lf': set_filter_lf, # Set Low Filter
    'set_filter_hf': set_filter_hf, # Set High Filter
    'set_f_sig': set_f_sig, #Set F Sig in Meg
    'set_f_sig2': set_f_sig2, #Set F Sig in Meg
    'add_server_connection': add_server_connection, # add a new server connection dont use wip might break stuff again. 
    'set_fn': set_fn, # Set File Name
}

param_types = {
    'set_fn': str,
}
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute commands on XML-RPC servers.')
    parser.add_argument('command', help='Name of the command to run.')
    parser.add_argument('params', nargs='*', help='Parameters for the command (separated by spaces). For Carriers use num in range of 0-n.')
    parser.add_argument('--server', default=None, help="Server index or 'all' to send the command to all servers (default: all)")

    args = parser.parse_args()

    if args.command.lower() in ['exit', 'quit', 'stop']:
        sys.exit(0)

    try:
        # Convert parameters according to the specified types for the given command
        if args.command in param_types:
            param_type = param_types[args.command]
        else:
            param_type = int
        params = [param_type(param) for param in args.params]

        if args.server is None or args.server.lower() == 'all':
            servers = server_list
        else:
            server_indices = [int(index.strip()) for index in args.server.split(',')]
            servers = [server_list[index] for index in server_indices]

        set_config_param(args.command, params, servers)

    except ValueError as e:
        print(f"Error: {e}")
















