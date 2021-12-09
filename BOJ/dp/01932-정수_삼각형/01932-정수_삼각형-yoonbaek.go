// git commit -m "code: Solve boj 01932 정수 삼각형 (yoonbaek)"

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var dp, graph [][]int
var INF = -1

func scan() (numbers []int) {
	sc.Scan()
	inputs := strings.Split(sc.Text(), " ")
	for _, input := range inputs {
		num, _ := strconv.Atoi(input)
		numbers = append(numbers, num)
	}
	return
}

func max(arr ...int) int {
	max := -1
	for _, elem := range arr {
		if elem > max {
			max = elem
		}
	}
	return max
}

func initDp(ch chan [][]int, N int) {
	dp := [][]int{}
	for i := 0; i < N; i++ {
		row := make([]int, N)
		for j := 0; j < N; j++ {
			row[j] = INF
		}
		dp = append(dp, row)
	}
	ch <- dp
}

func getGraph(ch chan [][]int, N int) {
	graph := [][]int{}
	for i := 0; i < N; i++ {
		graph = append(graph, scan())
	}
	ch <- graph
}

func updateRow(row int) {
	for col, val := range graph[row] {
		right := dp[row-1][col] + val
		if col == 0 {
			dp[row][col] = right
			continue
		}
		left := dp[row-1][col-1] + val
		dp[row][col] = max(left, right)
	}
}

func main() {
	sc.Split(bufio.ScanLines)
	N := scan()[0]

	dpCh, graphCh := make(chan [][]int), make(chan [][]int)

	go initDp(dpCh, N)
	go getGraph(graphCh, N)

	dp, graph = <-dpCh, <-graphCh

	dp[0][0] = graph[0][0]
	for row := 1; row < N; row++ {
		// update dp row
		updateRow(row)
	}

	fmt.Println(max(dp[N-1]...))
}
