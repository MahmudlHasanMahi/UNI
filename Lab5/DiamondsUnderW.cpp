#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dfs(vector<vector<char>>& adj, vector<vector<bool>>& visited, int x, int y, int rows, int cols) {
    visited[x][y] = true;
    int count = (adj[x][y] == 'D') ? 1 : 0;

    int dx[] = {1, -1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
            if (adj[nx][ny] != '#' && !visited[nx][ny]) {
                count += dfs(adj, visited, nx, ny, rows, cols);
            }
        }
    }

    return count;
}

int traverse(vector<vector<char>>& adj, int rows, int cols) {
    vector<vector<bool>> visited(rows, vector<bool>(cols, false));
    int maxDiamonds = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (adj[i][j] != '#' && !visited[i][j]) {
                maxDiamonds = max(maxDiamonds, dfs(adj, visited, i, j, rows, cols));
            }
        }
    }

    return maxDiamonds;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c;
    cin >> r >> c;

    vector<vector<char>> adj(r, vector<char>(c));
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cin >> adj[i][j];
        }
    }

    cout << traverse(adj, r, c) << "\n";

    return 0;
}