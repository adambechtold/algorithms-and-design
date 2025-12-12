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

function parseNumbersRow(s: string): number[] {
  return s.trim().split(/\s+/).filter(Boolean).map(Number);
}
assertEquals(parseNumbersRow("1  2"), [1, 2]);

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

function parseInputString(s: string): Equation[] {
  const lines = s.split("\n");
  console.log(lines);
  const operations = parseOperationRow(lines.slice(-1)[0]);
  const numberRows = lines.slice(0, -1).map(parseNumbersRow);

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

const example = parseInputString(exampleString);
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

console.log(
  sumEquationResults(parseInputString(Deno.readTextFileSync("dec-6.txt"))),
);

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
