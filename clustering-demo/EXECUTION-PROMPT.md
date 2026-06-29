###  Execution Prompt    
 
> **System instruction / Prompt:**  

"As the Principal Research Synthesizer, assume you have already loaded the AGENTS.md, CONTEXT.md, and WORKFLOW.md files into your context. The input data for this task are the article summaries (in *.md format) located in the ./summaries directory.
> 
> Here is your task:  
First, start logging your thought process and execution traces, and save these logs in the ./agent_logs directory.
> 
> Next, **read everything** from the ./summaries directory carefully to fully grasp the research context. Then, **group thematically** these texts into logical clusters.
> 
> For every single cluster you create, you must strictly follow the format defined in WORKFLOW.md. Explicitly include the following sections for each group: **Proposed Order**, **Cluster Name**, **Short Definition**, **List of Texts**, **Common Concepts**, **Tensions within the Group**, and **Gaps in the Material**.
> 
> Based on this detailed synthesis, **identify possible research problems** across the whole domain that have not yet been sufficiently explored.
> 
> Finally, **save the report + outline** into the ./outputs directory in two separate formats:
> 
> 1. Save the main analytical document as ./outputs/report.md.
> 
> 2. Save the structural plan (table of contents) for writing our own 'Literature Review' paper as a valid XML/OPML file named ./outputs/outline.opml.
> 
> Be precise and maintain strict academic rigor throughout the process."