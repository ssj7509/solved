# [Platinum III] Cave - 7872 

[문제 링크](https://www.acmicpc.net/problem/7872) 

### 성능 요약

메모리: 48032 KB, 시간: 2192 ms

### 분류

자료 구조, 덱, 분할 정복, 구현, 세그먼트 트리, 시뮬레이션, 스택

### 제출 일자

2024년 2월 28일 03:02:27

### 문제 설명

<p>As an owner of a land with a cave you were delighted when you last heard that underground fuel tanks are great business. Of course, the more volume one can store, the better. In case of your cave, the effective volume is not easy to calculate, because the cave has a rather sophisticated shape (see figure). Thank heavens it is degenerate in one dimension!</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0a665cf0-74b4-4970-bab6-44fe881fe192/-/preview/" style="width: 456px; height: 227px;"></p>

<p style="text-align: center;">The cave. All ponds that can be flooded with fuel are marked black.</p>

<p>Furthermore, there is some electrical wiring on the ceiling of the cave. You can never be sure if the insulation is intact, so you want to keep the fuel level just below the ceiling at every point. You can pump the fuel to whatever spots in the cave you choose, possibly creating several ponds. Bear in mind though that the fuel is a liquid, so it minimises its gravitational energy, e.g., it will run evenly in every direction on a flat horizontal surface, pour down whenever possible, obey the rule of communicating vessels, etc. As the cave is degenerate and you can make the space between the fuel level and the ceiling arbitrarily small, you actually want to calculate the maximum possible area of ponds that satisfy aforementioned rules.</p>

### 입력 

 <p>The input contains several test cases. The first line of the input contains a positive integer Z ≤ 15, denoting the number of test cases. Then Z test cases follow,.</p>

<p>In the first line of an input instance, there is an integer n (1 ≤ n ≤ 10<sup>6</sup>) denoting the width of the cave. The second line of input consists of n integers p<sub>1</sub>, p<sub>2</sub>, . . . , p<sub>n</sub> and the third line consists of n integers s<sub>1</sub>, s<sub>2</sub>, . . . , s<sub>n</sub>, separated by single spaces. The numbers p<sub>i</sub> and s<sub>i</sub> satisfy 0 ≤ p<sub>i</sub> < s<sub>i</sub> ≤ 1000 and denote the floor and ceiling level at interval [i, i + 1), respectively.</p>

### 출력 

 <p>Your program is to print out one integer: the maximum total area of admissible ponds in the cave.</p>

