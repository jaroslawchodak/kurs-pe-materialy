# Thematic Synthesis: AI and the Social Sciences

**Domain corpus:** 10 article summaries (2025–2026 plus one 2019 chapter and one 2009 commentary), ingested from `./summaries/`.
**Method:** semantic clustering with explicit mapping of tensions, gaps, and unidentified research problems.
**Outputs (this document):** `./outputs/report.md`; structural plan in `./outputs/outline.opml`.
**Agent log:** `./agent_logs/run_log.md` (every analytical decision traceable).

---

## Executive Map of the Domain

The 10 texts can be productively organized into **five semantic clusters** that re-cut and deepen the four axes announced in `CONTEXT.md` (Ethics & Bias; Work & Economy; Politics & Media; Relationships & Psychology). The fifth cluster is meta-disciplinary and could not be folded into the original axes without distortion.

| # | Cluster | Texts | Tightest CONTEXT.md axis |
|---|---|---|---|
| 1 | Politics, Information & Democratic Integrity | Gilbert 2026; Goudarzi 2025 | Politics & Media (+ Ethics) |
| 2 | Labor, Economy & Cultural Production | Zahidi 2026; Farley 2025 | Work & Economy (+ Politics & Media) |
| 3 | Intimacy, Companionship & Homo Digitalis | Sussman 2026; Watercutter 2025; Kirk 2025 | Relationships & Psychology (+ Ethics) |
| 4 | Design Philosophy: Humanlike AI and Its Discontents | Sandry 2019; Shneiderman 2020 | Relationships & Psychology (design turn) + Ethics |
| 5 | Building Computational Social Science | Lazer 2009 | Meta-disciplinary / Ethics & Bias |

The ordering is deliberate. Clusters 1–3 march from macro-political effects, to labor-cultural effects, to micro-psychological effects. Cluster 4 steps back into the design layer that *explains* the harms observed in 1–3. Cluster 5 closes the loop by reflecting on what kind of social science is needed to study these phenomena at all.

---

## Cluster 1 (1 of 5) — Politics, Information & Democratic Integrity

- **Proposed Order:** 1 of 5. The cluster opens the review because the most consequential near-term claim in the corpus — Gilbert's prediction of AI-influence inflection by the 2028 U.S. presidential election — is also the most temporally urgent. It also sets the macro-political envelope (what happens to democracies) within which labor, intimacy, and design debates unfold.
- **Cluster Name:** Politics, Information & Democratic Integrity: Algorithmic Influence, Surveillance and the Erosion of the Public-Private Boundary.
- **Short Definition:** This cluster gathers texts that treat AI as a force reshaping political communication and state-civil-society relations. Both texts diagnose threats to democratic legitimacy, but they do so via different mechanisms: one (Gilbert) focuses on autonomous influence operations on social platforms, the other (Goudarzi) on a state-corporate surveillance complex that weaponizes benign data.
- **List of Texts:**
  - Gilbert, D. (2026). *AI-Powered Disinformation Swarms Are Coming for Democracy.* Wired. Reporting on the 22-author *Science* paper on AI swarms. {Gilbert, 2026 #146943}
  - Goudarzi, S. (2025). *How AI and Surveillance Capitalism Are Undermining Democracy.* Bulletin of the Atomic Scientists (Opinion). {Goudarzi, 2025 #221094}
- **Common Concepts:** coordinated inauthentic behavior; *AI swarms*; computational propaganda; *surveillance ratchet*; *behavioral homogenization*; *decontextualization of prediction*; blurring of public and private spheres; AI Influence Observatory; chilling causal reversal; micro-A/B testing at machine speed.
- **Tensions Within the Group:**
  1. **Time horizon of harm.** Gilbert frames harm as a 2028 inflection (presidential election); Goudarzi treats harm as thoroughly present (Catch and Revoke program since March 2025; Meta/Flo jury verdict March 2025). The two temporal frames are not reconciled, but combined they imply *both* the institutional structures and the agentic scale are arrived.
  2. **Locus of threat.** Goudarzi locates danger predominantly in the *vertical* axis (state plus platform corporations); Gilbert locates it in the *horizontal* axis (decentralized swarm operators on open platforms). The texts speak past each other on whether AI-mediated democracy erosion needs primarily regulatory or observatory-style responses.
  3. **Governance remedy.** Goudarzi proposes nuclear-style *restrictive* controls (preservation-of-freedom-first). Gilbert proposes a lightweight, NGO-and-academic *AI Influence Observatory* explicitly excluding platform executives. These are not the same model of governance: one is prohibitive, the other is sensemaking-first.
  4. **The role of consumer platforms.** Gilbert is explicit that platforms conceal AI-driven engagement to protect valuations. Goudarzi treats platforms as one node in a wider surveillance-capitalism network but does not explain the same incentive structure with the same precision.
- **Gaps in the Material:**
  - No comparative analysis across democratic regimes (parliamentary, presidential, hybrid) and across regime durability (old vs. new democracies).
  - Empirical operationalization of "behavioral homogenization" is missing; Goudarzi asserts it conceptually without measurement.
  - No discussion of AI swarms' potential utility for *civil-society counter-orchestration* (e.g., pro-democracy campaigns); the texts trace only the offensive use case.
  - Detection-tool bias and false-positive regimes are not addressed — important because detection systems are themselves AI.
  - Gilbert's *Science* paper is reported via one magazine feature; the underlying methodology (e.g., simulation assumptions, threat-model calibration) is not independently interrogated by the corpus.

---

## Cluster 2 (2 of 5) — Labor, Economy & Cultural Production

- **Proposed Order:** 2 of 5. Sits between the political cluster and the cluster on intimacy to invite the reader to consider how AI restructures the *economy of meaning* (cultural production) and the *economy of work* (labor markets) before zooming into the formation of persons through AI companionship.
- **Cluster Name:** Labor, Economy & Cultural Production: Reskilling, Creative Authenticity and the End of Naïve Technological Determinism.
- **Short Definition:** Two texts that, despite sharing the premise that AI refashions markets, approach the question from opposite directions: one (Zahidi) privileges macro-structural context (geoeconomics, demographics, AI literacy) over displacement narratives; the other (Farley) reads the moment through a cultural-industries lens, taking authenticity, creative struggle, and anthropomorphization as the contested stakes.
- **List of Texts:**
  - Zahidi, S. (2026). *The Real Economics of AI and Jobs.* TIME (Opinion / WEF synthesis). {Zahidi, 2026 #204061}
  - Farley, C. J. (2025). *It's Time to Rage Against the AI Music Machine.* TIME (Opinion). {Farley, 2025 #115990}
- **Common Concepts:** labor-displacing technology; *creative struggle*; *authenticity discourse*; *AI literacy*; multiplier effects; geoeconomics; *industrial policy for entrepreneurship*; *downward spiral into slop*; Guaranteed Human; Hot AI Products Chart; generational labor-market transitions.
- **Tensions Within the Group:**
  1. **Displacement vs. augmentation.** Zahidi (following WEF) argues net job creation in the near term; Farley describes a chartable present-tense displacement (Xania Monet, Breaking Rust, six AI acts on Billboard). Both reject technological determinism but allocate weight differently to displacement vs. augmentation.
  2. **Macro vs. micro register.** Zahidi builds multi-causal arguments from FDI flows, tariffs, and demographics; Farley builds a single-industry argument from one Billboard chart. The two scales are not bridged.
  3. **Anthropomorphization as policy lever.** Both texts engage with how AI is named/categorized, but to opposite ends: Zahidi wants AI integrated into roles through literacy so its outputs are accepted; Farley wants AI acts *un-named* (as "products" not "artists") precisely because integration masks harm.
  4. **Speed of transition.** Zahidi notes prior industrial transitions took 10–40 years and warns of investment bubbles; Farley treats 2025 as the chartable year of arrival. Both cohere on "faster than before" but disagree on whether that speed is techno-economic or cultural.
  5. **Geography.** Zahidi's analysis is global and explicitly comparative (UK FDI decline; Mexico 64,000 factory-job loss; South Korea/Turkey/Poland defense boom). Farley's frame is resolutely U.S.-centric (Billboard, U.S. consumer survey).
- **Gaps in the Material:**
  - No empirical study of GenAI diffusion in Global South creative industries beyond Zahidi's mention of Nigerian freelancing/digital-export policy.
  - The Ipsos/Deezer "97% cannot distinguish" figure (in Farley) is accepted without methodological scrutiny; no replication or independent cross-cultural figures are cited.
  - Alternative ownership structures (platform cooperatives, creative-commons licensing, unions of AI-supplemented workers) are absent.
  - Zahidi's "industrial policy for entrepreneurship" rests on national cases (Nigeria, Singapore) without comparative causal analysis.
  - No analysis of how authenticity discourse operates differently in non-Western musical forms (e.g., the AI-music question in K-pop, Bollywood, or Afrobeats industries is absent).
  - The two texts do not interact with each other; reconciliation is left entirely to the reader.

---

## Cluster 3 (3 of 5) — Intimacy, Companionship & Homo Digitalis

- **Proposed Order:** 3 of 5. Comes after macro-structures because intimate life is the *micro* consequence of macro forces, and before the design-philosophy cluster because it is the empirical site at which design choices produce observable human behaviors.
- **Cluster Name:** Intimacy, Companionship & Homo Digitalis: AI as Companion, Substitute and Stressor.
- **Short Definition:** A three-text cluster that examines the social-psychological consequences of AI-mediated intimacy and friendship. The texts triangulate the phenomenon through evolutionary grievance (Sussman on the "intimacy crisis"), digital-cultural critique of platform capitalism (Watercutter on AI-as-fake-friend), and HCI-ethics theorization of "socioaffective alignment" (Kirk on social reward hacking).
- **List of Texts:**
  - Sussman, A. L. (2026). *The Basic Drive That Humans Might Be Losing.* The Atlantic (Feature / book-review essay on J. R. Garcia's *The Intimate Animal*). {Sussman, 2026 #119050}
  - Watercutter, A. (2025). *Tech Disrupted Friendship. It's Time to Bring It Back.* Wired. {Watercutter, 2025 #225917}
  - Kirk, H. R., Gabriel, I., Summerfield, C., Vidgen, B., & Hale, S. A. (2025). *Why human–AI relationships need socioaffective alignment.* Humanities and Social Sciences Communications. {Kirk et al., 2025 #268678}
- **Common Concepts:** AI companionship; *intimacy crisis*; *social reward hacking*; *parasocial relationship*; *hyperpersonal relationship*; *sycophancy*; *emotional offloading*; *frictionless interactions*; *digitally generated toxic positivity*; Basic Psychological Needs Theory (competence, autonomy, relatedness); *socioaffective alignment*; *touch starvation*; *generalized anxiety*; looksmaxxing; heteropessimism.
- **Tensions Within the Group:**
  1. **Mechanism of harm.** Sussman leans evolutionary ("4.4 million years of pair-bonding disrupted"); Watercutter leans infrastructural (platform capitalism eroded face-to-face community and now offers AI as a substitute); Kirk leans intra-personal (preferences and perceptions are reshaped inside the interaction itself). These are competing causal logics that the corpus does not reconcile.
  2. **Harms vs. benefits.** Kirk is openly ambivalent — citing both suicide-mitigation evidence and addiction/depression/anxiety harms. Watercutter hears the harms register more loudly in 2025 (teen-suicide Senate testimony, Pew 50/5% result). Sussman, via Garcia, is more skeptical of AI companions and skeptical of the "tactile VR" solution advocated by Thao Ha.
  3. **Substitution vs. complement.** Watercutter (via Gabriel) frames AI friendship as *substitution*. Kirk's "Balancing AI companionship with human relationships" intrapersonal dilemma treats it as a *governable complement*. Sussman's framing is again more ambivalent.
  4. **The public's verdict.** Watercutter reports two 2025 polling signals (Pew 50/5%; Common Sense Media/Stanford 72% teen interaction) pointing to public skepticism and use-at-scale simultaneously. The texts do not adjudicate this paradox.
  5. **Methodological asymmetry.** Kirk is a peer-reviewed theoretical paper drawing on neuroscience, psychology, and HCI. Sussman and Watercutter are journalistic syntheses drawing on few primary sources (Garcia's book; Common Sense Media; Stanford assessment). The weight of evidence is uneven within the cluster.
- **Gaps in the Material:**
  - No longitudinal clinical study of measurable psychological outcomes from AI companion use.
  - No cross-cultural or non-Western empirical work; East-Asian patterns (Japan/South Korea unpartnered populations, mentioned by Sussman) are asserted but not studied.
  - The political economy of AI companionship is undertreated — who funds, who regulates, who profits, who decides default settings, who audits injury claims.
  - Disability-community use cases (e.g., AAC users, neurodivergent users) are entirely absent; the cluster cannot exclude potentially beneficial uses.
  - No engagement with feminist / queer-theoretical framings of chosen family, polyamory, or solitude as alternative ethical horizons to "pair-bonding" — whatever evolutionary evidence is cited, the singular privileging of pair bonds is not interrogated.
  - No empirical work on the *causal* contribution of AI companions to loneliness (vs. correlation with prior loneliness).
  - No attention to AI companion *withdrawal* as a structural phenomenon (Soulmate shutdown grief noted briefly by Watercutter but not researched).

---

## Cluster 4 (4 of 5) — Design Philosophy: Humanlike AI and Its Discontents

- **Proposed Order:** 4 of 5. Placed after the empirical clusters because both texts in this cluster *explain* why the harms observed in Clusters 1–3 arise: they trace them to a single design-philosophical error (humanlikeness) and propose design alternatives. This is the analytic climax of the review.
- **Cluster Name:** Design Philosophy: Humanlike AI and Its Discontents — Non-Human Alterity, Human-Centered AI, and the Politics of Machine Design.
- **Short Definition:** Two theoretical texts that, by different routes, contest the dominant paradigm of humanlike AI. Sandry retrieves Levinas's ethics of alterity to defend the philosophical possibility of *overtly non-human* machines as social others. Shneiderman mounts a design-pragmatist critique, arguing that effective AI must be tool-like, "in the loop" around humans, and governed by a three-tier reliability-safety-trust architecture.
- **List of Texts:**
  - Sandry, E. (2019). *Taking Social Machines Beyond the Ideal Humanlike Other.* In Z. Papacharissi (Ed.), *A Networked Self and Human Augmentics, Artificial Intelligence, Sentience.* Routledge, Chapter 6, 69–82. {Sandry, 2019 #192562@69–80}
  - Shneiderman, B. (2020). *Human-Centered Artificial Intelligence: Three Fresh Ideas.* AIS Transactions on Human-Computer Interaction, 12(3), 109–124. {Shneiderman, 2020 #253839@110–120}
- **Common Concepts:** *Nass's Fallacy*; *Teammate Fallacy*; *Computers-in-the-Loop Reality*; *Shneiderman's Conjecture*; *Second Copernican Revolution*; *human-centered AI (HCAI)*; *obstacle of animism* (Mumford); *evocative object* vs. *relational artifact*; *absolute alterity*; *the face* (Levinas); two-dimensional HCAI framework; design tradeoffs; information-abundant displays; safety culture.
- **Tensions Within the Group:**
  1. **Saving vs. abandoning sociality.** Sandry wants to preserve *sociality* but reconceived through overtly non-human alterity. Shneiderman wants machines primarily as *tools* — useful, embedded, controlled — where "sociality" with the machine is itself the design error (Nass's Fallacy). Their normative endpoints converge (less mimicry) but their ontologies diverge (machines as social non-human-others vs. machines as tools).
  2. **Theoretical lineage.** Sandry draws on Levinas's ethical phenomenology (otherness as constitutive of the self). Shneiderman draws on Mumford's historical technology studies and design pragmatism. Their disagreement is partly a function of different philosophical sources.
  3. **Posture toward anthropomorphic demand.** Both texts reject the humanlike-machine paradigm abstractly, but neither engages with empirical evidence of *consumer demand* for anthropomorphism (e.g., the 97% "can't tell AI vs. human music" finding in Farley).
  4. **Relation to governance.** Shneiderman's three-level governance (reliable systems, safety culture, trustworthy certification) is more developed; Sandry has no governance proposal but instead offers a philosophical reorientation.
  5. **Treatment of generative AI.** Both papers pre-date (or barely engage with) the post-2022 LLM explosion. The corpus lacks any post-2022 design-philosophy rebuttal or extension of these positions.
- **Gaps in the Material:**
  - No engagement with consumer preference or behavioral evidence that design-philosophy arguments need to address.
  - No accounting for the *economic* pressures on design teams to anthropomorphize (anthropomorphic products monetize engagement better per Watercutter's cluster observations).
  - The cluster focuses on individual machine artifacts and largely omits *networked* or *system-level* AI effects (swarms, feeds, recommender systems).
  - Accessible / disability-positive design of non-humanlike machines is not discussed.
  - The textual lineage (Nass, Mumford, Levinas) is thin; cultural-studies and postcolonial critiques of "anthropomorphism" as a Western philosophical preoccupation are absent.

---

## Cluster 5 (5 of 5) — Building Computational Social Science

- **Proposed Order:** 5 of 5. The cluster closes the review by stepping outside substantive content to ask the meta-question: with what kind of science can we study all of the above? Lazer's 2009 *Science* commentary is included as a foundational benchmark whose optimism must be re-read in light of the post-2016 reality described in the other clusters.
- **Cluster Name:** Building Computational Social Science: From Institutional Vision to Crisis of Data Stewardship.
- **Short Definition:** A single-text cluster that positions computational social science (CSS) as an emergent discipline at risk of capture by either corporate proprietary actors or classified state programs. Lazer argues that institutional design (data sharing, training, IRB capacity, privacy-preserving methods) is a precondition for the field's scientific legitimacy. Read against the later texts in the corpus, the cluster is also a diagnostic of how that institutional vision fared.
- **List of Texts:**
  - Lazer, D., Pentland, A., Adamic, L., Aral, S., Barabási, A.-L., Brewer, D., Christakis, N., Contractor, N., Fowler, J., Gutmann, M., Jebra, T., King, G., Macy, M., Roy, D., & Van Alstyne, M. (2009). *Computational Social Science.* Science. {Lazer et al., 2009 #191478@721–722}
- **Common Concepts:** computational social science; *sociometers*; *macro social network*; *de-anonymization*; interdisciplinary training; ethics-by-design (via IRBs); privacy-preserving computation; cognitive-science analogy.
- **Tensions Within the Group (and against the corpus):**
  1. **Lazer's 2009 institutional optimism vs. 2026 reality.** Lazer imagines a public-interest, IRB-analog-governed CSS that could rival cognitive science. The later texts (Goudarzi 2025 — surveillance ratchets; Watercutter 2025 — platform consolidation; Gilbert 2026 — researcher access restrictions; Kirk 2025 — preference-formation changes that may invalidate prior consent frameworks) suggest that Lazer's institutional imagination was incomplete.
  2. **Lazer's technology vs. methodology balance.** Lazer largely treats AI as a *tool* for studying humans. The other clusters treat AI as a *phenomenon* altering humans. The methodological implication is large: who studies whom, and with what epistemology?
  3. **Privacy assumptions.** Lazer's de-anonymization examples (NIH/Wellcome Trust genetic databases) pre-date the inferential power of foundation models trained on leaked or purchased datasets. The cluster does not extend to that scenario.
- **Gaps in the Material:**
  - U.S.-centric institutional imagination; the global architecture of CSS (China, EU, India, Brazil) is not addressed.
  - No treatment of platform-governance proposals (the *AI Influence Observatory* proposed by Gilbert in 2026 reads as a belated descendant of Lazer's institutional vision, but the linkage is implicit in the corpus).
  - Lazer's framework does not anticipate that data *producers* (the public) might themselves be generative AI agents producing synthetic training content — the silicon-sample problem.
  - No attention to the moral and epistemological status of "computational simulation" as evidence (cf. Gilbert's *Science* paper, which uses simulation to forecast 2028 elections).
  - CSS-as-discipline has limited engagement with critical theory; the dominant frame is method-opportunity, not power-analysis.

---

## Cross-Cutting Tensions Across the Whole Domain

**T1. Humanlike AI — attractive or harmful?**
- *Affirmative:* Kirk 2025 documents empirically and theoretically that humans' evolved social-cognitive apparatus treats social cues as social; Farley 2025 and Watercutter 2025 demonstrate that *users* find AI artifacts indistinguishable from or preferable to human ones.
- *Critical:* Sandry 2019 and Shneiderman 2020 argue the design choice to anthropomorphize is itself the source of harm.
- *Practitioner ambivalence:* Sussman 2026 quotes proponents of "tactile-VR" AI companions; Kirk et al. note both harm and suicide-mitigation benefits.

**T2. Governance: prohibitive vs. observatory vs. self-regulatory.**
- *Prohibitive:* Goudarzi 2025 — nuclear-style restrictive controls.
- *Observatory:* Gilbert 2026 — academic/NGO observatory excluding platforms.
- *Self-regulatory, multi-level:* Shneiderman 2020 — engineering practices + safety culture + external certification.
- *Engineering-aligned oversight:* Kirk 2025 — transparent oversight mechanisms inside AI products.

**T3. The substitutability of human capacities and relations.**
- Where it is *denied* (Sussman/Garcia's evolutionary argument; Watercutter's "ChatGPT is not leaving its laundry on the floor" anecdote; Sandry's alterity argument).
- Where it is *measured* (Bruch's 25% aspirational-dating finding; Pew 50% / 5%; Common Sense Media 72%).
- Where it is *designed* (Shneiderman's tool-loop; Sandry's evocative object).

**T4. Speed of change.**
- Cluster 1 disagreement: 2025 already (Goudarzi) vs. 2028 inflection (Gilbert).
- Cluster 2: 10–40-year transitions (Zahidi) vs. 2025 chartable (Farley).
- Cluster 3: a "long" 20-year social-media erosion (Watercutter) punctuated by a 2025 inflection.

**T5. Diagnosis of loneliness and disconnection.**
- Evolutionary (Sussman/Garcia).
- Infrastructural / political-economic (Watercutter).
- Structural-intrapersonal / alignment (Kirk).
- Each diagnosis implies a different remedy (cultural restoration; antitrust and platform regulation; alignment engineering).

---

## Identified Research Gaps and Unaddressed Research Problems

The gaps above (within clusters) consolidate into research-problem candidates that span the domain and merit serious empirical and theoretical work. Twelve are listed in escalating scope.

### Gap-level research problems (focused, actionable)

**RP-1. The substitutability evidence gap.**
What do rigorous, preregistered, mixed-methods studies of humans' ability to distinguish AI from human outputs in creative and emotional registers actually show? Domain-specific replications of the Farley/Ipsos 97% figure (music), drawing on Wasserburger-Feingold-type paradigms from animal cognition.
*Cut across:* Clusters 2, 3, 4.

**RP-2. Platform business-model diagnosis with named empirical metrics.**
What concrete engagement, retention, and monetization metrics tie platform revenue to (a) anthropomorphic interfaces, (b) sycophantic model behavior, and (c) filter-bubble / swarm dynamics? The corpus asserts these ties (Watercutter, Gilbert, Goudarzi) but does not measure them.
*Cut across:* Clusters 1, 3, 4.

**RP-3. Comparative democratic-resilience study of AI swarms.**
How have authoritarian, hybrid, and consolidated democracies withstood (or failed to withstand) computational influence operations through 2024–2028? Uses Gilbert's 2028 prediction as pre-registered hypothesis.
*Cut across:* Cluster 1.

**RP-4. Empirical social-reward-hacking measurements.**
Do AI companion users exhibit measurable shifts in Basic Psychological Needs satisfaction, attachment style, or social-network composition over 6–24 months? Kirk et al. call for such studies; none appear in the corpus.
*Cut across:* Cluster 3.

**RP-5. Cross-cultural AI-companion ethnography.**
Where are AI companion markets mature (China, Japan, U.S.) and what are the locally specific harms/benefits, including East-Asian "touch starvation" framings and Islamic, Hindu, Buddhist, and Confucian ethical matrices around simulative intimacy?
*Cut across:* Cluster 3.

**RP-6. Global-South diffusion maps for generative AI in creative work.**
Farley focuses on Billboard; the actual geography of GenAI music and writing production is multi-polar and largely unmapped (cf. work on Nigerian, Brazilian, Indian, Filipino creator economies).
*Cut across:* Cluster 2.

### Mid-level research problems (synthesis, multi-cluster)

**RP-7. Anthropomorphism as a Western-provincial concept.**
How do Sinophone, Indic, Islamic, and Indigenous philosophy traditions frame non-human personhood (pre-existing concepts of jinn, kami, senshi, spirits, totems) — and how does that reframe the Sandry/Shneiderman design-philosophy debate? Could overcome the Nass-Fallacy problem from within rather than from without.
*Cut across:* Cluster 4 → Cluster 3.

**RP-8. Disability / neurodivergence use of AI companion systems.**
Do companion AIs measurably improve social participation, AAC accessibility, executive function, or affective regulation for disabled users? Significant counter-evidence to a "AI companionship = harm" frame may sit here, and is underrepresented in Cluster 3.
*Cut across:* Clusters 3, 4.

**RP-9. Auditing the AI-Influence Observatory model.**
Before any "AI Influence Observatory" (Gilbert) is implemented, what are its political-economy risks: who funds it, who regulates its access to platforms, how is its impartiality maintained when 72% of teens already use AI companions (Watercutter)?
*Cut across:* Clusters 1, 5.

**RP-10. Computational Social Science in the era of generative AI.**
Lazer's 2009 vision assumed passively collected passive data (phone records, badges). The post-2022 world features active agents producing synthetic data at scale (comments, posts, ratings, even replies to surveys). What becomes of CSS epistemics, IRB protocols, and replicability standards when up to half of online interaction may be synthetic? This is the central methodological crisis the corpus only obliquely gestures at.
*Cut across:* Cluster 5 with effects across all.

### High-level research problems (critical, paradigm-shifting)

**RP-11. Constitutive regulation of human-machine sociality.**
Treating AI companionship and AI influence as a single class of constitutive-relations problem (rather than as separate ethical problems) could yield a unified research agenda: who is permitted to design what kind of social relation into an AI, under what procedural legitimacy (democratic deliberation, regulatory standard-setting, community consent)? Bridges Kirk's intrapersonal dilemma language with Sandry's alterity language and Gilbert's observatory proposal.
*Cut across:* All clusters.

**RP-12. A field architecture for "AI and Society."**
Lazer's 2009 vision asked: what kind of science can study the digital society? Today, the renamed question is: what kind of science — and what kind of public-interest infrastructure — can study, regulate, and refuse the AI-mediated society? It requires interdisciplinary careers, field-grade journals, public funding for replication, and protection for "watchdog" researchers from platform retaliation. The corpus calls for this implicitly; it is rarely named as a research problem per se.
*Cut across:* All clusters.

---

## Methodological Notes & Transparency

- **Inclusion logic.** All 10 summaries were included. Five clusters were derived empirically; no summary was eliminated.
- **Cluster boundaries.** Boundaries were drawn by *primary* thematic content, with secondary cross-references recorded in "Tensions within the Group" and "Gaps in the Material."
- **Decisions logged.** Each analytical decision (whether Lazer 2009 deserves its own cluster, how to weight Sandry vs. Shneiderman, etc.) is traceable in `./agent_logs/run_log.md`, including rejected alternatives.
- **No outside material.** All claims are based on the ingested summaries; the citations in-cluster are reproduced from those summaries exactly as written, with `{Author, Year #ID}` markers preserved for downstream citation review.

---

## Final Note to the Reviewer

The five clusters and twelve research-problem candidates together define the *narrowest defensible* literature review for a paper titled along the lines of *"The Social Life of AI: From Platform Influence to Companion Affordances — A Critical Synthesis."* A wider topic (e.g., "AI and Society: Five Years After Lazer") would push Cluster 5 forward and tighten Clusters 1–3; a tighter topic (e.g., "Companion AI and Its Discontents") would dissolve Clusters 1–2 and 5 into context. The outline in `./outputs/outline.opml` follows the present, balanced organization.
