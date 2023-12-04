class MedicalChatbot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def get_response(self, user_input):
        user_input = user_input.lower()
        response = "I'm sorry, I don't understand. Can you please rephrase your question?"

        for keyword, answer in self.knowledge_base.items():
            if keyword in user_input:
                response = answer
                break

        return response

def main():
    knowledge_base = {
         "symptoms of flu": "Common symptoms of the flu include fever, cough, sore throat, body aches, and fatigue.",
        "how to prevent COVID-19": "To prevent COVID-19, practice good hygiene, wear masks, maintain social distancing, and get vaccinated.",
        "what is diabetes": "Diabetes is a chronic condition that affects how your body turns food into energy. There are different types of diabetes, including Type 1 and Type 2.",
        "first aid for burns": "For minor burns, run cool water over the affected area for at least 10 minutes. Do not use ice. Cover the burn with a clean, non-stick bandage.",
        "common causes of headaches": "Headaches can be caused by various factors, including stress, dehydration, lack of sleep, or underlying medical conditions. If persistent, consult with a healthcare professional.",
        "signs of a heart attack": "Common signs of a heart attack include chest pain or discomfort, shortness of breath, nausea, lightheadedness, and discomfort in other areas of the upper body.",
        "recommended daily water intake": "The recommended daily water intake varies but is generally around 8 glasses or 2 liters. Individual needs depend on factors like age, weight, and activity level.",
        "how to perform CPR": "To perform CPR, place the heel of your hand on the center of the person's chest, interlock fingers, and perform chest compressions. Follow with rescue breaths if trained.",
        "benefits of regular exercise": "Regular exercise has numerous benefits, including improved cardiovascular health, weight management, stress reduction, and enhanced mood.",
        "what is the purpose of vaccinations": "Vaccinations help prevent the spread of infectious diseases by stimulating the immune system to recognize and fight specific pathogens.",
        "how to relieve stress": "Stress relief techniques include deep breathing exercises, meditation, physical activity, and maintaining a healthy work-life balance.",
        "recommended daily intake of fruits and vegetables": "Aim for at least 5 servings of fruits and vegetables per day to ensure a diverse range of nutrients and promote overall health.",
        "common allergies and their symptoms": "Common allergies include pollen, pet dander, and certain foods. Symptoms may include sneezing, itching, hives, and respiratory problems.",
        "how to manage diabetes through diet": "Managing diabetes involves monitoring carbohydrate intake, eating a balanced diet, and maintaining a healthy weight. Consult with a healthcare professional for personalized advice.",
        "how to lower blood pressure naturally": "To lower blood pressure naturally, adopt a healthy diet (low in sodium), engage in regular physical activity, maintain a healthy weight, and manage stress.",
    }

    chatbot = MedicalChatbot(knowledge_base)

    print("Medical Chatbot:")
    print("You can ask medical-related questions. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
