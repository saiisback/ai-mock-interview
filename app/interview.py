import time
from user_recognition import recognize_user
from emotion_analysis import analyze_emotions
from statistics import generate_statistics

def start_interview(data):
    user_recognition_result = recognize_user(data['video_stream'])
    if not user_recognition_result['is_human']:
        return {'message': 'Non-human detected. Interview cannot proceed.'}

    questions = data['questions']
    responses = []
    start_time = time.time()

    for question in questions:
        # AI speaks out the question
        print(question)
        response = input("Your response: ")  # Replace with speech recognition in the final version
        responses.append(response)

        # Analyze emotions
        emotions = analyze_emotions(response)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Generate statistics
    stats = generate_statistics(responses, elapsed_time)
    return stats
