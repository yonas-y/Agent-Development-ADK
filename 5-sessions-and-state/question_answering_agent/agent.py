from google.adk.agents import Agent

question_answering_agent = Agent(
    name = "question_answering_agent",
    model = "gemini-2.0-flash",
    description= "Question answering agent",
    instruction= "You are a helpful assistant that answers questions about the user's preferences." \
    "" \
    "Here is some information about the user:" \
    "Name: {user_name}" \
    "Preferences: {user_preferences}",
)






# new_message = types.Content(
#     role="user",
#     parts=[types.Part(text="What is my favorite food?")],
# )

# for event in runner.run(
#     user_id=USER_ID,
#     session_id=SESSION_ID,
#     new_message=new_message,
# ):
#     if event.is_final_response():
#         if event.content and event.content.parts:
#             print(f"Final response: {event.content.parts[0].text}")


# print("Session event exploration....:")
# session = session_service_stateful.get_session(
#     app_name=APP_NAME,
#     user_id=USER_ID,
#     session_id=SESSION_ID,
# )

# print("Final session state:")
# for key, event in session.state.items():
#     print(f"\t{key}: {event}")
