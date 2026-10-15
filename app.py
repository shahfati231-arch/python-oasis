from flask import Flask, render_template_string

app = Flask(__name__)

# Ultimate Python Oasis - Blue, Matcha & Pink Aesthetic with 4 Quiz Tasks & Expanded Sandbox
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Oasis - Learn, Test & Code</title>
    <style>
        :root {
            --matcha-primary: #588157;
            --matcha-light: #a3b18a;
            --matcha-bg: #f4f7f2;
            --blue-deep: #1d3557;
            --blue-accent: #457b9d;
            --blue-soft: #e0fbfc;
            --pink-accent: #ff69b4;
            --pink-soft: #fff0f5;
            --pink-deep: #c71585;
            --card-shadow: 0 15px 35px rgba(29, 53, 87, 0.1);
        }

        body {
            background: linear-gradient(135deg, #f4f7f2 0%, #fff0f5 50%, #e0fbfc 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: var(--blue-deep);
            margin: 0;
            padding: 40px 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 950px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.97);
            padding: 50px;
            border-radius: 24px;
            box-shadow: var(--card-shadow);
            border: 2px solid #ffb6c1;
            transform: perspective(1000px);
            transition: transform 0.5s ease;
        }

        h1 {
            color: var(--pink-deep);
            text-align: center;
            font-size: 3.2em;
            margin-bottom: 5px;
            font-weight: 800;
            letter-spacing: -1px;
        }

        .subtitle {
            text-align: center;
            color: var(--matcha-primary);
            font-style: italic;
            margin-bottom: 40px;
            font-size: 1.3em;
            font-weight: 500;
        }

        h2 {
            color: var(--blue-accent);
            border-bottom: 2px solid var(--pink-accent);
            padding-bottom: 8px;
            margin-top: 45px;
            font-size: 1.7em;
        }

        p, li {
            line-height: 1.8;
            font-size: 1.12em;
            color: #334155;
        }

        ul {
            padding-left: 20px;
        }

        /* 3D Elevated Card Effects */
        .info-card, .quiz-box, .sandbox-box {
            background: #ffffff;
            border: 2px solid var(--matcha-light);
            padding: 30px;
            border-radius: 18px;
            margin-top: 35px;
            box-shadow: 0 8px 20px rgba(88, 129, 87, 0.08);
            transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        }

        .info-card:hover, .quiz-box:hover, .sandbox-box:hover {
            transform: translateY(-6px) scale(1.01);
            box-shadow: 0 20px 40px rgba(255, 105, 180, 0.15);
            border-color: var(--pink-accent);
        }

        .code-box {
            background-color: var(--blue-deep);
            border-left: 6px solid var(--pink-accent);
            padding: 20px;
            font-family: 'Fira Code', monospace;
            border-radius: 10px;
            margin: 25px 0;
            color: #f1faee;
            box-shadow: inset 0 2px 5px rgba(0,0,0,0.2);
        }

        .score-display {
            font-size: 1.3em;
            font-weight: bold;
            color: var(--pink-deep);
            background: var(--pink-soft);
            padding: 12px 20px;
            border-radius: 12px;
            display: inline-block;
            margin-bottom: 20px;
            border: 1px solid var(--pink-accent);
        }

        button {
            background: linear-gradient(135deg, var(--pink-accent), #db7093);
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 1.05em;
            font-weight: 600;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(255, 105, 180, 0.3);
        }

        button:hover {
            background: linear-gradient(135deg, #db7093, var(--pink-accent));
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(255, 105, 180, 0.4);
        }

        button:active {
            transform: translateY(1px);
        }

        input[type="text"] {
            padding: 12px 16px;
            width: 62%;
            border: 2px solid #ffb6c1;
            border-radius: 10px;
            font-size: 1.05em;
            margin-right: 10px;
            transition: border-color 0.3s ease;
        }

        input[type="text"]:focus {
            outline: none;
            border-color: var(--pink-accent);
            box-shadow: 0 0 0 3px rgba(255, 105, 180, 0.15);
        }

        textarea {
            width: 100%;
            height: 130px;
            padding: 15px;
            border: 2px solid #ffb6c1;
            border-radius: 10px;
            font-family: 'Fira Code', monospace;
            font-size: 1.05em;
            background-color: #fff5f8;
            color: var(--blue-deep);
            box-sizing: border-box;
            resize: vertical;
            transition: border-color 0.3s ease;
        }

        textarea:focus {
            outline: none;
            border-color: var(--pink-accent);
            box-shadow: 0 0 0 3px rgba(255, 105, 180, 0.15);
        }

        .feedback {
            margin-top: 12px;
            font-weight: 600;
        }

        .terminal-output {
            background-color: #0f172a;
            color: #34d399;
            padding: 15px;
            border-radius: 10px;
            font-family: 'Fira Code', monospace;
            margin-top: 15px;
            min-height: 45px;
            white-space: pre-wrap;
            border-left: 4px solid var(--pink-accent);
        }

        .aesthetic-banner {
            text-align: center;
            font-size: 2em;
            letter-spacing: 8px;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="aesthetic-banner">
            🌸 🌿 💧 🌷 🌸
        </div>
        <h1>Python Oasis</h1>
        <p class="subtitle">Where clean code, pink blossoms, and serene logic meet.</p>
        
        <!-- Extended Learning Module 1 -->
        <div class="info-card">
            <h2>What is Python?</h2>
            <p>Python is an interpreted, high-level, and general-purpose programming language created by Guido van Rossum and first released in 1991. Its design philosophy emphasizes code readability with its notable use of significant whitespace. Because of its clear syntax and object-oriented approach, it allows programmers to write clear, logical code for small and large-scale projects.</p>
            <p>Today, Python stands as one of the most dominant languages in the technology sector. It powers complex machine learning models, handles massive datasets in data science, drives backend infrastructure for major web platforms, and automates everyday tedious tasks effortlessly.</p>
        </div>

        <!-- Extended Learning Module 2 -->
        <div class="info-card">
            <h2>Why Learn Python & Core Concepts</h2>
            <ul>
                <li><strong>Easy to Read & Write:</strong> Python code resembles natural English grammar, lowering the learning curve for beginners.</li>
                <li><strong>Data Types:</strong> Python works with various data types, such as strings (text wrapped in quotes like <code>"Hello"</code>), integers (whole numbers like <code>42</code>), and floats (decimals like <code>3.14</code>).</li>
                <li><strong>Control Flow & Loops:</strong> Using loops like <code>for</code> and <code>while</code> allows developers to repeat blocks of code efficiently without rewriting lines manually.</li>
                <li><strong>Incredible Ecosystem:</strong> Frameworks like Flask for web apps and Pandas for data science provide pre-built tools for any problem.</li>
            </ul>
        </div>

        <!-- Code Example Showcase -->
        <div class="info-card">
            <h2>Your First Python Code Structure</h2>
            <p>To understand how Python executes instructions sequentially, examine this snippet utilizing variables, strings, and formatted outputs:</p>
            <div class="code-box">
                # Welcome to Python Oasis!<br>
                learner_name = "Future Developer"<br>
                streak_days = 5<br>
                print(f"Hello, {learner_name}! You have a {streak_days}-day coding streak.")
            </div>
        </div>

        <!-- Interactive Quiz Section -->
        <div class="quiz-box">
            <h2>🌷 The Greenhouse Quiz (4 Tasks)</h2>
            <div class="score-display">Your Points: <span id="score">0</span> 🌸</div>
            
            <!-- Question 1 -->
            <p><strong>Task 1:</strong> Which built-in Python function is used to display text or output onto the screen?</p>
            <input type="text" id="answer1" placeholder="Type answer...">
            <button onclick="checkAnswer(1)">Submit 1</button>
            <p id="feedback1" class="feedback"></p>

            <hr style="border: 0; border-top: 1px solid #ffb6c1; margin: 25px 0;">

            <!-- Question 2 -->
            <p><strong>Task 2:</strong> What symbol is used in Python to assign a value to a variable?</p>
            <input type="text" id="answer2" placeholder="Type answer...">
            <button onclick="checkAnswer(2)">Submit 2</button>
            <p id="feedback2" class="feedback"></p>

            <hr style="border: 0; border-top: 1px solid #ffb6c1; margin: 25px 0;">

            <!-- Question 3 -->
            <p><strong>Task 3:</strong> What specific Python data type is used to store text inside quotation marks (e.g., <code>"Python"</code>)?</p>
            <input type="text" id="answer3" placeholder="Type answer...">
            <button onclick="checkAnswer(3)">Submit 3</button>
            <p id="feedback3" class="feedback"></p>

            <hr style="border: 0; border-top: 1px solid #ffb6c1; margin: 25px 0;">

            <!-- Question 4 -->
            <p><strong>Task 4:</strong> Which keyword is commonly used in Python to create a loop that iterates over a sequence?</p>
            <input type="text" id="answer4" placeholder="Type answer...">
            <button onclick="checkAnswer(4)">Submit 4</button>
            <p id="feedback4" class="feedback"></p>
        </div>

        <!-- Interactive Code Playground / Sandbox -->
        <div class="sandbox-box">
            <h2>💧 Python Code Playground</h2>
            <p>Test your logic right here! Type your print statements below and click run to execute:</p>
            <textarea id="userCode">print("Hello from my Python Oasis!")
print("Learning Python is fun!")</textarea>
            <button onclick="runCode()">Run Code 🚀</button>
            <div class="terminal-output" id="terminalOutput">Terminal output will appear here...</div>
        </div>
    </div>

    <script>
        let score = 0;
        let answered = {1: false, 2: false, 3: false, 4: false};

        function checkAnswer(taskNum) {
            const inputField = document.getElementById('answer' + taskNum);
            const feedback = document.getElementById('feedback' + taskNum);
            const userAnswer = inputField.value.trim().toLowerCase();

            if (answered[taskNum]) {
                feedback.style.color = "#c71585";
                feedback.textContent = "You've already earned points for Task " + taskNum + "! 🌱";
                return;
            }

            let isCorrect = false;
            let correctMsg = "";

            if (taskNum === 1) {
                if (userAnswer === 'print' || userAnswer === 'print()') {
                    isCorrect = true;
                    correctMsg = "🎉 Correct! print() displays output.";
                }
            } else if (taskNum === 2) {
                if (userAnswer === '=') {
                    isCorrect = true;
                    correctMsg = "🎉 Correct! The equals sign (=) assigns variables.";
                }
            } else if (taskNum === 3) {
                if (userAnswer === 'string' || userAnswer === 'str') {
                    isCorrect = true;
                    correctMsg = "🎉 Correct! Text data is stored as a string.";
                }
            } else if (taskNum === 4) {
                if (userAnswer === 'for' || userAnswer === 'while') {
                    isCorrect = true;
                    correctMsg = "🎉 Correct! 'for' or 'while' handles loops.";
                }
            }

            if (isCorrect) {
                score += 10;
                document.getElementById('score').textContent = score;
                feedback.style.color = "#2e7d32";
                feedback.textContent = correctMsg;
                answered[taskNum] = true;
            } else {
                feedback.style.color = "#c62828";
                feedback.textContent = "❌ Not quite right. Give it another try!";
            }
        }

        function runCode() {
            const code = document.getElementById('userCode').value;
            const output = document.getElementById('terminalOutput');
            
            // Extract all print statements or text inside quotes safely
            const regex = /print\s*\(\s*["']([^"']*)["']\s*\)/g;
            let match;
            let results = [];
            
            while ((match = regex.exec(code)) !== null) {
                results.push(match[1]);
            }
            
            if (results.length > 0) {
                output.style.color = "#34d399";
                output.textContent = ">>> " + results.join("\\n>>> ");
            } else if (code.trim() !== "") {
                output.style.color = "#ffb6c1";
                output.textContent = ">>> Code parsed successfully (Make sure to use print(\"your text\")).";
            } else {
                output.style.color = "#f87171";
                output.textContent = ">>> Error: Sandbox is empty. Type a print statement!";
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)