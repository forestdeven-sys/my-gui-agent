# GUI Agent MVP

This project is a simple, standalone Python application that acts as a "GUI Agent." It uses the Gemini API as its "brain" to generate a step-by-step plan and Selenium to control the Chrome browser as its "hands" to execute that plan.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project directory. Add your Gemini API key to this file as follows:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```
    Replace `your_api_key_here` with your actual Gemini API key.

3.  **Install dependencies:**
    Make sure you have Python 3 installed. Then, install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
    You will also need to have Google Chrome installed on your system. The script attempts to use `chromedriver` automatically, but if you encounter issues, you may need to install it manually and ensure it is in your system's PATH.

## How to Run

To run the GUI Agent, execute the `main.py` script from your command line and provide a mission as an argument.

**Example:**

```bash
python main.py "Create a Google Form"
```

The agent will then:
1.  Connect to the Gemini API to get a step-by-step plan for the mission.
2.  Open the Chrome browser.
3.  Execute the steps in the plan.

The application will print status updates to the console as it progresses.

**Note:** This is a Minimum Viable Product (MVP). The plan parsing and execution are very basic and may not handle complex or unexpected web page structures. The agent's ability to "see" or "understand" the page is limited to the simple commands defined in `action_engine.py`.
