import { assertEquals } from "jsr:@std/assert@1.0.16/equals";

type Equation = [OperationSymbol, number, number, number];

function assembleEquations(
  operations: OperationSymbol[],
  numberRows: number[][],
) {
  console.log(operations, numberRows);

  if (!numberRows.length || !operations.length) {
    throw new Error("Rows must have length");
  }
  if (!numberRows.every((r) => r.length === numberRows[0].length)) {
    throw new Error("Number rows must be equal length");
  }
  if (numberRows[0].length !== operations.length) {
    throw new Error(
      `Operations has length ${operations.length}. Number rows have length ${
        numberRows[0].length
      }`,
    );
  }
  const equations: Equation[] = [];

  const operationsStack = [...operations];
  const numberStacks = numberRows.map((r) => [...r]);

  while (operationsStack.length) {
    const numbers = numberStacks.map((s) => s.pop());
    const operation = operationsStack.pop();

    const result = [operation, ...numbers];
    if (!isEquation(result)) {
      throw new Error(`Created invalid Equation ${result}`);
    }
    equations.push(result);
  }

  return equations;
}

assertEquals(assembleEquations(["+"], [[1], [2]]), [["+", 1, 2]]);
assertEqualsUnordered(assembleEquations(["+", "*"], [[1, 4], [2, 5]]), [[
  "+",
  1,
  2,
], [
  "*",
  4,
  5,
]]);

function parseNumberRowsHuman(numberRows: string[]) {
  return numberRows.map(parseNumbersRow);
}

function parseNumbersRow(s: string): number[] {
  return s.trim().split(/\s+/).filter(Boolean).map(Number);
}
assertEquals(parseNumbersRow("1  2"), [1, 2]);

function rotate90(text: string): string {
  const lines = text.split("\n");
  const height = lines.length;
  const width = Math.max(...lines.map((line) => line.length));

  const paddedLines = lines.map((line) => line.padEnd(width, " "));

  // Rotate 90 degrees clockwise
  const result: string[] = [];
  for (let col = 0; col < width; col++) {
    let newLine = "";
    for (let row = height - 1; row >= 0; row--) {
      newLine += paddedLines[row][col];
    }
    result.push(newLine);
  }

  return result.join("\n");
}

function parseEquationsAsCephalopod(s: string) {
  return rotate90(s).split(/(?=[+*])/)
    .filter((part) => part.trim())
    .map((part) => {
      const op = part[0] as "+" | "*";
      const numbers = part.slice(1)
        .split(/\s+/)
        .filter(Boolean)
        .map((numStr) => Array.from(numStr).reverse().join(""))
        .map(Number);
      return [op, ...numbers] as Equation;
    });
}

function buildValueFromDigits(digits: number[]): number {
  if (!digits.length) throw new Error(`Cannot provide digits ${digits}`);
  let result = digits[0];
  digits.slice(1).forEach((value) => {
    result = result * 10 + value;
  });
  return result;
}

assertEquals(buildValueFromDigits([1]), 1);
assertEquals(buildValueFromDigits([1, 0]), 10);
assertEquals(buildValueFromDigits([0, 9]), 9);
assertEquals(buildValueFromDigits([8, 9]), 89);

type MultiplyOperationSymbol = "*";
type AddOperationSymbol = "+";
type OperationSymbol = AddOperationSymbol | MultiplyOperationSymbol;
function parseOperationRow(s: string): OperationSymbol[] {
  return s.replaceAll(" ", "").split("") as OperationSymbol[];
}
assertEquals(parseOperationRow("+ *"), ["+", "*"]);
assertEquals(parseOperationRow("   +   *  "), ["+", "*"]);
assertEquals(parseOperationRow("*** + **"), ["*", "*", "*", "+", "*", "*"]);

function isEquation(a: unknown): a is Equation {
  if (!Array.isArray(a)) return false;
  if (!a.length) return false;

  if (a.length < 2) return false;

  if (!isOperationSymbol(a[0])) return false;
  if (a.slice(1).some((i) => !Number.isInteger(i))) return false;

  return true;
}

function parseInputStringHuman(s: string): Equation[] {
  const lines = s.split("\n");
  console.log(lines);
  const operations = parseOperationRow(lines.slice(-1)[0]);
  const numberRows = parseNumberRowsHuman(lines.slice(0, -1)) as number[][];

  if (!operations.every(isOperationSymbol)) {
    throw new Error(
      `There are non operations in operations row: ${operations}`,
    );
  }
  if (!numberRows.every((row) => row.every(Number.isInteger))) {
    throw new Error(`Some numbers are not number: ${numberRows}`);
  }

  console.log({ operations, numberRows });

  return assembleEquations(operations, numberRows);
}

const exampleString = `123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + `;

const example = parseInputStringHuman(exampleString);
assertEquals(example[3], ["*", 123, 45, 6]);
assertEquals(example[2], ["+", 328, 64, 98]);
assertEquals(example[1], ["*", 51, 387, 215]);
assertEquals(example[0], ["+", 64, 23, 314]);

function evaluteEquation(eq: Equation): number {
  const isAddition = eq[0] === "+";
  const numbers = eq.slice(1) as number[];

  let result = numbers[0];
  for (const n of numbers.slice(1)) {
    result = isAddition ? result + n : result * n;
  }
  return result;
}
assertEquals(evaluteEquation(["+", 1, 2, 3]), 6);
assertEquals(evaluteEquation(["*", 4, 2, 3]), 24);
assertEquals(evaluteEquation(["+", 4, 2, 3]), 9);

function sumEquationResults(eqs: Equation[]): number {
  return eqs.map(evaluteEquation).reduce(
    (acc: number, value: number) => acc + value,
    0,
  );
}
assertEquals(
  sumEquationResults([["+", 1, 2, 3], ["*", 4, 2, 3], ["+", 4, 2, 3]]),
  39,
);

const equations = parseEquationsAsCephalopod(
  Deno.readTextFileSync("dec-6.txt"),
);
console.log(equations.slice(0, 3));
console.log(sumEquationResults(equations));

function isOperationSymbol(a: unknown): a is OperationSymbol {
  return a === "*" || a === "+";
}

function assertEqualsUnordered<T>(actual: T[], expected: T[]) {
  assertEquals(actual.length, expected.length);
  assertEquals(
    actual.sort(),
    expected.sort(),
  );
}

assertEqualsUnordered([1, 2, 3], [3, 1, 2]);
