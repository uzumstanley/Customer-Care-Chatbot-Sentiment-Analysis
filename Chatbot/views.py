import subprocess
import re
import time
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration, pipeline
from django.http import JsonResponse
from django.shortcuts import render
import os
import warnings

# Set the path for Node.js and npx
os.environ["PATH"] += os.pathsep + r"C:\Program Files\nodejs"

warnings.filterwarnings("ignore", category=UserWarning, module='transformers')

# Load Pre-trained Model and Tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Load Hugging Face sentiment analysis pipeline
sentiment_classifier = pipeline('sentiment-analysis', model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')


# Define chatbot response logic with name and perfect response
def chatbot_response(user_input, conversation_history):
    # Analyze sentiment
    sentiment = sentiment_classifier(user_input)[0]
    sentiment_label = sentiment['label']
    sentiment_score = sentiment['score']
    
    # Customized responses based on common customer care scenarios
    if "refund" in user_input.lower():
        bot_reply = "To request a refund, please visit our support page or contact customer service at Tbiggest4@gmail.com."
    elif "order status" in user_input.lower():
        bot_reply = "You can check your order status by logging into your account on our website."
    elif "support" in user_input.lower():
        bot_reply = "Feel free to reach us at Tbiggest4@gmail.com for further assistance."
    else:
        # Generate response from BlenderBot model for general queries
        inputs = tokenizer([user_input], return_tensors="pt")
        reply_ids = model.generate(inputs['input_ids'], max_length=100, pad_token_id=tokenizer.eos_token_id)
        bot_reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    
    # Adjust chatbot tone based on sentiment analysis
    if sentiment_label == "NEGATIVE" and sentiment_score > 0.9:
        bot_reply += " I understand this might be frustrating. How else can I assist you?"

    # Prepend the chatbot's name (T.Biggest) to the response
    bot_reply = f"T.Biggest: {bot_reply}"

    # Update the conversation history
    conversation_history.append(f"User: {user_input}")
    conversation_history.append(f"Bot: {bot_reply}")
    
    return bot_reply, conversation_history

# Django view to render the chatbot interface
def index(request):
    # Initialize conversation history in session
    if 'conversation_history' not in request.session:
        request.session['conversation_history'] = []
    
    return render(request, 'chatbot/index.html')

# Django view for processing chatbot responses
def chatbot_response_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        # Handle case where user_input might be empty
        if not user_input:
            return JsonResponse({'response': "Please enter a valid message."})
        
        # Retrieve conversation history from session
        conversation_history = request.session.get('conversation_history', [])
        
        # Get bot response
        try:
            bot_reply, conversation_history = chatbot_response(user_input, conversation_history)
        except Exception as e:
            return JsonResponse({'response': f"An error occurred: {str(e)}"})
        
        # Update session with new conversation history
        request.session['conversation_history'] = conversation_history
        
        return JsonResponse({'response': bot_reply})
