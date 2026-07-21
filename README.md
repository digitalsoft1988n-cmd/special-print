# Special Print

> Beautiful terminal output for Python.

**Special Print** is a Python package that makes console output clean, structured, and visually appealing. Display variables, objects, dictionaries, and lists using boxes, tables, frames, panels, and other formatted layouts with a simple, intuitive API.

---

## Features

* 📦 Beautiful boxes and frames
* 📊 Formatted tables
* 🔍 Pretty-print variables and objects
* 🎨 Multiple border styles
* 🌈 Optional colors and themes
* 🌳 Tree view for nested data
* ⚡ Lightweight and easy to use

---

## Installation

```bash
pip install special-print
```

---

## Quick Start

```python
import special_print as sp

name = "Alice"
age = 24

sp.box("Hello, World!")
sp.vars(name, age)
```

Output:

```text
╭────────────────────╮
│ Hello, World!      │
╰────────────────────╯

╭────────────────────╮
│ name : Alice       │
│ age  : 24          │
╰────────────────────╯
```

---

## Examples

### Box

```python
sp.box("Special Print")
```

### Table

```python
sp.table([
    {"Name": "Alice", "Age": 24},
    {"Name": "Bob", "Age": 30},
])
```

### Frame

```python
sp.frame("Application Started")
```

### Pretty Print

```python
sp.pretty(data)
```

### Variables

```python
username = "admin"
logged_in = True

sp.vars(username, logged_in)
```

---

## Planned Features

* Panels
* Banners
* Tree rendering
* JSON formatting
* Markdown tables
* Progress bars
* Logging integration
* Custom themes
* Syntax highlighting

---

## Contributing

Contributions, ideas, and bug reports are welcome. Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.
