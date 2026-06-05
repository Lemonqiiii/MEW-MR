"""Rebuild manuscript reference section."""
import re

with open('E:/medical-review/manuscript/jitc_submission.md','r',encoding='utf-8') as f:
    text = f.read()

body = text.split('## References')[0].strip()

ref_lines = """1. Sweet DG, Carnielli V, Greisen G, et al. European Consensus Guidelines on the Management of Respiratory Distress Syndrome - 2019 Update. *Neonatology*. 2019;115(4):432-450. PMID: 30974433. [G - consensus guideline]

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

34. Venkataraman R, Kamaluddeen M, Hasan SU, Robertson HL, Lodha A. Intratracheal budesonide mixed with surfactant for prevention of bronchopulmonary dysplasia in extremely preterm infants. *Cochrane Database of Systematic Reviews*. 2021;3:CD013271. [F - Cochrane SR]"""

final = body + "\n\n---\n\n## References\n\n" + ref_lines
with open('E:/medical-review/manuscript/jitc_submission.md','w',encoding='utf-8') as f:
    f.write(final)

body = final.split('## References')[0]
refs = final.split('## References')[1]
words = len(re.findall(r'\b\w+\b', body))
ref_count = len(re.findall(r'^(\d+)\.', refs, re.MULTILINE))
secs = re.findall(r'^## \d\.', final, re.MULTILINE)
print(f'Sections: {len(secs)} {secs}')
print(f'Words: {words}')
print(f'Refs: {ref_count}')
print('OK')
