package main

import (
	"bufio"
	. "fmt"
	"os"
)

const MIN = 1000 * 1000

var (
	r          = bufio.NewReader(os.Stdin)
	N, R, G, B int
	costs, dp  [][]int
)

// func backtrack(recur, prev, acc int) {
// 	if recur == N {
// 		if acc < min {
// 			min = acc
// 		}
// 		return
// 	}

// 	if acc >= min {
// 		return
// 	}

// 	for i := 0; i < 3; i++ {
// 		if i != prev {
// 			backtrack(recur+1, i, acc+costs[recur][i])
// 		}
// 	}
// }

func min(numbers ...int) (min_num int) {
	min_num = MIN
	for _, number := range numbers {
		if number < min_num {
			min_num = number
		}
	}
	return
}

func main() {
	Fscan(r, &N)

	for i := 0; i < N; i++ {
		Fscan(r, &R, &G, &B)
		costs = append(costs, []int{R, G, B})
	}

	for i := 0; i < N; i++ {
		dp = append(dp, []int{0, 0, 0})
	}
	dp[0] = costs[0]

	for row := 1; row < N; row++ {
		dp[row][0] = min(dp[row-1][1], dp[row-1][2]) + costs[row][0]
		dp[row][1] = min(dp[row-1][0], dp[row-1][2]) + costs[row][1]
		dp[row][2] = min(dp[row-1][0], dp[row-1][1]) + costs[row][2]
	}
	Println(min(dp[N-1]...))
}

// git commit -m "code: Solve boj 01149 RGB거리 (yoonbaek)"
