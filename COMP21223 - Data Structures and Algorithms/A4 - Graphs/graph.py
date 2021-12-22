"""
The polar expedition graph!
===========================

Contains the graph connecting the vertices (or base stations) on the map.

This is going to be the main file that you are modifying. :)

Usage:
    Contains the graph, requires the connection to vertices and edges.
"""
import math

from vertex import Vertex
from edge import Edge


# Define a "edge already exists" exception
# Don't need to modify me.
class EdgeAlreadyExists(Exception):
    """Raised when edge already exists in the graph"""

    def __init__(self, message):
        super().__init__(message)


class Graph:
    """
    Graph Class
    -----------

    Represents the graph of vertices, which is equivalent to the map of base
    stations for our polar expedition.

    Attributes:
        * vertices (list): The list of vertices
    """

    def __init__(self):
        """
        Initialises an empty graph
        """
        self._vertices = []

    def insert_vertex(self, x_pos, y_pos):
        """
        Insert the vertex storing the y_pos and x_pos

        :param x_pos: The x position of the new vertex.
        :param y_pos: The y position of the new vertex.

        :type x_pos: float
        :type y_pos: float

        :return: The new vertex, also stored in the graph.
        """

        v = Vertex(x_pos, y_pos)
        self._vertices.append(v)
        return v

    def insert_edge(self, u, v):
        """
        Inserts the edge between vertex u and v.

        We're going to assume in this assignment that all vertices given to
        this will already exist in the graph.

        :param u: Vertex U
        :param v: Vertex V

        :type u: Vertex
        :type v: Vertex

        :return: The new edge between U and V.
        """

        e = Edge(u, v)

        # Check that the edge doesn't already exist
        for i in u.edges:
            if i == e:
                # Edge already exists.
                raise EdgeAlreadyExists("Edge already exists between vertex!")

        # Add the edge to both nodes.
        u.add_edge(e)
        v.add_edge(e)

    def remove_vertex(self, v):
        """
        Removes the vertex V from the graph.
        :param v:  The pointer to the vertex to remove
        :type v: Vertex
        """

        # Remove it from the list
        del self._vertices[self._vertices.index(v)]

        # Go through and remove all edges from that node.
        while len(v.edges) != 0:
            e = v.edges.pop()
            u = self.opposite(e, v)
            u.remove_edge(e)

    @staticmethod
    def distance(u, v):
        """
        Get the distance between vertex u and v.

        :param u: A vertex to get the distance between.
        :param v: A vertex to get the distance between.

        :type u: Vertex
        :type v: Vertex
        :return: The Euclidean distance between two vertices.
        """

        # Euclidean Distance
        # sqrt( (x2-x1)^2 + (y2-y1)^2 )

        return math.sqrt(((v.x_pos - u.x_pos) ** 2) + ((v.y_pos - u.y_pos) ** 2))

    @staticmethod
    def opposite(e, v):
        """
        Returns the vertex at the other end of v.
        :param e: The edge to get the other node.
        :param v: Vertex on the edge.
        :return: Vertex at the end of the edge, or None if error.
        """

        # It must be a vertex on the edge.
        if v not in (e.u, e.v):
            return None

        if v == e.u:
            return e.v

        return e.u

    ##############################################
    # Implement the functions below
    ##############################################

    def find_emergency_range(self, v):
        """
        Returns the distance to the vertex W that is furthest from V.
        :param v: The vertex to start at.
        :return: The distance of the vertex W furthest away from V.
        """
        distance_list = []
        for u in self._vertices:
            d = self.distance(v, u)
            distance_list.append(d)
        return max(distance_list)

    def find_path(self, b, s, r):
        """
        Find a path from vertex B to vertex S, such that the distance from B to
        every vertex in the path is within R.  If there is no path between B
        and S within R, then return None.

        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :param r: The maximum range of the radio.
        :return: The LIST of the VERTICES in the path.
        """

        # Generate a list of paths that can be taken to travel from vertex B to vertex S.
        path_list = self.fpath(b, s)
        within = []

        for ls in path_list:  # Iterate through every path
            within_range = True

            for i in range(1, len(ls)):
                # Calculate the distance from vertex B to every other vertex in the path
                d = self.distance(b, ls[i])
                if d > r:  # If the distance is greater than the range R, the path is automatically eliminated
                    within_range = False
                    break

            if within_range:
                within.append(ls)

        # If there is no path between B and S within R, then return None.
        if len(within) == 0:
            return None

        # If there is a path between B and S within R, return any path that satisfies the condition.
        return within[0]

    def minimum_range(self, b, s):
        """
        Returns the minimum range required to go from Vertex B to Vertex S.
        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :return: The minimum range in the path to go from B to S.
        """

        # Generate a list of paths that can be taken to travel from vertex B to vertex S.
        # Calculate the communication range for each path
        # Returns the minimum range required to go from B to S.

        path_list = self.fpath(b, s)
        rangePath_ls = []
        for path in path_list:
            path_range = self.minimumRangeOnePath(path, b)
            rangePath_ls.append(path_range)
        return min(rangePath_ls)

    def minimumRangeOnePath(self, path, b):
        """
        Calculating the distance from vertex B to every other vertex in the given path.
        The communication range required to cover this path would be the maximum distance from B to another vertex.

        Args:
            path: A path starting from Vertex B.
            b: Vertex B to start from.

        Returns: The range required to cover the path starting from B (in terms of radius)

        """
        range_ls = []
        for i in range(len(path)):
            r = self.distance(b, path[i])
            range_ls.append(r)
        return max(range_ls)

    def move_vertex(self, v, new_x, new_y):
        """
        Move the defined vertex.

        If there is already a vertex there, do nothing.

        :param v: The vertex to move
        :param new_x: The new X position
        :param new_y: The new Y position
        """
        # Check if there is already a vertex at the position to be moved
        for u in self._vertices:
            if u.x_pos == new_x and u.y_pos == new_y:
                return

        v.move_vertex(new_x, new_y)

    def neighbors(self, v):
        """
        Returns the neighbour list of a vertex v

        Args:
            v: The vertex to find the adjacent list

        Returns:

        """
        neighbour = []

        for e in v.edges:
            u = self.opposite(e, v)
            neighbour.append(u)
        return neighbour

    def fpath(self, b, s):
        """
        USYD CODE CITATION ACKNOWLEDGEMENT
        I declare the following lines of code have been copied from the website titled:
        "Print all paths from a given source to a destination"
        and partially edited to fit the purpose of the function and it is not my own work.

        Original URL: https://www.geeksforgeeks.org/find-paths-given-source-destination/
        Last access April, 2020

        Args:
            b: Starting vertex
            s: Ending vertex

        Returns: The list of paths from b to s
        """

        visited = {}
        path_ls = []
        path = []

        # Given the assumption that the graph is connected
        for u in self._vertices:
            visited[u] = False
        visited[b] = True

        self.fpath_each(b, s, visited, path, path_ls)
        return path_ls

    def fpath_each(self, u, s, visited, path, path_ls):
        visited[u] = True
        path.append(u)

        # If the current node is the ending node, add the current path to the list
        if u == s:
            p = []
            for n in path:
                p.append(n)
            path_ls.append(p)

        # Else, we call the function recursively on its neighours
        else:
            for node in self.neighbors(u):
                if not visited[node]:
                    self.fpath_each(node, s, visited, path, path_ls)
        path.pop()
        visited[u] = False

        # End of copied code