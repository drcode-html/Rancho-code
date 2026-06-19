<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coding Quiz</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            max-width: 600px;
            margin: 40px auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
        }
        .question-block {
            margin-bottom: 20px;
        }
        .question-title {
            font-weight: bold;
            margin-bottom: 10px;
        }
        .choice-label {
            display: block;
            margin-bottom: 8px;
            cursor: pointer;
        }
        button {
            display: block;
            width: 100%;
            padding: 12px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 20px;
        }
        button:hover {
            background-color: #0056b3;
        }
        #results {
            margin-top: 30px;
            padding: 20px;
            border-radius: 5px;
            display: none;
        }
        .feedback {
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;
        }
        .correct { color: #28a745; font-weight: bold; }
        .incorrect { color: #dc3545; font-weight: bold; }
    </style>
</head>
<body>

    <h1>5-Question Coding Quiz</h1>
    <div id="quiz-container"></div>
    <button id="submit-btn">Submit Answers</button>
    <div id="results"></div>

    <script>
        // 1. Define the quiz questions, choices, and the index of the correct answer
        const quizData = [
            {
                question: "What does HTML stand for?",
                choices: [
                    "Hyper Text Markup Language",
                    "High Tech Modern Language",
                    "Hyperlink and Text Markup Language"
                ],
                correctAnswer: 0
            },
            {
                question: "Which symbol is used to indicate a single-line comment in JavaScript?",
                choices: [
                    "",
                    "//",
                    "/* comment */"
                ],
                correctAnswer: 1
            },
            {
                question: "What does CSS do?",
                choices: [
                    "Manages server-side databases",
                    "Styles the visual layout of a webpage",
                    "Creates interactive logic for user clicks"
                ],
                correctAnswer: 1
            },
            {
                question: "Which of these is a boolean value?",
                choices: [
                    "\"true\"",
                    "100",
                    "false"
                ],
                correctAnswer: 2
            },
            {
                question: "What is the correct syntax to print a message in the JavaScript console?",
                choices: [
                    "console.print(\"Hello\");",
                    "print.console(\"Hello\");",
                    "console.log(\"Hello\");"
                ],
                correctAnswer: 2
            }
        ];

        const quizContainer = document.getElementById('quiz-container');
        const submitBtn = document.getElementById('submit-btn');
        const resultsContainer = document.getElementById('results');

        // 2. Function to build the quiz HTML dynamically
        function buildQuiz() {
            quizData.forEach((currentQuestion, questionNumber) => {
                const questionBlock = document.createElement('div');
                questionBlock.classList.add('question-block');

                // Add the question text
                const questionTitle = document.createElement('div');
                questionTitle.classList.add('question-title');
                questionTitle.innerText = `${questionNumber + 1}. ${currentQuestion.question}`;
                questionBlock.appendChild(questionTitle);

                // Add the radio button choices
                currentQuestion.choices.forEach((choice, choiceNumber) => {
                    const label = document.createElement('label');
                    label.classList.add('choice-label');
                    
                    const radio = document.createElement('input');
                    radio.type = 'radio';
                    radio.name = `question${questionNumber}`;
                    radio.value = choiceNumber;

                    label.appendChild(radio);
                    label.appendChild(document.createTextNode(" " + choice));
                    questionBlock.appendChild(label);
                });

                quizContainer.appendChild(questionBlock);
            });
        }

        // 3. Function to calculate the score and display the results
        function showResults() {
            let score = 0;
            let resultsHTML = "<h2>Your Results</h2>";

            quizData.forEach((currentQuestion, questionNumber) => {
                // Find the selected answer for this specific question
                const selector = `input[name=question${questionNumber}]:checked`;
                const userAnswerElement = document.querySelector(selector);
                const userAnswer = userAnswerElement ? parseInt(userAnswerElement.value) : null;

                resultsHTML += `<div class="feedback">`;
                resultsHTML += `<strong>Q: ${currentQuestion.question}</strong><br>`;

                if (userAnswer === currentQuestion.correctAnswer) {
                    score++;
                    resultsHTML += `<span class="correct">✓ Correct!</span>`;
                } else {
                    resultsHTML += `<span class="incorrect">✗ Incorrect.</span><br>`;
                    const correctAnswerText = currentQuestion.choices[currentQuestion.correctAnswer];
                    resultsHTML += `<em>The correct answer was: ${correctAnswerText}</em>`;
                }
                resultsHTML += `</div>`;
            });

            // Display final score
            resultsHTML = `<h3>You scored ${score} out of ${quizData.length}!</h3>` + resultsHTML;
            
            resultsContainer.innerHTML = resultsHTML;
            resultsContainer.style.display = 'block';
            resultsContainer.style.backgroundColor = '#e9ecef';
            
            // Disable the submit button after submitting
            submitBtn.disabled = true;
            submitBtn.innerText = "Quiz Submitted";
            submitBtn.style.backgroundColor = "#ccc";
        }

        // 4. Initialize the quiz and set up the button click event
        buildQuiz();
        submitBtn.addEventListener('click', showResults);

    </script>
</body>
</html>