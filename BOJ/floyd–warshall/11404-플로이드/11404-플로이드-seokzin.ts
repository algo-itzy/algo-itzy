// const fs = require("fs");

// const input: string[] = (
//   process.platform === "linux" ? fs.readFileSync("/dev/stdin") : ``
// )
//   .toString()
//   .split("\n")
//   .map((x: string) => x.trim());

const input: string[] = [""];

const solution = (input: string[]): string => {
  const [in1, in2, ...in3] = input;
  const n = Number(in1);
  const m = Number(in2);
  const graph = Array.from(Array(n), () => Array(n).fill(Infinity));
  let res: string = "";

  for (let i = 0; i < m; i++) {
    const [a, b, w] = in3[i].split(" ").map(Number);
    graph[a - 1][b - 1] = Math.min(w, graph[a - 1][b - 1]);
  }

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (i === j) {
          graph[i][j] = 0;
        } else {
          graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
        }
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (graph[i][j] === Infinity) {
        graph[i][j] = 0;
      }
    }
  }

  graph.forEach((x) => {
    res += `${x.join(" ")}\n`;
  });

  return res;
};

console.log(solution(input));

export {};
