# KHAOS code review: minimalism + complexity

## The performance contract

For each meaningful algorithm, state:
- Inputs: `n = number of users`, `m = number of records`, etc.
- Workload: expected and worst-case volumes, update frequency, latency target.
- Baseline: time complexity, memory complexity and the critical data access path.
- Decision: keep, optimize or measure — with justification.

**Never impose O(n) blindly.** The goal is to avoid *accidental expensive work*, not to force every algorithm to linear time. O(n log n) comparison sorts are normally fine; dense graph algorithms and required all-pairs calculations may be quadratic. The small-input simplest solution can be preferable.

## Classic hidden O(n²) join

Bad for large input (n users, m orders):

```ts
const views = users.map(user => ({
  ...user,
  orders: orders.filter(order => order.userId === user.id)
})); // time O(n*m), not O(n)
```

When repeated lookup is relevant, an index trades memory for speed:

```ts
const ordersByUser = new Map<string, Order[]>();
for (const order of orders) {
  const bucket = ordersByUser.get(order.userId) ?? [];
  bucket.push(order);
  ordersByUser.set(order.userId, bucket);
}
const views = users.map(user => ({
  ...user,
  orders: ordersByUser.get(user.id) ?? []
})); // expected time O(n+m), additional space O(m)
```

Map lookup is expected average O(1), not a deterministic worst-case complexity guarantee. Measure for real workload if this matters.

## Other recurring slop

- `.includes()` inside large loops: consider `Set` membership if repeated.
- N+1 DB/API queries: batch or join when the endpoint and workload justify it.
- Re-sort/re-filter expensive arrays on every render: compute when inputs change;
  do not add memoization blindly for tiny collections.
- Parse same payload repeatedly inside loops: parse once, reuse.
- Add queue/cache/microservice for 50 records: avoid premature infrastructure.
- New abstraction for one call site: use the direct implementation first.
- Install dependency for one standard-library operation: reuse built-ins.
- Silently swallow exceptions, duplicate authentication mechanisms, expose secrets.
- Huge unrelated refactor: keep diff reviewable; preserve contracts.

## Tests to require

- Unit test for a branch, loop, parser, monetary operation or security boundary.
- Error handling test for a failed external call and invalid input.
- If complexity is a selling point, benchmark with representative sizes and report
  method, hardware, samples and results; **no measured claims without measurement**.
- Verify the API and UI end-to-end; a passing build is not a working feature.

## Short review template

`Input size: ... / Baseline: O(...), space O(...) / Choice: ... / Why: ... / Tested: ... / Skipped: ...`

Inspired by the *principles* of Ponytail (YAGNI, reuse, smallest safe change), not a copy of Ponytail's skill. Upstream: https://github.com/DietrichGebert/ponytail
Community observations: https://www.reddit.com/r/cscareerquestions/comments/1oa5nx7/ai_slop_code_ai_is_hiding_incompetence_that_used/ and https://www.reddit.com/r/ExperiencedDevs/comments/1jfhqye
