# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "fastapi",
#   "uvicorn",
# ]
# ///

import httpx
import os
from typing import Dict, Any
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Make sure this covers your client's origin
    allow_credentials=True,
    allow_methods=["*"],  # Ensure this includes 'OPTIONS'
    allow_headers=["*"],  # Make sure the necessary headers are included
)







tools = [
    {
        "type": "function",
        "function": {
            "name": "get_ticket_status",
            "description": "Get the status of a particular ticket",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticket_id": {
                        "type": "integer",
                        "description": "Ticket ID number"
                    }
                },
                "required": ["ticket_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "schedule_meeting",
            "description": "Schedule a meeting",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date of the meeting"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time of the meeting"
                    },
                    "meeting_room": {
                        "type": "string",
                        "description": "Meeting Room for the meeting"
                    }

                },
                "required": ["date", "time", "meeting_room"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_expense_balance",
            "description": "Shows the expense balance for an employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    }
                },
                "required": ["employee_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    {
        "type": "function",
        "function": {
            "name": "calculate_performance_bonus",
            "description": "Calculate the performance bonus for an employee in a given year",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    },

                    "year": {
                        "type": "integer",
                        "description": "Year"
                    }
                    
                },
                "required": ["employee_id", "year"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    {
        "type": "function",
        "function": {
            "name": "report_office_issue",
            "description": "Report an office issue for a specific department",
            "parameters": {
                "type": "object",
                "properties": {
                    "issue_code": {
                        "type": "integer",
                        "description": "Issue Code number"
                    },

                    "department": {
                        "type": "string",
                        "description": "Department for which the issue is reported"
                    }
                },
                "required": ["issue_code", "department"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
]


@app.get("/execute")
def query_gpt(q= Query(None, title="Query string", description="The query string to search for"), tools=tools):
    response = httpx.post(
        "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('AIPROXY_TOKEN')}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": q}],
            "tools": tools,
            "tool_choice": "auto",
        },
    )

    output = response.json()["choices"][0]["message"]
    return {"name": output["tool_calls"][0]["function"]["name"] , "arguments": output["tool_calls"][0]["function"]["arguments"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
