import { assertEquals } from "jsr:@std/assert";

function isInvalidId(id: string) {
  const idParts = splitStringEvenly(id);
  if (!idParts) return false;

  return idParts[0] === idParts[1];
}

assertEquals(isInvalidId("99"), true);
assertEquals(isInvalidId("91"), false);
assertEquals(isInvalidId("1"), false);
assertEquals(isInvalidId("11"), true);
assertEquals(isInvalidId("222222"), true);
assertEquals(isInvalidId("231123"), false);
assertEquals(isInvalidId("231231"), true);

function isInvalidIdSplitLength(id: string, partitionSize: number): boolean {
  const canBeSplitIntoEvenChunks = id.length % partitionSize === 0;
  if (!canBeSplitIntoEvenChunks) return false;

  const isPartitionSizeMoreThanHalfOfLength = partitionSize > (id.length / 2);
  if (isPartitionSizeMoreThanHalfOfLength) return false;

  const chunks = chunkString(id, partitionSize);

  const set = new Set(chunks);
  return set.size === 1;
}

assertEquals(isInvalidIdSplitLength("ab", 1), false);
assertEquals(isInvalidIdSplitLength("aa", 1), true);
assertEquals(isInvalidIdSplitLength("aa", 2), false);
assertEquals(isInvalidIdSplitLength("aa", 3), false);
assertEquals(isInvalidIdSplitLength("abc", 1), false);
assertEquals(isInvalidIdSplitLength("abab", 1), false);
assertEquals(isInvalidIdSplitLength("abab", 2), true);
assertEquals(isInvalidIdSplitLength("aaaa", 2), true);
assertEquals(isInvalidIdSplitLength("aaaa", 1), true);
assertEquals(isInvalidIdSplitLength("12", 1), false);
assertEquals(isInvalidIdSplitLength(String(12), 1), false);

assertEquals(isInvalidIdSplitLength("38593859", 4), true);

function chunkString(s: string, size: number) {
  const r: string = [];
  for (let i = 0; i < s.length; i += size) {
    r.push(s.slice(i, i + size));
  }
  return r;
}

assertEquals(chunkString("a", 1), ["a"]);
assertEquals(chunkString("a", 2), ["a"]);
assertEquals(chunkString("ab", 1), ["a", "b"]);
assertEquals(chunkString("ab", 2), ["ab"]);

function splitStringEvenly(s: string): [string, string] | null {
  if (s.length % 2 === 1) return null;

  return [s.slice(0, s.length / 2), s.slice(s.length / 2)];
}

assertEquals(splitStringEvenly("a"), null);
assertEquals(splitStringEvenly("ab"), ["a", "b"]);
assertEquals(splitStringEvenly("abc"), null);
assertEquals(splitStringEvenly("abcd"), ["ab", "cd"]);

type IdRange = [number, number];

function parseInputString(s: string): IdRange {
  const parts = s.split("-");
  return parts.map(Number);
}

assertEquals(parseInputString("11-22"), [11, 22]);
assertEquals(parseInputString("0-100"), [0, 100]);
assertEquals(parseInputString("11-11"), [11, 11]);

function parseInputIntoRanges(s: string) {
  const ranges = s.split(",");
  return ranges.map(parseInputString);
}

assertEquals(parseInputIntoRanges("11-22,0-100"), [[11, 22], [0, 100]]);

function sumInvalidIdsInRange(range: IdRange): number {
  let sum = 0;

  for (let i = range[0]; i <= range[1]; i++) {
    if (isInvalidId(String(i))) sum += i;
  }

  return sum;
}

assertEquals(sumInvalidIdsInRange([0, 1]), 0);
assertEquals(sumInvalidIdsInRange([11, 11]), 11);
assertEquals(sumInvalidIdsInRange([11, 20]), 11);
assertEquals(sumInvalidIdsInRange([11, 22]), 33);

function sumInvalidIdsInRangePartitioned(range: IdRange): number {
  let sum = 0;

  for (let i = range[0]; i <= range[1]; i++) {
    for (
      let partitionSize = 1;
      partitionSize <= String(i).length / 2;
      partitionSize++
    ) {
      if (isInvalidIdSplitLength(String(i), partitionSize)) {
        sum += i;
        break;
      }
    }
  }

  return sum;
}

assertEquals(sumInvalidIdsInRangePartitioned([11, 22]), 33);
assertEquals(sumInvalidIdsInRangePartitioned([95, 115]), 210);
assertEquals(
  sumInvalidIdsInRangePartitioned([824824821, 824824827]),
  824824824,
);
assertEquals(sumInvalidIdsInRangePartitioned([38593856, 38593862]), 38593859);

// Solve Puzzle
function solve(s: string, sumInvalidIdsFn: (range: IdRange) => number): number {
  const ranges = parseInputIntoRanges(s);

  return ranges.reduce((acc, range) => {
    const sum = sumInvalidIdsFn(range);
    return acc + sum;
  }, 0);
}

assertEquals(solve("11-22", sumInvalidIdsInRangePartitioned), 33);
assertEquals(solve("95-115", sumInvalidIdsInRangePartitioned), 210);
assertEquals(solve("11-22,95-115", sumInvalidIdsInRangePartitioned), 243);
assertEquals(
  solve(
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124",
    sumInvalidIdsInRange,
  ),
  1227775554,
);

console.log("solve");
assertEquals(
  solve(
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124",
    sumInvalidIdsInRangePartitioned,
  ),
  4174379265,
);

console.log(
  solve(Deno.readTextFileSync("dec-2.txt"), sumInvalidIdsInRangePartitioned),
);
