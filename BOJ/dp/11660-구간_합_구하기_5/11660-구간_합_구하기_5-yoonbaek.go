// git commit -m "code: Solve boj 11660 구간 합 구하기 5 (yoonbaek)"
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc                   = bufio.NewScanner(os.Stdin)
	wr                   = bufio.NewWriter(os.Stdout)
	n, m, x1, x2, y1, y2 int
	acc                  [][]int
)

// utils
func scan() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

func main() {
	defer wr.Flush()

	sc.Split(bufio.ScanWords)

	n, m = scan(), scan()
	solve(n, m)
}

// utils
func getAcc(n int) [][]int {
	acc := make([][]int, n)
	total := 0
	for row := range acc {
		acc[row] = make([]int, n)
		for col := range acc {
			val := scan()
			total += val
			acc[row][col] = total
		}
	}
	return acc
}

// 2524ms
func solveFirst(n, m int) {
	acc = getAcc(n)

	for i := 0; i < m; i++ {
		x1, y1, x2, y2 = scan()-1, scan()-1, scan()-1, scan()-1
		total := 0
		for row := x1; row <= x2; row++ {
			total += acc[row][y2]
			if y1 == 0 {
				if row == 0 {
					continue
				}
				total -= acc[row-1][n-1]
				continue
			}
			total -= acc[row][y1-1]
		}
		fmt.Fprintln(wr, total)
	}
}

func getSquareAcc(n int) [][]int {
	acc := make([][]int, n)
	for row := range acc {
		acc[row] = make([]int, n)
		for col := range acc {
			var left, up, start int
			if col > 0 {
				left = acc[row][col-1]
			}
			if row > 0 {
				up = acc[row-1][col]
			}
			if row > 0 && col > 0 {
				start = acc[row-1][col-1]
			}
			acc[row][col] = scan() + left + up - start
		}
	}
	return acc
}

// 176ms
func solve(n, m int) {
	acc = getSquareAcc(n)

	for ; m > 0; m-- {
		x1, y1, x2, y2 = scan()-1, scan()-1, scan()-1, scan()-1
		var left, up, start int
		if y1 > 0 {
			left = acc[x2][y1-1]
		}
		if x1 > 0 {
			up = acc[x1-1][y2]
		}
		if y1 > 0 && x1 > 0 {
			start = acc[x1-1][y1-1]
		}
		fmt.Fprintln(wr, acc[x2][y2]-left-up+start)
	}
}
