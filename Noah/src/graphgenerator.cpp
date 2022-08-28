#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

int main() {

  ofstream fout;
  size_t i, j;
  int fromi, toi;
  char from, to;
  int total;
  int counter = 0;
  fout.open("./trafficfiles/example.txt");
  printf("Total number of nodes: ");
  cin >> total;
  fout << total + 3 << endl;

  if (total > 'z' - 'A' + 1) {

    for (i = 0; i < total; i++) {

      fromi =  i;

      if (i != total-1) {
        toi = i +  1;
        fout << fromi << " " << toi << " " << i + 100 << endl;
      }

      if (i != 0) {
        toi = i - 1;
        fout << fromi << " " << toi << " " << 200 + i<< endl;
      }
    }
  } else {

    for (i = 'A'; i < 'A' + total + 1; i++) {

      if (i > 'Z' && counter == 0) {
        i = 'a';
        counter++;
      }

      from =  i;

      if (i != ('A' + total) || i != 'Z') {
        to = i +  1;
        fout << from << " " << to << " " << i + 100 << endl;
      }

      if (i != 'A' && i != 'a') {
        to = i - 1;
        fout << from << " " << to << " " << 200 + i<< endl;
      }

      if (i == 'a') {
        fout << 'Z' << " " << 'a' << " " << 120 << endl;
      }
    }
  }


  return 0;


}
