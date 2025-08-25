# Customer/Learner Service Agent

## Overview

The **Customer/Learner Service Agent** is a multi-agent system built in Google ADK for **educational purposes**. It provides personalized support for learners, coordinating multiple sub-agents to manage course information, policies, purchases, refunds, and engagement guidance.

---

## Purpose

* Acts as the main interface for learners interacting with the educational platform.
* Coordinates sub-agents to deliver accurate, personalized, and timely assistance.
* Ensures consistent and friendly communication across all learner interactions.

---

## Sub-Agents

| Sub-Agent                                 | Responsibility                                                                            | Notes                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Policy Agent**                          | Provides general and course-specific policies (attendance, grading, deadlines).           | Answers compliance-related queries.                     |
| **Sales Agent**                           | Manages course purchases, tracks learner’s courses and deadlines.                         | Supports follow-up on purchased courses.                |
| **Course Support Agent**                  | Provides course highlights, objectives, and content overviews.                            | Engages learners without revealing full course content. |
| **Order Agent**                           | Handles refunds, cancellations, and prevents repeat recommendations of cancelled courses. | Tracks user order history.                              |
| **Progress Tracker Agent** *(optional)*   | Monitors learner progress and sends reminders for pending assignments.                    | Enhances engagement and personalized guidance.          |
| **Feedback Collector Agent** *(optional)* | Collects learner satisfaction ratings or reviews.                                         | Helps improve courses and agent responses.              |

---

## Tools

* **Knowledge Base Tool**: Access FAQs, course descriptions, and platform policies.
* **Current Time Tool**: Track deadlines, schedules, and timestamps.
* **Payment/Transaction Tool**: Manage and retrieve transaction information.
* **Recommendation Tool**: Suggest courses based on user interests and history.

---

## Guidelines / Behavior

* Be friendly, professional, and concise.
* Verify learner context before answering.
* Provide personalized, actionable, and relevant responses.
* Maintain privacy and security of learner data.
* Escalate tasks to sub-agents or human support if outside your scope.

---

## Short Description

> The Customer/Learner Service Agent coordinates multiple sub-agents to provide learners with personalized educational support, including course information, policies, purchases, refunds, and engagement guidance.

---

## Folder Structure

```
customer_learner_service_agent/
│
├─ main.py                  # Main entry point for the Customer/Learner Service Agent
├─ instruction.py           # Instructions for the main agent and sub-agents
├─ tools/                   # All tools as separate modules
│   ├─ knowledge_base.py
│   ├─ get_current_time_tool.py
│   ├─ payment_tool.py
│   └─ recommendation_tool.py
│
├─ sub_agents/              # Each sub-agent in its own module
│   ├─ policy_agent.py
│   ├─ sales_agent.py
│   ├─ course_support_agent.py
│   ├─ order_agent.py
│   ├─ progress_tracker_agent.py   # optional enhancement
│   └─ feedback_collector_agent.py # optional enhancement
│
└─ utils/                   # Helper functions, e.g., logging, validation
    ├─ logger.py
    └─ user_context.py
```

---

## Notes

* Each sub-agent module defines an `Agent` object with its model, instructions, and tools.
* Tools are modular and reusable across sub-agents.
* `main.py` instantiates the Customer/Learner Service Agent and registers sub-agents and tools.
* Optional sub-agents can be added later without changing the main agent structure.

---

## Getting Started

1. Install dependencies:

```bash
pip install google-generativeai
```

2. Configure your agents and tools in the respective folders.

3. Run `main.py` to start the Customer/Learner Service Agent.

---

## License

This project is for **educational purposes only**.
