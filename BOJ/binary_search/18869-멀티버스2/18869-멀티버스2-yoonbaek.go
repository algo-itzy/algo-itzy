// git commit -m "code: Solve boj 18869 멀티버스2 (yoonbaek)"

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var (
	m,n int
	multiverse []universe
	sc = bufio.NewScanner(os.Stdin)
)

func init() {
	sc.Split(bufio.ScanWords)
}

func main() {
	m, n = scan(), scan()
	multiverse = make([]universe, m)
	for i := 0; i < m; i++ {
		universe := make(universe, n)
		for j := 0; j < n; j++ {
			universe[j] = planet{j, scan()}
		}
		sort.Sort(universe)
		multiverse[i] = universe
	}
	fmt.Println(criterion())
}

func scan() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

type planet struct {
	index, size int
}

type universe []planet
func (u universe) Len() int           { return len(u) }
func (u universe) Swap(i, j int)      { u[i], u[j] = u[j], u[i] }
func (u universe) Less(i, j int) bool { return u[i].size < u[j].size }

func criterion() int {
	cnt := 0
	for i := 0; i < m; i++ {
		for j := i+1; j < m; j++ {
			match := true
			iPrev, jPrev := -1, -1
			for k := 0; k < n; k++ {
				left := multiverse[i][k]
				right:= multiverse[j][k]
				if left.index != right.index {
					match = false
					break
				}
				if (iPrev == left.size) != (jPrev == right.size) {
					match = false
					break
				}
				iPrev, jPrev = left.size, right.size
			}
			if match {
				cnt++
			}
		}
	}
	return cnt
}