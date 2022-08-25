//Shortest Distance Project
#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <fstream>

using namespace std;

class Edge {
  public:
    class Node *to;
    class Node *from;
    double weight;
};

//node class
class Node {
  public:
    Node();
    bool visited;
    char id;                         //name of node
    multimap <double, Edge*> edges;  //edge list
    list <Edge*> ledges;
    Edge *backlink;
    double distance;
    ~Node();
};

Node::Node() {
  backlink = NULL; //set backlinks to null
  visited = false; //set visited to false
  distance = -1;
}

Node::~Node() {

  list <Edge*>::const_iterator lit;

  for (lit = ledges.begin(); lit != ledges.end(); lit++) {
    delete *lit;
  }

}

//graph class
class Graph {
  public:
    map <char, Node *> graph;
    multimap <double, Node*> Dmap;
    vector <Node *> v;
    deque <Node*> path;
    void Dijkstra(Node *start, Node *end);
    void DFS(Node *n, Node *end);
    ~Graph();                  //destructor to delete all nodes
};

//Tests if path exists
void Graph::DFS(Node *n, Node *end) {

  if (n->visited) return;

  n->visited = true;

  list <Edge*>::const_iterator lit;

  for (lit = n->ledges.begin(); lit != n->ledges.end(); lit++) {
    DFS((*lit)->to, end);
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

Graph::~Graph() {

  size_t i;

  for (i = 0; i < v.size(); i++) {
    delete v[i];
  }


}

int main(int argc, char *argv[]) {

  Graph g;
  map <char, Node*>::const_iterator mit;
  map <double, Edge*>::const_iterator eit;
  int total = 0;
  char from, to, start, end;
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

  //get total number of nodes
  fin >> total;

  for (i = 'A'; i < total + 'A'; i++) {

    Node *n = new Node;
    n->id = i;
    g.graph.insert(make_pair(n->id, n));
    //i put it all on a vector so I can delete it easierly
    g.v.push_back(n);
  }

  //read input in format
  while (fin >> from >> to >> weight) {
    Node *n1 = g.graph.find(from)->second;
    Node *n2 = g.graph.find(to)->second;
    Edge *e = new Edge;
    e->weight = weight;
    e->from = n1;
    e->to = n2;
    n1->edges.insert(make_pair(weight, e));
    n1->ledges.push_back(e);

  }

  //choose starting and ending node
  cin >> start  >> end;

  s = g.graph.find(start)->second;
  e = g.graph.find(end)->second;

  //tests if path is available
  g.DFS(s, e);

  //If yes, runs Dijkstra
  if (e->visited) {
    g.Dijkstra(s, e);
  } else {
    printf("There is no path from %c to %c\n", s->id, e->id);
    return 0;
  }

  //this prints out the path and distance
  printf("Path: ");


  for (j = 0; j < g.path.size() - 1; j++) 
    printf("%c->", g.path[j]->id);

  printf("%c\n", g.path[j]->id);

  total = e->distance;
  minutes = total/60;
  seconds = total%60;

  sprintf(buff, "%d:%02d", minutes, seconds);
  string time = buff;
  printf("Total Time: %s\n", time.c_str());


  return 0;
}
