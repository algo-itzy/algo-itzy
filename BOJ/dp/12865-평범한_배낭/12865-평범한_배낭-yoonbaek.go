// git commit -m "code: Solve boj 12865 평범한 배낭 (yoonbaek)"
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc = bufio.NewScanner(os.Stdin)
)

// utils
func scan() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

// utils
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	sc.Split(bufio.ScanWords)

	n, wLimit := scan(), scan()
	dp := make([]int, wLimit+1)

	for i := 1; i <= n; i++ {
		weight, value := scan(), scan()
		for j := wLimit; j-weight >= 0; j-- {
			dp[j] = max(dp[j], dp[j-weight]+value)
		}
	}
	fmt.Println(dp[wLimit])
}
