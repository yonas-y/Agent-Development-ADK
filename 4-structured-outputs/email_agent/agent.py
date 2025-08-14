from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

# ------ Define the output schema ------- #
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject of the email. Should be concise and descriptive."
        )
    body: str = Field(
        description="The body content of the email. Should provide detailed information."
        )

# ------ Create Email Generator Agent ------- #
root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    instruction= 
    """ 
        You are an email generation assistant. 
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Be concise and to the point.
        - Use a professional tone for business communication and friendly tone for colleague communication.
        - Include a greeting and closing.
        - Suggest relevant attachments if applicable (empty list if not needed).

        IMPORTANT:
        Your response MUST be valid JSON matching this structure:

        {
            "subject": "Subject line here",
            "body": "Email body content here with proper paragraphs and formatting."
        }

        Do not include any explanations or additional information outside of the JSON structure.
    """,
    description="An agent that generates email content.",
    output_schema=EmailContent,
    output_key="email"
)
