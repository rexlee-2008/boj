#include <bits/stdc++.h>
using namespace std;

static const int max_num = 1001;

char mp[max_num][max_num + 1];
int dista[max_num][max_num][2];

struct node { 
    int r, c, b; 
};

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> mp[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            dista[i][j][0] = dista[i][j][1] = -1;
        }
    }

    queue<node> q;
    dista[0][0][0] = 1;
    q.push({0, 0, 0});

    while (!q.empty()) {
        auto cur = q.front(); q.pop();
        int r = cur.r, c = cur.c, b = cur.b;
        int d = dista[r][c][b];

        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];

            if (nr < 0 || nr >= n || nc < 0 || nc >= m) 
                continue;

            if (mp[nr][nc] == '0' && dista[nr][nc][b] == -1) {
                dista[nr][nc][b] = d + 1;
                q.push({nr, nc, b});
            }

            else if (mp[nr][nc] == '1' && b == 0 && dista[nr][nc][1] == -1) {
                dista[nr][nc][1] = d + 1;
                q.push({nr, nc, 1});
            }
        }
    }

    int d0 = dista[n-1][m-1][0];
    int d1 = dista[n-1][m-1][1];
    int ans = -1;
    if (d0 != -1 && d1 != -1) ans = min(d0, d1);
    else if (d0 != -1)       ans = d0;
    else if (d1 != -1)       ans = d1;
    //printf("----------------");
    cout << ans << "\n";
    return 0;
}

/*
7 6
000000
011110
011110
011000
011011
011011
010000

6 4
0000
1110
1000
0000
0111
0000

4 4
0011
0011
1100
1100

4 4
0111
1111
1111
1110

6 4
0100
1110
1000
0000
0111
0000
*/