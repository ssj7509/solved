# [Gold III] City Skyline - 26998 

[문제 링크](https://www.acmicpc.net/problem/26998) 

### 성능 요약

메모리: 31120 KB, 시간: 52 ms

### 분류

자료 구조, 스택

### 제출 일자

2024년 3월 3일 04:53:49

### 문제 설명

<p>The best part of the day for Farmer John's cows is when the sun sets. They can see the skyline of the distant city. Bessie wonders how many buildings the city has. Write a program that assists the cows in calculating the minimum number of buildings in the city, given a profile of its skyline.</p>

<p>The city in profile is quite dull architecturally, featuring only box-shaped buildings. The skyline of a city on the horizon is somewhere between 1 and W units wide (1 ≤ W ≤ 1,000,000) and described using N (1 ≤ N ≤ 50,000) successive x and y coordinates (1 ≤ x ≤ W, 0 ≤ y ≤ 500,000), defining at what point the skyline changes to a certain height.</p>

<p>An example skyline could be:</p>

<pre>..........................
.....XX.........XXX.......
.XXX.XX.......XXXXXXX.....
XXXXXXXXXX....XXXXXXXXXXXX</pre>

<p>and would be encoded as (1,1), (2,2), (5,1), (6,3), (8,1), (11,0), (15,2), (17,3), (20,2), (22,1).</p>

<p>This skyline requires a minimum of 6 buildings to form; below is one possible set of six buildings whose could create the skyline above:</p>

<pre>.......................... ..........................
.....22.........333....... .....XX.........XXX.......
.111.22.......XX333XX..... .XXX.XX.......5555555.....
X111X22XXX....XX333XXXXXXX 4444444444....5555555XXXXX

..........................
.....XX.........XXX.......
.XXX.XX.......XXXXXXX.....
XXXXXXXXXX....666666666666</pre>

### 입력 

 <ul>
	<li>Line 1: Two space separated integers: N and W</li>
	<li>Lines 2..N+1: Two space separated integers, the x and y coordinate of a point where the skyline changes. The x coordinates are presented in strictly increasing order, and the first x coordinate will always be 1.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: The minimum number of buildings to create the described skyline.</li>
</ul>

