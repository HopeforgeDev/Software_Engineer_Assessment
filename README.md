# Technical Assessment Solutions

This repository contains solutions to three technical tasks focused on **chatbot design**, **performance testing optimization**, and **systematic debugging**. Below is an overview of each solution and how to navigate this repository.

---

## Table of Contents
1. [Chatbot Flow Design](#chatbot-flow-design)
2. [Performance Testing Exercise](#performance-testing-exercise)
3. [Systematic Debugging Exercise](#systematic-debugging-exercise)
4. [Repository Structure](#repository-structure)
5. [GitHub URL](#github-url)

---

## Chatbot Flow Design
### Overview
A multi-step chatbot flow designed to collect user information while minimizing attributes and handling edge cases. Key features:
- **Attributes Used**: `isReturningUser`, `userAge`, `lifestyleFlags` (encoded 3 booleans), `promoCodeValid`, etc.
- **Excluded Attributes**: `debugMode`, `mysteryFlag`, `serviceTimeRange` (redundant or irrelevant).
- **Logic**: Validates inputs (e.g., age ≥ 0), handles under-18 consent, and encodes lifestyle flags into a 3-bit binary.
- **Pseudo-Code**: See [Solution Details](#solution-details).

### Key Features
- Input validation and re-prompting.
- Branching logic for product/service selection.
- Regex validation for promo codes (`[A-Z]{3}\d{4}[!@#$%^&*]{2}[a-z]{3}`).

---

## Performance Testing Exercise
### Problem Statement
Select 2 out of 6 test cases for an ATM system to maximize functionality coverage.

### Solution
- **Optimal Pair**: **TC2 (Check Balance → Change PIN)** + **TC5 (Deposit → Transfer with Discount)**.
- **Covered Functionalities**:
  - F1 (Discount), F2 (Balance), F3 (Change PIN), F5 (Transfer), F6 (Deposit).
- **Uncovered Functionality**: F4 (View Statements).

---

## Systematic Debugging Exercise
### Scenario
Debugging inconsistent discounts for promo code `SAVE20` in an online bookstore.

### Steps Taken
1. **Replicate the Issue**: Tested with members/non-members and varying order totals.
2. **Code Review**: Found membership discounts overriding `SAVE20`.
3. **Root Cause**: Flawed conditional logic prioritizing member status over promo codes.
4. **Fix**: Enforced promo code priority and added unit tests.

### Key Code Snippet
```python
# Fixed discount logic
def apply_discount(order_total, promo_code, is_member):
    if promo_code == "SAVE20":
        return order_total * 0.8  # 20% discount enforced
    elif is_member:
        return order_total * 0.9  # Fallback member discount
