import openai
import json
from utils import log_event, handle_error, chunk_content, format_insights

# Load configuration settings
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

OPENAI_API_KEY = config.get('OPENAI_API_KEY', '')
ANTHROPIC_API_KEY = config.get('ANTHROPIC_API_KEY', '')
API_SELECTION = config.get('api_selection', 'openai')
INSIGHT_COUNT = config.get('insight_count', 10)
CONTEXT_WINDOW_SIZE = config.get('chunk_size', 2048)

# Initialize the OpenAI or Anthropic API client based on the configuration
if API_SELECTION == 'openai' and OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY
elif API_SELECTION == 'anthropic' and ANTHROPIC_API_KEY:
    # Placeholder for Anthropic API client initialization
    # anthropic.api_key = ANTHROPIC_API_KEY
    pass
else:
    raise ValueError("API key for the selected model is not provided in config.json")

def generate_summary(content):
    """
    Generates a summary for the given content using the selected language model.
    If the content is too large, it chunks the content to fit the model's context window.
    
    :param content: The content to summarize.
    :return: A dictionary with the summary and key insights.
    """
    try:
        # Chunk the content if it's too large
        chunks = chunk_content(content, CONTEXT_WINDOW_SIZE)

        # Initialize summary data
        summary_data = {
            'summary': '',
            'key_insights': []
        }

        # Process each chunk
        for chunk in chunks:
            # Generate the summary for the chunk
            if API_SELECTION == 'openai':
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Summarize the following content into {INSIGHT_COUNT} key insights:\n\n{chunk}",
                    max_tokens=150
                )
                summary = response.choices[0].text.strip()
            elif API_SELECTION == 'anthropic':
                # Placeholder for Anthropic API call
                # summary = anthropic.generate_summary(chunk, INSIGHT_COUNT)
                summary = "Anthropic summary placeholder"
            else:
                raise ValueError("Invalid API selection in config.json")

            # Format the insights
            formatted_insights = format_insights(summary, INSIGHT_COUNT)

            # Append to the summary data
            summary_data['summary'] += summary + '\n\n'
            summary_data['key_insights'].extend(formatted_insights)

        return summary_data

    except Exception as e:
        handle_error(e)
        log_event(f"Error generating summary: {str(e)}", "LOG_ERROR")
        return None
