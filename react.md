# React

## [Hooks in depth](https://btholt.github.io/complete-intro-to-react-v7/)

- [Code sandbox with all hooks](https://codesandbox.io/s/github/btholt/react-hooks-examples-v4/tree/main/?file=/src/index.js)

- [useContext](https://btholt.github.io/complete-intro-to-react-v7/lessons/hooks-in-depth/usecontext): eliminates prop drilling, by creating "a wormhole where stuff goes in and a wormhole in a child component where that same data comes out and the stuff in the middle doesn't know it's there"
- [useRef](https://btholt.github.io/complete-intro-to-react-v7/lessons/hooks-in-depth/useref): ref vs state, ref will be the most update the value vs stateNumber is what is captured in the closure
  - use this when you need the most up to date, current thing across renders. Ex. referencing a html DOM

```js
function incrementAndDelayLogging() {
  setStateNumber(stateNumber + 1);
  numRef.current++;
  setTimeout(
    () => alert(`state: ${stateNumber} | ref: ${numRef.current}`),
    1000
  );
}
```

- [useReducer](https://btholt.github.io/complete-intro-to-react-v7/lessons/hooks-in-depth/usereducer): rather than having many functions to update properties, have one reducer that does it based on action type, preferable when state updates are complex

- [useMemo](https://btholt.github.io/complete-intro-to-react-v7/lessons/hooks-in-depth/usememo): this along with useCallback are performance optimizations, useMemo memoizes expensive functions such that they are only re-evaluated as needed
  - in this case, `fibonacci` will only be called if num changes, rather than on render
  -

```js
const fibonacci = (n) => {
  if (n <= 1) return 1;
  return fibonacci(n - 1) + fibonacci(n - 2);
};

const MemoComponent = () => {
  const [num, setNum] = useState(1);
  // This will be very slow
  // const fib = fibonacci(num);
  const fib = useMemo(() => fibonacci(num), [num]);
```

- [useCallback](https://btholt.github.io/complete-intro-to-react-v7/lessons/hooks-in-depth/usecallback):

```js
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

- "Pass an inline callback and an array of dependencies. useCallback will return a memoized version of the callback that only changes if one of the dependencies has changed. This is useful when passing callbacks to optimized child components that rely on reference equality to prevent unnecessary renders"
- `useCallback(fn, deps)` equivalent to `useMemo(() => fn, deps)`
- Below, we use it to make sure that React is handing the same fibonacci to ExpensiveComputationComponent every time so it passes its React.memo check every single time. Now it's only if count changes will it actually re-render (as evidenced by the time.)
  - Typically memo is used with useCallback

```js
// memo checks props and only re-render if they change, is needed for this example
const ExpensiveComputationComponent = memo(({ compute, count }) => {
  return (
    <div>
      <h1>computed: {compute(count)}</h1>
      {/* If date is updated then it is re-rendered */}
      <h4>last re-render {new Date().toLocaleTimeString()}</h4>
    </div>
  );
});

export default function CallbackComponent() {
  const [time, setTime] = useState(new Date());
  const [count, setCount] = useState(1);
  useEffect(() => {
    const timer = setTimeout(() => setTime(new Date()), 1000);
    return () => clearTimeout(timer);
  });

  const fibonacci = (n) => {
    if (n <= 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
  };

  return (
    <div>
      <h1>useCallback Example {time.toLocaleTimeString()}</h1>
      <button onClick={() => setCount(count + 1)}>
        current count: {count}
      </button>
      <ExpensiveComputationComponent
        // compute={fibonacci} <- this will be very slow on renders
        compute={useCallback(fibonacci, [])}
        count={count}
      />
    </div>
  );
}
```

- [useLayoutEffect](https://btholt.github.io/complete-intro-to-react-v7/lessons/hooks-in-depth/uselayouteffect): like useEffect, except it is synchronous. i.e. after react renders the next call will be useLayoutEffect. Should only be using this hook to measure DOM nodes for things like animations

```ts
export default function LayoutEffectComponent() {
  const [width, setWidth] = useState(0);
  const el = useRef();

  useLayoutEffect(() => {
    setWidth(el.current.clientWidth);
  });

  return (
    <div>
      <h1>useLayoutEffect Example</h1>
      <h2>textarea width: {width}px</h2>
      <textarea
        onClick={() => {
          setWidth(0);
        }}
        ref={el}
      />
    </div>
  );
}
```

- [useImperativeHandle](https://btholt.github.io/complete-intro-to-react-v7/lessons/hooks-in-depth/useimperativehandle):
  - must be used with forwardRef, typically this is used by library development
  - ["customizes the instance value that is exposed to parent components when using ref"](https://reactjs.org/docs/hooks-reference.html#useimperativehandle)
- [useDebugValue](https://btholt.github.io/complete-intro-to-react-v7/lessons/hooks-in-depth/usedebugvalue): allows you to surface information from your custom hook into the dev tools

<br/>

## [Testing](https://btholt.github.io/complete-intro-to-react-v7/lessons/testing/testing-react)

- test from user perspective rather than developer, don't test implementation details
- Used `data-testid` id, pro decouple from CSS
- To test custom hooks, a generic component was created to run the hook
- use `jest-fetch-mock` to mock fetch
- https://frontendmasters.com/courses/intermediate-react-v4/snapshots/
