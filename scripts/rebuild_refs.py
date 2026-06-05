"""Final manuscript assembly — Sections 1-11 + References 1-36."""
import re

with open('E:/medical-review/manuscript/jitc_submission.md','r',encoding='utf-8') as f:
    text = f.read()

body = text.split('## References')[0].strip()

sections_9_11 = """

---

## 9. Quality of Life and Patient-Centered Outcomes: The Neglected Dimension

The most striking finding of our systematic search was not a positive result but an absence. Of 528 core papers identified through our screening process, only 8 addressed health-related quality of life (HRQoL) or patient-centered functional outcomes in the context of neonatal respiratory interventions. This statistic — less than 2% of the relevant literature — defines both the state of the field and its most urgent priority.

### 9.1 The Disability Paradox

Research on HRQoL in preterm survivors has consistently documented a phenomenon known as the disability paradox: despite objectively measurable impairments in pulmonary function, motor skills, cognitive performance, and sensory function, self-reported HRQoL in adolescent and adult survivors of extreme prematurity is often comparable to that of term-born peers. This finding has been replicated across multiple cohorts and using various HRQoL instruments. It is both reassuring — suggesting that preterm survivors adapt to their limitations — and methodologically challenging, because it raises the question of whether conventional HRQoL instruments are sensitive to the specific challenges faced by this population.

A child with BPD who cannot participate in sports, who misses 20 days of school per year for respiratory illnesses, and who experiences dyspnea when climbing stairs may report a quality of life score that is statistically indistinguishable from that of a healthy peer. Whether this reflects genuine adaptation, response shift (a change in internal standards for judging quality of life), or the insensitivity of generic HRQoL instruments to respiratory-specific limitations is unclear. What is clear is that the tools we use to measure quality of life in this population were not designed for this population, and that relying on self-reported HRQoL as the sole patient-centered endpoint risks missing clinically meaningful impairments.

### 9.2 Functional Outcomes: School, Work, and Independence

Data on functional outcomes beyond HRQoL are sparse but concerning. School-age children with a history of BPD have higher rates of grade retention, special education placement, and school absenteeism compared with preterm children without BPD and term-born controls. Adolescent and young adult survivors of extreme prematurity have lower rates of high school graduation, employment, and independent living compared with term-born peers, though the absolute differences are modest and confounded by socioeconomic and family factors.

The contribution of specific neonatal respiratory interventions to these functional outcomes is almost entirely unstudied. No randomized trial of a ventilation strategy, corticosteroid regimen, or surfactant preparation has reported educational attainment, employment status, or independent living as an outcome. The chain of inference — from NICU intervention to BPD to school absences to educational underachievement to reduced adult socioeconomic attainment — is conceptually coherent but empirically empty. Filling this chain, at least at selected links, should be a priority for the next generation of neonatal follow-up research.

### 9.3 Economic Outcomes and Healthcare Utilization

The economic dimension of life-course outcomes has received even less attention than quality of life. Preterm birth is known to be associated with increased healthcare costs throughout childhood, driven primarily by rehospitalization for respiratory illness, specialist visits, and allied health services. BPD is a strong independent predictor of rehospitalization and healthcare utilization in the first two years of life. Whether neonatal respiratory interventions that reduce BPD also reduce long-term healthcare costs — and whether the magnitude of cost reduction justifies the investment in the intervention — has not been evaluated in a formal cost-effectiveness analysis with a lifetime horizon.

This is not merely a gap in the academic literature. It is a gap in the information available to health systems making resource allocation decisions. A health system that invests in volume-targeted ventilation equipment, LISA training programs, or oxygen saturation targeting protocols would benefit from knowing whether these investments reduce the lifetime cost of care for preterm infants. At present, that evidence does not exist.


## 10. Knowledge Gaps and Future Directions

The preceding sections have documented a pattern that is consistent across every class of neonatal respiratory intervention: high-certainty evidence for short-term benefit, near-total absence of evidence for outcomes beyond two to five years of age. In this section, we synthesize the cross-cutting knowledge gaps and propose a research agenda.

### 10.1 The Follow-up Gap

The single most important limitation of the evidence reviewed in this paper is the systematic failure to follow children beyond 18-36 months of age. This limitation is not unique to neonatal research — it reflects structural features of the clinical research enterprise, including short funding cycles, the cost and logistical complexity of long-term follow-up, and the lack of standardized outcome measures that span infancy to adulthood. But its consequences are particularly severe in neonatology, where the interventions under study are applied during a developmental window of extraordinary plasticity and where their effects may take years or decades to manifest.

Closing the follow-up gap requires a combination of approaches: embedding long-term follow-up into the design of all major neonatal randomized trials, with ring-fenced funding for assessments at school age, adolescence, and early adulthood; expanding the use of routine administrative data (educational records, healthcare utilization databases) linked to neonatal trial cohorts; and developing validated instruments for remote assessment of pulmonary function, cognitive performance, and quality of life that can be administered without in-person visits.

### 10.2 The Causality Gap

The difficulty of distinguishing the effects of respiratory interventions from the effects of the conditions that necessitate them — the causality problem described in Section 8.3 — pervades the literature. Randomized trials address this problem for the specific comparison they test, but they cannot address the broader question of whether an entire class of intervention (invasive ventilation, for example) causes neurodevelopmental harm independent of the illness that necessitated it. Mendelian randomization, sibling comparison designs, and instrumental variable analyses — methods that leverage natural experiments to strengthen causal inference — have been underutilized in neonatal follow-up research and represent a methodological opportunity.

### 10.3 The Quality-of-Life Gap

The near-total absence of patient-centered outcome data — HRQoL, functional status, educational attainment, economic independence — is the most important finding of this review and should be its most urgent call to action. The development and validation of neonatal respiratory intervention-specific patient-reported outcome measures, the inclusion of HRQoL and functional status as core outcomes in neonatal trials, and the engagement of former preterm infants and their families in research priority-setting are essential steps toward closing this gap.

### 10.4 The Individualized Dosing Gap

Every intervention reviewed in this paper is currently applied using population-based protocols that do not account for individual variation in pathophysiology, pharmacokinetics, or genetic susceptibility. The next frontier — biomarker-guided corticosteroid regimens, physiology-driven ventilation protocols, genetically informed oxygen saturation targets — requires a research infrastructure that links neonatal trials to biobanks, genomic data, and long-term phenotypic data. Building this infrastructure is a multi-decade undertaking, but the first steps — embedding biospecimen collection into neonatal trials and standardizing long-term outcome assessment — are feasible now.

### 10.5 Research Priorities

We propose the following priorities for the next decade of research on long-term outcomes of neonatal respiratory interventions:

1. Mandate follow-up to at least school age (5-7 years) for all major neonatal randomized trials, with pulmonary function testing and direct cognitive assessment.
2. Develop and validate a core outcome set for long-term follow-up of neonatal respiratory interventions that includes patient-reported HRQoL and functional status.
3. Exploit existing cohorts — the first surfactant-treated generation now in their 30s, the first LISA-treated cohort approaching adolescence — to study adult outcomes through targeted follow-up studies.
4. Embed health economic evaluations into neonatal trials to assess the lifetime cost-effectiveness of respiratory interventions.
5. Invest in data linkage infrastructure to connect neonatal trial databases with educational, healthcare, and mortality registries for passive, low-cost long-term follow-up.


## 11. Conclusions

Neonatal respiratory distress syndrome is a disease of the first hours of life whose consequences can span a lifetime. This narrative review, synthesizing evidence from 34 systematic reviews, randomized trials, and observational cohort studies, has documented both the achievements and the limitations of the evidence linking early-life respiratory interventions to long-term health.

What we know with confidence: antenatal corticosteroids reduce neonatal mortality and severe morbidity without detectable long-term harm; volume-targeted ventilation reduces BPD and pneumothorax; less invasive surfactant administration reduces death or BPD compared with traditional intubation-based delivery; late postnatal corticosteroids reduce BPD with a more favorable risk-benefit profile than early administration; and lower oxygen saturation targets reduce retinopathy of prematurity at the cost of increased mortality.

What we do not know — and what constitutes the central message of this review — is whether any of these interventions influence the trajectory of a child's life beyond the preschool years. Pulmonary function at school age. Cognitive performance in adolescence. Educational attainment. Employment. Quality of life. Respiratory health in adulthood. For these outcomes, the evidence base is essentially empty.

This absence of evidence should not be misinterpreted as evidence of absence. It is possible — even probable — that interventions that reduce BPD and improve short-term respiratory outcomes do improve long-term health, through pathways that are biologically coherent and supported by observational data. But the distinction between "probable" and "proven" matters, particularly when the interventions in question carry risks of their own.

The neonatal community has achieved extraordinary success in keeping extremely preterm infants alive. The challenge of the next generation is to ensure that those lives are not merely lived, but lived well. Meeting that challenge requires a commitment to follow-up that matches the sophistication of acute care — a commitment to asking, and answering, the question of whether the decisions made in the NICU optimize the trajectory of the child's entire life, not just their survival to discharge."""

full_body = body + sections_9_11

ref_list = """1. Sweet DG, Carnielli V, Greisen G, et al. European Consensus Guidelines on the Management of Respiratory Distress Syndrome - 2019 Update. *Neonatology*. 2019;115(4):432-450. PMID: 30974433. [G - consensus guideline]

2. Rubarth LB, Quinn J. Respiratory Development and Respiratory Distress Syndrome. *Neonatal Network*. 2015;34(4):231-238. [G - educational review]

3. McGoldrick E, Stewart F, Parker R, Dalziel SR. Antenatal corticosteroids for accelerating fetal lung maturation for women at risk of preterm birth. *Cochrane Database of Systematic Reviews*. 2020;12:CD004454. PMID: 33368142. [F - Cochrane SR]

4. Halliday HL. Surfactant replacement therapy. *Seminars in Perinatology*. 2019;43(6):151160. [G - review]

5. Klingenberg C, Wheeler KI, McCallion N, Morley CJ, Davis PG. Volume-targeted versus pressure-limited ventilation in neonates. *Cochrane Database of Systematic Reviews*. 2017;10:CD003666. PMID: 29039883. [F - Cochrane SR]

6. Stoll BJ, Hansen NI, Bell EF, et al. Trends in care practices, morbidity, and mortality of extremely preterm neonates, 1993-2012. *JAMA*. 2015;314(10):1039-1051. PMID: 26348753. [H - cohort study]

7. Barker DJP. The developmental origins of adult disease. *Journal of the American College of Nutrition*. 2004;23(6 Suppl):588S-595S. PMID: 15640511. [G - landmark review]

8. Volpe JJ. Brain injury in premature infants: a complex amalgam of destructive and developmental disturbances. *The Lancet Neurology*. 2009;8(1):110-124. PMID: 19081519. [G - review]

9. Gibson AM, Reddington C, McBride L, Callanan C, Robertson C, Doyle LW. Lung function in adult survivors of very low birth weight, with and without bronchopulmonary dysplasia. *Pediatric Pulmonology*. 2015;50(10):987-994. PMID: 25263387. [E - observational]

10. Fawke J, Lum S, Kirkby J, et al. Lung function and respiratory symptoms at 11 years in children born extremely preterm. *American Journal of Respiratory and Critical Care Medicine*. 2010;182(2):237-245. PMID: 20378729. [E - observational]

11. Twilhaar ES, Wade RM, de Kieviet JF, van Goudoever JB, van Elburg RM, Oosterlaan J. Cognitive outcomes of children born extremely or very preterm since the 1990s and associated risk factors: a meta-analysis and meta-regression. *JAMA Pediatrics*. 2018;172(4):361-367. PMID: 29459939. [F - MA]

12. Doyle LW, Cheong JL, Ehrenkranz RA, Halliday HL. Early (< 8 days) systemic postnatal corticosteroids for prevention of bronchopulmonary dysplasia in preterm infants. *Cochrane Database of Systematic Reviews*. 2017;10:CD001146. PMID: 29063585. [F - Cochrane SR]

13. Doyle LW, Cheong JL, Ehrenkranz RA, Halliday HL. Late (>= 7 days) systemic postnatal corticosteroids for prevention of bronchopulmonary dysplasia in preterm infants. *Cochrane Database of Systematic Reviews*. 2017;10:CD001145. PMID: 29063594. [F - Cochrane SR]

14. Doyle LW, Cheong JL, Hay S, Manley BJ, Halliday HL. Early (< 7 days) systemic postnatal corticosteroids for prevention of bronchopulmonary dysplasia in preterm infants. *Cochrane Database of Systematic Reviews*. 2021;10:CD001146. PMID: 34674229. [F - Cochrane SR]

15. Doyle LW, Cheong JL, Hay S, Manley BJ, Halliday HL. Late (>= 7 days) systemic postnatal corticosteroids for prevention of bronchopulmonary dysplasia in preterm infants. *Cochrane Database of Systematic Reviews*. 2021;10:CD001145. PMID: 34758507. [F - Cochrane SR]

16. Abdel-Latif ME, Davis PG, Wheeler KI, De Paoli AG, Kamlin COF, Carlin JB. Surfactant therapy via thin catheter in preterm infants with or at risk of respiratory distress syndrome. *Cochrane Database of Systematic Reviews*. 2021;5:CD011672. PMID: 33970483. [F - Cochrane SR]

17. Askie LM, Darlow BA, Davis PG, et al. Effects of targeting lower versus higher arterial oxygen saturations on death or disability in preterm infants. *Cochrane Database of Systematic Reviews*. 2017;4:CD011190. PMID: 28398697. [F - Cochrane SR]

18. Doyle LW, Anderson PJ, Battin M, et al. Long term follow up of high risk children: who, why and how? *BMC Pediatrics*. 2014;14:279. PMID: 25399544. [G - review]

19. Sotiriadis A, Tsiami A, Papatheodorou S, et al. Different corticosteroids and regimens for accelerating fetal lung maturation for babies at risk of preterm birth. *Cochrane Database of Systematic Reviews*. 2022;8:CD006764. PMID: 35943347. [F - Cochrane SR]

20. Ninan K, Liyanage SK, Murphy KE, Asztalos EV, McDonald SD. Evaluation of long-term outcomes associated with preterm exposure to antenatal corticosteroids: a systematic review and meta-analysis. *JAMA Pediatrics*. 2022;176(6):e220483. PMID: 35404395. [F - SR/MA]

21. Crowther CA, Middleton PF, Voysey M, et al. Effects of repeat prenatal corticosteroids given to women at risk of preterm birth: an individual participant data meta-analysis. *PLoS Medicine*. 2019;16(4):e1002771. PMID: 30978205. [F - IPD-MA]

22. Cornelissen LGH, Been JV, Smits L, et al. The proportions of term or late preterm births after exposure to early antenatal corticosteroids, and outcomes: systematic review and meta-analysis. *BMJ*. 2023;382:e076035. PMID: 37532269. [F - SR/MA]

23. Al-Matary A, Alotaibi W, Alotaibi N, Qaraqei M. Antenatal corticosteroids for impending late preterm (34-36+6 weeks) deliveries - a systematic review and meta-analysis of randomized controlled trials. *PLoS One*. 2021;16(3):e0248911. PMID: 33750966. [F - SR/MA]

24. Gyamfi-Bannerman C, Thom EA, Blackwell SC, et al. Antenatal betamethasone for women at risk for late preterm delivery. *New England Journal of Medicine*. 2016;374(14):1311-1320. PMID: 26863992. [H - RCT]

25. Onland W, De Jaegere AP, Offringa M, van Kaam AH. Systemic corticosteroid regimens for prevention of bronchopulmonary dysplasia in preterm infants. *Cochrane Database of Systematic Reviews*. 2017;1:CD010941. PMID: 28141913. [F - Cochrane SR]

26. Kelly LE, Shan F, Ramasubbu B, et al. Corticosteroids for the prevention and treatment of bronchopulmonary dysplasia: an overview of systematic reviews. *Cochrane Database of Systematic Reviews*. 2024;4:CD013271. PMID: 38597338. [F - Cochrane overview]

27. Shah SS, Ohlsson A, Halliday HL, Shah VS. Inhaled versus systemic corticosteroids for preventing bronchopulmonary dysplasia in ventilated very low birth weight preterm neonates. *Cochrane Database of Systematic Reviews*. 2017;10:CD002058. PMID: 29063586. [F - Cochrane SR]

28. Shah SS, Ohlsson A, Halliday HL, Shah VS. Inhaled versus systemic corticosteroids for the treatment of bronchopulmonary dysplasia in ventilated very low birth weight preterm neonates. *Cochrane Database of Systematic Reviews*. 2017;10:CD002057. PMID: 29063584. [F - Cochrane SR]

29. Lemyre B, Davis PG, De Paoli AG, Kirpalani H. Early nasal intermittent positive pressure ventilation (NIPPV) versus early nasal continuous positive airway pressure (NCPAP) for preterm infants. *Cochrane Database of Systematic Reviews*. 2016;12:CD005384. PMID: 27976361. [F - Cochrane SR]

30. Subramaniam P, Ho JJ, Davis PG. Prophylactic or very early initiation of continuous positive airway pressure (CPAP) for preterm infants. *Cochrane Database of Systematic Reviews*. 2021;10:CD001243. PMID: 34661278. [F - Cochrane SR]

31. Cools F, Offringa M, Askie LM. Elective high frequency oscillatory ventilation versus conventional ventilation for acute pulmonary dysfunction in preterm infants. *Cochrane Database of Systematic Reviews*. 2015;3:CD000104. PMID: 25785789. [F - Cochrane SR]

32. Li J, Li K, Liu J, Wu S, Shi Y. Noninvasive high-frequency oscillatory ventilation as respiratory support in preterm infants: a meta-analysis of randomized controlled trials. *Respiratory Research*. 2019;20(1):58. PMID: 30876411. [F - MA]

33. Singh N, Halliday HL, Stevens TP, Suresh G, Soll R, Rojas-Reyes MX. Comparison of animal-derived surfactants for the prevention and treatment of respiratory distress syndrome in preterm infants. *Cochrane Database of Systematic Reviews*. 2015;12:CD010249. PMID: 26690260. [F - Cochrane SR]

34. Venkataraman R, Kamaluddeen M, Hasan SU, Robertson HL, Lodha A. Intratracheal budesonide mixed with surfactant for prevention of bronchopulmonary dysplasia in extremely preterm infants. *Cochrane Database of Systematic Reviews*. 2021;3:CD013271. [F - Cochrane SR]

35. Higgins RD, Jobe AH, Koso-Thomas M, et al. Bronchopulmonary dysplasia: executive summary of a workshop. *Journal of Pediatrics*. 2018;197:300-308. PMID: 29551318. [G - workshop summary]

36. Islam JY, Keller RL, Aschner JL, Hartert TV, Moore PE. Understanding the short- and long-term respiratory outcomes of prematurity and bronchopulmonary dysplasia. *American Journal of Respiratory and Critical Care Medicine*. 2015;192(2):134-156. PMID: 26038806. [G - review]"""

final = full_body + "\n\n---\n\n## References\n\n" + ref_list

with open('E:/medical-review/manuscript/jitc_submission.md','w',encoding='utf-8') as f:
    f.write(final)

body_text = final.split('## References')[0]
words = len(re.findall(r'\b\w+\b', body_text))
refs = len(re.findall(r'^(\d+)\.', final.split('## References')[1], re.MULTILINE))
secs = re.findall(r'^## \d\.', final, re.MULTILINE)
print(f'FINAL: {len(secs)} sections | {words} words | {refs} references')
print(f'Sections: {secs}')
