
# Fixed Size Sliding Window Master Handbook (Interview-Oriented)

## Purpose

This document combines:

- Core fixed-size sliding window theory
- Your learning journey and observed mistakes
- Mental models
- Templates
- State design framework
- Deque & monotonic deque patterns
- Problem catalog with state hints
- Interview checklists

---

# Part 1: The Biggest Learning

At the start, most of the focus was on:

```text
How do lb and ub move?
```

Now the focus has evolved into:

```text
Objective
↓
Constraint
↓
State
↓
Invariant
↓
Evaluation
```

This is exactly the transition interviewers want to see.

You are no longer primarily debugging pointer movement.

You are debugging:

- state design
- invariants
- abstraction mistakes

That is a significant improvement.

---

# Part 2: Universal Fixed Window Template

## Mental Model

Every fixed-size window problem is:

```text
Expand
↓
Update state
↓
Shrink if size > k
↓
Evaluate if size == k
```

## Python Template

```python
lb = 0

for ub in range(len(nums)):

    # expand
    add_contribution(nums[ub])

    # shrink
    if ub - lb + 1 > k:
        remove_contribution(nums[lb])
        lb += 1

    # evaluate
    if ub - lb + 1 == k:
        evaluate()
```

---

# Part 3: Objective → Constraint → State

Before writing code:

## Step 1: Objective

Ask:

```text
What am I maximizing, minimizing, counting or returning?
```

Examples:

```text
Maximum sum
Count valid windows
Maximum distinct count
First negative
```

---

## Step 2: Constraint

Ask:

```text
What makes a window valid?
```

Examples:

```text
Window size = k
Distinct count = x
At least x evens
All unique elements
```

---

## Step 3: State

Ask:

```text
What information must be updated incrementally?
```

Examples:

| Requirement | State |
|------------|--------|
| Sum | running_sum |
| Even count | running_even |
| Odd count | running_odd |
| Distinct count | freq_map |
| First negative | deque |
| Maximum | monotonic deque |

---

# Part 4: Independent vs Derived State

One of the biggest lessons.

Bad:

```python
freq_map
distinct_count
```

when

```python
distinct_count == len(freq_map)
```

Good:

```python
freq_map
```

only.

Rule:

```text
If a state can be derived in O(1),
don't maintain it separately.
```

---

# Part 5: State Categories

## Category 1: Running Aggregate

Used when objective depends on totals.

Examples:

```python
running_sum
running_even
running_odd
running_vowel_count
```

Problems:

- Maximum sum subarray of size K
- Maximum average subarray
- Count windows with exactly X odds
- Maximum vowels in a substring

---

## Category 2: Frequency Map

Used when objective depends on occurrences.

Examples:

```python
freq_map[value] = count
```

Problems:

- Distinct count in every window
- Maximum distinct count
- Duplicate detection
- Exactly K distinct

---

## Category 3: Multiple States

Often needed in interview questions.

Examples:

```python
running_sum
+
freq_map
```

or

```python
running_sum
+
running_even_count
```

Problems:

- Maximum sum with all unique elements
- Maximum sum with exactly K distinct
- Maximum sum with at least X evens

---

## Category 4: Candidate Queue

Normal deque.

Used for:

```text
first
earliest
leftmost
```

Examples:

- First negative
- First vowel
- First repeating element

Invariant:

```text
dq[0] = first valid candidate
```

---

## Category 5: Monotonic Deque

Used for:

```text
maximum
minimum
largest
smallest
```

Invariant:

```text
dq[0] = best candidate
```

Examples:

- Sliding window maximum
- Sliding window minimum

---

# Part 6: First Negative Number Mental Model

Store:

```text
indices of negative numbers
```

When a negative enters:

```text
append index
```

When a negative leaves:

```text
remove from front
```

Evaluation:

```text
dq[0] = first negative
```

No scanning.

No recomputation.

---

# Part 7: Monotonic Deque Mental Model

The most important sentence:

```text
Deque stores candidates that can still win.
```

For maximum:

```python
while dq and nums[dq[-1]] < nums[ub]:
    dq.pop()
```

Meaning:

```text
Smaller candidate can never become maximum.
```

Remove it forever.

---

## Invariant

After processing each element:

```text
1. dq contains indices from current window
2. values are decreasing
3. dq[0] is maximum
```

---

# Part 8: Normal Deque vs Monotonic Deque

## Normal Deque

Question:

```text
Who arrived first?
```

Examples:

- First negative
- First vowel
- First repeating

---

## Monotonic Deque

Question:

```text
Who is best?
```

Examples:

- Maximum
- Minimum

---

# Part 9: The Index vs Value Mistake

One of the most frequent bugs.

Wrong:

```python
dq[0] & 1
```

Correct:

```python
nums[dq[0]] & 1
```

Rule:

```text
Deque stores indices.
Values are obtained through nums[index].
```

Mental check:

```text
What does dq[0] represent?
```

Always answer this before evaluation.

---

# Part 10: Common Mistakes Observed

## Mistake 1: Optimizing Wrong State

Example:

Maximum Sum of Distinct Elements.

Wrong:

```text
sum of distinct elements
```

Correct:

```text
sum of all elements
```

Constraint:

```text
all elements unique
```

Lesson:

```text
Track what objective depends on.
```

---

## Mistake 2: Mixing Objective and Constraint

Example:

Maximum element is even.

Needed:

```text
Track maximum
Then check parity
```

Not:

```text
Track all even elements
```

---

## Mistake 3: Redundant State

Maintaining:

```python
freq_map
distinct_count
```

when

```python
distinct_count = len(freq_map)
```

---

## Mistake 4: Using Monotonic Deque Everywhere

Not every deque problem is monotonic.

If problem says:

```text
first
earliest
leftmost
```

Use normal deque.

---

# Part 11: Interview Recognition Guide

If you see:

```text
sum
average
count
```

Think:

```text
running aggregate
```

---

If you see:

```text
distinct
duplicate
frequency
```

Think:

```text
freq_map
```

---

If you see:

```text
first
earliest
leftmost
```

Think:

```text
deque
```

---

If you see:

```text
maximum
minimum
largest
smallest
```

Think:

```text
monotonic deque
```

---

# Part 12: Problem Catalog

## Running Aggregate

### Maximum Sum Subarray of Size K
State Hint:

```text
running_sum
```

### Maximum Average Subarray of Size K
State Hint:

```text
running_sum
```

### Count Even Numbers in Every Window
State Hint:

```text
running_even_count
```

### Count Windows Having Exactly X Odd Numbers
State Hint:

```text
running_odd_count
```

### Maximum Number of Vowels in a Window
State Hint:

```text
running_vowel_count
```

---

## Frequency Map

### Distinct Count in Every Window
State Hint:

```text
freq_map
```

### Maximum Distinct Elements in Any Window
State Hint:

```text
freq_map
```

### Count Windows Having Exactly K Distinct Elements
State Hint:

```text
freq_map
```

### Count Windows Having At Least One Duplicate
State Hint:

```text
freq_map
```

---

## Multiple States

### Maximum Sum of Distinct Elements in Window
State Hint:

```text
running_sum
freq_map
```

### Maximum Sum Window Having Exactly K Distinct Elements
State Hint:

```text
running_sum
freq_map
```

### Maximum Sum Window Having At Least X Even Numbers
State Hint:

```text
running_sum
running_even_count
```

---

## Candidate Queue

### First Negative Number in Every Window
State Hint:

```text
deque of negative indices
```

### First Vowel in Every Window
State Hint:

```text
deque of vowel indices
```

### First Repeating Element in Every Window
State Hint:

```text
freq_map
deque
```

---

## Monotonic Deque

### Sliding Window Maximum
State Hint:

```text
monotonic decreasing deque
```

### Count Windows Where Maximum Element Is Even
State Hint:

```text
monotonic decreasing deque
```

### Sum of Maximum Elements of Every Window
State Hint:

```text
monotonic decreasing deque
```

---

## Dual Monotonic Deque

### Count Windows Where Max - Min <= X
State Hint:

```text
max deque
min deque
```

---

# Part 13: Fixed Window Checklist

Before coding:

```text
1. Objective?
2. Constraint?
3. State?
4. Can state be derived?
5. What does dq[0] represent?
6. When do I evaluate?
```

If all six are clear, implementation is usually straightforward.

---

# Final Assessment

Current Level:

```text
Comfortable with fixed-size sliding window fundamentals.
```

Strong Areas:

- Running aggregates
- Frequency maps
- Fixed window template
- State identification

Developing Areas:

- Faster state abstraction
- Monotonic deque recognition
- Avoiding objective/constraint confusion

Most Important Improvement:

```text
You have moved from pointer management
to invariant management.
```

That is the biggest sign of growth during this phase of interview preparation.
