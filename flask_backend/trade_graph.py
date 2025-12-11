import json 
import csv
from collections import deque, defaultdict 

class TradeGraph:

    """
    A class to construct a graph of trade networks between different countries in 2024. 

    Attributes
    ----------
    country_data : dict of dict/dict of list/ dict of tuple/etc...

    Methods
    -------
    add_edge (country_a, country_b)
        Constructs an edge between the provided two countries
    
    load_trade_data(data)
        loads trade data from a provided json file

    bfs (start)
        a basic bfs for the graph starting at search
    
    shortest_path (start, end)
        finds the shortest path via trade routes between two countries 
    
    number_of_connections
        sorts countries by number of trade partners

    clusters_on_graph (graph)
        finds all clusters in the graph

    bottleneck_clusters
        finds all bottlenecks and the clusters on each side of them
    """

    

       

    def __init__(self):

        """
        Constructs all the necessary attributes for the TradeGrapj object.

        """

        self.graph = defaultdict(set)
        self.country_data = {}

    
    def add_edge(self, country_a, country_b):
        
        """
        Add an edge between two countries that have a trade relationship
        
        Parameters
        ----------
        country_a, country_b : string
            The countries that have an edge between them 
        """
        if country_a == country_b:
            return
        self.graph[country_a].add(country_b)
        self.graph[country_b].add(country_a)

    def load_trade_data(self, data, valid_codes=None):

        """
        Load in pairs of countries with a trade relationship from the data file
        
        Parameters
        ----------
        data : string
            The country trade data

        """
        for row in data:
            a = str(row.get("reporterCode")).lstrip("0")
            b = str(row.get("partnerCode")).lstrip("0")
        # Filter out if not in valid_codes
            if valid_codes:
                if a not in valid_codes or b not in valid_codes:
                    continue
            if a is None or b is None:
                continue
            self.add_edge(a, b)
    
    def bfs(self, start):
        """
        A basic bfs for the graph
        
        Parameters
        ----------
        start : string
            The starting country

       Returns
        -------
        list
            A list of the countries visited in order by bfs 
       
         """
        if start not in self.graph:
            return None
        visited = set()
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order

    
    def shortest_path(self, start, end):

        """
        Finds the shortest trade path between two countries using bfs 
        
        Parameters
        ----------
        start : string
            The starting country
        end: string
            The ending country

       Returns
        -------
        list
            A list of the countries making up the shortest path between the start and end country
       
         """
        if start not in self.graph or end not in self.graph:
            return None
        if start == end:
            return [start]
        
        visited = set([start])
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            node = path[-1]
            for neighbor in self.graph[node]:
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None
    
    def number_of_connections(self):

        """
        Sorts countries by number of trade partners
        
        Returns
        ----------
        list
            A list of countries sorted by number of trade partners

        """
        return sorted(
            [(c, len(neighbors)) for c, neighbors in self.graph.items()],
            key = lambda x: x[1],
            reverse = True               
        )
    
    def clusters_on_graph(self, graph):
        """
        Provides list of connected components where each component is a list of country nodes 
        
        Returns
        ----------
        list
            A list of connected components

        """
        visited = set()
        all_clusters = []
        for country in list(graph.keys()):
            if country not in visited:
                comp = self.bfs(country)
                for c in comp:
                    visited.add(c)
                all_clusters.append(list(comp))
        return all_clusters
    
    def bottleneck_clusters(self):
        """
        For each bottleneck country, return the clusters of countries formed when the bottleneck is removed.

        Returns
        -------
        list of dicts:
            [{"bottleneck": code, "clusters": [[code1, code2, ...], ...]}, ...]
        """
        result = []
        original_nodes = list(self.graph.keys())
        base_clusters = self.clusters_on_graph(self.graph)
        base_cluster_count = len(base_clusters)
        import copy

        for node in original_nodes:
            temp_graph = copy.deepcopy(self.graph)
            
            if node in temp_graph:
                for n in temp_graph[node]:
                    temp_graph[n].discard(node)
                del temp_graph[node]
            clusters_after = self.clusters_on_graph(temp_graph)
            if len(clusters_after) > base_cluster_count:
                result.append({
                    "bottleneck": node,
                    "clusters": clusters_after
                })
        return result



def load_country_data(data):
    """
        A helper function to load the json file mapping countries to codes
        
        Parameters
        ----------
        data : json file
            json file mapping countries to codes
        
        Returns
        ----------
        dictionary
            country names mapped to codes     
        
        """
    with open(data, 'r') as file:
        mapping = json.load(file)
        return mapping


def get_code_from_name(name, mapping):
        """
        A helper function to get a country's code from its name
        
        Parameters
        ----------
        name : string
            The name of a country
        
        mapping : dictionary
            country names mapped to codes
        
        Returns
        ----------
        string
            the code for the inputted country     
            

        """
        name_lower = name.lower()
        for cn, code in mapping.items():
            if cn.lower() == name_lower:
                return code
        return None


def main():
    countries_codes = load_country_data("country_name_to_code.json")
    
    file_path = input("Enter path to your trade JSON file: ").strip()

    try:
        with open (file_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    
    tg = TradeGraph()
    valid_codes = set(countries_codes.values())
    tg.load_trade_data(data, valid_codes)

    while True:
        print("\nOptions:")
        print("1. Find trade partners of a country")
        print("2. Find shortest path between two countries")
        print("3. Show top countries by number of connections")
        print("4. Show number of clusters")
        print("5. Show bottleneck countries")
        print("6. Quit")
    
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            name = input("Enter country name: ").strip()
            code = get_code_from_name(name, countries_codes)
            if code not in tg.graph:
                print(f"No trade data found for {name}.")
            partners = tg.graph[code]
            if not partners:
                print(f"{name} has no trade partners in the data.")
                continue
            print(f"\nTrade partners of {name}:")
            for p in partners:
                partner_name = next((cn for cn, ccode in countries_codes.items() if ccode == p), p)
                print(f"\n - {partner_name}")
        
        elif choice == "2":
                name1 = input("Enter start country: ").strip()
                name2 = input("Enter end country: ").strip()
                code1 = get_code_from_name(name1, countries_codes)
                code2 = get_code_from_name(name2, countries_codes)
                if code1 is None or code2 is None:
                    print("One or both countries not found.")
                    continue
                path = tg.shortest_path(code1, code2)
                if path is None:
                    print(f"No path found betwen {name1} and {name2}.")
                    return
                print("Shortest trade path:")
                path_names = [next((cn for cn, ccode in countries_codes.items() if ccode == c), c) for c in path]
                print(" -> ".join(f"{n}" for n in zip(path_names, path)))

        elif choice == "3":
                results = tg.number_of_connections()
                print("\nTop countries by number of trade partners:")
                for c, deg in results[:20]:
                    name = next((cn for cn, ccode in countries_codes.items() if ccode == c), c)
                    print(f"{name} ({c}): {deg}")
        
        elif choice == "4":
            clusters = tg.clusters_on_graph(tg.graph)
            print(f"Total number of trade clusters: {len(clusters)}")
            sizes = [len(cluster) for cluster in clusters]
            print("Cluster sizes:", sizes)
        
        elif choice == "5":
            bottlenecks = tg.bottleneck_clusters()
            if not bottlenecks:
                print("No bottleneck countries detected.")
            else:
                print("Bottleneck countries:")
                print(bottlenecks)
        
        elif choice == "6":
            print("Thank you for visiting!")
            break

        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()

        

        