import sys, os, time
import networkx as nx

#### UTILS ####

def order_cycle_graph(g) :
    """
    sort the graph according to the succession of nodes
    """
    first_node = list(g.nodes)[0] #take 1st node
    result = [first_node] # result list
    result.append(list(g[first_node])[0]) # add 1st neigbour
    while len(result) != g.order() : # while we don't have all nodes sorted
        neighbours = list(g[result[-1]]) #get last nodes neighbours
        neighbours.remove(result[-2]) # remove sorted neighbour
        result.append(neighbours[0]) # add last neighbour
    return result

def cycle_dominant(g):
    dominant_set = set()
    ordered_graph = order_cycle_graph(g)
    for i in range(0, len(ordered_graph), 3):
        dominant_set.add(ordered_graph[i])
    return dominant_set



#### Dominant ####

def dominant(g):
    """
        A Faire:         
        - Ecrire une fonction qui retourne le dominant du graphe non dirigé g passé en parametre.
        - cette fonction doit retourner la liste des noeuds d'un petit dominant de g

        :param g: le graphe est donné dans le format networkx : https://networkx.github.io/documentation/stable/reference/classes/graph.html
    """
    paw = False

    all_nodes = set(g)
    neighbours_nb = {} # Dict where the key is the number of neighbours and the item is the node
    for node in all_nodes :
        neighbours_nb[g.degree[node]] = node

    if len(neighbours_nb) == 1 and (g.number_of_nodes() == g.number_of_edges()) : # Cycle graph case
        return cycle_dominant(g)

    else : # greedy algorithm

        max_neighbours = max(neighbours_nb.keys()) #node with the most neighbours
        max_node = neighbours_nb[max_neighbours]        
        dominating_set = {max_node}

        not_selected = all_nodes - {max_node} #nodes not selected for dominant
        all_nodes = all_nodes - set(g[max_node]) - {max_node} #nodes not "dominated"
        g = g.subgraph(not_selected) # graph remaining (without dominant nodes)

        while all_nodes :

            neighbours_nb = {} # same dict as before but this time we don't count nodes "dominated"
            for node in not_selected :
                remaining_reighbours = []
                for node2 in list(g[node]) :
                    if node2 in all_nodes :
                        remaining_reighbours.append(node2)
                neighbours_nb[len(remaining_reighbours)] = node


            if len(neighbours_nb) == 1 and (g.number_of_nodes() == g.number_of_edges()) : # Cycle graph case
                dominating_set |= cycle_dominant(g)
                return dominating_set

            max_neighbours = max(neighbours_nb.keys())
            max_node = neighbours_nb[max_neighbours]
            dominating_set.add(max_node)

            not_selected = not_selected - {max_node}
            all_nodes = all_nodes - set(g[max_node]) - {max_node}
            g = g.subgraph(not_selected)

    return dominating_set

#########################################
#### Ne pas modifier le code suivant ####
#########################################
if __name__=="__main__":
    input_dir = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])
    
    # un repertoire des graphes en entree doit être passé en parametre 1
    if not os.path.isdir(input_dir):
	    print(input_dir, "doesn't exist")
	    exit()

    # un repertoire pour enregistrer les dominants doit être passé en parametre 2
    if not os.path.isdir(output_dir):
	    print(output_dir, "doesn't exist")
	    exit()       
	
    # fichier des reponses depose dans le output_dir et annote par date/heure
    output_filename = 'answers_{}.txt'.format(time.strftime("%d%b%Y_%H%M%S", time.localtime()))             
    output_file = open(os.path.join(output_dir, output_filename), 'w')

    for graph_filename in sorted(os.listdir(input_dir)):
        # importer le graphe
        g = nx.read_adjlist(os.path.join(input_dir, graph_filename))
        
        # calcul du dominant
        D = sorted(dominant(g), key=lambda x: int(x))

        # ajout au rapport
        output_file.write(graph_filename)
        for node in D:
            output_file.write(' {}'.format(node))
        output_file.write('\n')
        
    output_file.close()