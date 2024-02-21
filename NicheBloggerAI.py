import openai
import logging
from openai import OpenAI

class NicheVerse:
    def __init__(self):
        self.conversation_memory = []
        self.client = OpenAI()  # API key is stored securely and not hard-coded
        self.niche = ""
        self.content_type = ""
        self.project_code = ""

    def generate_response(self, model_type, prompt, system_message=""):
        """
        Leveraging OpenAI to generate responses based on the user's input and the system's context.
        """
        messages = [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(model=model_type, messages=messages)   
        content = response.choices[0].message.content
        logging.info(f"Response: {content}")
        return content.strip()

    def set_niche(self, niche):
        """
        Set the target niche for content or code generation.
        """
        self.niche = niche

    def set_content_type(self, content_type):
        """
        Define the type of content to generate, e.g., blog post, ad copy, tutorial, or code snippet.
        """
        self.content_type = content_type

    def generate_niche_content(self, specifications):
        """
        Generate niche-specific content or code based on provided specifications.
        """
        system_message = f"Generate a {self.content_type} for {self.niche} niche. Specifications: {specifications}"
        prompt = f"Please write a {self.content_type.lower()} focusing on the following specifications: {specifications}"
        return self.generate_response('gpt-3.5-turbo', prompt, system_message)

    def display_niche_content(self, specifications):
        """
        Call the generate_niche_content function and print the result to the console.
        """
        niche_content = self.generate_niche_content(specifications)
        print(niche_content)

# Example usage
if __name__ == "__main__":
    niche_verse = NicheVerse()  # Creating an instance of NicheVerse
    # Setting the niche to 'sustainable gardening' and content type to 'blog post'
    niche_verse.set_niche('sustainable gardening')
    niche_verse.set_content_type('blog post')
    # Generating and displaying niche content with the specification of creating a home composting system
    niche_verse.display_niche_content('how to create a composting system at home')
