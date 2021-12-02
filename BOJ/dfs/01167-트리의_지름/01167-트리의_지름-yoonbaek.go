package main

import (
	"bufio"
	. "fmt"
	"os"
	"strconv"
	"strings"
)

var (
	r                    = bufio.NewReader(os.Stdin)
	V, max, farthestNode int
	visited              []int
	graph                [][]node
)

type node struct {
	num  int
	dist int
}

func stringsToNodes(line string) {
	stringSlice := strings.Split(strings.TrimSpace(line), " ")
	nodeNum, _ := strconv.Atoi(stringSlice[0])

	for i := 1; i < len(stringSlice)-1; i += 2 {
		num, _ := strconv.Atoi(stringSlice[i])
		dist, _ := strconv.Atoi(stringSlice[i+1])
		graph[nodeNum] = append(graph[nodeNum], node{num, dist})
	}
}

func initVisited() {
	visited = make([]int, V+1)
}

func dfs(nodeNum, acc int) {
	visited[nodeNum] = 1

	if acc > max {
		max = acc
		farthestNode = nodeNum
	}

	for _, node := range graph[nodeNum] {
		if visited[node.num] == 0 {
			dfs(node.num, acc+node.dist)
			visited[node.num] = 0
		}
	}
}

func main() {
	Fscanln(r, &V)

	graph = make([][]node, V+1)

	for i := 0; i < V; i++ {
		node_info, _ := r.ReadString('\n')
		stringsToNodes(node_info)
	}

	initVisited()
	dfs(1, 0)

	initVisited()
	dfs(farthestNode, 0)

	Println(max)
}

// git commit -m "code: Solve boj 01167 트리의 지름 (yoonbaek)"
