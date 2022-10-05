https://redux.js.org/tutorials/essentials/part-1-overview-concepts

- 1-way data flow: action -> state -> view
- action: something that happened in the app = type + payload
- reducer: function that takes current state + action, outputs new state
- store: redux state
  - dispatch: accepts action, only way to update state
- slice: collection of redux reducer logic and actions for a single feature in your app (typically defined together in a single file)

```ts
import { configureStore } from "@reduxjs/toolkit";
import usersReducer from "../features/users/usersSlice";
import postsReducer from "../features/posts/postsSlice";
import commentsReducer from "../features/comments/commentsSlice";

export default configureStore({
  reducer: {
    users: usersReducer,
    posts: postsReducer,
    comments: commentsReducer,
  },
});
```

```ts
//counterSlice.js
import { createSlice } from "@reduxjs/toolkit";

export const counterSlice = createSlice({
  name: "counter",
  initialState: {
    value: 0,
  },
  reducers: {
    increment: (state) => {
      // Redux Toolkit allows us to write "mutating" logic in reducers. It
      // doesn't actually mutate the state because it uses the immer library,
      // which detects changes to a "draft state" and produces a brand new
      // immutable state based off those changes
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    },
  },
});

console.log(counterSlice.actions.increment());

export const { increment, decrement, incrementByAmount } = counterSlice.actions;
// autocreated, {type: "counter/increment"}

export default counterSlice.reducer;
```

- You can only write "mutating" logic in Redux Toolkit's createSlice and createReducer because they use Immer inside! If you write mutating logic in reducers without Immer, it will mutate the state and cause bugs!
- skip thunk
- useSelector: select a value from state, auto runs on state changes
- useDispatch: gets the dispatch from the redux store

https://redux.js.org/tutorials/essentials/part-2-app-structure#what-youve-learned

https://redux.js.org/tutorials/essentials/part-3-data-flow#what-youve-learned

https://redux.js.org/tutorials/essentials/part-4-using-data#what-youve-learned

Redux middleware: extend the store, and allow you to:

- Execute extra logic when any action is dispatched (such as logging the action and state)
- Pause, modify, delay, replace, or halt dispatched actions
- Write extra code that has access to dispatch and getState
- Teach dispatch how to accept other values besides plain action objects, such as functions and promises, by intercepting them and dispatching real action objects instead
  Chart
  https://redux.js.org/tutorials/essentials/part-5-async-logic

- Thunk: piece of code that does some delayed work
  https://redux.js.org/tutorials/essentials/part-5-async-logic#what-youve-learned

https://redux.js.org/tutorials/essentials/part-6-performance-normalization#what-youve-learned

https://redux.js.org/tutorials/fundamentals/part-1-overview ???

https://redux.js.org/tutorials/essentials/part-7-rtk-query-basics
RTK query: data fetching and caching, addon to RTK

- data fetch & cache != state management
- 2 apis

  - createApi() - define set of endpoints, generally use this once per app and 1 api slice per base URL
  - fetchBaseQuery() - wrapper around fetch

- RTKQ - managing cached data
- createApi: needs baseQuery / endpoints, if reducerPath not given defaults to state.api
- hook convention
  - use - endpoint name caps - query / mutation
- hook result obj
  - data, undefined until response received
  - isLoading: is it currently making first request to server
  - isSuccess: successful request and data is available
  - isError: indicates last request had an error
  - error: serialized error object
- hook
  - isFetching: true for any request in progress
  - refetch: call to manually refetch
- RTKQ creates cache key for each unique endpoint + argument combination
- Query parameter must be a single value, if multiple is needed pass an object with multiple fields(a shallow compare will be used)

```ts
export const apiSlice = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: "/fakeApi" }),
  endpoints: (builder) => ({
    getPosts: builder.query({
      query: () => "/posts",
    }),
    getPost: builder.query({
      query: (postId) => `/posts/${postId}`,
    }),
    addNewPost: builder.mutation({
      query: (initialPost) => ({
        url: "/posts",
        method: "POST",
        // Include the entire post object as the body of the request
        body: initialPost, // body auto serialized
      }),
    }),
  }),
});

export const { useGetPostsQuery, useGetPostQuery, useAddNewPostMutation } =
  apiSlice;
```

- mutation hooks return array
  - trigger function, when called makes request to the server with given arguments
  - Obj about in progress request, isLoading

```ts
const [addNewPost, { isLoading }] = useAddNewPostMutation();

const onSavePostClicked = async () => {
  if (canSave) {
    try {
      // addNewPost returns a special promise with an .unwrap();
      await addNewPost({ title, content, user: userId }).unwrap();
      // post mutation success things...
    } catch (err) {
      console.error("Failed to save the post: ", err);
    }
  }
};
```

Tag: string/small obkect that lets you name certain types of data and invalidate portions of the cache. When cache tag is invalidated RTKQ auto refetches the endpoints marked with that tag

- Tag needs
  - tagTypes: array of string tag names
  - providesTags: set of tag describing the data in this query
  - invalidatesTags: array in mutation endpoints, what to invalidate when mutation is run

```ts
export const apiSlice = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: "/fakeApi" }),
  tagTypes: ["Post"], // just need matching string, could be 'anything'
  endpoints: (builder) => ({
    getPosts: builder.query({
      query: () => "/posts",
      providesTags: ["Post"],
      // auto refetch with addNewPost
    }),
    getPost: builder.query({
      query: (postId) => `/posts/${postId}`,
    }),
    addNewPost: builder.mutation({
      query: (initialPost) => ({
        url: "/posts",
        method: "POST",
        body: initialPost,
      }),
      invalidatesTags: ["Post"],
    }),
  }),
});
```

- RTK Query allows multiple components to subscribe to the same data, and will ensure that each unique set of data is only fetched once. When the number of active subscriptions goes down to 0, RTK Query starts an internal timer (default 60 seconds). If the timer expires before any new subscriptions for the data are added, RTK Query will remove that data from the cache automatically, because the app no longer needs the data. However, if a new subscription is added before the timer expires, the timer is canceled, and the already-cached data is used without needing to refetch it.
- RTK Query lets us define specific tags, which let us be more selective in invalidating data. These specific tags look like {type: 'Post', id: 123}.

```ts
export const apiSlice = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: "/fakeApi" }),
  tagTypes: ["Post"],
  endpoints: (builder) => ({
    getPosts: builder.query({
      query: () => "/posts",
      providesTags: (result = [], error, arg) => [
        "Post", // can invalidate all posts
        // invalidate single
        ...result.map(({ id }) => ({ type: "Post", id })),
      ],
    }),
    getPost: builder.query({
      query: (postId) => `/posts/${postId}`,
      providesTags: (result, error, arg) => [{ type: "Post", id: arg }],
    }),
    addNewPost: builder.mutation({
      query: (initialPost) => ({
        url: "/posts",
        method: "POST",
        body: initialPost,
      }),
      invalidatesTags: ["Post"],
    }),
    editPost: builder.mutation({
      query: (post) => ({
        url: `posts/${post.id}`,
        method: "PATCH",
        body: post,
      }),
      invalidatesTags: (result, error, arg) => [{ type: "Post", id: arg.id }],
    }),
  }),
});
```

https://redux-toolkit.js.org/rtk-query/usage/automated-refetching#tag-invalidation-behavior

https://redux.js.org/tutorials/essentials/part-8-rtk-query-advanced#selecting-users-data

Endpoints can define a `transformResponse` handler that can extract or modify the data received from the server before it's cached.

- RTK Query uses a "document cache" approach, not a "normalized cache" (like Apollo)
  - A fully normalized cache tries to deduplicate similar items across all queries, based on item type and ID
  - ex. getTodos(), getTodos({filter: 'odd'}), getTodo({id: 1})
  - Each of these query results would include a Todo object that looks like {id: 1}.
  - In a fully normalized de-duplicating cache, only a single copy of this Todo object would be stored.
- However, RTK Query saves each query result independently in the cache.
- However, if all the endpoints are consistently providing the same tags (such as {type: 'Todo', id: 1}), then invalidating that tag will force all the matching endpoints to refetch their data for consistency.

https://redux.js.org/tutorials/essentials/part-8-rtk-query-advanced#implementing-optimistic-updates

- RTK Query provides an onCacheEntryAdded endpoint lifecycle handler that lets us implement "streaming updates" to cached data

https://redux-toolkit.js.org/rtk-query/usage/queries
