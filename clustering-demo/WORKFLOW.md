# Workflow

When you receive the command to start working, follow these exact steps:

## Step 0: Initialize Logging
- Begin writing your thought process, intermediate decisions, and mapping strategies into a log file.
- Save this file into the `./agent_logs/` directory (e.g., `run_log.md`).

## Step 1: Ingestion and Initial Mapping
- Access the `./summaries` directory.
- Scan all the `*.md` files provided in this directory to identify the main thesis, methods, and key conclusions of each summary.

## Step 2: Clustering & Analysis
- Create distinct thematic groups (clusters) based on the ingested summaries.
- Analyze the relationships between the papers within each cluster.

## Step 3: Detailed Cluster Structuring
For each identified cluster, you MUST strictly format your output using the following exact structure:
1. **Proposed Order:** (Indicate the logical sequence of this cluster in the overall review, e.g., 1 of 4, and explain briefly why it sits here).
2. **Cluster Name:** (A precise, academic title for the group).
3. **Short Definition:** (A 2-3 sentence summary of what this cluster is about).
4. **List of Texts:** (Bullet points listing the specific files/authors assigned to this group).
5. **Common Concepts:** (Shared terminology, theoretical frameworks, or recurring variables).
6. **Tensions within the Group:** (Conflicting views, methodological disagreements, or differing conclusions among the authors in this cluster).
7. **Gaps in the Material:** (What is missing? What aspects are overlooked by these authors?).

## Step 4: Final Output Generation & Saving
- Compile the structured clusters and the broader research problems into a comprehensive Markdown document. Save it to `./outputs/report.md`.
- Based on the report, create a hierarchical outline for a potential review paper. You must format this outline strictly as a valid OPML (XML) structure and save it to `./outputs/outline.opml`.