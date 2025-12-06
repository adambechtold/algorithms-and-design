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

function findMaxJoltage(bank: JoltageBank, numberOfBatteries: number): number {
  let value = 0;
  let earliestAllowedIndex = 0;

  for (let i = numberOfBatteries; i > 0; i--) {
    const lastAllowedIndex = bank.length - i;
    const validBatteries = bank.slice(
      earliestAllowedIndex,
      lastAllowedIndex + 1,
    );
    const largestBattery = findFirstMaxEntryOrThrow(
      validBatteries,
    );
    earliestAllowedIndex = earliestAllowedIndex + largestBattery.index + 1;
    value = value * 10 + largestBattery.value;
  }

  return value;
}

assertEquals(findMaxJoltage([1, 1], 1), 1);
assertEquals(findMaxJoltage([1, 1], 2), 11);
assertEquals(findMaxJoltage([2, 1], 2), 21);
assertEquals(findMaxJoltage([1, 2], 2), 12);
assertEquals(findMaxJoltage([9, 9, 8, 8], 2), 99);
assertEquals(findMaxJoltage([9, 8, 8, 9], 2), 99);
assertEquals(findMaxJoltage([1, 8, 8, 9], 2), 89);
assertEquals(findMaxJoltage([1, 8, 8, 9], 3), 889);
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
  ], 2),
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
  ], 2),
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
  ], 2),
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
  ], 2),
  92,
);

function solve(joltageBanks: JoltageBank[], numberOfBatteries: number): number {
  let sum = 0;
  for (const bank of joltageBanks) {
    sum += findMaxJoltage(bank, numberOfBatteries);
  }
  return sum;
}

assertEquals(solve([[1, 1], [2, 2]], 2), 33);
const exampleInput: JoltageBank[] = [
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
];
assertEquals(solve(exampleInput, 2), 357);
assertEquals(solve(exampleInput, 12), 3121910778619);

function parseStringIntoJoltageBank(s: string) {
  return s.split("").map(Number);
}

assertEquals(parseStringIntoJoltageBank("1"), [1]);
assertEquals(parseStringIntoJoltageBank("12"), [1, 2]);

function parseTextFile(fileName: string): JoltageBank[] {
  const s = Deno.readTextFileSync(fileName);
  return s.split("\n").map(parseStringIntoJoltageBank);
}

console.log(solve(parseTextFile("dec-3.txt"), 12));
