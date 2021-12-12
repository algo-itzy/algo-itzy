// // git commit -m "code: Solve boj 02206 벽 부수고 이동하기 (yoonbaek)"

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc                = bufio.NewScanner(os.Stdin)
	N, M              int
	arr               [][]int
	broken, notBroken [][]bool
	moves             = []loc{{0, -1}, {0, 1}, {-1, 0}, {1, 0}}
)

func init() { sc.Split(bufio.ScanWords) }

// utils
func scan() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

func scanLine() []int {
	sc.Scan()
	row := make([]int, M)
	for i, b := range sc.Text() {
		row[i] = int(b - 48)
	}
	return row
}

// code
type loc struct{ row, col int }

type hero struct {
	loc
	steps int
	broke bool
}

type Queue chan hero

func (q *Queue) push(h hero) { *q <- h }

func (q *Queue) pop() hero { return <-*q }

func outRange(x, N int) bool { return N <= x || x < 0 }

func bfs(start hero) int {
	q := make(Queue, N*M)
	q.push(start)

	for len(q) > 0 {
		now := q.pop()

		if now.row == N-1 && now.col == M-1 {
			return now.steps
		}

		for _, move := range moves {
			row, col, steps, broke := now.row+move.row, now.col+move.col, now.steps+1, now.broke
			if outRange(row, N) || outRange(col, M) {
				continue
			}
			switch arr[row][col] {
			case 0:
				if !broke && !notBroken[row][col] {
					notBroken[row][col] = true
					q.push(hero{loc{row, col}, steps, broke})
					continue
				}
				if broke && !broken[row][col] {
					broken[row][col] = true
					q.push(hero{loc{row, col}, steps, broke})
				}
			case 1:
				if !broke {
					q.push(hero{loc{row, col}, steps, !broke})
					broken[row][col] = true
				}
			}
		}
	}
	return -1
}

func main() {
	N, M = scan(), scan()
	arr = make([][]int, N)
	for row := 0; row < N; row++ {
		arr[row] = scanLine()
	}
	notBroken = make([][]bool, N)
	broken = make([][]bool, N)
	for i := range notBroken {
		notBroken[i] = make([]bool, M)
		broken[i] = make([]bool, M)
	}
	start := hero{loc{0, 0}, 1, false}
	fmt.Println(bfs(start))
}
