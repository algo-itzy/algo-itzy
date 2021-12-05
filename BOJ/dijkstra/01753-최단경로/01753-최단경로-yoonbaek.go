// git commit -m "code: Solve boj 01753 최단경로 (yoonbaek)"
package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

var sc, w = bufio.NewScanner(os.Stdin), bufio.NewWriter(os.Stdout)
var V, E, K, start, end, W, INF int

func scan() int {
	sc.Scan()
	text := sc.Text()
	n, _ := strconv.Atoi(text)
	return n
}

func print(res []int) {
	defer w.Flush()

	for i := 1; i < V+1; i++ {
		if res[i] == INF {
			fmt.Fprintln(w, "INF")
			continue
		}
		fmt.Fprintln(w, res[i])
	}
}

///////////////////////////////code///////////////////////////////////

type Edge struct {
	to   int
	dist int
}

type PriorityQueue []*Edge

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].dist > pq[j].dist
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	edge := x.(*Edge)
	*pq = append(*pq, edge)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	pop := old[n-1]
	*pq = old[0 : n-1]
	return pop
}

func main() {
	sc.Split(bufio.ScanWords)
	V, E, K = scan(), scan(), scan()
	INF = 10*E + 1

	graph := map[int][]Edge{}
	weights := make([]int, V+1)
	for i := 1; i < V+1; i++ {
		weights[i] = INF
	}
	weights[K] = 0

	for i := 0; i < E; i++ {
		start, end, W = scan(), scan(), scan()
		graph[start] = append(graph[start], Edge{end, W})
	}
	dijkstra(Edge{K, 0}, weights, graph)

}

func dijkstra(start Edge, weights []int, graph map[int][]Edge) {
	pq := make(PriorityQueue, 0)
	heap.Init(&pq)
	heap.Push(&pq, &start)
	for pq.Len() > 0 {
		now := heap.Pop(&pq).(*Edge)
		now_node, now_dist := now.to, -now.dist

		for _, next := range graph[now_node] {
			next, next_dist := next.to, next.dist
			next_dist += now_dist
			if weights[next] > next_dist {
				weights[next] = next_dist
				heap.Push(&pq, &Edge{to: next, dist: -next_dist})
			}
		}
	}

	print(weights)
}
