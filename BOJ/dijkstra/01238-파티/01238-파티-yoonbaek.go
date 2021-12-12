// git commit -m "code: Solve boj 01238 파티 (yoonbaek)"

package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

const INF = 100*10000 + 1

var (
	sc                     = bufio.NewScanner(os.Stdin)
	N, M, X, start, end, T int
)

//utils
func scan() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

// heap interface
type PriorityQueue []*Edge

func (p PriorityQueue) Len() int { return len(p) }

func (p PriorityQueue) Swap(i, j int) { p[i], p[j] = p[j], p[i] }

func (p PriorityQueue) Less(i, j int) bool { return p[i].T < p[j].T }

func (p *PriorityQueue) Push(i interface{}) { *p = append(*p, i.(*Edge)) }

func (p *PriorityQueue) Pop() interface{} {
	tmp := *p
	pop := tmp[p.Len()-1]
	*p = tmp[0 : p.Len()-1]
	return pop
}

type Edge struct {
	to int
	T  int
}

func dijkstra(start int, graph [][]Edge) []int {
	p := PriorityQueue{}
	heap.Push(&p, &Edge{start, 0})

	visited := make([]bool, N)
	times := make([]int, N)

	for i := 0; i < N; i++ {
		times[i] = INF
	}

	for p.Len() > 0 {
		now := heap.Pop(&p).(*Edge)
		if visited[now.to] {
			continue
		}
		visited[now.to] = true
		for _, next := range graph[now.to] {
			T := now.T + next.T
			if times[next.to] > T {
				times[next.to] = T
				heap.Push(&p, &Edge{next.to, T})
			}
		}
	}
	return times
}

func main() {
	sc.Split(bufio.ScanWords)
	N, M, X = scan(), scan(), scan()-1
	graph, reverse := make([][]Edge, N), make([][]Edge, N)
	for i := 0; i < M; i++ {
		start, end, T = scan()-1, scan()-1, scan()
		graph[start] = append(graph[start], Edge{end, T})
		reverse[end] = append(reverse[end], Edge{start, T})
	}
	toParty := dijkstra(X, graph)
	toHome := dijkstra(X, reverse)

	max := -1
	for start := 0; start < N; start++ {
		if start == X {
			continue
		}
		cur := toParty[start] + toHome[start]
		if cur > max {
			max = cur
		}
	}
	fmt.Println(max)
}
