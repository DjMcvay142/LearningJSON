# Learning JSON

A collection of practical exercises for learning JSON and Python file operations from the ground up.

## About

This repository documents my journey learning how to work with JSON files in Python. I'm building these skills for use in Discord bot development, where I need to persist user data between bot restarts.

## What I Learned

### Core Concepts
- Python file operations (reading, writing, appending)
- JSON structure and how it relates to Python dictionaries
- Converting between Python data and JSON format
- The `json` module (`dump`, `load`, `dumps`, `loads`)

### Practical Skills
- Handling missing files with try/except
- Working with multiple users in dictionary structures
- Modifying data in memory before saving
- Formatting JSON files for readability

## Exercises

**Exercise 1:** Basic file operations (write, read, append)

**Exercise 2:** Writing and reading JSON files & Modifying existing JSON data

**Exercise 3:** Handling files that don't exist with try/except

**Exercise 4:** Working with multiple users in a dictionary structure

**Exercise 5:** Making JSON readable with indent and sort_keys

## Key Takeaways

- JSON files can't be appended to like text files - you must read, modify, and rewrite
- Always handle FileNotFoundError when working with files that might not exist
- Use `indent=4` to make JSON files human-readable
- Dictionary structure with user IDs as keys is ideal for Discord bots

## Next Steps

Apply these concepts to my Discord bot project for persistent user data storage.
