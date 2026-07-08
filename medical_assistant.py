#!/usr/bin/env python3
"""
Multi-turn AI Medical Study Assistant
This exercise demonstrates conversation memory and context retention
using the Anthropic Claude API.
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Initialize the Anthropic client
client = Anthropic()

# System prompt that defines the assistant's role and behavior
SYSTEM_PROMPT = """You are an AI Medical Study Assistant designed to help doctors and medical students learn about diseases and medical conditions. 

Your responsibilities:
1. Answer ONLY medical-related questions with accuracy and clarity
2. Maintain context of the entire conversation and remember previously discussed conditions
3. When students ask about unrelated topics (like weather), politely redirect them back to medical topics while still maintaining the conversation history
4. Provide comprehensive explanations covering causes, symptoms, diagnosis, stages, treatment, prevention, complications, patient management, medications, and lifestyle recommendations
5. Keep the conversation natural and educational

Important: Always remember what disease or condition was selected for deeper exploration, even if the conversation branches into unrelated questions. After handling interruptions, guide the conversation back to the medical topic.

When a student references a previously mentioned condition, recall that information and continue exploring it in depth."""


def run_medical_conversation():
    """Run a multi-turn medical study assistant conversation."""
    
    conversation_history = []
    
    print("=" * 70)
    print("MEDICAL STUDY ASSISTANT - Multi-turn Conversation Exercise")
    print("=" * 70)
    print("\nWelcome! I'm your AI Medical Study Assistant.")
    print("I'm here to help you learn about medical conditions and diseases.")
    print("Type 'quit' to exit the conversation.\n")
    print("-" * 70)
    
    # Initial greeting from the assistant
    initial_response = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": "Hello! I'm a medical student interested in learning about different diseases. Can you start by telling me about a few common diseases that are important for medical professionals to know about?"
        }]
    )
    
    assistant_message = initial_response.content[0].text
    conversation_history.append({
        "role": "user",
        "content": "Hello! I'm a medical student interested in learning about different diseases. Can you start by telling me about a few common diseases that are important for medical professionals to know about?"
    })
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    print("\n[Student]: Hello! I'm a medical student interested in learning about different diseases. Can you start by telling me about a few common diseases that are important for medical professionals to know about?")
    print(f"\n[Assistant]: {assistant_message}\n")
    print("-" * 70)
    
    # Continue the conversation with pre-defined turns to demonstrate the exercise
    conversation_turns = [
        "I found those explanations really helpful. I'm particularly interested in diabetes. Can you tell me more about diabetes in detail - what causes it, what are the symptoms, and how is it diagnosed?",
        "That's really informative. By the way, what's the weather like today?",
        "Anyway, going back to diabetes - you mentioned there are different types. Can you explain the stages or severity of diabetes and how they differ?",
        "What are the main treatment options for diabetes? Are there medications and lifestyle changes I should know about?",
        "How does diabetes affect patient management in a clinical setting? What should doctors monitor?",
        "What are the potential complications of untreated or poorly managed diabetes?",
        "Can you give me some specific medication names used in diabetes treatment and how they work?",
        "What lifestyle recommendations would you give to a diabetes patient to help manage their condition?",
        "How do we prevent diabetes in patients who are at risk? Are there screening methods?",
        "What are the follow-up care protocols for diabetic patients?",
        "How does diabetes interact with other conditions? What comorbidities should we watch for?",
        "Can you compare Type 1 and Type 2 diabetes in terms of patient management?",
        "What's the latest research or treatment approaches in diabetes care?",
        "How should we counsel patients about long-term prognosis and quality of life with diabetes?"
    ]
    
    turn_number = 1
    
    for user_input in conversation_turns:
        print(f"\n[Student]: {user_input}")
        
        # Add user message to conversation history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Get response from Claude
        response = client.messages.create(
            model="claude-opus-4-1-20250805",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=conversation_history
        )
        
        assistant_response = response.content[0].text
        
        # Add assistant response to conversation history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_response
        })
        
        print(f"\n[Assistant]: {assistant_response}")
        print("\n" + "-" * 70)
        
        turn_number += 1
    
    # Print conversation summary
    print("\n" + "=" * 70)
    print("CONVERSATION SUMMARY")
    print("=" * 70)
    print(f"\nTotal conversation turns: {len(conversation_history) // 2 + 1}")
    print(f"Total messages exchanged: {len(conversation_history)}")
    print("\nKey aspects demonstrated:")
    print("✓ Conversation memory maintained across all turns")
    print("✓ Context retention of the selected disease (Diabetes)")
    print("✓ Handling of unrelated questions (weather) with redirection")
    print("✓ Natural and continuous conversation flow")
    print("✓ Comprehensive medical information covering:")
    print("  - Causes and types")
    print("  - Symptoms and diagnosis")
    print("  - Stages/severity and treatment options")
    print("  - Medications and lifestyle recommendations")
    print("  - Prevention and complications")
    print("  - Patient management and follow-up care")
    print("\n" + "=" * 70)


def interactive_mode():
    """Allow for interactive conversation with the medical assistant."""
    
    conversation_history = []
    
    print("\n" + "=" * 70)
    print("INTERACTIVE MODE")
    print("=" * 70)
    print("\nYou can now have a free-form conversation with the Medical Assistant.")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Thank you for using the Medical Study Assistant. Goodbye!")
            break
        
        if not user_input:
            continue
        
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        response = client.messages.create(
            model="claude-opus-4-1-20250805",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=conversation_history
        )
        
        assistant_response = response.content[0].text
        conversation_history.append({
            "role": "assistant",
            "content": assistant_response
        })
        
        print(f"\nAssistant: {assistant_response}\n")


if __name__ == "__main__":
    # Run the pre-defined exercise demonstration
    run_medical_conversation()
    
    # Optionally, ask if user wants to continue in interactive mode
    print("\n\nWould you like to continue with interactive mode? (yes/no): ", end="")
    choice = input().strip().lower()
    
    if choice in ['yes', 'y']:
        interactive_mode()
