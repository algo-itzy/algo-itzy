// const fs = require("fs");

// const input: string[] = (
//   process.platform === "linux" ? fs.readFileSync("/dev/stdin") : `1000`
// )
//   .toString()
//   .split("\n")
//   .map((x: string) => x.trim());

const input: string[] = [""];

const solution = (input: string[]): number => {
  // JS는 함수를 최상단 배치하는 것이 맞을까?
  const multi = (a: number[][], b: number[][]): number[][] => {
    let mul = Array.from(Array(2), () => Array(2).fill(BigInt(0)));

    for (let i = 0; i < 2; i++) {
      for (let j = 0; j < 2; j++) {
        for (let k = 0; k < 2; k++) {
          mul[i][j] += BigInt(a[i][k]) * BigInt(b[k][j]);
        }
      }
    }

    for (let i = 0; i < 2; i++) {
      for (let j = 0; j < 2; j++) {
        mul[i][j] %= BigInt(1000000007);
      }
    }

    return mul;
  };

  let n = Number(input[0]);

  let mat: number[][] = [
    [1, 1],
    [1, 0],
  ];
  let res: number[][] = [
    [1, 0],
    [0, 1],
  ];

  while (n) {
    if (n % 2 === 1) {
      res = multi(res, mat);
    }
    mat = multi(mat, mat);

    n = Math.floor(n / 2); // JS는 n//2가 없음
  }

  return Number(res[1][0]);
};

// 디버깅 모두 정상으로 나오나 백준은 채점 하자마자 틀렸다고 나옴..
console.log(solution(input));

export {};
