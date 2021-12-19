// git commit -m "code: Solve boj 11404 플로이드 (yoonbaek)"
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const INF int = 100000*100 + 1

var (
	sc, wr                 = bufio.NewScanner(os.Stdin), bufio.NewWriter(os.Stdout)
	n, m, start, end, cost int
	costs                  [][]int
)

func main() {
	defer wr.Flush()

	sc.Split(bufio.ScanWords)
	n, m = scan(), scan()

	initCosts()

	for i := 0; i < m; i++ {
		start, end, cost = scan()-1, scan()-1, scan()
		if cost < costs[start][end] {
			costs[start][end] = cost
		}
	}

	floydWarshall()

	for i := range costs {
		print(costs[i]...)
	}
}

// utils
func scan() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

//utils
func print(nums ...int) {
	for _, num := range nums {
		if num == INF {
			num = 0
		}
		fmt.Fprintf(wr, "%d ", num)
	}
	fmt.Fprintln(wr)
}

// utils
func initCosts() {
	costs = make([][]int, n)
	for i := range costs {
		costs[i] = make([]int, n)
		for n := range costs[i] {
			if i == n {
				continue
			}
			costs[i][n] = INF
		}
	}
}

func floydWarshall() {
	for middle := range costs {
		for start := range costs {
			for end := range costs {
				transfer := costs[start][middle] + costs[middle][end]
				if costs[start][end] <= transfer {
					continue
				}
				costs[start][end] = transfer
			}
		}
	}
}
