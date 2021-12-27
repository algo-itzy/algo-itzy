// git commit -m "code: Solve boj 16236 아기 상어 (yoonbaek)"
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const sharkSize = 10000

var (
	sc                   *bufio.Scanner
	pool, visited, moves [][]int
	n, sec               int
	q                    queue
	s                    shark
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	moves = [][]int{
		{-1, 0}, {0, -1}, {1, 0}, {0, 1},
	}
}

func main() {
	n = scan()
	pool, visited = getPV(n)
	prev := s.meal
	for {
		s = getNearestPrey(s)
		if prev == s.meal {
			break
		}
		prev = s.meal
	}
	fmt.Println(sec)
}

func scan() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

type shark struct {
	row, col, size, meal int
}

type queue chan [2]int

func (q *queue) push(s [2]int) {
	*q <- s
}

func (q *queue) pop() [2]int {
	return <-*q
}

// returns pool info
func getPV(n int) ([][]int, [][]int) {
	pool = make([][]int, n)
	visited = make([][]int, n)
	for row := range pool {
		pool[row] = make([]int, n)
		visited[row] = make([]int, n)
		for col := range pool[row] {
			pool[row][col] = scan()
			if pool[row][col] == 9 {
				s = shark{row, col, 2, 0}
			}
		}
	}
	return pool, visited
}

func getNearestPrey(s shark) (next shark) {
	next = s
	q = make(queue, n*n)
	pool[s.row][s.col] = sharkSize
	q.push([2]int{s.row, s.col})
	distLimit, rowLimit, colLimit := n*n, n, n
	history := [][2]int{}

	for len(q) > 0 {
		now := q.pop()

		for _, move := range moves {
			row, col := now[0]+move[0], now[1]+move[1]
			if outOfRange(row, col) || isVisited(row, col) || isBigger(row, col, s) {
				continue
			}
			visited[row][col] = visited[now[0]][now[1]] + 1
			history = append(history, [2]int{row, col})

			if cur := visited[row][col]; cur <= distLimit {
				if isPrey(row, col, s.size) {
					if cur < distLimit {
						distLimit, rowLimit, colLimit = cur, row, col
						continue
					}
					if row <= rowLimit {
						if row < rowLimit {
							rowLimit, colLimit = row, col
							continue
						}
						if col < colLimit {
							colLimit = col
						}
					}
				}
				q.push([2]int{row, col})
			}
		}
	}
	defer restoreVisited(history)
	pool[s.row][s.col] = 0
	if rowLimit == n {
		return
	}
	next.row = rowLimit
	next.col = colLimit
	next.meal++
	if next.meal == next.size {
		next.size++
		next.meal = 0
	}
	sec += visited[next.row][next.col]
	return
}

func outOfRange(row, col int) bool {
	return row >= n || row < 0 || col >= n || col < 0
}

func isVisited(row, col int) bool {
	return visited[row][col] > 0
}

func isPrey(row, col, size int) bool {
	fish := pool[row][col]
	return fish < size && fish > 0
}

func isBigger(row, col int, s shark) bool {
	return pool[row][col] > s.size
}

func restoreVisited(path [][2]int) {
	for _, loc := range path {
		visited[loc[0]][loc[1]] = 0
	}
}
