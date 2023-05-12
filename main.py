# Step 2: Import data list and question model 
from question_model import Question
from data import question_data

# Step 5: Import QuizBrain
from quiz_brain import QuizBrain

# Step 3: Create question bank using the question_data that has been imported (hint: loops >_>)

# 3a. Place to store our questions in the question back, i.e. an empty list
question_bank = []

# 3b. Loop through the question_data
for question in question_data:
    # 3c. Get a hold of question text and question answers fro the question_data list
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # 3d. Create a new question using imported Class
    new_question = Question(question_text, question_answer)
    # 3e. Add question to the question_bank list
    question_bank.append(new_question)
    
# 3f. test to see if the loop works
# print(question_bank)

# Step 6: Create new QuizBrain object using the QuizBrain Class and pass in the question_bank
quiz = QuizBrain(question_bank)
# 6a. Run the next_question method on the object we just created

# quiz.next_question()

# 7a. Create a "game loop" 
while quiz.still_has_questions():
    # 7b. Move the quiz.next_question() from step 6a into the while loop
    quiz.next_question()
    
    
# Step 9. Notify the user when the quiz is completed and show the final score
print("You have completed the quiz!", f"your final score was: {quiz.score}/{quiz.question_number}")