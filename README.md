# Shopping Discount Calculator

## Overview

This is a **Python-based shopping discount calculator** that helps users keep track of their shopping expenses, discounts, and savings. It supports multiple items, calculates the discounted price per item, and provides a clear summary including whether the user stays within their budget.

## Features

- Input multiple shopping items with price and discount percentage.
- Automatically calculate savings and final price per item.
- Summarise total cost before and after discounts.
- Compare total cost with user budget and notify if within or over budget.
- Input validation for price and discount to ensure proper values.
- User-friendly interactive command-line interface.

## How It Works

1. The user sets a shopping budget.
2. For each item, the user enters:
   - Item name
   - Item price
   - Discount percentage (0% to 100%)
3. The program calculates:
   - Discount amount per item
   - Final price after discount
   - Total costs and savings across all items
4. After entering all items, the program prints a detailed summary showing individual item details and whether the user is within budget.

## Usage

Run the program in a Python 3 environment:

```bash
python shopping_discount_calculator.py

```
## Example Output
```
~ Hi, Welcome to Shopping Counter! ~

Enter your shopping budget: $100

Enter item name: Shampoo
Enter price of Shampoo: $12.50
Enter discount for Shampoo (%): 10

Enter item name: T-shirt
Enter price of T-shirt: $25.00
Enter discount for T-shirt (%): 20

Enter item name: done

~Shopping Summary Lists~
> Shampoo: Original Price: $12.50 | Discount: 10.0% | Final price: $11.25 | Money saved: $1.25
> T-shirt: Original Price: $25.00 | Discount: 20.0% | Final price: $20.00 | Money saved: $5.00

~Total Shopping Cost~
Total before discounts: $37.50
Total saved: $6.25
Total after discounts: $31.25

Good job! you are within your budget! You have saved $68.75 from your budget.

^Thank you for using this service! Hope to see you again!^
```
## Technology Used
- Python 3
- Standard Python libraries (no external dependencies)


