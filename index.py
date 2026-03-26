"""
╔══════════════════════════════════════════════════════╗
║         CS QUIZ — Computer Science & Tech           ║
║         Built by Muhammad Wudaid                    ║
║         BSc (Hons) Creative Computing               ║
╚══════════════════════════════════════════════════════╝

A terminal-based quiz app with:
 - 10 Computer Science & Tech questions
 - Multiple choice answers (A/B/C/D)
 - Timed questions with countdown
 - Score tracking with per-question feedback
 - Visual results screen with grade & bar chart
 - Play again loop

Requirements: Python 3.6+  (no external libraries needed)
Run with:     python quiz_app.py
"""

import time
import os
import sys
import random

# ─────────────────────────────────────────────
#  COLOUR HELPERS  (ANSI escape codes)
# ─────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BG_DARK = "\033[40m"

def clr(text, *codes):
    return "".join(codes) + str(text) + C.RESET

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ─────────────────────────────────────────────
#  QUESTION BANK  (20 questions, 10 picked randomly)
# ─────────────────────────────────────────────
ALL_QUESTIONS = [
    {
        "question": "What does 'CPU' stand for?",
        "options": ["A) Central Processing Unit", "B) Core Power Unit",
                    "C) Central Program Utility", "D) Computer Processing Unit"],
        "answer": "A",
        "explanation": "CPU stands for Central Processing Unit — the primary component that executes instructions."
    },
    {
        "question": "Which data structure operates on a LIFO (Last In, First Out) principle?",
        "options": ["A) Queue", "B) Linked List", "C) Stack", "D) Tree"],
        "answer": "C",
        "explanation": "A Stack is LIFO — the last item pushed is the first to be popped, like a stack of plates."
    },
    {
        "question": "What is the time complexity of binary search on a sorted array?",
        "options": ["A) O(n)", "B) O(n²)", "C) O(n log n)", "D) O(log n)"],
        "answer": "D",
        "explanation": "Binary search halves the search space each step, giving O(log n) time complexity."
    },
    {
        "question": "Which protocol is used to assign IP addresses automatically on a network?",
        "options": ["A) FTP", "B) DHCP", "C) DNS", "D) HTTP"],
        "answer": "B",
        "explanation": "DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses to devices."
    },
    {
        "question": "In Python, what does the 'def' keyword do?",
        "options": ["A) Defines a variable", "B) Declares a class",
                    "C) Defines a function", "D) Imports a module"],
        "answer": "C",
        "explanation": "'def' is used in Python to define (declare) a function."
    },
    {
        "question": "What does HTML stand for?",
        "options": ["A) Hyper Text Markup Language", "B) High Tech Modern Language",
                    "C) Hyper Transfer Markup Logic", "D) Home Tool Markup Language"],
        "answer": "A",
        "explanation": "HTML stands for HyperText Markup Language — the standard language for web pages."
    },
    {
        "question": "Which sorting algorithm has the best average-case time complexity?",
        "options": ["A) Bubble Sort", "B) Selection Sort", "C) Quick Sort", "D) Insertion Sort"],
        "answer": "C",
        "explanation": "Quick Sort has an average-case of O(n log n), making it one of the fastest in practice."
    },
    {
        "question": "What is a 'deadlock' in operating systems?",
        "options": [
            "A) A program that runs forever",
            "B) Two or more processes waiting on each other indefinitely",
            "C) When a CPU overheats and stops",
            "D) A corrupted file system"
        ],
        "answer": "B",
        "explanation": "A deadlock occurs when two or more processes each hold a resource the other needs, creating a standstill."
    },
    {
        "question": "Which layer of the OSI model is responsible for routing packets?",
        "options": ["A) Data Link Layer", "B) Transport Layer",
                    "C) Network Layer", "D) Session Layer"],
        "answer": "C",
        "explanation": "The Network Layer (Layer 3) handles logical addressing and routing of data packets."
    },
    {
        "question": "What is the base of the hexadecimal number system?",
        "options": ["A) 2", "B) 8", "C) 10", "D) 16"],
        "answer": "D",
        "explanation": "Hexadecimal is base-16, using digits 0–9 and letters A–F to represent values."
    },
    {
        "question": "Which of these is NOT an object-oriented programming language?",
        "options": ["A) Java", "B) Python", "C) C", "D) C++"],
        "answer": "C",
        "explanation": "C is a procedural language, not object-oriented. Java, Python and C++ all support OOP."
    },
    {
        "question": "What does 'RAM' stand for?",
        "options": ["A) Read Access Memory", "B) Random Access Memory",
                    "C) Rapid Application Memory", "D) Readable Array Module"],
        "answer": "B",
        "explanation": "RAM stands for Random Access Memory — volatile memory used for temporary data storage."
    },
    {
        "question": "Which CSS property is used to change the text colour?",
        "options": ["A) font-color", "B) text-color", "C) color", "D) foreground"],
        "answer": "C",
        "explanation": "In CSS, 'color' is the correct property for setting text colour. 'font-color' doesn't exist."
    },
    {
        "question": "What is the purpose of a foreign key in a relational database?",
        "options": [
            "A) To encrypt data in a table",
            "B) To uniquely identify each row",
            "C) To link two tables together",
            "D) To index a column for faster search"
        ],
        "answer": "C",
        "explanation": "A foreign key links a column in one table to the primary key of another, establishing a relationship."
    },
    {
        "question": "In version control (Git), what does 'git commit' do?",
        "options": [
            "A) Uploads changes to GitHub",
            "B) Saves a snapshot of staged changes to the local repository",
            "C) Creates a new branch",
            "D) Merges two branches"
        ],
        "answer": "B",
        "explanation": "'git commit' saves staged changes as a snapshot in your local repo. 'git push' uploads to remote."
    },
    {
        "question": "What does an API (Application Programming Interface) do?",
        "options": [
            "A) Designs the visual layout of an app",
            "B) Stores user data securely",
            "C) Allows different software systems to communicate",
            "D) Compiles source code into machine code"
        ],
        "answer": "C",
        "explanation": "An API defines how software components interact, allowing different systems to communicate."
    },
    {
        "question": "Which of the following best describes 'machine learning'?",
        "options": [
            "A) Programming a robot to move",
            "B) Writing code that fixes itself",
            "C) Training algorithms to learn patterns from data",
            "D) Using computers to simulate human emotions"
        ],
        "answer": "C",
        "explanation": "Machine learning is a subset of AI where algorithms learn patterns from data to make predictions."
    },
    {
        "question": "What is the function of a DNS server?",
        "options": [
            "A) Assigns IP addresses to devices",
            "B) Translates domain names to IP addresses",
            "C) Encrypts internet traffic",
            "D) Manages file transfers between servers"
        ],
        "answer": "B",
        "explanation": "DNS (Domain Name System) translates human-readable domain names (e.g. google.com) into IP addresses."
    },
    {
        "question": "In Python, which keyword is used to handle exceptions?",
        "options": ["A) catch", "B) error", "C) except", "D) handle"],
        "answer": "C",
        "explanation": "Python uses 'try/except' blocks for exception handling. 'catch' is used in Java/JavaScript."
    },
    {
        "question": "What is the main advantage of using a linked list over an array?",
        "options": [
            "A) Faster random access",
            "B) Less memory usage overall",
            "C) Dynamic size — efficient insertions and deletions",
            "D) Better cache performance"
        ],
        "answer": "C",
        "explanation": "Linked lists can grow and shrink dynamically and allow O(1) insertions/deletions at known positions."
    },
]

# ─────────────────────────────────────────────
#  UI COMPONENTS
# ─────────────────────────────────────────────
BANNER = f"""
{clr('╔══════════════════════════════════════════════════════╗', C.CYAN, C.BOLD)}
{clr('║', C.CYAN, C.BOLD)}  {clr('CS QUIZ', C.YELLOW, C.BOLD)}  {clr('·', C.DIM)}  Computer Science & Technology       {clr('║', C.CYAN, C.BOLD)}
{clr('║', C.CYAN, C.BOLD)}  {clr('by Muhammad Wudaid', C.DIM)}  ·  BSc (Hons) Creative Computing  {clr('║', C.CYAN, C.BOLD)}
{clr('╚══════════════════════════════════════════════════════╝', C.CYAN, C.BOLD)}
"""

def print_banner():
    print(BANNER)

def print_divider(char="─", width=56, color=C.DIM):
    print(clr(char * width, color))

def print_progress_bar(current, total, width=40):
    filled = int((current / total) * width)
    bar = "█" * filled + "░" * (width - filled)
    pct = int((current / total) * 100)
    print(f"  {clr(bar, C.CYAN)}  {clr(f'{pct}%', C.YELLOW, C.BOLD)}")

def print_timer_bar(seconds_left, total=15, width=30):
    filled = int((seconds_left / total) * width)
    color = C.GREEN if seconds_left > 8 else C.YELLOW if seconds_left > 4 else C.RED
    bar = "▓" * filled + "░" * (width - filled)
    print(f"  ⏱  {clr(bar, color)}  {clr(str(seconds_left) + 's', color, C.BOLD)}", end="\r")

def grade(score, total):
    pct = (score / total) * 100
    if pct == 100: return "S", C.YELLOW,  "Perfect Score! Legendary! 🏆"
    if pct >= 80:  return "A", C.GREEN,   "Excellent work! 🌟"
    if pct >= 60:  return "B", C.CYAN,    "Good job! Well done. 👍"
    if pct >= 40:  return "C", C.MAGENTA, "Not bad, keep studying! 📚"
    return            "D", C.RED,     "Keep practising — you'll get there! 💪"

def print_results_screen(score, total, results, time_taken):
    clear_screen()
    print_banner()
    print(clr("  RESULTS", C.BOLD, C.WHITE))
    print_divider("═")

    # Grade
    g, color, msg = grade(score, total)
    print(f"\n  Grade:  {clr(f' {g} ', color, C.BOLD, C.BG_DARK)}  {clr(msg, color)}")
    print(f"  Score:  {clr(str(score), C.YELLOW, C.BOLD)} / {total}   ({clr(f'{int(score/total*100)}%', C.YELLOW, C.BOLD)})")
    print(f"  Time:   {clr(f'{time_taken:.1f}s', C.CYAN)} total\n")

    # Bar chart
    print(clr("  Performance Chart", C.BOLD, C.WHITE))
    print_divider()
    for i, r in enumerate(results):
        tick = clr("✓", C.GREEN, C.BOLD) if r["correct"] else clr("✗", C.RED, C.BOLD)
        q_short = r["question"][:38] + "…" if len(r["question"]) > 38 else r["question"].ljust(39)
        time_bar_len = min(int(r["time"] * 1.5), 20)
        time_bar = clr("▪" * time_bar_len, C.BLUE)
        q_time_str = f"{r['time']:.1f}s"
        print(f"  {clr(str(i+1).zfill(2), C.DIM)}  {tick}  {clr(q_short, C.WHITE)}  {time_bar} {clr(q_time_str, C.DIM)}")

    # Summary breakdown
    correct_count = sum(1 for r in results if r["correct"])
    wrong_count = total - correct_count
    avg_time = sum(r["time"] for r in results) / total

    print_divider()
    print(f"\n  {clr('✓ Correct:', C.GREEN, C.BOLD)}   {correct_count}")
    print(f"  {clr('✗ Incorrect:', C.RED, C.BOLD)} {wrong_count}")
    print(f"  {clr('⏱ Avg time:', C.CYAN, C.BOLD)}  {avg_time:.1f}s per question\n")

    # Show wrong answers
    wrongs = [r for r in results if not r["correct"]]
    if wrongs:
        print(clr("  Review — Questions you missed:", C.YELLOW, C.BOLD))
        print_divider()
        for r in wrongs:
            print(f"\n  {clr('Q:', C.DIM)} {clr(r['question'], C.WHITE)}")
            print(f"  {clr('Your answer:', C.RED)}   {r['your_answer']}")
            print(f"  {clr('Correct answer:', C.GREEN)} {r['correct_answer']}")
            print(f"  {clr('Why:', C.CYAN)} {r['explanation']}")

    print_divider("═")

# ─────────────────────────────────────────────
#  TIMED INPUT
# ─────────────────────────────────────────────
def get_answer_timed(time_limit=15):
    """Get user input with a visible countdown timer."""
    import threading

    answer = [None]
    timed_out = [False]

    def get_input():
        try:
            raw = input(f"\n  {clr('Your answer (A/B/C/D):', C.CYAN, C.BOLD)} ").strip().upper()
            answer[0] = raw if raw in ['A', 'B', 'C', 'D'] else None
        except (EOFError, KeyboardInterrupt):
            answer[0] = None

    print()
    t = threading.Thread(target=get_input, daemon=True)
    t.start()

    start = time.time()
    while t.is_alive():
        elapsed = time.time() - start
        remaining = max(0, time_limit - elapsed)
        print_timer_bar(int(remaining), time_limit)
        if elapsed >= time_limit:
            timed_out[0] = True
            break
        time.sleep(0.25)

    print(" " * 50, end="\r")  # clear timer line

    t.join(timeout=0.1)

    elapsed = time.time() - start
    return answer[0], min(elapsed, time_limit), timed_out[0]

# ─────────────────────────────────────────────
#  MAIN QUIZ LOOP
# ─────────────────────────────────────────────
def run_quiz():
    clear_screen()
    print_banner()

    print(clr("  Welcome to the CS Quiz!", C.WHITE, C.BOLD))
    print(f"  {clr('10 questions', C.YELLOW)} on Computer Science & Technology.")
    print(f"  {clr('15 seconds', C.YELLOW)} per question. Answer with A, B, C or D.\n")
    print_divider()
    input(f"\n  {clr('Press ENTER to start...', C.CYAN, C.BOLD)}")

    questions = random.sample(ALL_QUESTIONS, 10)
    score = 0
    results = []
    quiz_start = time.time()

    for i, q in enumerate(questions):
        clear_screen()
        print_banner()

        # Progress
        print(f"  Question {clr(str(i+1), C.YELLOW, C.BOLD)} of {clr('10', C.YELLOW, C.BOLD)}\n")
        print_progress_bar(i, 10)
        print_divider()

        # Question text
        print(f"\n  {clr(q['question'], C.WHITE, C.BOLD)}\n")

        # Options
        option_colors = [C.CYAN, C.MAGENTA, C.GREEN, C.YELLOW]
        for j, opt in enumerate(q['options']):
            letter = opt[0]  # "A", "B", etc.
            rest   = opt[2:] # text after "A) "
            print(f"    {clr(f'[{letter}]', option_colors[j], C.BOLD)}  {clr(rest, C.WHITE)}")

        # Get answer
        user_ans, q_time, timed_out = get_answer_timed(time_limit=15)

        # Evaluate
        if timed_out or user_ans is None:
            print(f"\n  {clr('⏰ Time up!', C.RED, C.BOLD)}")
            user_ans = "—"
            correct = False
        elif user_ans == q['answer']:
            print(f"\n  {clr('✓ Correct!', C.GREEN, C.BOLD)}")
            score += 1
            correct = True
        else:
            print(f"\n  {clr('✗ Incorrect.', C.RED, C.BOLD)}  Correct answer: {clr(q['answer'], C.GREEN, C.BOLD)}")
            correct = False

        # Explanation
        print(f"  {clr('💡 ' + q['explanation'], C.DIM)}")

        # Score so far
        print_divider()
        print(f"  Score so far: {clr(str(score), C.YELLOW, C.BOLD)} / {i+1}")

        results.append({
            "question":       q["question"],
            "correct":        correct,
            "your_answer":    user_ans,
            "correct_answer": q["answer"],
            "explanation":    q["explanation"],
            "time":           round(q_time, 1),
        })

        time.sleep(1.4)

    total_time = time.time() - quiz_start
    print_results_screen(score, 10, results, total_time)

    # Play again
    again = input(f"\n  {clr('Play again? (Y/N):', C.CYAN, C.BOLD)} ").strip().upper()
    if again == 'Y':
        run_quiz()
    else:
        print(f"\n  {clr('Thanks for playing! — Muhammad Wudaid', C.YELLOW, C.BOLD)}\n")
        sys.exit(0)

# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print(f"\n\n  {clr('Quiz exited. See you next time!', C.YELLOW)}\n")
        sys.exit(0)