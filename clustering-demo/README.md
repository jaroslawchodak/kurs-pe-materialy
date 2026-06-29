# Project: Literature Clustering (AI & Social Science)

## Project Objective
The goal of this repository is to automate the process of reviewing, analyzing, and synthesizing scientific literature at the intersection of Artificial Intelligence (AI) and Social Sciences. The agentic system is designed to help researchers quickly identify patterns, theoretical tensions, knowledge gaps, and new research directions.

## System Files & Directories Structure
- `AGENTS.md` - Defines the role, competencies, and working style of the agent.
- `CONTEXT.md` - Provides domain knowledge regarding the intersection of AI and social sciences.
- `WORKFLOW.md` - Describes the agent's step-by-step operating procedure and exact output structure.
- `./summaries/` - Directory containing the article summaries in `*.md` format that are to be clustered (Input).
- `./outputs/` - Directory where the final results will be saved (`report.md` and `outline.opml`).
- `./agent_logs/` - Directory for saving the agent's internal reasoning, execution traces, and work logs.

## How to Get Started?
1. Ensure all article summaries (`*.md` files) are placed inside the `./summaries` directory.
2. Load the system files into the agent's memory (context).
3. Use the main execution prompt to start the analysis process.