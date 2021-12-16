// const fs = require("fs");

// const input: string[] = (
//   process.platform === "linux"
//     ? fs.readFileSync("/dev/stdin")
//     : `ACAYKP
//   CAPCAK`
// )
//   .toString()
//   .trim()
//   .split("\n")
//   .map((x: string) => x.trim());

const input: string[] = [``];

const solution = (input: string[]): number => {
  const [str1, str2] = input;
  const [len1, len2] = [str1.length, str2.length];

  const dp = Array.from(Array(Math.max(len1, len2) + 1), () => Array());

  for (let i = 0; i <= len1; i++) {
    for (let j = 0; j <= len2; j++) {
      dp[i][j] = 0;
    }
  }

  for (let i = 1; i <= len1; i++) {
    for (let j = 1; j <= len2; j++) {
      if (str1[i - 1] === str2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
      }
    }
  }
  return dp[len1][len2];
};

console.log(solution(input));

export {};
