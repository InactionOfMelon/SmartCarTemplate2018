#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;

int tot, last = 1, A[23333];
bool flag, g[60][60];

queue <int> Q;

int getint()
{
	char ch = getchar(); int ret = 0;
	while (ch < '0' || '9' < ch) ch = getchar();
	while ('0' <= ch && ch <= '9')
	{
		ret = ret * 10 + ch - '0', ch = getchar();
		if (ch == '\n') flag = 1;
	}
	return ret;
}

bool OK(int q)
{
	return 1 <= q && q <= 55;
}

/*void Print(int l, int r)
{
	int id = A[l];
	printf("g[%d] = Point(%d, %d);", id, A[l + 1], A[l + 2]);
	for (int i = l + 3; i <= r; i++)
		printf("Add_Edgs(%d, %d);", id, A[i], i == r);
}*/

int main()
{
	freopen("map.txt", "r", stdin);
	freopen("data.txt", "w", stdout);
    /*for (;;)
    {
    	A[++tot] = getint();
    	if (A[tot] == -1) {A[tot] = 233; break;}
    	//cout << A[tot] << endl;
    }

    for (int i = 4; i <= tot; i++)
    	if (!OK(A[i]) && OK(A[i - 1]))
    	{
    		Print(last, i - 2);
    		last = i - 1;
    	}
    */

	for (int i = 1; i <= 55; i++)
	{
		while (1)
		{
			int x = getint(); Q.push(x);
			if (flag) {flag = 0; break;}
		}
		Q.pop();
		int x = Q.front(); Q.pop();
		int y = Q.front(); Q.pop();
		//printf("p.append(Point(%d, %d))\n", x, y);
		while (!Q.empty())
		{
			int k = Q.front(); Q.pop();
			g[i][k] = 1;
		}
		//puts("");
	}
	for (int i = 1; i <= 55; i++)
		for (int j = 1; j <= 55; j++)
			if (g[i][j])
				printf("dis[%d][%d] = Length(Vector(p[%d], p[%d]))\n", i, j, i, j);

	return 0;
}