# [Gold V] Heavy Rainfall - 30612 

[문제 링크](https://www.acmicpc.net/problem/30612) 

### 성능 요약

메모리: 41008 KB, 시간: 160 ms

### 분류

자료 구조, 구현, 스택

### 제출 일자

2024년 3월 2일 02:01:06

### 문제 설명

<p>You're taking part in the development of a novel simulation system that is developed to help with extreme rain in mountainous areas. There have been many occasions of extreme weather recently, and there is a need to calculate the amount of water that will form between mountaintops in the worst-case scenario. This program will be used by experts to aid in predicting the outcome of future extreme weather events.</p>

<p>The program will accept a list of heights that result from discrete measurements from the corresponding mountain ranges. A lake can only form if it's surrounded by higher mountains, and its maximum height will be the minimum of the two surrounding mountains. If a height of 0 is given, it represents the ground. A lake cannot form if any of its parts would be connected to the ground; it would quickly drain otherwise. For each lake formed, its size is the number of 'discrete blocks' that it occupies between the mountaintops.</p>

### 입력 

 <p>It's easier to understand all of this if we visualize the problem. As an example, consider we're given as input the height values [3, 0, 6, 1, 2, 8, 6, 7, 3, 1, 2]. The mountains formed could be visualized as below:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6b7fd844-df23-4ee1-9d47-5b9ba6fe01b6/-/preview/" style="width: 395px; height: 200px;"></p>

<p>The biggest lakes that can form for this mountain range and their corresponding sizes would be the following:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/96a3c573-1436-487e-99de-c539788e7a62/-/preview/" style="width: 395px; height: 225px;"></p>

<p>None of the lakes could be bigger, since the water would fall off either side. Also, a lake cannot form in the first gap, as it drains to the ground.</p>

<p>The first line of the input file contains a single integer N, 0 ≤ N ≤ 10<sup>5</sup>, and the second a spaceseparated list of N integers that are the heights of the mountains. Each height value H given is within the range [0, 10<sup>5</sup>].</p>

### 출력 

 <p>The output is a single number S (in the range [0, 10<sup>10</sup>]) that is the sum of the maximally sized lakes that can form.</p>

