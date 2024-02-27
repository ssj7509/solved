#include <stdio.h>
int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		int N, **st = new int*[1000001], *D=new int[1000001], *U = new int[1000001], s = 0, m = 1002, p = 0;
		for (int i = 0; i < 1000001; i++) st[i] = new int[2];
		st[0][0] = 1002, st[0][1] = 1;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%d", D + i);
		for (int i = 0; i < N; i++)
			scanf("%d", U + i);
		D[N] = 1002, U[N] = 1002;
		for (int i = 0; i < N + 1; i++) {
			int d = D[i], u = U[i];
			if (d <= st[p][0] && u > st[p][0]) {
				st[++p][0] = d;
				st[p][1] = 1;
			}
			else {
				int c = 1, x = u > st[p][0];
				int y = x ? d : 1001;
				while (p >= 0) {
					if (y <= st[p][0])
						break;
					int t = st[p][0], l = st[p--][1];
					int h = (d >= m ? m : d) - t;
					s += ((x * (h > 0)) ? h : 0) * l;
					c += l;
				}
				st[++p][0] = d;
				st[p][1] = x ? c : 1;
			}
			int tm = (m >= u ? u : m);
			m = tm <= d ? d : tm;
		}
		printf("%d\n", s);
		delete[] U;
		delete[] D;
		for (int i = 0; i < 1000001; ++i) delete[] st[i];
		delete[] st;
	}
}