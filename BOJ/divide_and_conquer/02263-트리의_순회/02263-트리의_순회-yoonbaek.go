// git commit -m "code: Solve boj 02263 트리의 순회 (yoonbaek)"
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc, wr             = bufio.NewScanner(os.Stdin), bufio.NewWriter(os.Stdout)
	inOrder, postOrder []int
	memo               map[int]int
)

// utils
func scan() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

// utils
func printf(format string, i ...interface{}) {
	fmt.Fprintf(wr, format, i...)
}

// input
func getTree(N int) []int {
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = scan()
	}
	return arr
}

func toPreOrder(inStart, inEnd, postStart, postEnd int) {
	/*
		알아야 될 것.
		1. 중위트리의 루트노드의 인덱스,
		2. 후위트리의 왼쪽트리 크기
	*/
	if inStart > inEnd || postStart > postEnd {
		return
	}
	curRoot := postOrder[postEnd]
	printf("%d ", curRoot)
	inOrderRoot := memo[curRoot]      // 1
	leftSize := inOrderRoot - inStart // 2
	toPreOrder(inStart, inOrderRoot-1, postStart, postStart+leftSize-1)
	toPreOrder(inOrderRoot+1, inEnd, postStart+leftSize, postEnd-1)
}

// main
func main() {
	defer fmt.Println()
	defer wr.Flush()

	sc.Split(bufio.ScanWords)
	N := scan()

	inOrder = getTree(N)
	postOrder = getTree(N)

	memo = map[int]int{}
	for i := 0; i < N; i++ {
		memo[inOrder[i]] = i
	}
	toPreOrder(0, N-1, 0, N-1)
}
