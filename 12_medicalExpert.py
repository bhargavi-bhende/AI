# Define symptom categories and possible values
symptoms = {
    "fever": {"high", "moderate", "low"},
    "cough": {"dry", "wet", "persistent"},
    "sore_throat": {"severe", "mild", "none"},
    "fatigue": {"severe", "moderate", "mild"},
    "muscle_aches": {"severe", "moderate", "mild"},
    "headache": {"throbbing", "dull", "sharp"},
}

# Define potential diagnoses and their associated symptoms
diagnoses = {
    "flu": {"fever", "cough", "fatigue", "headache"},
    "cold": {"cough", "sore_throat", "fatigue", "headache"},
    "dehydration": {"fever", "fatigue"},
    "muscle_strain": {"muscle_aches"},
}

# Define a function to check if a symptom is present for a given diagnosis
def has_symptom(diagnosis, symptom, value):
    return symptom in diagnoses[diagnosis] and value in symptoms[symptom]

# Function to diagnose based on user input
def diagnose():
    # Collect user input for each symptom
    user_symptoms = {}
    for symptom, values in symptoms.items():
        selected_value = input(f"Do you have {symptom.replace('_', ' ')}? ({'/'.join(values)}): ").lower()
        if selected_value in values:
            user_symptoms[symptom] = selected_value

    # Check for each diagnosis and calculate a score based on matching symptoms
    diagnosis_scores = {diagnosis: sum(has_symptom(diagnosis, symptom, user_symptoms.get(symptom)) for symptom in required_symptoms) for diagnosis, required_symptoms in diagnoses.items()}

    # Identify the most likely diagnosis based on the highest score
    most_likely_diagnosis = max(diagnosis_scores, key=diagnosis_scores.get)
    confidence = diagnosis_scores[most_likely_diagnosis] / len(diagnoses[most_likely_diagnosis])

    # Print the results
    print(f"\nMost likely diagnosis: {most_likely_diagnosis} (confidence: {confidence:.2%})")
    print("Please note: This is not a substitute for professional medical advice.")

# Run the diagnosis function
diagnose()

# Sample 1
# Do you have a fever? (high/moderate/low): none
# Do you have a cough? (dry/wet/persistent): none
# Do you have a sore throat? (severe/mild/none): none
# Do you have fatigue? (severe/moderate/mild): mild
# Do you have muscle aches? (severe/moderate/mild): severe
# Do you have a headache? (throbbing/dull/sharp): none

# Sample 2
# Do you have fever? (high/low/moderate): high
# Do you have cough? (wet/persistent/dry): dry
# Do you have sore throat? (none/severe/mild): mild
# Do you have fatigue? (severe/mild/moderate): mild
# Do you have muscle aches? (severe/mild/moderate): mild
# Do you have headache? (throbbing/dull/sharp): none

# Sample 3
# Do you have a fever? (high/moderate/low): high
# Do you have a cough? (dry/wet/persistent): wet
# Do you have a sore throat? (severe/mild/none): severe
# Do you have fatigue? (severe/moderate/mild): severe
# Do you have muscle aches? (severe/moderate/mild): moderate
# Do you have a headache? (throbbing/dull/sharp): throbbing