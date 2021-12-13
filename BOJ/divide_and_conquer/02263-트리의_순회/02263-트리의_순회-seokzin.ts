// const fs = require("fs");

// const input: string[] = (
//   process.platform === "linux"
//     ? fs.readFileSync("/dev/stdin")
//     : `3
//     1 2 3
//     1 3 2`
// )
//   .toString()
//   .split("\n")
//   .map((x: string) => x.trim());

const input: string[] = [``];

interface Param {
  inL: number;
  inR: number;
  postL: number;
  postR: number;
}

const solution = (input: string[]): string => {
  const [in1, in2, in3] = input;

  const n: number = Number(in1);
  const inOrder: number[] = in2.split(" ").map(Number);
  const postOrder: number[] = in3.split(" ").map(Number);
  const res: number[] = [];
  // 유니온 타입으로 표현하고 싶음
  const callStack: any = [[0, n - 1, 0, n - 1]];

  while (callStack.length) {
    const [inL, inR, postL, postR] = callStack.pop();

    if (inL > inR || postL > postR) {
      continue;
    }

    const root = postOrder[postR];
    res.push(root);

    let inRootIndex: number = 0;

    for (let i = inL; i <= inR; i++) {
      if (inOrder[i] === root) {
        inRootIndex = i;
        break;
      }
    }
    const postLeftEnd = postL + (inRootIndex - 1 - inL);
    callStack.push([inRootIndex + 1, inR, postLeftEnd + 1, postR - 1]);
    callStack.push([inL, inRootIndex - 1, postL, postLeftEnd]);
  }

  return res.join(" ");
};

// node의 call stack 사이즈는 최대 1만이므로 재귀 풀이는 지양하자
console.log(solution(input));

export {};
