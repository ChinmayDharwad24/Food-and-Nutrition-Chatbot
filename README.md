# Food-and-Nutrition-Chatbot

This is a simple chatbot that leverages Hugging Face's GPT-2 model to provide responses to queries about food, recipes, and nutrition. The application uses Streamlit for the user interface.

## Features
- Suggest recipes based on available ingredients.
- Provide nutritional information for various foods and dishes.
- Offer dietary advice tailored to specific health goals.
- Suggest ingredient substitutes.
- Provide cooking tips and techniques.

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- [PyTorch](https://pytorch.org/get-started/locally/) or [TensorFlow](https://www.tensorflow.org/install)
- [Hugging Face Transformers](https://huggingface.co/transformers/installation.html)
- [Streamlit](https://docs.streamlit.io/library/get-started/installation)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/food-nutrition-chatbot.git
   cd food-nutrition-chatbot
   ```


### Setup Instructions

1. **Create and Activate a Virtual Environment**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows: `env\Scripts\activate`
    ```
2. **Install Required Packages**
    ```sh
    pip install transformers streamlit
    pip install tensorflow
    ```

3. **Running the Application**

    Navigate to the project directory:

    ```sh
    cd path/to/food-nutrition-chatbot
    ```

    Run the Streamlit application:

    ```sh
    streamlit run app.py
    ```

    Open your web browser and go to:
    ```sh
    http://localhost:8501
    ```

### Evaluation and Testing

1. ***Usefulness of Responses:***
The chatbot provides relevant responses related to food, recipes, nutrition, and dietary advice. Users can ask questions about specific recipes, nutritional values of foods, dietary recommendations, ingredient substitutes, and cooking techniques.

2. ***Variety of Queries:***
The application handles a variety of queries, including but not limited to:

- "What are some healthy breakfast recipes?"
- "How many calories are in an apple?"
- "Can you suggest a substitute for butter in baking?"
- "What are the nutritional benefits of spinach?"
- "How can I cook chicken breast without drying it out?"

3. Users can explore different topics related to food and nutrition through natural language queries.

### API Documentation

The application integrates with the Hugging Face Transformers library for natural language processing using the GPT-2 model. For detailed documentation on using Transformers with Streamlit and setting up the environment, refer to:

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Additional Information

- Code Overview: The main application code is located in app.py.
- YouTube Video: For a demonstration of the application, please watch the YouTube video.