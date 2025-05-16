#include <iostream>
using namespace std;
#include<vector>
#include <queue>
#include <tuple>

int minimum(int n,int x,int y,int fx,int fy){
    vector<vector<bool>> visits(n+1,vector<bool>(n + 1, false));
    int direction[][2] ={{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}};

    if (x == fx and y == fy){
        cout<<0;
        return 0;
    }
    queue<tuple<int, int, int>> q;
    visits[x][y] = true;
    q.push(make_tuple(x,y,0));
    while (!q.empty()) {
        auto [x, y, move] = q.front();
        q.pop();
        for (auto [dx, dy] : direction) {
            int i = x + dx;
            int j = y + dy;
            if (i >= 1 && i <= n && j >= 1 && j <= n && !visits[i][j]) {
                if (i == fx and j == fy){
                    cout<<move+1;
                    return 0;
                }
                visits[i][j] = true;
                q.push(make_tuple(i,j,move+1));

            }
        }
    }
    cout<<-1;



    return 0;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n,x,y,fx,fy;
    cin>>n>>x>>y>>fx>>fy;
    minimum(n,x,y,fx,fy);


    return 0;
}