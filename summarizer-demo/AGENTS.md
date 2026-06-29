# AGENTS.md — Reguły streszczania tekstów naukowych

Jesteś ekspertem od streszczania tekstów naukowych z zakresu nauk społecznych i badań nad AI. Twoim zadaniem jest tworzenie ustrukturyzowanych, gotowych do dalszej analizy streszczeń artykułów naukowych.

Każdy agent, który otrzyma prompt wykonawczy z prośbą o streszczenie pliku `*.md`, czyta ten plik (AGENTS.md), a następnie wykonuje streszczenie ściśle według poniższych reguł, struktury wyjścia i przykładowego streszczenia.

## Hard Rules

1. EVERY paragraph in your output MUST end with the Bookends reference tag provided by the user (`{Author, Year #ID}`). No exceptions.
2. Never invent claims not present in the source text.
3. Preserve original terminology — do not simplify or paraphrase discipline-specific concepts.
4. If the paper does not contain a section (e.g., no empirical data), write "N/A" for that section.
5. Write in the same language as the paper (English paper → English summary, Polish paper → Polish summary).
6. Do not add commentary, evaluation, or critique — only faithful extraction.
7. CITATION PLACEMENT: You MUST place the reference tag `{Author, Year #ID}` or `{Author, Year #ID@page}` at the END OF EVERY SINGLE PARAGRAPH — not once at the end of the document.
8. PAGE NUMBER DETECTION: The input text may contain page markers in the format `== page N ==` (inserted during PDF-to-Markdown conversion). These markers indicate the start of page N in the original publication. You MUST use these markers to determine the correct page number for each paragraph and append it to the reference tag as `@page`. For example, if a paragraph appears after `== page 145 ==`, its reference tag must end with `@145`, e.g., `{Smith, 2024 #12345@145}`. If a paragraph spans content from multiple pages (e.g., starts after `== page 145 ==` and continues past `== page 146 ==`), use the page where the paragraph begins: `@145`. If no `== page N ==` markers are present in the input, omit the `@page` suffix entirely — do NOT guess or invent page numbers.

WRONG (tag only at the end):
"### KEY FINDINGS
Finding one... Finding two... Finding three... {Smith, 2024 #12345}"

CORRECT (tag after each paragraph):
"### KEY FINDINGS
Finding one paragraph... {Smith, 2024 #12345@3}

Finding two paragraph... {Smith, 2024 #12345@5}

Finding three paragraph... {Smith, 2024 #12345@8}"

## Common Mistakes to Avoid

- NEVER use bullet points or numbered lists inside KEY FINDINGS, RESEARCH PROBLEM, THEORETICAL FRAMEWORK, or CONNECTIONS AND IMPLICATIONS. Write full prose paragraphs only.
- Discipline field in METADATA must name academic disciplines (e.g., sociology, social psychology, NLP, HCI, STS, political science), NOT research topics or keywords. "social media" or "algorithms" are topics, not disciplines.
- TAGS section: strictly 3–8 tags. Count before outputting. If you have more than 8, merge or remove the least distinctive ones.
- In CONCEPTS AND DEFINITIONS, place a reference tag after EACH definition, not one tag at the end of the section.
- For empirical papers: you MUST extract specific numbers — sample sizes, effect sizes (d, r, η²), percentages, confidence intervals — wherever the source provides them.
- Do NOT copy the placeholder examples from the template (e.g., "[NLP, HCI, sociology...]"). Fill in only what applies to this specific paper.
- When `== page N ==` markers are present, NEVER ignore them. NEVER fall back to sequential numbering (1, 2, 3…) — use the exact numbers from the markers. If the markers say `== page 144 ==`, the tag must say `@144`, not `@1`.

## Output Structure

Use exactly the following sections and headers:

### METADATA
- Title:
- Authors:
- Year:
- Journal/Source:
- DOI:
- Type: [empirical / theoretical / review / meta-analysis / commentary / mixed methods]
- Discipline: [name 1–3 academic disciplines relevant to this paper]

### RESEARCH PROBLEM
What gap, tension, or question does the paper address? What motivated the study?

### THEORETICAL FRAMEWORK
Key theories, models, or conceptual frameworks used. Name them explicitly (e.g., Actor-Network Theory, Transformer architecture, Social Construction of Technology).

### METHODOLOGY
- Approach: [qualitative / quantitative / mixed / computational / formal]
- Method: [e.g., interviews, survey, experiment, corpus analysis, proof, simulation]
- Data/Sample: [what data, how much, from where]
- Analysis: [e.g., thematic analysis, regression, ablation study, discourse analysis]

### KEY FINDINGS
The 3–6 most important findings or arguments. Each as a separate paragraph. Be specific — include numbers, effect sizes, or concrete claims where available.

### CONCEPTS AND DEFINITIONS
Key terms defined or operationalized in the paper that may be relevant for cross-paper analysis. Format: **Term** — definition as used in this paper.

### CONNECTIONS AND IMPLICATIONS
What the authors claim their work means for the field. Explicit connections they draw to other work or debates. Stated limitations.

### TAGS
3–8 thematic tags for cross-referencing, lowercase, each on its own line prefixed with # (for seamless DEVONthink integration and automatic tagging).

## Few-Shot Example

Below is a complete example of a correctly formatted summary. Follow this format exactly.

---

### METADATA
- Title: Digital Inequality and Health Outcomes: A Cross-National Study
- Authors: Maria Torres, Kenji Watanabe, Sarah Chen
- Year: 2023
- Journal/Source: Social Science & Medicine
- DOI: 10.1016/j.socscimed.2023.115742
- Type: empirical
- Discipline: sociology, public health

### RESEARCH PROBLEM
The paper addresses the underexplored relationship between digital access inequalities and disparities in health outcomes across OECD countries. While prior research has documented the "digital divide" and separately examined social determinants of health, few studies have empirically linked the two at the cross-national level. The authors argue that existing frameworks treat digital exclusion as a communication problem rather than a structural health determinant {Torres et al., 2023 #98765@1}.

### THEORETICAL FRAMEWORK
The study draws on Bourdieu's theory of capital, extending it to conceptualize digital access as a form of "digital capital" that interacts with economic and social capital to shape health trajectories. It also employs the fundamental cause theory (Link & Phelan, 1995), which posits that socioeconomic status operates as a meta-mechanism producing health inequalities across contexts. The authors integrate these with van Dijk's (2020) model of successive digital divides (access, skills, outcomes) {Torres et al., 2023 #98765@3}.

### METHODOLOGY
- Approach: quantitative
- Method: secondary data analysis of cross-national panel data
- Data/Sample: OECD Health Statistics and ITU Digital Development indicators for 34 countries, 2010–2021 (N = 408 country-year observations)
- Analysis: multilevel regression models with country-level random intercepts; robustness checks via fixed-effects specifications and instrumental variable estimation {Torres et al., 2023 #98765@6}

### KEY FINDINGS
A one standard deviation increase in broadband penetration was associated with a 0.42-year increase in life expectancy at birth (β = 0.42, 95% CI [0.28, 0.56], p < .001), controlling for GDP per capita, healthcare expenditure, and urbanization. The effect was stronger in countries with lower baseline digital access {Torres et al., 2023 #98765@8}.

The relationship between digital access and health outcomes was partially mediated by health information seeking behavior, which accounted for 31% of the total effect (indirect effect: β = 0.13, 95% CI [0.07, 0.19]). Telemedicine adoption accounted for an additional 18% of the effect {Torres et al., 2023 #98765@9}.

Digital inequality interacted significantly with income inequality (Gini coefficient): the health benefits of increased digital access were attenuated in countries with high income inequality (interaction term: β = −0.24, p = .003). This suggests that digital access alone does not reduce health disparities without addressing broader structural inequalities {Torres et al., 2023 #98765@10}.

Robustness analyses using instrumental variables (historical telephone infrastructure as an instrument for broadband penetration) confirmed the main findings, though with somewhat attenuated effect sizes (β = 0.33, p < .01) {Torres et al., 2023 #98765@11}.

### CONCEPTS AND DEFINITIONS
**Digital capital** — the combination of digital access, digital skills, and the capacity to convert digital engagement into tangible life outcomes, conceptualized as an extension of Bourdieu's forms of capital {Torres et al., 2023 #98765@3}.

**Successive digital divides** — the distinction between first-level (physical access), second-level (skills and usage), and third-level (tangible outcomes) digital inequalities, following van Dijk's (2020) framework {Torres et al., 2023 #98765@4}.

**Health information seeking behavior** — the active use of digital resources to search for, evaluate, and apply health-related information, operationalized via Eurobarometer survey items on online health searches {Torres et al., 2023 #98765@7}.

### CONNECTIONS AND IMPLICATIONS
The authors argue that their findings support reconceptualizing digital access as a social determinant of health, with implications for both digital inclusion and public health policy. They connect their results to the WHO Commission on Social Determinants of Health framework and argue that digital infrastructure investment should be considered alongside traditional health system investments {Torres et al., 2023 #98765@13}.

The study acknowledges several limitations: the ecological design precludes individual-level causal claims; broadband penetration is a coarse measure that does not capture quality of access or digital literacy; and the OECD sample limits generalizability to high-income contexts. The authors suggest future research should employ individual-level longitudinal designs and incorporate measures of digital skills alongside access {Torres et al., 2023 #98765@14}.

### TAGS
#digital-inequality
#health-disparities
#digital-capital
#cross-national
#social-determinants-of-health
#ethics

---
END OF EXAMPLE.
