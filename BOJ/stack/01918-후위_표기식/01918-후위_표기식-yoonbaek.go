// git commit -m "code: Solve boj 01918 후위 표기식 (yoonbaek)"

package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	sc         = bufio.NewScanner(os.Stdin)
	answer     string
	priority   int
	priorities = map[string]int{
		"+": 0, "-": 0,
		"*": 1, "/": 1,
	}
	s Stack
)

func scan() (res []string) {
	sc.Scan()
	for _, byte := range sc.Text() {
		res = append(res, string(byte))
	}
	return
}

type operator struct {
	op       string
	priority int
}

type Stack []operator

func (s Stack) isEmpty() bool {
	return len(s) <= 0
}

func (s Stack) Rear() interface{} {
	if s.isEmpty() {
		return nil
	}
	return s[len(s)-1]
}

func (s *Stack) Push(x operator) {
	*s = append(*s, x)
}

func (s *Stack) Pop() interface{} {
	if s.isEmpty() {
		return nil
	}
	tmp := *s
	*s = tmp[0 : len(tmp)-1]
	return tmp[len(tmp)-1]
}

func stackOp(p int, char string) {
	p += priority
	op := operator{char, p}
	defer s.Push(op)

	for !s.isEmpty() && p <= s.Rear().(operator).priority {
		answer += s.Pop().(operator).op
	}
}

func cleanStack() {
	for !s.isEmpty() {
		answer += s.Pop().(operator).op
	}
}

func main() {
	for _, char := range scan() {
		p, exists := priorities[char]
		if exists {
			stackOp(p, char)
			continue
		}
		switch char {
		case "(":
			priority += 2
		case ")":
			priority -= 2
		default:
			answer += char
		}
	}
	cleanStack()
	fmt.Println(answer)
}
