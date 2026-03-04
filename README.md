# Syntexchub_RuleBased_ExpertSystem
## Overview
This project implements a simple Rule-based Expert system using forward chaining.
The system applies predefined IF-THEN rules to user provided facts and infers conclusions based on logical reasoning.

## Objective
The goal of this project is to demonstrate how an expert system can simulate decision-making using logical rules and inference.

## Features
- Rule engine using IF-THEN rules
- Accepts user facts as inputs
- Applies forward chaining inference
- Supports multi-step reasoning
- Logs reasoning steps for transparency

## How it works
1. The user provides initial facts(symptoms).
2. The system checks which rules are satisfied.
3. When conditions of a rule are met, the conclusion is added as a new fact.
4. The process continues until no new conclusions can be generated.

## Technologies used
- Python
- Basic rule inference logic
