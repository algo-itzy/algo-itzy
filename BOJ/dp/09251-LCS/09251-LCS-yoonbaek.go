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
)

func scan() string {
	sc.Scan()
	return sc.Text()
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LCS(i, j int, mem [][]int) {
	if first[i] == second[j] {
		mem[i+1][j+1] = mem[i][j] + 1
		return
	}
	mem[i+1][j+1] = max(mem[i][j+1], mem[i+1][j])
}

func main() {
	sc.Split(bufio.ScanLines)

	first, second = scan(), scan()
	F, S := len(first), len(second)
	mem := make([][]int, F+1)
	for row := range mem {
		mem[row] = make([]int, S+1)
	}

	for row := range first {
		for col := range second {
			LCS(row, col, mem)
		}
	}

	fmt.Println(mem[F][S])
}
