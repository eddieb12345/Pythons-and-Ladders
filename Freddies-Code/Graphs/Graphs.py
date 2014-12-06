import os.path

def check_file(file_name):                                                                          #Checks if the file exists
    return os.path.exists(file_name)

def check_consistency(file_name):                                                                   #Checks that the graph is square and calculates the number of edges and vertices
    if check_file(file_name) == False:                                                              #Performs the check_file
        print('That file does not exist.')
    else:    
        file = open(file_name,'r')                                                                  #Opens the file
        raw_file_string = file.read()                                                               #Creates a string from the raw file
        global one_way_edges
        one_way_edges = 0                                       
        count = 0
        global file_string                                                                          #Creates a new string to store just the 1s and 0s in
        file_string = ''
        for char in raw_file_string:                                                                #Counts the 1s and 0s
            if char == '1':
                count += 1
                one_way_edges += 1                                                                  #Counts the number of directional edges
                file_string += '1' 
            elif char == '0':  
                count += 1
                file_string += '0'
        global vertices       
        vertices = count**0.5                                                                       #Calculates the number of vertices
        if vertices%1 != 0:                                                                         #Checks if the graph is square
            return False,0
        else:
            vertices = int(vertices)
            return True,vertices

def read_graph(file_name):                                                                          #Converts the file to a list of lists
    check_consistency(file_name)                        
    if check_consistency(file_name)[0] == False:        
            print('The graph is not square.')
    else:
        global graph
        graph = []                                      
        for n in range(vertices):                      
            row = []
            for i in range(n*vertices,(n+1)*vertices):
                row.append(file_string[i])                                                          #Adds each number as a element to the list row
            row[n]='0'                                                                              #Removes any self loops
            graph.append(row)                                                                       #Adds each row to the list graph

def print_adj_matrix():                                                                             #Prints the graph as an adjacency matrix
    for row in graph:
        print(' '.join(row))
        
def digraph_check():                                                                                #Checks if a graph has direction
    digraph = False
    for i in range(vertices):
        for j in range(vertices):
            if graph[i][j] == '1' and graph[j][i] != '1':                                           #If there is an edge (i,j) and there is not an edge (j,i), the graph has direction
                digraph = True
    return digraph

def graph_facts():                                                                                  #Displays information about a graph
    global edges
    edges = int(one_way_edges/2)                                                                    #Calculates the number of directionless edges     
    max_degree = 0
    total_degree = 0
    for row in graph:                                                                               #Calculates the maximum the vertices
        if row.count('1') > max_degree:
            max_degree = row.count('1')
        total_degree += row.count('1')
    avg_degree = total_degree/vertices                                                              #Calculates the average degree of the vertices
    print_adj_matrix()
    print('The graph is directionless.')
    print('The number of vertices is ' + str(vertices))
    print('The number of edges is ' + str(edges))
    print('The maximum degree of any vertex is ' + str(max_degree))
    print('The average degree of the vertices is ' + str(avg_degree))

def digraph_facts():                                                                                #Displays information about a digraph       
    global edges
    edges = one_way_edges                           
    max_degree = 0
    min_degree = vertices
    total_degree = 0
    for row in graph:                                   
        if row.count('1') > max_degree:                                                             #Calculates the maximum degree of the vertices
            max_degree = row.count('1')
        if row.count('1') < min_degree:                                                             #Calculates the minimum degree of the vertices
            min_degree = row.count('1')
        total_degree += row.count('1')
    avg_degree = total_degree/vertices                                                              #Calculates the average degree of the vertices
    print_adj_matrix()
    print('The graph is a digraph.')
    print('The number of vertices is ' + str(vertices))
    print('The number of edges is ' + str(edges))
    print('The maximum degree of any vertex is ' + str(max_degree))
    print('The minimum degree of any vertex is ' + str(min_degree))    
    print('The average degree of the vertices is ' + str(avg_degree))

def convert_digraph_to_graph():                                                                     #Makes a directed graph undirected
    for i in range(vertices):
        for j in range(vertices):                   
            if graph[i][j] == '1':                                                                  #If there is an edge (i,j), there is an edge (j,i)
                graph[j][i] = '1'

def convert():                                                                                      #Shortcut to convert
    convert_digraph_to_graph()

def facts():                                                                                        #Displays relevent information based on the type of graph
    if digraph_check() == True:                                 
        digraph_facts()
    elif digraph_check() == False:
        graph_facts()
    else:
        print('Graph type could not be determined.')

def write_adj_matrix(new_file_name):                                                                #Writes the graph to a file as an adjacency matrix
    file = open('samplegraphs/' + new_file_name + '.txt','a')
    for row in graph:
        file.write(' '.join(row)+ '\n')

def save_to_file(new_file_name):                                                                    #Saves the adjacency matrix in a new file
        if os.path.exists('samplegraphs/' + new_file_name + '.txt'):                                #Checks to see if it exists
            print('A file with that name already exists.')
            overwrite_loop(new_file_name)
        else:
            file = open('samplegraphs/' + new_file_name + '.txt','w')
            write_adj_matrix(new_file_name)                                                         #Writes the graph neatly 

def overwrite_loop(new_file_name):                                                                  #Asks for a y/n input until one is given
        overwrite = input('Would you like to overwrite the file? Y/N: ')
        if overwrite.lower() == 'y' or overwrite.lower() == 'yes':
            file = open('samplegraphs/' + new_file_name + '.txt','w')                               #Overwrites the previous file
            write_adj_matrix(new_file_name)                                                         #Writes the graph neatly                                 
            print('File overwritten.')
        elif overwrite.lower() == 'n' or overwrite.lower() == 'no':
            print('File not created.')
        else:
            print('I\'m sorry, I didn\'t get that. Please try again.')
            overwrite_loop(new_file_name)

def greedy_graph_colouring_1():
    colour_dict = {}
    for vertex in range(len(graph)):               #Each row in the graph is a vertex
        colour_dict[vertex + 1] = 'red'         #Adds the vertices to the dictionary
    for key in colour_dict:
        print('vertex' + str(key) + ':' + colour_dict[key])
                            
def startup():                                                                                      #Starts the program
    file_name = 'samplegraphs/peterson.txt' #'samplegraphs/' + input('Please enter the name of the graph file: ') + '.txt'       #Formats the user input into the file address
    read_graph(file_name)
    facts()
    greedy_graph_colouring_1()

startup()


