// git commit -m "code: Solve boj 02295 세 수의 합 (yoonbaek)"

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var (
	n, max int
	nums   Set
	sc     = bufio.NewScanner(os.Stdin)
	count  = map[int]bool{}
)

func init() {
	sc.Split(bufio.ScanLines)
}

// sort Interface
type Set []int

func (s Set) Len() int {
	return len(s)
}

func (s Set) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s Set) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func main() {
	n = scan()
	nums = make(Set, n)

	for i := 0; i < n; i++ {
		num := scan()
		nums[i] = num
		count[num] = true
	}

	sort.Sort(nums)
	leftSide()
	rightSide()
	fmt.Println(max)
}

// utils
func scan() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

// logics
func leftSide() {
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			count[nums[i]+nums[j]] = true
		}
	}
}

func rightSide() {
	for i := n - 1; i >= 0; i-- {
		for j := i; j >= 0; j-- {
			if count[nums[i]-nums[j]] {
				max = nums[i]
				return
			}
		}
	}
}
