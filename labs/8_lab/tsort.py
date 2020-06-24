from sys import setrecursionlimit#, argv
setrecursionlimit(1500)

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    if len(vertices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")
    links = {i:[0, []] for i in sorted(set(vertices), reverse=True)}
    for i in range(len(vertices) - 1, 0, -2):
       links[vertices[i]][0] += 1
       links[vertices[i-1]][1].append(vertices[i])
    output = []
    while len(links) != 0:
        for i in links:
            if links[i][0] == 0:
                outputer(links, output, i)
                break
        else:
            raise ValueError("input contains a cycle")
    return "\n".join(output)
    
def outputer(links, output, i):
    output.append(i)
    for ii in links[i][1]:
        links[ii][0] -= 1
        if links[ii][0] == 0:
            try:
                del links[i]
            except KeyError:
                pass
            outputer(links, output, ii)
    try:
        del links[i]
    except KeyError:
        pass
    return False

#def main():
#    '''Entry point for the tsort utility allowing the user to specify
#       a file containing the edge of the DAG'''
#    if len(argv) != 2:
#        print("Usage: python3 tsort.py <filename>")
#        exit()
#    try:
#        f = open(argv[1], 'r')
#    except FileNotFoundError as e:
#        print(argv[1], 'could not be found or opened')
#        exit()
#    
#    vertices = []
#    for line in f:
#        vertices += line.split()
#       
#    try:
#        result = tsort(vertices)
#        print(result)
#    except Exception as e:
#        print(e)
#    
#if __name__ == '__main__': 
#    main()
