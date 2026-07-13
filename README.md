# Medical Study Assistant - Multi-Turn Conversation Exercise

## Overview

This exercise demonstrates a **multi-turn AI conversation** with an AI Medical Study Assistant that maintains conversation state and context retention across multiple turns. The assistant is built using the **Anthropic Claude API** and showcases how to build stateful conversational AI applications.

## What This Exercise Demonstrates

### Core Concepts Implemented

1. **Conversation Memory**: The assistant remembers all previous messages in the conversation
2. **Context Retention**: Information about the selected disease (Diabetes) is maintained throughout
3. **Natural Interruptions**: The conversation includes an unrelated question (weather) that is handled gracefully while maintaining focus
4. **Comprehensive Topic Exploration**: The disease is explored in depth across 12+ turns covering:
   - Causes and types
   - Symptoms and diagnosis methods
   - Stages/severity levels
   - Treatment options
   - Medications and their mechanisms
   - Lifestyle recommendations
   - Prevention strategies
   - Complications and comorbidities
   - Patient management protocols
   - Follow-up care

### Conversation Flow

1. **Initial Setup**: Student asks about multiple diseases
2. **Topic Selection**: Student chooses Diabetes for deeper exploration
3. **Interruption Handling**: Student asks an unrelated question about weather
4. **Focus Maintenance**: Assistant redirects back to Diabetes while maintaining context
5. **Deep Exploration**: 12+ turns exploring various aspects of Diabetes

## Architecture

### Key Components

- **Anthropic Client**: Uses `anthropic` Python SDK to interact with Claude API
- **System Prompt**: Defines the assistant's role, behavior, and constraints
- **Conversation History**: Maintains a list of all messages to provide context to the model
- **Multi-turn Logic**: Sequences through pre-defined turns to demonstrate the exercise

### How It Works

```
User Input
    ↓
Add to Conversation History
    ↓
Send History + System Prompt to Claude API
    ↓
Receive Response
    ↓
Add Response to History
    ↓
Display to User
```

Each API call includes:
- **System Prompt**: Instructions for the assistant's behavior
- **Full Message History**: All previous turns in the conversation
- **User Input**: The current message

This ensures Claude has complete context for generating appropriate responses.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Anthropic API Key (stored in `.env` file)

### Installation Steps

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Environment Variable**:
   The `.env` file should contain:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

3. **Run the Exercise**:
   ```bash
   python medical_assistant.py
   ```

## Project Files

- **medical_assistant.py**: Main application file containing:
  - System prompt definition
  - Conversation loop logic
  - Pre-defined conversation turns
  - Interactive mode option
  - Summary output

- **requirements.txt**: Python dependencies:
  - `anthropic`: Anthropic Python SDK
  - `python-dotenv`: Environment variable loader

- **.env**: Contains your API credentials

- **README.md**: This file

## Running the Exercise

### Mode 1: Pre-defined Exercise (Recommended for First Run)

The script runs a complete multi-turn conversation demonstrating:
- 14+ conversation turns
- Proper context maintenance
- Graceful handling of interruptions
- Comprehensive medical topic exploration

Simply run:
```bash
python medical_assistant.py
```

The conversation will display with `[Student]:` and `[Assistant]:` labels, showing how the assistant maintains context throughout.

### Mode 2: Interactive Mode

After the pre-defined exercise completes, you can choose to enter interactive mode where you can have your own free-form conversation with the Medical Assistant.

## Technical Details

### System Prompt Strategy

The system prompt instructs Claude to:
1. Answer only medical-related questions
2. Maintain conversation context
3. Remember previously discussed conditions
4. Politely redirect non-medical topics
5. Provide comprehensive medical explanations

### Context Management

- Each turn appends the new message to the conversation history
- The entire history is sent with each API request
- This allows Claude to maintain perfect context awareness
- The model understands which disease was selected and remembers discussions about it

### Conversation State

The conversation maintains:
- User inputs (what the student asks)
- Assistant responses (medical explanations)
- Chronological order (turns happen in sequence)
- Full context (nothing is forgotten)

## Example Conversation Flow

```
Turn 1:  Student asks about multiple diseases → Assistant lists several diseases
Turn 2:  Student chooses Diabetes → Assistant begins detailed explanation
Turn 3:  Student asks about causes and symptoms → Assistant explains thoroughly
Turn 4:  Student asks about weather (interruption) → Assistant redirects
Turn 5+: Student continues exploring Diabetes → Assistant maintains focus on Diabetes
```

## Key Learning Outcomes

After studying this exercise, you'll understand:

1. **How to Build Stateful Conversations**: Maintaining message history for context
2. **System Prompts**: How to guide AI behavior through instructions
3. **API Integration**: Working with Anthropic's Claude API
4. **Conversation Design**: Creating natural, multi-turn interactions
5. **Context Retention**: Ensuring AI remembers important information
6. **Edge Case Handling**: Managing interruptions and off-topic questions

## Extending the Exercise

You can modify this exercise to:

- Change the domain (e.g., IT Support, Legal Consulting)
- Adjust the number of conversation turns
- Add different types of interruptions
- Implement conversation logging/analytics
- Add user feedback mechanisms
- Test different conversation strategies

## Troubleshooting

### API Key Issues
- Ensure `.env` file is in the same directory as `medical_assistant.py`
- Verify the API key is valid and hasn't expired
- Check that `python-dotenv` is installed

### Import Errors
- Run `pip install -r requirements.txt` to install all dependencies
- Ensure Python 3.8+ is being used

### Rate Limiting
- The Anthropic API has rate limits; if you encounter errors, wait a moment and retry
- For production use, implement exponential backoff

## Summary

This exercise demonstrates production-grade conversational AI by showing:
- ✓ Stateful conversation management
- ✓ Context retention across interruptions
- ✓ Domain-specific AI behavior
- ✓ Professional conversation flows
- ✓ API integration best practices

The implementation is clean, well-commented, and can serve as a template for building similar conversational AI applications.
