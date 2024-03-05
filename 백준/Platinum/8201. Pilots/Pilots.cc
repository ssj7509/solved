#include <stdio.h>
#include <deque>
using namespace std;
struct S {
	int n, i;
};
int main(void) {
	deque<S> d1,d2;
	int N, M,*L,n,t=0,r=0;
	scanf("%d %d", &M, &N);
	L = new int[N];
	for (int i = 0; i < N; i++) {
		scanf("%d",&n);
		while (d1.size()) {
			if (d1.back().n < n) break;
			d1.pop_back();
		}
		while (d2.size()) {
			if (d2.back().n > n) break;
			d2.pop_back();
		}
		d1.push_back({ n,i });
		d2.push_back({ n,i });
		while (d1.size() && d2.size() && d2.front().n - d1.front().n > M) {
			while (d1.size()) {
				if (d1.front().i > t) break;
				d1.pop_front();
			}
			while (d2.size()) {
				if (d2.front().i > t) break;
				d2.pop_front();
			}
			t++;
		}
		r = r > i - t + 1 ? r : i - t + 1;
	}
	printf("%d", r);
	return 0;
}