# AI Mock Interview

Welcome to the AI Mock Interview project! This application simulates an interview scenario where an AI interacts with users, evaluates their responses, and provides feedback based on various metrics.

## Features

- **Human Recognition**: The AI can identify whether the user is a human or not using webcam input.
- **Speech Interaction**: Users can respond to AI-generated questions using voice input.
- **Emotion Analysis**: The AI analyzes the user's emotions throughout the interview.
- **Statistics Generation**: At the end of the interview, users receive detailed statistics, including:
  - Average time per question
  - Accuracy of answers
  - Confidence in answers
  - Topics discussed
  - Basic understanding of the topics
  - Areas for improvement
  - Average mood throughout the interview

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/saiisback/ai-mock-interview.git
   cd ai-mock-interview
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r app/requirements.txt
   ```

4. Configure API keys:
   - Create a file named `api_keys.py` in the `config` directory and add your API keys for OpenAI and emotion analysis.

### Running the Application

To start the application, run the following command:
```bash
python app/main.py
```

### API Endpoints

- **POST /start-interview**: Start the interview session.
  - **Request Body**:
    ```json
    {
      "video_stream": "base64_encoded_video_stream",
      "questions": ["What is your greatest strength?", "Describe a challenge you faced."]
    }
    ```

## Usage

1. Start the application and use a frontend interface to initiate the interview.
2. Follow the AI's prompts and respond as directed.
3. Review the statistics provided at the end of the session.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
