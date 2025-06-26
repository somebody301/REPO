import random

def main():
    print("Welcome to R.E.P.O. (Repository Exploration and Programming Operations)!")
    score = 0
    questions = [
        {
            "question": "What command initializes a new Git repository?",
            "answer": "git init"
        },
        {
            "question": "How do you stage all files for commit?",
            "answer": "git add ."
        },
        {
            "question": "What command commits staged changes with a message?",
            "answer": "git commit -m 'message'"
        },
        {
            "question": "How do you check the status of your repo?",
            "answer": "git status"
        },
        {
            "question": "What command creates a new branch named 'feature'?",
            "answer": "git branch feature"
        },
        {
            "question": "How do you switch to the branch 'main'?",
            "answer": "git checkout main"
        },
        {
            "question": "How do you push your commits to the remote repository?",
            "answer": "git push"
        },
        {
            "question": "What command pulls the latest changes from the remote repo?",
            "answer": "git pull"
        }
    ]

    random.shuffle(questions)

    for q in questions:
        print("\n" + q["question"])
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {q['answer']}")

    print(f"\nGame Over! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
