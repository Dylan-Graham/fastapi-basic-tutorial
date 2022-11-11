---
id: ADR-FastAPI
title: API web framework
date: 2022-11-11
status: Proposed
deprecated by: null
---
# Context
We require a web framework that is python-based to build our api. The framework has to satisfy the following requirements:
1. Easy to get setup and develop features with.
2. Modern (compatible with python >=3.7) and easy to inegrate with other python packages.
3. Fast and highly performant.
4. Python based, most of our developers use python programming language.
# Decision
The decision has been made to move from PostgREST and use FastAPI.
# Consequences
All future API applications will be built/developed using FastAPI.