# Library Management System

## Overview
This project implements a simple Library Management System designed to handle the following operations efficiently:
- Search for books by title or author.
- Add new books to the system.

The system is implemented in Python and supports basic data attributes for each book.

---

## Design Considerations

### Data Attributes:
- **Mandatory**: Title, Authors, Genre, Publication Year.

### Functional Requirements:
1. Search for books:
   - By Title.
   - By Author.
2. Add a new book.

---

## Design Options

### Option A: Use a List of Dictionaries
- **Structure**: Each book is stored as a dictionary within a list.
- **Advantages**:
  - Easy to implement.
  - Simplistic approach for small-scale data.
- **Disadvantages**:
  - Linear search makes operations slower as the dataset grows.
  - Not suitable for handling very large datasets.

### Option B: Use a Dictionary with Title as Key
- **Structure**: Books are stored in a dictionary where the key is the title, and the value contains all attributes.
- **Advantages**:
  - Faster search by title (O(1)).
  - More scalable for larger datasets.
- **Disadvantages**:
  - Duplicate titles cannot be handled without extra logic.
  - Searching by author requires linear iteration.

---

## Chosen Design
We chose **Option A** (List of Dictionaries) due to its simplicity and the need for minimal upfront setup, as the system's scale is not expected to grow significantly.

---

## Code Implementation

### Usage Instructions
1. Run the script using Python 3.x.
2. Use the menu to search for books or add a new book.
3. Data is stored in memory for this version.