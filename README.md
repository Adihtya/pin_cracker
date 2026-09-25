# 🔐 4-Digit PIN Brute-Force Simulator

A simple Python project that demonstrates how a **brute-force attack** works by systematically testing every possible 4-digit PIN combination until the correct PIN is found.

This project is created for **educational purposes** to understand Python loops, string formatting, counters, execution-time measurement, and basic cybersecurity concepts.

---

## 📌 About the Project

A 4-digit numeric PIN can have **10,000 possible combinations**, ranging from:

```text
0000 → 9999
```

The program takes a 4-digit PIN as input and then starts testing combinations sequentially from `0000`.

For every attempt, it:

- Generates a 4-digit PIN
- Counts the attempt
- Displays the current guess
- Compares the guess with the entered PIN
- Stops when the correct PIN is found
- Displays the number of attempts and execution time

---

## ⚙️ How It Works

The program uses Python's `range()` function to generate all possible numbers from `0` to `9999`.

```python
for number in range(10000):
```

Each number is converted into a 4-digit PIN using:

```python
guess = f"{number:04d}"
```

For example:

```text
0     → 0000
7     → 0007
42    → 0042
123   → 0123
4829  → 4829
```

The generated PIN is then compared with the secret PIN:

```python
if guess == secret_pin:
```

When a match is found, the program stops using:

```python
break
```

---

## 🧠 Brute-Force Concept

A brute-force attack attempts possible combinations systematically rather than trying to predict the correct password.

For a 4-digit PIN:

```text
10 × 10 × 10 × 10 = 10,000
```

possible combinations exist.

The program searches through them in order:

```text
0000
0001
0002
0003
...
4829
```

If the PIN is `4829`, the program will stop when it reaches that combination.

---

## 🛠️ Technologies Used

- Python 3
- `time` module
- `for` loops
- `range()`
- `if` statements
- f-strings
- String comparison
- Counters

**No external libraries are required.**

---

## 📂 Project Structure

```text
PIN-Brute-Force/
│
├── pin_cracker.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed.

Check your Python version:

```bash
python3 --version
```

---

### Run the Project

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd PIN-Brute-Force
```

Run the program:

```bash
python3 pin_cracker.py
```

---

## 💻 Example

### Input

```text
Enter a 4-digit PIN to crack: 1234
```

### Output

```text
Starting brute-force attack...

Trying: 0000
Trying: 0001
Trying: 0002
...
Trying: 1233
Trying: 1234

==============================
       PIN FOUND!
==============================
PIN: 1234
Attempts: 1235
Time: 0.00xx seconds
```

The exact execution time will vary depending on the computer and Python environment.

---

## 📊 Attempt Calculation

The number of attempts depends on the position of the PIN in the search sequence.

| PIN | Attempts |
|---|---:|
| `0000` | 1 |
| `0001` | 2 |
| `0010` | 11 |
| `0100` | 101 |
| `1234` | 1,235 |
| `5000` | 5,001 |
| `9999` | 10,000 |

The maximum number of attempts is therefore:

```text
10,000
```

---

## ⏱️ Execution Time

The program measures the time required to find the PIN using Python's `time` module.

The starting time is recorded before the attack:

```python
start_time = time.time()
```

When the PIN is found, the ending time is recorded:

```python
end_time = time.time()
```

The total execution time is calculated as:

```python
end_time - start_time
```

---

## 📈 Time Complexity

For a fixed 4-digit PIN, the program can perform up to:

```text
10,000 attempts
```

Therefore, the search is:

```text
O(10,000)
```

For an `n`-digit numeric PIN, the search space becomes:

```text
10ⁿ
```

For example:

| PIN Length | Possible Combinations |
|---:|---:|
| 1 digit | 10 |
| 2 digits | 100 |
| 3 digits | 1,000 |
| 4 digits | 10,000 |
| 5 digits | 100,000 |
| 6 digits | 1,000,000 |
| 8 digits | 100,000,000 |

This demonstrates how increasing credential length dramatically increases the number of possible combinations.

---

## 🔐 Cybersecurity Learning

This project demonstrates the basic concept behind **brute-force attacks**.

In real authentication systems, security mechanisms are commonly used to reduce the effectiveness of repeated guessing, such as:

- Rate limiting
- Login attempt restrictions
- Account lockouts
- Increasing delays
- CAPTCHA
- Multi-factor authentication
- Strong password policies
- Security monitoring

---

## ⚠️ Disclaimer

This project is intended **only for educational and authorized testing purposes**.

Do not use brute-force techniques against accounts, devices, applications, or systems that you do not own or have explicit permission to test.

The program in this project operates only on a PIN manually entered by the user.

---

## 🎯 Learning Objectives

This project helped demonstrate:

- Python `for` loops
- `range()`
- User input
- String formatting
- f-strings
- Conditional statements
- Counters
- `break`
- Python modules
- Execution-time measurement
- Exhaustive search
- Basic cybersecurity concepts
- Search-space complexity

---

## 🔮 Future Improvements

Possible improvements include:

- [ ] Add input validation
- [ ] Add a progress bar
- [ ] Calculate attempts per second
- [ ] Support different PIN lengths
- [ ] Add multiple test cases
- [ ] Add performance statistics
- [ ] Create a graphical interface
- [ ] Visualize search progress
- [ ] Compare different PIN lengths

---

## 👨‍💻 Author

**Aditya Chaudhari**

B.Tech — Computer Science & Artificial Intelligence

### Interests

- Artificial Intelligence
- Cybersecurity
- Software Development
- Competitive Programming
- Problem Solving
- Emerging Technologies

---

## ⭐ Project Goal

The goal of this project is to understand how a simple brute-force algorithm works and how the size of a credential's search space affects the effort required to exhaustively search it.

> **Learn how the attack works → understand its limitations → understand how secure systems defend against it.**
