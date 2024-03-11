#include <stdio.h>
int A[1000000], B[1000000];
int main(void) {
	int i, t, N, M, iL[2] = { 0,0 };
	scanf("%d %d", &N, &M);
	for (i = 0; i < N; i++)scanf("%d", &A[i]);
	for (i = 0; i < M; i++)scanf("%d", &B[i]);
	for (i = 0; i < N + M; i++) {
		t = iL[1] < M && (iL[0] == N || A[iL[0]] > B[iL[1]]);
		printf("%d ", (t ? B : A)[iL[t]++]);
	}
}