# Day 05 - Smart Transport Load Balancing

**Full Name:** Nandini Badiginchala  
**L value (letters excluding spaces):** 19  
**PLI value:** 1  
**Applied Rule:** Rule B - Remove Very Light items  

## Problem Statement
Classify package weights into Very Light, Normal, Heavy, Overload, or Invalid entries. Apply personalized logic (PLI) based on the number of letters in the name.

## Approach / Logic Used
1. Take input weights and classify based on ranges.
2. Apply PLI rules based on L % 3.
3. Display final categorized weights and counts.

## Test Cases
Input: [4, 18, 70, -2, 30, 55, 0]  
Output: Very Light: [], Normal Load: [18], Heavy Load: [30, 55], Overload: [70], Invalid Entries: [-2], Total Valid Weights: 6, Affected items due to PLI: 2


