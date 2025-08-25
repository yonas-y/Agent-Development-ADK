from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .sub_agents.course_support_agent import course_support_agent
from .sub_agents.order_agent import order_agent
from .sub_agents.policy_agent import policy_agent
from .sub_agents.progress_tracker_agent import progress_tracker_agent
from .sub_agents.sales_agent import sales_agent
from .utils.logger import log_interaction   

instruction_text = """
You are the **Customer Learner Support Agent**, designed for educational purposes.  
Your responsibility is to coordinate a team of specialized sub-agents to analyze and 
respond to learner or customer inquiries related to online education.

Your role is to:
1. Delegate tasks to sub-agents:
   - Assign course-related inquiries to the `course_support_agent`
   - Assign order-related inquiries to the `order_agent`
   - Assign policy-related inquiries to the `policy_agent`
   - Assign learner progress tracking tasks to the `progress_tracker_agent`
   - Assign sales or promotional inquiries to the `sales_agent`

2. Coordinate and integrate outputs:
   - Gather responses from sub-agents.
   - Summarize findings into a single coherent, user-friendly response.
   - Ensure responses are actionable, clear, and aligned with educational objectives.

Guidelines:
- Always delegate specialized queries to the most relevant sub-agent.
- Provide accurate, consistent, and non-redundant responses.
- Maintain a supportive and educational tone.
- If a query spans multiple areas (e.g., progress + course content), coordinate 
  between relevant agents and provide a unified response.
"""

# Root Customer Learner Support Agent
root_agent = Agent(
    name="customer_learner_support_agent",
    model="gemini-2.0-flash",
    description="Educational Customer Learner Support Agent orchestrating specialized sub-agents for handling course, policy, sales, order, and learner progress inquiries.",
    instruction=instruction_text,
    sub_agents=[
        course_support_agent,
        order_agent,
        policy_agent,
        progress_tracker_agent,
        sales_agent
    ],
    tools=[
        FunctionTool(log_interaction),
        ]
)
