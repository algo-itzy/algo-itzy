// git commit -m "code: Solve boj 09251 LCS (yoonbaek)"
package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	sc            = bufio.NewScanner(os.Stdin)
	first, second string
	maxLen        int
)

func scan() string {
	sc.Scan()
	return sc.Text()
}

func max(nums ...int) (max int) {
	for _, num := range nums {
		if max < num {
			max = num
		}
	}
	return
}

func LCS(i, j int, memo []int) {
	if maxLen < memo[j] {
		maxLen = memo[j]
		return
	}
	if first[i] == second[j] {
		memo[j] = maxLen + 1
	}
}

func main() {
	sc.Split(bufio.ScanLines)

	first, second = scan(), scan()
	memo := make([]int, len(second))

	for row := range first {
		maxLen = 0
		for col := range second {
			LCS(row, col, memo)
		}
	}

	fmt.Println(max(memo...))
}
