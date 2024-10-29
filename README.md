# Customer Care Chatbot

**Customer Care Chatbot** is an AI-driven chatbot designed to handle customer inquiries efficiently and provide personalized responses. This project integrates natural language processing (NLP) models for sentiment analysis and text generation, allowing the chatbot to understand customer emotions and respond appropriately. It is built using Django and leverages cutting-edge deep learning models from Hugging Face.

## Table of Contents

- [Description]
- [Methodology]
- [Tools and Technologies]
- [Deployment Scenarios]
- [Project Screenshots]
- [Video Demo]

## Description

This project showcases a chatbot designed to enhance customer service by providing real-time, dynamic responses. The chatbot is capable of:
- **Responding to Common Queries**: It offers predefined responses for frequent inquiries, such as "refund" or "order status."
- **Context-Aware Conversations**: For general queries, it uses the **BlenderBot** model to generate thoughtful, contextually relevant responses.
- **Sentiment-Aware Interactions**: It adjusts the tone of its responses based on the user’s sentiment using **DistilBERT**, showing empathy for negative feedback.

## Methodology

The workflow of the chatbot is as follows:

1. **User Input**: The chatbot receives input from the user through a text-based interface.
2. **Sentiment Analysis**: The input is passed to a sentiment analysis model (DistilBERT) to determine if the sentiment is positive, neutral, or negative.
3. **Response Generation**:
   - If the input matches specific customer service scenarios (e.g., "refund"), the chatbot provides predefined responses.
   - If no match is found, the **BlenderBot** model generates a response based on the conversation context.
4. **Tone Adjustment**: If the sentiment is negative, the chatbot adjusts its response to be more empathetic and understanding.
5. **Response Display**: The generated response is then displayed on the front-end in a chat-like format.

## Tools and Technologies

- **BlenderBot Model**: Used for generating context-aware responses.
- **DistilBERT**: Pre-trained sentiment analysis model for identifying user emotions.
- **Django**: Backend framework to handle HTTP requests and manage the chatbot's logic.
- **HTML/CSS**: For building the chatbot's user interface.
- **JavaScript (AJAX)**: Allows real-time communication between the front-end and backend.
- **Python**: Powers the backend and integrates the machine learning models.

## Deployment Scenarios

This chatbot can be deployed in various environments such as:

- **Customer Service Platforms**: Automate responses to FAQs, improving the efficiency of customer support teams.
- **E-commerce Sites**: Handle real-time inquiries related to orders, refunds, or product availability.
- **Corporate Websites**: Provide automated helpdesk support to clients and employees, handling basic queries before escalating them to human agents.

## Project Screenshots

1. **Chatbot Interface**  
![Screenshot (69)](https://github.com/user-attachments/assets/7d35d0c8-1622-4c84-9ed6-d1c37fa6f359)

2. **HTML File**  
![Screenshot (71)](https://github.com/user-attachments/assets/3475fe24-0652-4a23-adaf-772e85d860d8)

3. **Django Settings.py**   
![Screenshot (70)](https://github.com/user-attachments/assets/01539963-2257-4cbd-ab63-c28a3fadf159)

## Video Demo


https://github.com/user-attachments/assets/fe2d3ce9-ffdc-4476-a5d4-63f55333c9d2
