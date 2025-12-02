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

function solve(s: string): number {
  const ranges = parseInputIntoRanges(s);

  return ranges.reduce((acc, range) => {
    return acc + sumInvalidIdsInRange(range);
  }, 0);
}

assertEquals(solve("11-22"), 33);
assertEquals(
  solve(
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124",
  ),
  1227775554,
);

console.log(solve(Deno.readTextFileSync("dec-2.txt")))
