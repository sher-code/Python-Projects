import tkinter as tk
from tkinter import messagebox

quiz_questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Islamabad", "Karachi", "Lahore", "Quetta"],
        "answer": "Islamabad"
    },
    {
        "question": "Who developed Python language?",
        "options": ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x300")

        self.q_index = 0
        self.score = 0
        self.username = ""

        # Welcome screen
        self.welcome_frame = tk.Frame(root)
        self.welcome_frame.pack(fill="both", expand=True)

        tk.Label(self.welcome_frame, text="Welcome to the Quiz App!", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.welcome_frame, text="Enter your name:", font=("Arial", 12)).pack()
        self.name_entry = tk.Entry(self.welcome_frame, font=("Arial", 12))
        self.name_entry.pack(pady=10)

        tk.Button(self.welcome_frame, text="Start Quiz", command=self.start_quiz).pack()

        # Quiz screen
        self.quiz_frame = tk.Frame(root)

        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 14), wraplength=450)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(self.quiz_frame, text="", variable=self.var, value="", font=("Arial", 12))
            rb.pack(anchor="w", padx=20)
            self.options.append(rb)

        self.next_btn = tk.Button(self.quiz_frame, text="Next", command=self.next_question)
        self.next_btn.pack(pady=20)

    def start_quiz(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name to start.")
            return
        self.username = name
        self.welcome_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        self.load_question()

    def load_question(self):
        question_data = quiz_questions[self.q_index]
        self.question_label.config(text=question_data["question"])
        self.var.set(None)
        for i, option in enumerate(question_data["options"]):
            self.options[i].config(text=option, value=option)

    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        correct_answer = quiz_questions[self.q_index]["answer"]
        if selected == correct_answer:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(quiz_questions):
            self.load_question()
        else:
            with open("results.txt", "a") as file:
                file.write(f"Name: {self.username} - Score: {self.score}/{len(quiz_questions)}\n")

            messagebox.showinfo("Quiz Completed", f"{self.username}, your score is {self.score}/{len(quiz_questions)}\nSaved to 'results.txt'")
            self.root.destroy()

# Run app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
