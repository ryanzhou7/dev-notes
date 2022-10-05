# typescript

# [TypeScript Fundamentals v3](https://github.com/mike-north/ts-fundamentals-v3)

## Setup

- [Setting up a TS compiler](https://www.typescript-training.com/course/fundamentals-v3/02-hello-typescript/)
- .ts files contain info and runs
- .js run only
- .d.ts only contain info
- `export` is CommonJS modules

<br/>

## Variables and Values

- in TS, variables are born with their types
  - `const age = 6`, type is 'immutable value type'
  - `let age = 6; age = "not a number"` Type 'string' is not assignable to type 'number'
  - type inference is not so specific that `age` cannot be assigned to another number
- literal types: 6, 'hello'

<br/>

## Objects, Arrays and Tuples

- object literal type may only specific known props, unstated types will cause an error
  - `const obj: { name: string } = { name: 'joe', age: 1};` -> error
- `const obj: { [k: string]: string } = { name: 'joe'};` -> keys and values = string

- **Tuple**: multi-element, ordered data structure, position of each item has special meaning

```ts
let myCar = [2002, "Toyota", "Corolla"];
const [year, make, model] = myCar;
// TS chooses the most specific type that describes the entire contents of the array
// model type is string | number
// why not that model is always string? too restrictive...
// Thus, we need to explicitly state the type of a tuple
let myCar: [number, string, string] = [2002, "Toyota", "Corolla"];

// but as of TS 4.3 tuple support is limited
const numPair: [number, number] = [4, 5];
numPair.push(6); // OK
```

<br/>

## Structural vs. Nominal Types

- Type-checking can be thought of as a task that attempts to evaluate the question of compatibility or type equivalence
- **Nominal type system**: are about names

```java
// java
public class CarChecker {
  // takes a `Car` argument, returns a `String`
  public static String printCar(Car car) {  }
}
Car car = new Car();
CarChecker.checkCar(car); // checks if car is instance of class named Car car
```

- **Structural type system**: (which TS is) are about structure or shape

```ts
class Car {
  make: string;
  model: string;
}
// Only cares that argument has suitable props
function printCar(car: { make: string; model: string }) {
  console.log(`${car.make} ${car.model} `);
}

printCar(new Car()); // Fine
printCar({
  make: "Honda",
  model: "Accord",
  year: 2017,
}); // Fine
```

<br/>

## Union and Intersection Types

- **Type guards**: expressions, which when used with control flow statement, allow us to have a more specific type for a particular value

```ts
const e: Error | string = '';
if( e instance of Error){ // <- type guard
  // can do Error specific code here, aka narrowing
}else{
  // Discriminated Unions, can do string things here as if it's not error it's a string
}
```

<br/>

## Interfaces and Type Aliases

- 2 ways to define types, type alias & interfaces
- type alias declaration is per scope

```ts
// Intersection types: combine existing types
type SpecialDate = Date & { getReason(): string };
```

- **Interface**: defines an object type, i.e. an instance of a class could look like this

```ts
// heritage clauses = extends, a subclass extends from a base class
interface Animal {
  isAlive(): boolean;
}
interface Mammal extends Animal {
  getFurOrHairColor(): string;
}

// implement: a given class should produce instances that confirm to given interface implements
interface AnimalLike {
  eat(food): void;
}
class Dog implements AnimalLike {
  eat() {
    return "woof";
  }
}
```

- no multiple inheritance, but can implement multiple interfaces
- Best to use implement with interface NOT type alias, if the type ever breaks the “object type” rules there’s [some potential for problems…](https://www.typescript-training.com/course/fundamentals-v3/07-interfaces-and-type-aliases/)

```ts
// what it means for interfaces to be open
interface AnimalLike {
  isAlive(): boolean;
}
interface AnimalLike {
  eat(food): void;
}
// this is fine, they will merge together
```

### Type vs interfaces

1. If you need to define something other than an object type (e.g., use of the | union type operator), you must use a type alias
2. If you need to define a type to use with the implements heritage term, it’s best to use an interface
3. If you need to allow consumers of your types to augment them, you must use an interface.

- [**Recursion types**](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-1.html#recursive-conditional-types): self-referential, and are often used to describe infinitely nestable types

```ts
type NestedNumbers = number | NestedNumbers[];
const val: NestedNumbers = [3, 4, [5, 6, [7], 59], 221];
```

<br/>

## Functions

- Both below describe [**call signatures**](https://www.typescriptlang.org/docs/handbook/2/functions.html#call-signatures)

```ts
interface TwoNumberCalculation {
  (x: number, y: number): number;
}

type TwoNumberCalc = (x: number, y: number) => number;
```

- [**Construct signatures**](https://www.typescriptlang.org/docs/handbook/2/functions.html#construct-signatures) are similar to call signatures, except they describe what should happen with the new keyword.
- void type: the return value of a void function is intended to be ignored
- function overloads - defining multiple function heads that serve as entry points to a single implementation

```ts
// not good as HTMLFormElement and FormSubmitHandler should link, but this defines the entire cardinal set
function handleMainEvent(
  elem: HTMLFormElement | HTMLIFrameElement,
  handler: FormSubmitHandler | MessageHandler
) {}

// improved, we state only this permutations are possible
function handleMainEvent(elem: HTMLFormElement, handler: FormSubmitHandler);
function handleMainEvent(elem: HTMLIFrameElement, handler: MessageHandler);
function handleMainEvent(
  elem: HTMLFormElement | HTMLIFrameElement,
  handler: FormSubmitHandler | MessageHandler
) {
  // implementation...
}
// looks like 3 function declarations but really just 2 heads exposed, the last is inaccessible
// note: the implementation must be general enough to include everything that possible through the exposed
```

```ts
function myClickHandler(event: Event) {
  this.disabled = true;
  // ERROR 'this' implicitly has type 'any' because it does not have a type annotation.
}
myClickHandler(new Event("click")); // seems ok

// Fix, "this" type
function myClickHandler(this: HTMLButtonElement, event: Event) {
  this.disabled = true;
}
```

- Function type best practices: Explicitly define return types
- Ex. We’ll see some type-checking errors pop up, but at the invocation site, not the declaration site.

```ts
async function getData(url: string) {
  const resp = await fetch(url);
  if (resp.ok) {
    const data = (await resp.json()) as {
      properties: string[];
    };
    return data;
  }
}

function loadData() {
  getData("https://example.com").then((result) => {
    console.log(result.properties.join(", ")); // ERROR Object is possibly 'undefined'.
  });
}
// FIX
async function getData(url: string): Promise<{ properties: string[] }> {
  const resp = await fetch(url);
  if (resp.ok) {
    const data = (await resp.json()) as {
      properties: string[];
    };
    return data;
  }
}
```

<br/>

## [Classes (skipped)](https://www.typescript-training.com/course/fundamentals-v3/10-classes/)

<br/>

## Top and bottom types

- **Top type (symbol: ⊤)**: is a type that describes any possible value allowed by the system, i.e. `any` & `unknown`
  - Any differs from unknown in that values with an unknown type cannot be used without first applying a type guard
- **Bottom type (symbol: ⊥)**: is a type that describes no possible value allowed by the system, i.e. `never`
  - usage below

```ts
// @errors: 2322
function obtainRandomVehicle(): any {
  return {} as any;
}
/// ---cut---
class Car {}
class Truck {}
class Boat {}
type Vehicle = Truck | Car | Boat; // if you add boat...

let myVehicle: Vehicle = obtainRandomVehicle();

// The exhaustive conditional
if (myVehicle instanceof Truck) {
} else if (myVehicle instanceof Car) {
} else {
  // You'll get helpful ERROR! Type 'Boat' is not assignable to type 'never'
  // Signal a case in which if we are in this cond it myVehicle better be a never
  // aka, you never expect to reach this code
  const neverValue: never = myVehicle;

  // typically throw an error here
  class UnreachableError extends Error {
    constructor(_nvr: never, message: string) {
      super(message);
    }
  }

  throw new UnreachableError(
    myVehicle,
    `Unexpected vehicle type: ${myVehicle}`
  );
}
```

<br/>

## Type guards and narrowing

### Built in type guards

```ts
let value:
  | Date
  | null
  | undefined
  | "pineapple"
  | [number]
  | { dateRange: [Date, Date] };

// instanceof
if (value instanceof Date) {
}
// typeof
else if (typeof value === "string") {
}
// Specific value check
else if (value === null) {
}
// Truthy/falsy check
else if (!value) {
}
// Some built-in functions
else if (Array.isArray(value)) {
}
// Property presence check
else if ("dateRange" in value) {
} else {
  // if top was exhaustive, value should be never here
}
```

### User-defined type guards

```ts
interface CarLike {
  make: string;
  year: number;
}

let maybeCar: unknown;

// the guard, NOTE the return to now utilize CarLike narrowing
function isCarLike(valueToTest: any): valueToTest is CarLike {
  return (
    valueToTest && // is it nullish?
    typeof valueToTest === "object" &&
    "make" in valueToTest &&
    typeof valueToTest["make"] === "string" &&
    "year" in valueToTest &&
    typeof valueToTest["year"] === "number"
  );
  // NOTE, if you write a non-exhaustive guard... you'll get an error further down the line
}

// Another usage - eliminates using this as an if statement
function assertsIsCarLike(valueToTest: any): asserts valueToTest is CarLike {
  if (!isCarLike(valueToTest))
    throw new Error(`Value does not appear to be a CarLike${valueToTest}`);
}

assertsIsCarLike(maybeCar);
maybeCar; // now known type is CarLike
```

<br/>

## Nullish values

- **Non-null assertion operator**

```ts
// !. tells ts to ignore possibility that value could null / undefined
cart.fruits!.push({ name: "kumkuat", qty: 1 });
```

- [**Definite assignment operator (skip)**](https://www.typescript-training.com/course/fundamentals-v3/13-nullish-values/#definite-assignment-operator)

<br/>

## Generics

**Generics:** function arguments, but for types. Describes the minimum requirement for a type param

```ts
interface HasId {
  id: string;
}
interface Dict<T> {
  [k: string]: T;
}
function listToDict<T extends HasId>(list: T[]): Dict<T> {}
// generic constraints
```

- Best Practices, use each type parameter at least twice. Any less and you might be casting with the as keyword

```ts
function returnAs<T>(arg: any): T {
  return arg; // 🚨 an `any` that will _seem_ like a `T`
}

// 🚨 DANGER! 🚨
const first = returnAs<number>(window);
// const first: number
// const sameAs = window as any as number
```

<br/>
<br/>

# [ Making TypeScript Stick](https://www.typescript-training.com/course/making-typescript-stick)

## 6 significant TS updates

```ts

```

[TS](https://www.typescript-training.com/course/making-typescript-stick/03-recent-updates-to-typescript/)
tuple type: an ordered collection (often of known length), with the type of each member known as well.
