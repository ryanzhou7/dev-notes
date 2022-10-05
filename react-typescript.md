# react-typescript

# [Steve kinney FEM ](https://stevekinney.github.io/react-and-typescript/)

- Theme - ts does it's best to infer types for you
- Equivalent dictionaries

```ts
type ItemHash = {
  [key: string]: Item;
};
Record<string, Item>;
```

- Functions

```ts
type ContrivedExampleProps = {
  onHover: () => void;
  onChange: (id: number) => void;
};
```

- CSSProperties

```ts
type BoxProps = { children: React.ReactNode; style?: React.CSSProperties };
const Box = ({ children, style = {} }: BoxProps) => {
  return (
    <section style={{ padding: "1em", border: "5px solid purple", ...style }}>
      {children}
    </section>
  );
};
```

- Input handler inference

```ts
// typically
const changeCount = (e: ChangeEvent<HTMLInputElement>) => {
  setCount(+event.target.value);
};

// when directly on change handler, you can actually omit ChangeEvent<HTMLInputElement>
<input
  onChange={(e) => {
    setCount(+event.target.value);
  }}
/>;
```

- useReducer hook, improvement

```ts
// This is better rather than payload?: number;
type BasicCounterAction = {
  type: "INCREMENT" | "DECREMENT";
};
type SetCounterAction = {
  type: "SET";
  payload: number;
};
const reducer = (
  state: CounterState,
  action: BasicCounterAction | SetCounterAction
) => {
  switch (action.type) {
    case "INCREMENT":
      return { value: state.value + 1 };
    case "DECREMENT":
      return { value: state.value - 1 };
    case "SET":
      return { value: action.payload };
  }
};
```

- TS `as` keyword, ex. `{} as RGBContextType`
  - tell TS that you know better
  - ex. string as one of these types

## Context - skipped

- [Video](https://frontendmasters.com/courses/react-typescript/context-api/)
- [Site](https://stevekinney.github.io/react-and-typescript/passing-dipatch)

<br/>

```ts
export interface ColorAdjustmentProps {
  // the component is any component with these props
  Adjustment: React.ComponentType<AdjustmentInputProps>;
}
// ColorAdjustmentProps is HOC
```

## Generics

```ts
function tap<T>(arr: T, fn: (arr: T) => void): T {
  fn(arr);
  return arr;
}
const arrayWithoutLast = tap([1, 2, 3, 4], function (array) {
  return array.pop();
});
```

## [Utility types](https://stevekinney.github.io/react-and-typescript/utility-types)

- **keyof**: keys of a type

```ts
type ObjectLiteralType = {
  first: 1;
  second: 2;
};
type Result = keyof ObjectLiteralType; // Inferred Type: "first" | "second"
```

- getting the type of a single key in an object

```ts
type Obj = {
  0: "a";
  1: "b";
  prop1: "d";
};

// Inferred Type: "c"
type Result0 = Obj["prop0"];

// Inferred Type: "a" | "b"
type Result1 = Obj[0 | 1];
```

- Getting type values

```ts
type Obj = {
  a: "A";
  b: "B";
  c: number;
};
type Values = Obj[keyof Obj]; // Inferred Type: number | "A" | "B"
```

- Union with Objects

```ts
type ObjectTypeA = {
  firstProp: number;
  sharedProp: string;
};

type ObjectTypeB = {
  secondProp: boolean;
  sharedProp: string;
};

type Union = ObjectTypeA | ObjectTypeB;
const u: Union = { sharedProp: "hey", firstProp: 11, secondProp: true };
// allows us to assume that u.sharedProp: string will always exist
```

- **Intersections**: only what appears in both

```ts
type A = "a" | "b" | "c";
type B = "b" | "c" | "d";

// Inferred Type: "b" | "c"
type Intersection = A & B;

// but for objects (above), it will combine them
```

- **Conditionals**: ternaries only

```ts
type Wrap<T> = T extends { length: number } ? [T] : T; //EX.1

type IsAssignableTo<A, B> = A extends B ? true : false; //EX.2

// Type `123` is assignable to type `number`
// Inferred Type: true
type Result1 = IsAssignableTo<123, number>;

// Type `number` is not assignable to type `123`
// Inferred Type: false
type Result2 = IsAssignableTo<number, 123>;
```

- **Exclude**: removes values from union, takes stuff out of a union

```ts
type Exclude<T, U> = T extends U ? never : T;

// Inferred Type: 1 | 3
type Result0 = Exclude<1 | 2 | 3, 2>;

// Inferred Type: "a" | "b"
type Result1 = Exclude<1 | "a" | 2 | "b", number>;

// Inferred Type: "a" | 2
type Result2 = Exclude<1 | "a" | 2 | "b", 1 | "b" | "c">;
```

- **Extract**: the opposite of exclude

```ts
type Extract<T, U> = T extends U ? T : never;

// Inferred Type: 1 | 2
type Result1 = Extract<1 | "a" | 2 | "b", number>;

// Inferred Type: 1 | "b"
type Result2 = Extract<1 | "a" | 2 | "b", 1 | "b" | "c">;
```

- Union iteration

```ts
// Inferred Type: { a: number; b: number; c: number; }
type Result = {
  [K in "a" | "b" | "c"]: number;
};

type Mask = {
  [K in keyof ObjectLiteralType]: boolean;
};
```

- **Pick**: pick out certain keys from an object type

```ts
// Inferred Type: { george: 2; ringo: 4; }
type Result = Pick<
  { john: 1; paul: 2; george: 3; ringo: 4 },
  "george" | "ringo"
>;
```

- **Omit**: opposite of pick, leave out particular properties

```ts
// Inferred Type: { john: 1; paul: 2; }
type Result = Omit<
  {
    john: 1;
    paul: 2;
    george: 3;
    ringo: 4;
  },
  "george" | "ringo"
>;
```

- String Manipulation Utilities

```ts
type UppercaseWes = Uppercase<"wes">;
type LowercaseWes = Lowercase<"Wes">;
type CapitalizeWes = Capitalize<"wes">;
type UncapitalizeWes = Uncapitalize<"Wes">;
```

## React specific types

- **React.HTMLProps\<HTMLXXXElement\>**: A type representing Props of specified native HTML element. Useful for extending HTML Elements

```ts
const Input = (props: <Props & React.HTMLProps<HTMLInputElement>) => {
  // our custom props + everything you can pass to the html
}

<Input about={...} accept={...} alt={...} ... />
```

- Props of a component

```ts
type MyComponentProps = React.ComponentProps<typeof MyComponent>;
```

- Template literals

```ts
type VerticalAlignment = "top" | "center" | "bottom";
type HorizonalAlignment = "left" | "center" | "right";
type Alignment = Exclude<
  `${VerticalAlignment}-${HorizonalAlignment}` | "center",
  "center-center"
>;
// if we wanted center rather than center-center
```

## [HOC with TS](https://stevekinney.github.io/react-and-typescript/higher-order-components)

- Create a HOC that accepts a character compatible component, that you can later instantiate and pass any props
- HOC has logic + data, passes data to any data compatible component

```ts
import { ComponentType, useState, useEffect, CSSProperties } from "react";
import * as React from "react";

// Allows us to know that CharacterInformation has CharacterType compatible props
const CharacterInformationWithCharacter = withCharacter(CharacterInformation);
export default function Application() {
  return (
    <CharacterInformationWithCharacter style={{ backgroundColor: "pink" }} />
  );
}

export type CharacterType = {
  name: string;
  alignment: string;
  power: number;
};

const CharacterInformation = ({
  character: { name, alignment, power },
  style,
}: {
  character: CharacterType;
  style: CSSProperties;
}) => {
  return (
    <div style={style}>
      <h1>{name}</h1>
      <div>Alignment: {alignment}</div>
      <div>Power: {power}</div>
    </div>
  );
};

type WithCharacterProps = {
  character: CharacterType;
};
// <T extends WithCharacterProps> defines T
function withCharacter<T extends WithCharacterProps>(
  Component: ComponentType<T>
) {
  type withoutCharacterProps = Omit<T, keyof WithCharacterProps>;
  return function (props: withoutCharacterProps) {
    const [character, setCharacter] = useState<CharacterType | null>(null);
    useEffect(() => {
      new Promise(function (resolve, _) {
        setTimeout(function () {
          resolve({
            name: "3-D Man",
            alignment: "neutral",
            power: 25,
          });
        }, 2000);
      }).then((c: CharacterType) => {
        setCharacter(c);
      });
    }, []);

    return character ? (
      <Component character={character} {...(props as T)} />
    ) : (
      <h1>Loading…</h1>
    );
  };
}
```

- Another example

```ts
import { ComponentType } from "react";
import * as React from "react";

type UserModel = {
  accountId: string;
  displayName: string;
  isVerified: boolean;
};

type NameTagProps = {
  salutation: string;
  user: UserModel;
};

type WithUserProps = { user: UserModel };

function withCurrentUser<T extends WithUserProps>(
  WrappedComponent: ComponentType<T>
) {
  const currentUser = { displayName: "J Mascis" };
  return function (props: Omit<T, keyof WithUserProps>) {
    return <WrappedComponent {...(props as T)} user={currentUser} />;
  };
}

const NameTag = ({ user, salutation }: NameTagProps) => {
  return (
    <main>
      <h1>{salutation}</h1>
      <p>My Name Is</p>
      <p>{user.displayName}</p>
    </main>
  );
};

const NameTagWithCurrentUser = withCurrentUser(NameTag);

export default function Application() {
  <NameTagWithCurrentUser salutation="Howdy" />;
}
```

## Advanced Component Patterns

### [Limiting props a component can take based on other props](https://stevekinney.github.io/react-and-typescript/limiting-props)

- Ex: `<Button primary />` but not `<Button primary secondary/>`

```ts
import * as React from "react";

// Defaults as button, but can underlying be something else
type ButtonOwnProps<E extends React.ElementType = React.ElementType> = {
  children: string;
  primary?: boolean;
  secondary?: boolean;
  destructive?: boolean;
  as?: E;
};

// ButtonProps has our button props (ButtonOwnProps) + the react component's props
type ButtonProps<E extends React.ElementType> = ButtonOwnProps<E> &
  Omit<React.ComponentProps<E>, keyof ButtonOwnProps>;

const createClassNames = (classes: { [key: string]: boolean }): string => {
  let classNames = "";
  for (const [key, value] of Object.entries(classes)) {
    if (value) classNames += key + " ";
  }
  return classNames.trim();
};

const defaultElement = "button";

function Button<E extends React.ElementType = typeof defaultElement>({
  children,
  primary = false,
  secondary = false,
  destructive = false,
  as,
}: ButtonProps<E>) {
  const TagName = as || defaultElement; // if there was an as, otherwise default
  let classNames = createClassNames({ primary, secondary, destructive });
  if (TagName !== "button") classNames += " button";

  return <TagName className={classNames}>{children}</TagName>;
}

export default function Application() {
  return (
    <main>
      <Button primary as="a">
        Primary
      </Button>
      <Button secondary>Secondary</Button>
      <Button destructive>Destructive</Button>
    </main>
  );
}
```

### [Polymorphic components](https://stevekinney.github.io/react-and-typescript/polymorphic-components)

```ts
import * as React from "react";

type TextOwnProps<E extends React.ElementType = React.ElementType> = {
  children: string;
  as?: E;
};

type TextProps<E extends React.ElementType> = TextOwnProps &
  Omit<React.ComponentProps<E>, keyof TextOwnProps>;

function Text<E extends React.ElementType>({
  children,
  as,
  ...rest
}: TextProps<E>) {
  const TagName = as || "div";
  return <TagName {...rest}>{children}</TagName>;
}

const Application = () => {
  return (
    <main>
      <Text as="label" htmlFor="id">
        Hello
      </Text>
    </main>
  );
};

export default Application;
```

### [Function overloads](https://stevekinney.github.io/react-and-typescript/overloads)

- Ability to give more than one type signature to the same function
  - Declare multiple head functions with a single tail that handles all of these

```ts
// simplest
function add(a: number): (b: number) => number;
function add(a: number, b: number): number;
function add(a: any, b?: any): number | ((b: number) => number) {
  if (b === undefined) return (b: number) => a + b;
  return a + b;
}
const five = add(2, 3);
const add2 = add(2);
five === add2(3);
```

```ts
// more complicated
type callback = (result: number) => void;
function asyncAdd(a: number, b: number): Promise<number>;
function asyncAdd(a: number, b: number, fn: callback): void;
function asyncAdd(a: number, b: number, fn?: callback) {
  const result = a + b;
  if (fn) return fn(result);
  else return Promise.resolve(result);
}
```

### [Demanding Props Based on Other Props](https://stevekinney.github.io/react-and-typescript/dependent-props)

- Component function overloading example in react

```ts
// react
type TextProps = {
  children: string;
} & React.ComponentPropsWithoutRef<"div">;

type NoTruncateTextProps = TextProps & { truncate?: false };
type TruncateTextProps = TextProps & { truncate: true; expanded?: boolean };

const truncateString = (string: string, length = 10) =>
  string.slice(0, length) + "…";

function Text(props: NoTruncateTextProps): JSX.Element;
function Text(props: TruncateTextProps): JSX.Element;
function Text(props: TextProps & { truncate?: boolean; expanded?: boolean }) {
  const { children, truncate, expanded, ...otherProps } = props;
  const shouldTruncate = truncate && !expanded;
  return (
    <div aria-expanded={!!expanded} {...otherProps}>
      {shouldTruncate ? truncateString(children) : children}
    </div>
  );
}

const longText = "Potentially long text";
export default function Application() {
  const [expanded, setExpanded] = useState(false);
  return (
    <main>
      {/* you can only use expanded if truncated is included */}
      <Text truncate expanded={expanded} id="Text" style={{ color: "red" }}>
        {longText}
      </Text>
      <section style={{ marginTop: "1em" }}>
        <button onClick={() => setExpanded(!expanded)}>
          {expanded ? "Contract" : "Expand"}
        </button>
      </section>
      {/* ERROR - no overload matches this */}
      <Text expanded={expanded}>{longText}</Text>
      {/* OK */}
      <Text truncate>{longText}</Text>
    </main>
  );
}
```

### [Context API Edge Cases](https://stevekinney.github.io/react-and-typescript/create-context)

- Context API Edge Cases, eliminating `as` cast
- [Video](https://frontendmasters.com/courses/react-typescript/context-api-edge-cases/)

## Migrating from JS

- [TS handbook guide](https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html)
- [Project Example](https://github.com/Microsoft/TypeScript-React-Conversion-Guide#typescript-react-conversion-guide)
