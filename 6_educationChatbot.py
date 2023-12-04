import random

class SimpleChatbot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def get_response(self, user_input):
        user_input = user_input.lower()
        response = "I'm sorry, I don't understand. Can you please rephrase your question?"

        for question, answer in self.knowledge_base.items():
            if question in user_input:
                response = answer
                break

        return response

def main():
    knowledge_base = {
        "what is your name": "I am a simple chatbot.",
        "how are you": "I don't have feelings, but thanks for asking!",
        "who is the president of the United States": "I'm sorry, I don't have real-time information.",
        "what is computer science": "Computer science is the study of computers and computational systems.",
        "who invented the internet": "The internet was developed by multiple people over time.",
        
        # Educational System Questions and Answers
        "what is the purpose of education": "The purpose of education is to provide individuals with knowledge, skills, and values needed for personal development and societal contribution.",
        "how many continents are there": "Geography is not directly related to the educational system, but there are seven continents: Africa, Antarctica, Asia, Europe, North America, Australia, and South America.",
        "what are the primary subjects in school": "Common subjects include mathematics, science, English, social studies, and physical education. However, it may vary depending on the educational system and grade level.",
        "who is considered the father of modern physics": "Albert Einstein is often considered the father of modern physics due to his groundbreaking contributions, such as the theory of relativity.",
        "what is the importance of literature in education": "Literature in education helps develop critical thinking, empathy, and language skills. It exposes students to different cultures and perspectives.",
        "how does online learning work": "Online learning involves using the internet to access educational materials and participate in virtual classes. It provides flexibility for students to learn at their own pace.",
        "what is the role of a teacher": "Teachers play a crucial role in facilitating learning, providing guidance, and creating a positive and inclusive learning environment.",
        "how does the grading system work": "Grading systems vary, but they typically involve assigning letter grades (A, B, C, etc.) or numerical scores to assess a student's performance in exams, assignments, and participation.",
    }

    chatbot = SimpleChatbot(knowledge_base)

    print("Simple Educational Chatbot:")
    print("You can start a conversation by asking questions. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
