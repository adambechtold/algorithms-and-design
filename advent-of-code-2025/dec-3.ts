import { assertEquals } from "jsr:@std/assert@1.0.16/equals";

// first max should win
function findFirstMaxEntryOrThrow(arr: number[]) {
  if (!arr.length) throw new Error("Do not provide empty array.");

  let currMax = 0;
  let indexOfMax = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > currMax) {
      indexOfMax = i;
      currMax = arr[i];
    }
  }

  return {
    index: indexOfMax,
    value: currMax,
  };
}

assertEquals(findFirstMaxEntryOrThrow([1]), { index: 0, value: 1 });
assertEquals(findFirstMaxEntryOrThrow([1, 2]), { index: 1, value: 2 });
assertEquals(findFirstMaxEntryOrThrow([2, 2, 1]), { index: 0, value: 2 });
assertEquals(findFirstMaxEntryOrThrow([2, 2, 9]), { index: 2, value: 9 });

type JoltageBank = number[];

function findMaxJoltage(bank: JoltageBank): number {
  const tensPlace = findFirstMaxEntryOrThrow(bank.slice(0, -1));
  const onesPlace = findFirstMaxEntryOrThrow(bank.slice(tensPlace.index + 1));

  return (tensPlace.value * 10) + onesPlace?.value;
}

assertEquals(findMaxJoltage([1, 1]), 11);
assertEquals(findMaxJoltage([2, 1]), 21);
assertEquals(findMaxJoltage([1, 2]), 12);
assertEquals(findMaxJoltage([9, 9, 8, 8]), 99);
assertEquals(findMaxJoltage([9, 8, 8, 9]), 99);
assertEquals(findMaxJoltage([1, 8, 8, 9]), 89);
assertEquals(
  findMaxJoltage([
    9,
    8,
    7,
    6,
    5,
    4,
    3,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
  ]),
  98,
);
assertEquals(
  findMaxJoltage([
    8,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    9,
  ]),
  89,
);
assertEquals(
  findMaxJoltage([
    2,
    3,
    4,
    2,
    3,
    4,
    2,
    3,
    4,
    2,
    3,
    4,
    2,
    7,
    8,
  ]),
  78,
);
assertEquals(
  findMaxJoltage([
    8,
    1,
    8,
    1,
    8,
    1,
    9,
    1,
    1,
    1,
    1,
    2,
    1,
    1,
    1,
  ]),
  92,
);

function solve(joltageBanks: JoltageBank[]) {
  let sum = 0;
  for (const bank of joltageBanks) {
    sum += findMaxJoltage(bank);
  }
  return sum;
}

assertEquals(solve([[1, 1], [2, 2]]), 33);
assertEquals(
  solve(
    [
      [
        9,
        8,
        7,
        6,
        5,
        4,
        3,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
      ],
      [
        8,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        9,
      ],
      [
        2,
        3,
        4,
        2,
        3,
        4,
        2,
        3,
        4,
        2,
        3,
        4,
        2,
        7,
        8,
      ],
      [
        8,
        1,
        8,
        1,
        8,
        1,
        9,
        1,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
      ],
    ],
  ),
  357,
);

function parseStringIntoJoltageBank(s: string) {
  return s.split("").map(Number);
}

assertEquals(parseStringIntoJoltageBank("1"), [1]);
assertEquals(parseStringIntoJoltageBank("12"), [1, 2]);

function parseTextFile(fileName: string): JoltageBank[] {
  const s = Deno.readTextFileSync(fileName);
  return s.split("\n").map(parseStringIntoJoltageBank);
}

console.log(solve(parseTextFile("dec-3.txt")));
