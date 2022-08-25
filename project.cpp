//Shortest Distance Project
#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <fstream>
#include <stack>

using namespace std;

class Edge {
  public:
    class Node *to;
    class Node *from;
    double weight;
    int road;
};

//node class
class Node {
  public:
    Node();
    bool visited;                    //This is used in the DFS function
    int id;                          //name of node
    multimap <double, Edge*> edges;  //edge list
    list <Edge*> ledges;            //keeps track of edges
    Edge *backlink;                 //shows what comes before the node
    double distance;                //distance that node is from the beginning
    ~Node();                        //destructor
};

Node::Node() {
  backlink = NULL; //set backlinks to null
  visited = false; //set visited to false
  distance = -1;  //sentinilize distance
}

//Destructor
Node::~Node() {

  list <Edge*>::const_iterator lit;

  for (lit = ledges.begin(); lit != ledges.end(); lit++) {
    delete *lit;
  }

}

//graph class
class Graph {
  public:
    map <int, Node *> graph;
    multimap <double, Node*> Dmap;
    vector <Node *> v;
    deque <Node*> path;
    void Dijkstra(Node *start, Node *end);
    void DFS(Node *n);
    ~Graph();

    //list of locations
    map <int, string> locations {

      {2, "Melrose & Volunteer"}, {3, "Lake & Melrose"}, {4, "Cumberland & Volunteer"},
        {5, "Peyton & Volunteer"}, {6, "17 & Cumberland"}, {7, "17 & White"},
        {8, "17 & Clinch"}, {9, "16 & Clinch"}, {10, "Clinch & James"},
        {11, "16 & White"}, {12, "James & White"}, {13, "Cumberland & James"},
        {13, "Cumberland & Phillip"}, {14, "James & Peyton"},
        {15, "Neyland"}, {1, "Hodges"}

    };

    //List of roads
    map <int, string> roads {

      {0, "Melrose Avenue"}, {1, "Melrose Avenue"}, {2, "Volunteer"},
        {3, "Volunteer"}, {4, "Volunteer"}, {5, "Volunteer"},
        {6, "Melrose Avenue"}, {7, "Cumberland Avenue"}, {8, "Cumberland Avenue"},
        {9, "17th Street"}, {10, "17th Street"}, {11, "17th Street"},
        {12, "17th Street"}, {13, "17th Street"}, {14, "17th Street"},
        {15, "Clinch Avenue"}, {16, "Clinch Avenue"}, {17, "Clinch Avenue"},
        {18, "Clinch Avenue"}, {19, "16th Street"}, {20, "16th Street"},
        {21, "James Agee"}, {22, "James Agee"}, {23, "16th Street"},
        {24, "16th Street"}, {25, "White Avenue"}, {26, "James Agee"},
        {27, "James Agee"}, {28, "James Agee"}, {29, "James Agee"},
        {30, "Peyton Manning Pass"}, {31, "Peyton Manning Pass"}, {32, "James Agee"},
        {33, "James Agee"}, {34, "Cumberland Avenue"}, {35, "Cumberland Avenue"},
        {36, "White Avenue"}

    };





};

//Tests if path exists

//RECURSIVE
/*void Graph::DFS(Node *n, Node *end) {

  if (n->visited) return;

  n->visited = true;

  list <Edge*>::const_iterator lit;

  for (lit = n->ledges.begin(); lit != n->ledges.end(); lit++)
  DFS((*lit)->to, end);

  }*/

//Tests if path exists

//ITERATIVE
void Graph::DFS(Node *n) {

  deque <Node *> stack;

  stack.push_back(n);

  while (!stack.empty()) {
    Node *t = stack.front();
    stack.pop_front();

    if (!t->visited) t->visited = true;


    list <Edge*>::const_iterator lit;

    for (lit = t->ledges.begin(); lit != t->ledges.end(); lit++)
      if (!((*lit)->to->visited)) stack.push_front((*lit)->to);

  }

}

//Dijkstra's algorithm
void Graph::Dijkstra(Node *start, Node *end) {
  list <Edge*>::const_iterator lit;
  Dmap.insert(make_pair(0, start));
  start->distance = 0;
  double d;
  Node *n;
  Edge *e;
  double dist;

  while (!Dmap.empty()) {
    n = Dmap.begin()->second;
    dist = Dmap.begin()->first;
    Dmap.erase(Dmap.begin()->first);

    for (lit = n->ledges.begin(); lit != n->ledges.end(); lit++) {
      e = *lit;
      d = e->weight + dist;

      if (e->to->distance == -1 || d < e->to->distance) {
        if (Dmap.find(e->to->distance) != Dmap.end())
          Dmap.erase(e->to->id);

        e->to->distance = d;
        e->to->backlink = e;
        Dmap.insert(make_pair(e->to->distance, e->to));
      }
    }
  }

  n = end;
  while (n != start) {
    if (n == NULL) return;
    path.push_front(n);
    n = n->backlink->from;
  }

  path.push_front(start);

}

//Destructor
Graph::~Graph() {

  size_t i;

  for (i = 0; i < v.size(); i++) {
    delete v[i];
  }


}

int main(int argc, char *argv[]) {

  Graph g;
  map <int, Node*>::const_iterator mit; //iterator
  map <double, Edge*>::const_iterator eit; //iterator
  int total = 0;
  int from, to, start, end;
  double weight;
  int i, minutes, seconds;
  Node *s;
  Node *e;
  ifstream fin;
  char buff[512];
  size_t j;


  if (argc != 2) {
    printf("usage: echo 'start' 'end' | ./bin/project 'edgefile.txt'\n");
    return -1;
  }

  fin.open(argv[1]);

  if (!fin.is_open()) {
    printf("File does not exist\n");
    return 0;
  }

  //get total number of nodes
  fin >> total;

  for (i = 1; i < 1 + total; i++) {

    Node *n = new Node;
    n->id = i;
    g.graph.insert(make_pair(n->id, n));

    //i put it all on a vector so I can delete it more easily
    g.v.push_back(n);
  }

  //read input in format
  for (i = 0; fin >> from >> to >> weight; i++) {
    Node *n1 = g.graph.find(from)->second;
    Node *n2 = g.graph.find(to)->second;
    Edge *e = new Edge;
    e->weight = weight;
    e->from = n1;
    e->to = n2;
    e->road = i;
    n1->edges.insert(make_pair(weight, e));
    n1->ledges.push_back(e);
  }

  fin.close();
  //choose starting and ending node
  cin >> start  >> end;

  s = g.graph.find(start)->second;
  e = g.graph.find(end)->second;

  //tests if path is available
  g.DFS(s);

  //If yes, runs Dijkstra
  if (e->visited) {
    g.Dijkstra(s, e);
  } else {
    printf("There is no path from %s to %s\n", g.locations[s->id].c_str(), g.locations[e->id].c_str());
    return 0;
  }

  //this prints out the path and distance
  printf("Path:\n");

  for (j = 0; j < g.path.size() - 1; j++)
    printf("%s->", g.locations[g.path[j]->id].c_str());

  printf("%s\n", g.locations[g.path[j]->id].c_str());

  printf("\nDirections:\n");

  for (j = 0; j < g.path.size() - 1; j++)
    printf("From %s take %s to get to %s\n", g.locations[g.path[j]->id].c_str(), g.roads[g.path[j+1]->backlink->road].c_str(), g.locations[g.path[j+1]->id].c_str());

  total = e->distance;
  minutes = total/60;
  seconds = total%60;

  sprintf(buff, "%d:%02d", minutes, seconds);
  string time = buff;
  printf("\nTotal Time: %s\n", time.c_str());


  return 0;
}
