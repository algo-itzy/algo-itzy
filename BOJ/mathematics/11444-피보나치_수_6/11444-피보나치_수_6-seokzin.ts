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
    let mul = Array.from(Array(2), () => Array(2).fill(0));

    for (let i = 0; i < 2; i++) {
      for (let j = 0; j < 2; j++) {
        for (let k = 0; k < 2; k++) {
          mul[i][j] += a[i][k] * b[k][j];
        }
      }
    }

    for (let i = 0; i < 2; i++) {
      for (let j = 0; j < 2; j++) {
        mul[i][j] %= 1000000007;
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

  return res[1][0];
};

// 실패 코드 - JS는 최대 안전 정수값이 존재. 그 이상은 부동소수점으로 저장하여 오차 발생 (Number.MAX_SAFE_INTEGER = 9007199254740991)
// 그럼에도 JS로 푼 사람들이 있는데 그 방법은 수학적인 것 같아서 모르겠네요
console.log(solution(input));

export {};
