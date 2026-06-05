# Mechanisms of Immunotherapy Resistance in Squamous Cell Carcinoma of Non-Small Cell Lung Cancer

## Title Page

**Title**: Mechanisms of Immunotherapy Resistance in Squamous Cell Carcinoma of Non-Small Cell Lung Cancer

**Running title**: Immunotherapy Resistance in Lung Squamous Cell Carcinoma

**Article type**: Review

**Authors**: [Author 1]¹, [Author 2]¹, [Author 3]¹\*

**Affiliations**:
1. [Department/Institution Name], [City], [Country]

**\*Corresponding author**:
[Name], [Full address], [Email], [Phone]

**Word count**: ~9,300 (main text incl. Search Strategy); 246 (abstract)

**Number of figures**: 1 | **Number of tables**: 2 | **References**: 41

**Figures and Tables**: Figure 1 (Three-dimensional resistance framework); Table 1 (Tumor-intrinsic mechanisms of ICI resistance in LUSC); Table 2 (TME-mediated resistance mechanisms and therapeutic interventions).

**Keywords**: lung squamous cell carcinoma; immunotherapy resistance; immune checkpoint inhibitors; tumor microenvironment; T cell exhaustion; KEAP1/NRF2

---

## Abstract

Lung squamous cell carcinoma (LUSC), accounting for approximately 30% of non-small cell lung cancers, is characterized by a paucity of actionable driver mutations and a consequent reliance on immunotherapy as the cornerstone of systemic treatment. Immune checkpoint inhibitors (ICIs) targeting the PD-1/PD-L1 and CTLA-4 axes have transformed the therapeutic landscape; however, only a minority of patients achieve durable benefit, with both primary and acquired resistance representing critical clinical challenges. Resistance in LUSC arises through a complex interplay of tumor-intrinsic alterations, tumor microenvironment (TME)-mediated immunosuppression, and treatment-induced adaptive changes. This review provides a comprehensive synthesis of the mechanisms underlying ICI resistance in LUSC, organized across three interconnected dimensions. First, we survey the unique immune landscape of LUSC, including molecular classification frameworks and the clinically significant Exhausted Immune Class (EIC) present in 28–36% of patients. Second, we examine tumor-intrinsic resistance mechanisms encompassing oncogenic signaling pathways (PI3K/AKT, KEAP1/NRF2, p38 MAPK), epithelial-mesenchymal transition, epigenetic dysregulation, and defective cell death programs. Third, we analyze TME-mediated resistance driven by T cell exhaustion with multi-checkpoint co-expression, immunosuppressive cell populations (TAMs, CAFs, MDSCs, Tregs), metabolic constraints including hypoxia and lactic acidosis, and the emerging role of the intratumoral microbiome. We further discuss acquired resistance through clonal evolution, histological transformation, and phenotypic plasticity. Finally, we evaluate therapeutic strategies to overcome these barriers, including rational immunotherapy combinations, tumor-intrinsic pathway targeting, TME remodeling, and biomarker-guided precision approaches. By integrating these mechanistic insights, we aim to provide a framework for understanding and ultimately overcoming immunotherapy resistance in LUSC.

---

## Key Messages

**What is already known on this topic**
- Immune checkpoint inhibitors are standard-of-care for advanced LUSC, yet response rates remain limited.
- LUSC harbors a distinct genomic landscape (TP53, PI3KCA, KEAP1 mutations; lack of targetable drivers) that influences immunotherapy outcomes.
- The LUSC tumor microenvironment exhibits unique features including high CAF content and prevalent immune exclusion.

**What this study adds**
- A comprehensive three-dimensional framework (tumor-intrinsic, TME-mediated, acquired) for understanding immunotherapy resistance specifically in LUSC.
- Integration of the Exhausted Immune Class (EIC) concept, present in 28–36% of LUSC patients, with therapeutic implications for multi-checkpoint blockade.
- Systematic analysis of 18 cross-cutting resistance mechanisms with corresponding therapeutic strategies.
- A TIME-based therapeutic decision framework for personalized immunotherapy in LUSC.

**How this study might affect research, practice, or policy**
- Provides mechanistic rationale for LUSC-specific combination immunotherapy trial design.
- Identifies KEAP1/NRF2, EMT-LAMC2-CD44, ALDOA-driven metabolic suppression, and STING pathway suppression as high-priority therapeutic targets.
- Supports the need for TIME-based patient stratification in future clinical trials.

---

## 1. Introduction

Lung cancer remains the leading cause of cancer-related mortality worldwide, with non-small cell lung cancer (NSCLC) accounting for approximately 85% of all cases [1]. Among NSCLC subtypes, lung squamous cell carcinoma (LUSC) represents roughly 30% of diagnoses, making it the second most prevalent histological subtype after lung adenocarcinoma (LUAD) [2]. Patients with LUSC face particularly challenging clinical outcomes, with a five-year survival rate below 20% for advanced-stage disease [3]. Historically, the standard-of-care options were largely confined to platinum-based chemotherapy, which offered marginal survival benefits and substantial toxicity [4].

What most profoundly shapes the LUSC therapeutic landscape is an absence: the striking paucity of actionable driver mutations. Unlike LUAD, in which targeted therapies against EGFR, ALK, ROS1, BRAF, and KRAS G12C have transformed treatment paradigms, LUSC harbors remarkably few therapeutically tractable genomic alterations [5,6]. Instead, the genomic landscape of LUSC is dominated by frequent alterations in tumor suppressor genes—including *TP53* (~80%), *CDKN2A* (~70%, encompassing mutation, deletion, and epigenetic silencing), and *KEAP1* (~12%)—as well as recurrent amplifications of *PIK3CA* (~30–40%), *FGFR1* (~20%), and the chromosome 3q locus encompassing the squamous lineage transcription factors *SOX2* and *TP63* [5,7]. Despite numerous clinical trials evaluating targeted agents directed at these genomic features, none have yet yielded a regulatory approval specifically for LUSC, underscoring the urgent unmet need for effective therapeutic strategies in this patient population [7].

The advent of immune checkpoint inhibitors (ICIs) has fundamentally altered the treatment landscape for LUSC. Antibodies targeting programmed death-1 (PD-1; nivolumab, pembrolizumab), its ligand PD-L1 (atezolizumab, durvalumab), and cytotoxic T-lymphocyte antigen 4 (CTLA-4; ipilimumab) have demonstrated meaningful clinical activity across multiple lines of therapy in advanced NSCLC, with LUSC patients consistently deriving benefit comparable to or exceeding that observed in non-squamous histology [8–10]. Landmark phase III trials—including KEYNOTE-407 (pembrolizumab + chemotherapy in first-line squamous NSCLC), CheckMate-017 (nivolumab in second-line squamous NSCLC), and IMpower-131 (atezolizumab + chemotherapy in squamous NSCLC, which demonstrated progression-free survival benefit though overall survival improvement did not reach statistical significance in the intention-to-treat population)—established immunotherapy-based regimens as new standards of care [8,11]. More recently, cemiplimab, a fully human anti-PD-1 antibody with an engineered hinge-region designed to minimize immunogenicity, has demonstrated particular promise in LUSC patients with ultra-high PD-L1 expression (tumor proportion score ≥ 90%), defining a potentially distinct therapeutic niche for this challenging histology [12].

Despite these advances, only a minority of patients achieve durable clinical benefit from ICI therapy. Across advanced NSCLC populations, objective response rates to first-line pembrolizumab monotherapy in PD-L1-high (≥50%) patients range from approximately 40–45%, while the addition of platinum-based chemotherapy increases responses to approximately 55–60% in squamous NSCLC (KEYNOTE-407) [8,13]. However, a substantial proportion of patients exhibit **primary resistance**, defined as disease progression without any evidence of initial clinical benefit, while many initial responders eventually develop **acquired resistance**, manifesting as tumor regrowth after an initial period of disease control [14]. The Lung-MAP S1400F substudy, which specifically evaluated dual PD-L1/CTLA-4 blockade (durvalumab + tremelimumab) in anti-PD-(L)1-resistant squamous NSCLC, reported objective response rates of only 7% in the primary resistance cohort and 0% in the acquired resistance cohort, illustrating the formidable challenge of overcoming established immunotherapy resistance [15]. Similarly, the Lung-MAP S1400I phase III trial comparing nivolumab plus ipilimumab versus nivolumab alone in previously treated squamous NSCLC did not demonstrate a significant overall survival benefit for dual checkpoint blockade over monotherapy (HR 0.87, P = 0.36), underscoring the complexity of optimizing combination immunotherapy in this histology [40].

Underlying these disappointing clinical outcomes is a complex web of resistance mechanisms spanning three interconnected domains: tumor cell-intrinsic alterations, dynamic remodeling of the tumor microenvironment (TME), and treatment-induced selective pressures that drive clonal evolution and phenotypic adaptation [14,16]. The LUSC TME is distinguished by several features that collectively create an immune-evasive niche: a high prevalence of immunosuppressive cell populations including M2-polarized tumor-associated macrophages (TAMs), regulatory T cells (Tregs), and myeloid-derived suppressor cells (MDSCs); a cytokine milieu dominated by transforming growth factor-β (TGF-β) and interleukin-6 (IL-6); and a metabolically hostile microenvironment characterized by hypoxia, lactic acidosis, and nutrient depletion [16,17]. Furthermore, recent multi-omics studies have identified a distinct **Exhausted Immune Class** (EIC) present in 28–36% of LUSC patients, characterized by dense lymphocytic infiltration paradoxically coupled with co-upregulation of up to nine inhibitory immune checkpoints, including PD-1, CTLA-4, LAG-3, TIGIT, and TIM-3 [18]. This state of "inflamed but functionally suppressed" immunity highlights the inadequacy of single-agent PD-1/PD-L1 blockade and underscores the need for mechanistically informed combination strategies.

In this review, we provide a comprehensive synthesis of the current understanding of immunotherapy resistance mechanisms in LUSC, organized across three interconnected dimensions (**Figure 1**). First, we survey the immune landscape of LUSC, including its unique TIME composition and molecular classification frameworks that inform patient stratification. Second, we dissect **tumor-intrinsic resistance mechanisms**—from oncogenic signaling pathways and epigenetic dysregulation to EMT-driven immune exclusion and dysregulated cell death programs. Third, we examine **TME-mediated resistance** arising from immunosuppressive cell populations, cytokine networks, metabolic reprogramming, and the emerging role of the intratumoral microbiome. We then discuss **acquired resistance** driven by clonal evolution, histological transformation, and phenotypic plasticity under therapeutic pressure. Finally, we evaluate emerging therapeutic strategies designed to overcome these resistance barriers, including rational immunotherapy combinations, TME-remodeling approaches, and biomarker-guided precision immunotherapy. By integrating findings across these mechanistic domains, this review aims to provide a framework for understanding the multifaceted nature of immunotherapy resistance in LUSC and to identify actionable opportunities for improving outcomes in this challenging disease.

---

## 2. The Immune Landscape of LUSC

Understanding the mechanisms of immunotherapy resistance in LUSC requires a foundational appreciation of its unique tumor immune microenvironment (TIME). While LUSC and LUAD share a common anatomical origin in the lung, their immune landscapes diverge substantially, reflecting differences in mutational processes, stromal composition, and evolutionary trajectories. Recent advances in single-cell RNA sequencing (scRNA-seq), spatial transcriptomics, and multi-omics integration have provided unprecedented resolution in dissecting the cellular and molecular architecture of the LUSC TIME, revealing distinct immune subtypes and immunosuppressive circuits that directly inform both prognosis and therapeutic strategy.

### 2.1 TIME Heterogeneity and Molecular Classification

The TIME of LUSC is characterized by profound inter-tumoral and intra-tumoral heterogeneity that fundamentally shapes responsiveness to immunotherapy [16]. Building on the canonical tripartite classification of tumor immune phenotypes—immune-inflamed, immune-excluded, and immune-desert—recent studies have refined these categories specifically for LUSC using integrative multi-omics approaches [16,19].

**Immune-inflamed LUSC** is defined by abundant infiltration of CD8+ cytotoxic T lymphocytes (CTLs), activated CD4+ memory T cells, and dendritic cells (DCs) within the tumor parenchyma. These tumors typically express high levels of effector cytokines and cytolytic markers, consistent with an ongoing—albeit ultimately ineffective—anti-tumor immune response [16]. Paradoxically, many immune-inflamed LUSCs simultaneously upregulate multiple inhibitory immune checkpoints and harbor elevated frequencies of immunosuppressive regulatory T cells (Tregs) and M2-polarized macrophages, creating a state of **"inflamed but functionally suppressed"** immunity that frequently underpins primary resistance to single-agent PD-1/PD-L1 blockade [18,20].

**Immune-excluded LUSC** is characterized by CTLs and other immune effector cells that are restricted to the stromal compartment surrounding tumor nests, unable to penetrate the tumor parenchyma. This exclusion is largely mediated by cancer-associated fibroblasts (CAFs), which deposit dense extracellular matrix (ECM) components—including collagen, fibronectin, and laminin—that form a physical barrier to T cell infiltration [16]. In particular, POSTN+ CAFs and FAP+ CAFs have been shown to create chemorepellent gradients and align ECM fibers perpendicular to the tumor boundary, effectively trapping T cells in the peritumoral stroma [16]. Spatial transcriptomic analyses have revealed close co-localization of CAF subsets with APOE+ tumor-associated macrophages (TAMs), identifying a CAF-TAM signaling axis that reinforces immune exclusion through coordinated cytokine and chemokine secretion [16].

**Immune-desert LUSC** represents a minority of cases and is marked by a near-complete absence of T cells within both the tumor and stromal compartments. This phenotype is thought to arise from defective innate immune sensing—including impaired STING/cGAS pathway activation—and insufficient dendritic cell priming, resulting in a failure to initiate productive anti-tumor T cell responses [16,19]. Immune-desert tumors pose a particularly difficult therapeutic challenge, as ICI monotherapy is unlikely to be effective in the absence of pre-existing T cell infiltration.

Beyond these qualitative descriptions, integrative genome-scale analyses have established molecular classification frameworks for LUSC based on immune gene expression signatures, immune cell deconvolution algorithms, and multi-omics data integration [19,21]. Yin et al. identified distinct immune subtypes of LUSC through unsupervised clustering of immune-related gene expression profiles, stratifying patients into groups with divergent survival outcomes and predicted immunotherapy responsiveness [19]. Similarly, Yang et al. identified a cytokine-dominated immunosuppressive class—discussed in detail below—that exhibits a unique molecular profile with direct therapeutic implications [18]. Song et al., using bulk and single-cell RNA sequencing of 513 LUSC samples, delineated six molecular subtypes (CS1–CS6) and identified CS3 as a lymphocyte-infiltrated subtype that paradoxically displays elevated exhaustion markers (CTLA-4, LAG-3, PD-1) and predicted resistance to ICB therapy through TIDE analysis [20]. These classification efforts consistently converge on the observation that the mere presence of tumor-infiltrating lymphocytes is insufficient to predict ICI responsiveness in LUSC; rather, the functional state and spatial organization of the immune infiltrate are critical determinants of therapeutic outcome.

### 2.2 LUSC versus LUAD: Divergent Immune Contextures

Although LUSC and LUAD are both classified as NSCLC, they arise from distinct cells of origin, harbor fundamentally different genomic landscapes, and exhibit markedly divergent immune microenvironments [22,23]. These differences have profound implications for the design and interpretation of immunotherapy strategies.

At the genomic level, LUAD is enriched for targetable driver mutations—most notably *EGFR* (~30–40% in East Asian, ~10–15% in Western populations), *KRAS* (~30%), *ALK* rearrangements (~5%), and *ROS1* fusions (~1–2%)—which are associated with relatively lower tumor mutational burden (TMB) and a less inflamed TIME in the EGFR-mutant subset [22]. LUSC, in contrast, is dominated by loss-of-function mutations in tumor suppressors (*TP53*, *CDKN2A*, *KEAP1*) and recurrent amplifications (*PIK3CA*, *FGFR1*, *SOX2*), generating a higher overall TMB and neoantigen burden that would theoretically predict greater immunogenicity [22,23]. However, this elevated neoantigen load does not translate into superior ICI responses in LUSC compared to LUAD, suggesting the presence of potent counter-regulatory immunosuppressive mechanisms.

At the cellular level, comparative analyses have revealed systematic differences in the immune composition of LUSC and LUAD [23]. Yan et al. performed a comprehensive lncRNA-based immune heterogeneity analysis comparing LUAD and LUSC and found that the two subtypes differ significantly in the proportions and functional states of infiltrating immune cells. Specifically, LUSC tumors exhibit higher infiltration of M2 macrophages and resting CD4+ memory T cells, whereas LUAD tumors tend to have greater infiltration of naïve B cells and plasma cells [23]. LUSC also demonstrates a higher prevalence of the immune-excluded phenotype compared to LUAD, driven by more extensive CAF activation and ECM remodeling [16,22]. Furthermore, the cytokine milieu in LUSC is skewed toward TGF-β and IL-6/STAT3 signaling, promoting both immune suppression and EMT, while LUAD is more commonly associated with EGFR-driven immunosuppressive programs [22].

These subtype-specific immune features carry direct clinical implications. First, the high prevalence of immune exclusion in LUSC suggests that strategies targeting CAF-mediated stromal barriers—such as FAP inhibitors, hedgehog pathway antagonists, or TGF-β blockade—may be particularly relevant for this histology. Second, the distinct immune checkpoint expression profiles between LUSC and LUAD may inform the rational selection of combination immunotherapy partners [22]. Third, prognostic and predictive biomarkers developed in LUAD may not be directly transferable to LUSC, given the divergent immune biology. These considerations underscore the need for LUSC-specific immunotherapeutic strategies and highlight the importance of developing biomarkers specifically validated in squamous histology.

### 2.3 The Exhausted Immune Class: A Framework for Understanding Resistance

A landmark contribution to the understanding of LUSC immune biology was the identification of the **Exhausted Immune Class (EIC)** by Yang et al., who performed unsupervised clustering of RNA sequencing data from 624 LUSC samples [18]. This analysis revealed that approximately 28–36% of LUSC patients belong to the EIC, which is characterized by a distinctive molecular signature with critical implications for immunotherapy resistance.

The EIC is defined by the concurrent presence of four hallmark features [18]. First, tumors in this class exhibit significant enrichment of T cell exhaustion signatures, with elevated expression of canonical exhaustion-associated transcription factors including TOX and EOMES, accompanied by reduced expression of TCF-1 (encoded by *TCF7*), a marker of progenitor exhausted T cells (Tpex) that retain proliferative capacity and responsiveness to PD-1 blockade. This shift from a Tpex-dominant to a terminally exhausted T cell compartment represents a critical barrier to ICI efficacy, as terminally exhausted T cells are largely refractory to PD-1 pathway reactivation.

Second, the EIC is characterized by the co-upregulation of up to **nine inhibitory immune checkpoints**—CTLA-4, PD-1 (PDCD1), LAG-3, BTLA, TIGIT, TIM-3 (HAVCR2), IDO1, SIGLEC7, and VISTA—representing a state of broad, multi-receptor immunosuppression that renders single-agent PD-1/PD-L1 blockade mechanistically insufficient [18]. This finding provides a molecular explanation for the clinical observation that many LUSC patients with high PD-L1 expression nevertheless fail to respond to pembrolizumab or nivolumab monotherapy.

Third, EIC tumors are heavily infiltrated by immunosuppressive cell populations, with a particularly high fraction of M2-polarized macrophages and CD4+FOXP3+ Tregs. These cells produce immunosuppressive cytokines—including TGF-β, IL-10, and CCL18—that directly inhibit CTL effector function and promote further T cell exhaustion [18].

Fourth, the EIC is paradoxically associated with high overall densities of tumor-infiltrating lymphocytes (TILs), yet these patients experience significantly worse prognosis compared to those with lower TIL infiltration. This finding reinforces the critical distinction between immune infiltration *quantity* and immune *competence*, and highlights the inadequacy of TIL density alone as a biomarker for ICI responsiveness in LUSC.

The EIC concept has been corroborated and extended by subsequent studies. Song et al. identified a similar phenotype in their CS3 molecular subtype, which demonstrated high lymphocyte infiltration coupled with elevated exhaustion markers and predicted ICB resistance through independent computational methods [20]. Furthermore, the CS3 subtype was found to specifically upregulate the LAMC2-CD44 molecular axis, an EMT-associated pathway that modulates both tumor proliferation and immune exclusion, providing a potential mechanistic link between tumor cell-intrinsic programs and the exhausted immune phenotype.

Taken together, the characterization of the LUSC TIME—spanning its heterogeneous cellular composition, its divergent features relative to LUAD, and the clinically critical EIC—establishes the biological foundation upon which specific resistance mechanisms operate. The following sections will dissect these mechanisms in detail, beginning with tumor cell-intrinsic determinants of resistance.

---

## 3. Tumor-Intrinsic Resistance Mechanisms

Tumor cell-intrinsic alterations represent a fundamental layer of immunotherapy resistance in LUSC, operating through diverse mechanisms that converge on a common endpoint: the failure of immune effector cells to recognize and eliminate malignant cells. These mechanisms range from oncogenic signaling pathways that actively sculpt an immunosuppressive microenvironment, to epigenetic programs that silence antigen presentation machinery, to cell death pathway defects that render tumor cells resistant to CTL-mediated killing.

### 3.1 Oncogenic Signaling Pathways

#### 3.1.1 PI3K/AKT/mTOR Pathway

The phosphatidylinositol 3-kinase (PI3K) pathway is among the most frequently activated oncogenic networks in LUSC, with *PIK3CA* amplification and activating mutations occurring in approximately 30–40% of cases [5]. Activation of PI3K/AKT/mTOR signaling promotes tumor cell proliferation and survival while concurrently driving immune evasion through multiple mechanisms: upregulation of PD-L1 expression via AKT-mediated stabilization of PD-L1 mRNA; increased secretion of immunosuppressive cytokines including IL-10 and TGF-β; and promotion of M2 macrophage polarization within the TME [5,7]. Preclinical studies have demonstrated that mTOR inhibition can reverse PI3K-driven PD-L1 expression and restore T cell-mediated killing, providing a rationale for the combination of PI3K/mTOR inhibitors with ICIs in *PIK3CA*-altered LUSC [5]. However, clinical development of these combinations remains in early stages for squamous NSCLC, and the therapeutic window may be limited by the metabolic and immunologic toxicities of mTOR inhibition.

#### 3.1.2 KEAP1/NRF2 Pathway

Mutations in *KEAP1* (Kelch-like ECH-associated protein 1), occurring in approximately 12% of LUSC, have emerged as one of the most robust predictors of primary resistance to ICIs across NSCLC subtypes [5,7]. Under physiological conditions, KEAP1 targets the transcription factor NRF2 (nuclear factor erythroid 2-related factor 2) for proteasomal degradation. KEAP1 loss-of-function mutations result in constitutive NRF2 stabilization and nuclear translocation, driving a broad transcriptional program of antioxidant and cytoprotective genes [5]. This activated NRF2 program profoundly alters the immunogenicity of tumor cells through several convergent mechanisms: enhanced scavenging of reactive oxygen species (ROS) reduces immunogenic cell death and impairs dendritic cell activation; upregulation of xenobiotic efflux transporters limits intracellular accumulation of cytotoxic molecules released by CTLs; and suppression of pro-inflammatory cytokine production, including type I interferons, attenuates innate immune sensing [5,7]. Clinically, *KEAP1*-mutant LUSC is associated with significantly shorter progression-free survival on ICI therapy, and emerging evidence suggests that these tumors may require distinct therapeutic strategies—potentially including NRF2 inhibitors, glutaminase antagonists, or STING agonists to bypass the suppressed innate immune axis [5].

#### 3.1.3 MAPK/p38 Signaling

Beyond the well-characterized RAS/RAF/MEK/ERK cascade, the stress-activated p38 MAPK pathway has recently been implicated in LUSC immune evasion. Lin et al. demonstrated that transglutaminase 2 (TGM2), an enzyme that catalyzes protein cross-linking, is significantly overexpressed in LUSC and independently predicts poor overall survival (P = 0.00018) [24]. Mechanistically, TGM2 activates p38 MAPK signaling, which in turn promotes tumor cell proliferation, migration, invasion, and resistance to apoptosis. Concurrently, TGM2-high tumors exhibit an immunosuppressive TME characterized by reduced Th1 cell infiltration and enrichment of immunosuppressive cell populations [24]. The upstream regulator of TGM2 was identified as the glucocorticoid receptor NR3C1, which directly binds the *TGM2* promoter and drives its transcription, as validated by chromatin immunoprecipitation-qPCR. This NR3C1–TGM2–p38 MAPK axis represents a potentially targetable tumor-intrinsic mechanism linking stress signaling to immune evasion in LUSC [24].

#### 3.1.4 FGFR1 and EGFR: The Paradox of RTK Overexpression

Fibroblast growth factor receptor 1 (*FGFR1*) amplification occurs in approximately 20% of LUSC, and epidermal growth factor receptor (EGFR) protein is frequently overexpressed on the tumor cell surface [5,7]. However, the clinical experience with targeted agents directed against these receptors in LUSC has been uniformly disappointing. FGFR inhibitors, including erdafitinib and infigratinib, have shown minimal single-agent activity in *FGFR1*-amplified LUSC, likely because FGFR1 amplification does not consistently translate to pathway addiction in the context of multiple co-occurring genomic alterations [5]. The failure of EGFR-targeted therapies is perhaps even more instructive: despite robust EGFR protein expression in many LUSC tumors, EGFR tyrosine kinase inhibitors (TKIs) are clinically ineffective, and activating *EGFR* mutations—the cardinal predictor of TKI sensitivity in LUAD—are exceedingly rare in LUSC [25]. Mechanistic studies have revealed that EGFR protein expression in LUSC is accompanied by constitutive, ligand-independent activation of the downstream RAS/MAPK and PI3K/AKT pathways, which are sustained by parallel inputs from FGFR1, PI3KCA, and other receptor tyrosine kinases [25]. Consequently, EGFR signals are functionally dispensable, and EGFR TKI monotherapy is mechanistically futile—a phenomenon that illustrates a broader principle in LUSC biology: the redundancy and interconnectivity of oncogenic signaling networks that limit the efficacy of single-pathway inhibition [5,7,25].

### 3.2 Epithelial-Mesenchymal Transition (EMT)

Epithelial-mesenchymal transition is a developmental program that, when aberrantly activated in carcinoma cells, confers invasive and metastatic capability while simultaneously driving immune evasion [21]. In LUSC, EMT activation is strongly associated with an immunosuppressive TME and resistance to ICIs, operating through multiple intersecting mechanisms.

Transcriptional profiling of LUSC has consistently identified EMT-related gene signatures as powerful prognostic discriminants. Zhang et al. constructed a six-gene EMT-based prognostic model (GAB2, ALDOA, PCDHA3, TMEM92, ERH, IRS4) that stratified LUSC patients into distinct risk groups with significantly different immune infiltration profiles: low-risk tumors were enriched for activated CD8+ T cells, activated CD4+ memory T cells, and naïve B cells, whereas high-risk tumors exhibited high fractions of resting CD4+ memory T cells and M0 macrophages—a pattern consistent with diminished adaptive immune engagement [21].

A critical molecular link between EMT and immune exclusion in LUSC was identified by Song et al., who demonstrated that the laminin γ2 (LAMC2)–CD44 axis is a key driver of immune resistance in the lymphocyte-infiltrated CS3 molecular subtype [20]. LAMC2, an ECM component of the laminin-332 complex, and CD44, its principal cell-surface receptor, are both EMT-associated genes whose co-expression is tightly correlated with immune exclusion. Multicolor immunofluorescence revealed an inverse spatial relationship between LAMC2-CD44 expression and CD8+ T cell infiltration, suggesting that this axis promotes immune exclusion by remodeling the peritumoral ECM and enhancing tumor cell-ECM adhesion, thereby physically impeding CTL access to tumor cells [20].

Beyond the LAMC2-CD44 axis, EMT contributes to immune resistance through several complementary mechanisms. Mesenchymal tumor cells upregulate the expression of multiple immunosuppressive factors including TGF-β, VEGF, and IL-6, which collectively promote Treg expansion, M2 macrophage polarization, and MDSC recruitment [5,21]. EMT is also associated with downregulation of E-cadherin, which has been shown to impair the formation of immunological synapses between CTLs and tumor cells. Furthermore, mesenchymal tumor cells exhibit increased expression of PD-L1, driven in part by EMT-associated transcription factors including ZEB1 and SNAIL, creating a direct molecular coupling between the mesenchymal phenotype and checkpoint-mediated immune suppression [20,21].

### 3.3 Epigenetic Dysregulation

#### 3.3.1 DNA Methylation

Aberrant DNA methylation is a hallmark of LUSC that contributes to immune evasion through epigenetic silencing of genes critical for immune recognition [26]. Genome-wide methylation profiling has revealed hypermethylation of promoter CpG islands in multiple tumor suppressor genes and, importantly, in genes involved in antigen processing and presentation. Silencing of MHC class I and class II genes, as well as components of the antigen processing machinery (TAP1, TAP2, LMP2, LMP7), has been documented in LUSC and represents a reversible mechanism by which tumor cells evade CTL recognition [26]. Sasa et al. comprehensively reviewed the interplay between DNA methylation, lncRNA dysregulation, and immunotherapy response in LUSC, highlighting that DNA methyltransferase inhibitors (DNMTis) such as decitabine and azacitidine can restore expression of epigenetically silenced immune genes and synergize with ICIs in preclinical models [26]. The clinical development of epigenetic priming strategies—administering DNMTis or HDAC inhibitors prior to ICI therapy—represents a promising avenue for overcoming epigenetically mediated immune resistance in LUSC.

#### 3.3.2 Histone Modifications

Post-translational histone modifications, including acetylation and methylation, regulate chromatin accessibility and gene expression. In LUSC, overexpression of histone deacetylases (HDACs) and the polycomb repressive complex 2 (PRC2) catalytic subunit EZH2 has been linked to immune evasion. HDAC-mediated deacetylation silences interferon-stimulated genes (ISGs) and chemokine loci critical for T cell recruitment, while EZH2-mediated H3K27 trimethylation represses tumor suppressor genes and MHC expression [26]. Preclinical evidence supports the combination of HDAC inhibitors with ICIs to enhance tumor immunogenicity, and early-phase clinical trials are evaluating these combinations in NSCLC [5].

#### 3.3.3 Non-coding RNAs

The mammalian transcriptome encodes thousands of long non-coding RNAs (lncRNAs) and circular RNAs (circRNAs) that function as master regulators of gene expression through chromatin modification, transcriptional regulation, and post-transcriptional processing [26]. In LUSC, lncRNAs have been implicated in virtually every hallmark of cancer, including immune evasion. Sasa et al. summarized the functional roles of LUSC-associated lncRNAs, which modulate immune-related pathways through multiple mechanisms: acting as competitive endogenous RNAs (ceRNAs) that sponge microRNAs targeting immune checkpoint genes; scaffolding chromatin-modifying complexes to immune gene loci; and regulating mRNA stability of cytokines and chemokines [26].

A notable example is the circular RNA **circHMGB2**, which was shown to drive immunosuppression and anti-PD-1 resistance in both lung adenocarcinoma and squamous cell carcinoma [27]. circHMGB2 functions as a miRNA sponge, sequestering tumor-suppressive miRNAs and thereby upregulating immunosuppressive factors that inhibit T cell function. Knockdown of circHMGB2 in preclinical models synergized with anti-PD-1 therapy, resulting in enhanced CD8+ T cell infiltration and tumor regression [27]. These findings identify circHMGB2 as both a biomarker of anti-PD-1 resistance and a potential therapeutic target, and illustrate the broader principle that non-coding RNA networks represent an underexplored layer of immune regulation in LUSC [26,27].

### 3.4 Cell Death Pathways and Immune Resistance

The mode and immunogenicity of tumor cell death are critical determinants of anti-tumor immunity. Immunogenic cell death (ICD)—characterized by the release of damage-associated molecular patterns (DAMPs) including calreticulin, ATP, and HMGB1—promotes dendritic cell maturation and efficient cross-priming of tumor-specific CTLs. Conversely, defects in cell death pathways or shifts toward non-immunogenic death modalities can contribute to immune evasion and ICI resistance [28,29].

**Anoikis resistance**, the ability of tumor cells to survive detachment from the ECM, has recently been linked to immune modulation in LUSC. Anoikis-resistant tumor cells exhibit activation of pro-survival signaling pathways, including PI3K/AKT and SRC/FAK, that simultaneously suppress apoptosis and alter the secretome toward an immunosuppressive profile [28]. Lu et al. identified three anoikis-related genes—S100A7, S100A8, and SPP1—that were significantly associated with immune infiltration patterns in LUSC, particularly with the abundance of immunosuppressive Tregs, M2 macrophages, and dendritic cells. A prognostic nomogram integrating these markers with clinical variables demonstrated predictive utility for overall survival, suggesting that anoikis resistance and immune evasion may be linked through shared molecular determinants [28]. Similarly, a novel anoikis resistance-associated gene model characterized the immune microenvironment of LUSC and identified potential targets for reversing immune suppression [29].

**Ferroptosis**, an iron-dependent form of regulated necrosis characterized by lipid peroxidation, has been implicated in both tumor suppression and immunotherapy responses. Epigenetic activation of SLC7A11, a key negative regulator of ferroptosis, was shown to define a ferroptosis-immune axis associated with DNA methylation-based classification of LUSC, providing a link between epigenetic dysregulation, cell death resistance, and immune evasion [30]. Pyroptosis, a lytic and highly immunogenic form of programmed cell death mediated by gasdermin family members, has also been investigated in LUSC: pyroptosis-related gene signatures have been developed that can predict the composition of the immune microenvironment and the likelihood of immunotherapy response [31]. Collectively, these findings highlight the intimate connections between cell death pathway dysregulation and immune resistance in LUSC, and suggest that strategies to restore immunogenic cell death—through ferroptosis inducers, pyroptosis activators, or anoikis sensitizers—may enhance the efficacy of ICIs.

### 3.5 Genomic Instability and Neoantigen Dynamics

While LUSC generally exhibits a high TMB relative to other solid tumors—a feature attributed to chronic tobacco carcinogen exposure—the relationship between TMB and ICI responsiveness in LUSC is more complex than initially appreciated [7,26]. Although TMB-high LUSC tumors are more likely to harbor immunogenic neoantigens, several factors limit the predictive utility of TMB alone. First, clonal neoantigens (present in all tumor cells) are more effective at eliciting productive anti-tumor immunity than subclonal neoantigens, and the clonality of mutations in LUSC varies substantially between tumors [7]. Second, chromosomal instability and aneuploidy—both prevalent in LUSC—can paradoxically suppress anti-tumor immunity despite increasing overall mutation burden, possibly through the coordinated dysregulation of large numbers of immune-related genes or through the induction of a chronic ER stress response that impairs antigen presentation [7]. Third, under therapeutic pressure from ICIs, tumors can undergo immunoediting, with selective elimination of neoantigen-expressing clones and outgrowth of neoantigen-depleted or HLA-deficient subclones—a dynamic process that contributes to acquired resistance [7,14]. The major tumor-intrinsic resistance mechanisms discussed in this section are summarized in **Table 1**.

The tumor-intrinsic mechanisms discussed above do not operate in isolation; rather, they are deeply interconnected with the TME that surrounds them. Oncogenic signaling pathways shape the cytokine milieu; EMT programs recruit and activate stromal cells; and epigenetic alterations determine how tumor cells present themselves to the immune system. The next section will examine how the cellular and molecular components of the TME independently drive immunotherapy resistance in LUSC.

---

## 4. Tumor Microenvironment-Mediated Resistance

While tumor-intrinsic alterations establish the molecular foundation for immune evasion, the tumor microenvironment—comprising diverse immune cell populations, stromal elements, cytokines, metabolites, and microbial communities—constitutes the battlefield on which immunotherapy succeeds or fails. In LUSC, the TME is characterized by a convergence of immunosuppressive forces that collectively drive resistance to ICIs, even in tumors with abundant T cell infiltration.

### 4.1 T Cell Exhaustion and Dysfunction

T cell exhaustion—a state of progressive loss of effector function arising from chronic antigen stimulation—is a central mechanism of immune evasion in LUSC [16]. The exhausted T cell differentiation trajectory is governed by a hierarchical transcriptional program: progenitor exhausted T cells (Tpex), characterized by TCF-1 expression and maintained by the transcription factor TOX at intermediate levels, retain proliferative capacity and are the primary cellular targets of PD-1 blockade [16,18]. As exhaustion progresses, Tpex differentiate into terminally exhausted T cells (Tex-term) that express high levels of TOX, multiple inhibitory receptors, and exhibit severely impaired cytokine production and cytolytic function [18]. Critically, Tex-term cells are largely refractory to anti-PD-1 therapy, as their dysfunctional state is maintained by epigenetic imprinting rather than ongoing PD-1 signaling [16].

In the LUSC Exhausted Immune Class described by Yang et al., the T cell compartment is skewed toward a Tex-term-dominant state, with diminished TCF-1+ Tpex frequencies, elevated TOX and EOMES expression, and co-expression of numerous inhibitory receptors [18]. This exhaustion state is reinforced by multiple TME-derived factors: persistent antigen exposure from high neoantigen burden; immunosuppressive cytokines including IL-10, TGF-β, and CCL18; metabolic competition from tumor cells that depletes glucose and glutamine essential for T cell effector function; and chronic type I interferon signaling that, while initially immunostimulatory, can paradoxically drive T cell exhaustion when sustained [16,18].

### 4.2 Multi-Receptor Immune Checkpoint Co-Expression

A defining feature of the LUSC EIC is the co-upregulation of up to nine inhibitory immune checkpoints—CTLA-4, PD-1, LAG-3, BTLA, TIGIT, TIM-3, IDO1, SIGLEC7, and VISTA—creating a state of broad, multi-receptor immunosuppression [18]. This co-expression pattern carries critical therapeutic implications: blockade of the PD-1/PD-L1 axis alone leaves multiple alternative inhibitory pathways intact, enabling compensatory signaling through other checkpoints to maintain T cell suppression [7,18]. This concept is supported by the clinical experience in the Lung-MAP S1400F substudy, in which dual PD-L1/CTLA-4 blockade (durvalumab + tremelimumab) produced minimal clinical benefit in patients with acquired resistance to prior anti-PD-(L)1 therapy, suggesting that resistance in these patients is maintained through checkpoint-independent or additional checkpoint-mediated mechanisms [15].

The specific repertoire of co-expressed checkpoints has implications for rational combination design. LAG-3 and TIGIT, both frequently co-expressed with PD-1 in LUSC, engage distinct ligands (MHC class II and CD155/PVR, respectively) and signal through independent intracellular pathways, making them attractive targets for combination with PD-1 blockade [7,18]. The bispecific antibody rilvegostomig, which simultaneously targets PD-1 and TIGIT, is currently being evaluated in phase III trials in NSCLC; although the TROPION-Lung10 trial enrolled a nonsquamous population, the strong biological rationale for TIGIT co-blockade—given the high frequency of TIGIT co-expression within the EIC—applies across NSCLC histologies including LUSC [32]. Similarly, TIM-3, which marks highly dysfunctional CD8+ T cells and is co-expressed with PD-1 on tumor-infiltrating lymphocytes in LUSC, represents a clinically relevant target with anti-TIM-3 antibodies in development [18].

### 4.3 Immunosuppressive Cell Populations

#### 4.3.1 Tumor-Associated Macrophages (TAMs)

Tumor-associated macrophages represent the most abundant immune cell population in the LUSC TME and are a dominant driver of immunosuppression [17]. TAMs exhibit remarkable functional plasticity, with their polarization state heavily influenced by local environmental cues. In LUSC, TAMs are predominantly polarized toward an M2-like phenotype, characterized by expression of CD163, CD206, and APOE, driven by TME-derived signals including CSF-1, IL-4, IL-10, lactic acid, and tumor-secreted exosomes [17].

Ji et al. demonstrated that aldolase A (ALDOA), a key glycolytic enzyme, is significantly overexpressed in LUSC and strongly correlates with macrophage infiltration. Spatial transcriptomics and immunofluorescence confirmed co-localization of ALDOA-expressing tumor cells with CD68+ macrophages in LUSC tissues [17]. Functional analyses revealed that ALDOA-driven glycolytic flux generates a lactate-rich microenvironment that promotes M2 macrophage polarization, establishing a self-reinforcing metabolic-immune circuit: elevated glycolysis → lactic acid secretion → M2 TAM polarization → immunosuppressive cytokine production → T cell dysfunction [17]. High ALDOA expression was independently associated with poor overall survival, disease-specific survival, and progression-free interval in LUSC.

Recent studies have identified a CAF-TAM signaling axis in squamous carcinomas, in which CAF-derived factors reinforce M2 macrophage polarization while TAMs reciprocally secrete growth factors that sustain CAF activation [16]. This CAF-TAM co-dependency creates a spatially organized immunosuppressive niche at the tumor-stromal interface that contributes to CD8+ T cell exclusion and functional suppression [16].

#### 4.3.2 Cancer-Associated Fibroblasts (CAFs)

CAFs are activated fibroblasts that constitute a major component of the LUSC stroma and contribute to immune resistance through multiple mechanisms [5,16]. In LUSC, the CAF compartment is heterogeneous, with functionally distinct subpopulations: inflammatory CAFs (iCAFs) that secrete cytokines and chemokines; myofibroblastic CAFs (myCAFs) that deposit ECM components; and antigen-presenting CAFs (apCAFs) that may modulate T cell responses [5].

The most well-characterized immune-evasion mechanism mediated by CAFs in LUSC is the physical exclusion of T cells. POSTN+ and FAP+ CAFs deposit dense ECM—particularly collagen type I, fibronectin, and laminin—creating a physical barrier that prevents CTL penetration into tumor nests [5,16]. ECM alignment perpendicular to the tumor boundary, mediated by CAF contractile forces, creates tracks that guide T cell migration along the tumor periphery rather than into the tumor interior. Beyond physical exclusion, CAFs secrete chemokines—including CXCL12 and CCL2—that actively repel T cells while recruiting immunosuppressive populations including Tregs and MDSCs. Furthermore, CAF-secreted TGF-β drives EMT in tumor cells and directly inhibits CTL function, creating multiple reinforcing immunosuppressive loops [5].

#### 4.3.3 Myeloid-Derived Suppressor Cells (MDSCs) and Regulatory T Cells (Tregs)

MDSCs are a heterogeneous population of pathologically activated immature myeloid cells that expand in the LUSC TME and exert potent immunosuppressive functions through diverse mechanisms: depletion of arginine and cysteine, essential amino acids for T cell activation, via arginase-1 and xCT transporter expression; production of ROS and peroxynitrite that nitrosylate T cell receptor (TCR) components, rendering T cells unresponsive to antigen stimulation; and secretion of IL-10 and TGF-β that promote Treg expansion and inhibit DC maturation [5,16]. In LUSC, MDSC frequencies in peripheral blood and tumor tissue correlate with disease stage and inversely correlate with response to ICIs, suggesting that MDSC burden may serve as a predictive biomarker.

CD4+FOXP3+ Tregs are enriched in the LUSC TME, particularly in the EIC subtype, where their abundance is a defining feature [18]. Tregs suppress anti-tumor immunity through contact-dependent mechanisms—including CTLA-4-mediated transendocytosis of CD80/CD86 from DCs and granzyme B-mediated killing of effector T cells—and through secretion of immunosuppressive cytokines (IL-10, TGF-β, IL-35). The chemokine milieu of the LUSC TME, characterized by CCL22 and CCL17 production by TAMs and tumor cells, actively recruits CCR4+ Tregs, establishing a positive-feedback loop of immunosuppression [18].

### 4.4 Cytokine Networks

The LUSC cytokine milieu is dominated by a network of immunosuppressive mediators that collectively paralyze anti-tumor immunity. **TGF-β** is the central orchestrator, produced by tumor cells, CAFs, TAMs, and Tregs. TGF-β signaling in CD8+ T cells directly represses the expression of cytolytic effector molecules—perforin, granzyme B, and IFN-γ—while simultaneously promoting Treg differentiation and EMT in tumor cells [5,16]. The EIC is characterized by elevated TGF-β and CCL18 expression: CCL18, primarily secreted by M2 TAMs, recruits additional Tregs and immature DCs while promoting further TAM M2 polarization [18].

**Interleukin-6** (IL-6) activates STAT3 signaling in tumor cells and immune cells, driving a feed-forward loop of chronic inflammation that promotes tumor progression and immune evasion. **IL-10**, produced by Tregs, TAMs, and exhausted T cells, broadly suppresses antigen presentation, co-stimulatory molecule expression, and pro-inflammatory cytokine production by DCs and macrophages [18].

### 4.5 Metabolic Immune Modulation

#### 4.5.1 Glycolysis and Lactic Acidosis

The LUSC TME is metabolically characterized by the Warburg effect—aerobic glycolysis resulting in high rates of glucose consumption and lactic acid production by tumor cells [17]. This metabolic program has profound consequences for anti-tumor immunity. Lactic acid accumulation acidifies the TME to pH 6.0–6.5, which directly inhibits T cell proliferation, cytokine production, and cytolytic activity while promoting Treg stability and M2 macrophage polarization [17]. The glucose-depleted TME metabolically starves CTLs, which are highly dependent on glycolysis for effector function, while Tregs—which can utilize fatty acid oxidation—maintain a metabolic advantage in low-glucose conditions [17,33].

ALDOA overexpression in LUSC, as discussed above, exemplifies how tumor cell-intrinsic metabolic reprogramming drives immune suppression [17]. Beyond ALDOA, multi-omics analyses have revealed complex interactions between the intratumoral microbiome composition, lactic acid metabolism, and immune status in LUSC, suggesting that microbial metabolites may directly modulate the metabolic-immune axis within the TME [33].

#### 4.5.2 Hypoxia-Driven Immune Evasion

Hypoxia is a pervasive feature of the LUSC TME resulting from aberrant tumor vasculature and high metabolic demand [34]. Hypoxia-inducible factor-1α (HIF-1α) is stabilized under low oxygen tension and transcriptionally activates a program that simultaneously promotes tumor survival and immune evasion: PD-L1 upregulation; VEGF secretion that promotes abnormal angiogenesis and further hypoxia; and recruitment of MDSCs and TAMs [34].

A recently elucidated mechanism linking hypoxia to immune resistance involves the STING (stimulator of interferon genes) pathway, a critical node in innate immune sensing of cytosolic DNA [34]. Hypoxia suppresses STING signaling through HIF-1α-mediated mechanisms, resulting in decreased production of type I interferons, impaired dendritic cell maturation, and diminished cross-priming of tumor-specific CD8+ T cells. Restoration of STING signaling—either through hypoxia relief or direct STING agonism—has been shown to enhance ICI efficacy in preclinical LUSC models, identifying the hypoxia-STING axis as a therapeutically tractable immune evasion mechanism [34].

Clinically, radiologic features such as intrapulmonic cavity or necrosis on baseline CT have been associated with improved efficacy of anti-PD-(L)1 inhibitors in advanced LUSC, potentially reflecting hypoxia-driven immune priming [41]. A hypoxia-related lncRNA signature has also been developed in LUSC that stratifies patients by immune characteristics and prognosis [35]. High hypoxia scores were found to be associated with reduced immune infiltration and an immunosuppressive microenvironment, particularly in EGFR-wild-type, low-PD-L1 tumors—a population for whom ICI monotherapy is often of limited benefit [35].

#### 4.5.3 Amino Acid and Tryptophan Metabolism

Indoleamine 2,3-dioxygenase 1 (IDO1), one of the nine co-upregulated checkpoints in the LUSC EIC [18], catalyzes the rate-limiting step of tryptophan degradation along the kynurenine pathway. Tryptophan depletion and kynurenine accumulation act synergistically to suppress T cell proliferation—through GCN2 kinase activation and mTOR inhibition—while promoting Treg differentiation through aryl hydrocarbon receptor (AhR) activation [18]. Arginine metabolism by arginase-1-expressing MDSCs and TAMs similarly depletes the TME of arginine, which is essential for TCR ζ-chain expression and T cell activation [16].

### 4.6 Tumor Microbiome-Immune Crosstalk

An emerging dimension of LUSC TME biology is the role of the intratumoral microbiome in modulating immune responses and immunotherapy outcomes [33]. Multi-omics integration has revealed that the composition of the intratumoral microbiota in LUSC is significantly correlated with lactic acid metabolism, immune cell infiltration patterns, and immune checkpoint expression [33]. Specific bacterial taxa have been associated with distinct immune phenotypes: enrichment of *Lactobacillus* species correlates with an immunosuppressive TME characterized by M2 macrophage predominance and attenuated CD8+ T cell responses, potentially through modulation of tryptophan and lactate metabolism [33].

Conversely, certain microbial signatures are associated with immune-inflamed tumors and may predict favorable ICI responses, paralleling observations in LUAD and other cancers where gut and intratumoral microbiome composition influences immunotherapy outcomes [33]. While the mechanistic links between the LUSC microbiome and immune resistance are still being defined, these findings raise the possibility that microbiome-directed interventions—including antibiotics, probiotics, or metabolite supplementation—could be leveraged to modulate immunotherapy responses in LUSC. The key TME-mediated resistance mechanisms and corresponding therapeutic interventions discussed in this section are summarized in **Table 2**.

---

The TME-mediated resistance mechanisms described above do not arise *de novo* at the time of treatment; rather, they evolve dynamically under the selective pressure of ICI therapy. The following section will examine how therapeutic pressure drives acquired resistance through clonal evolution, histological transformation, and phenotypic plasticity.

---

## 5. Acquired Resistance Mechanisms

While primary resistance reflects the pre-existing inability of the tumor-immune system to mount an effective anti-tumor response, acquired resistance emerges under the selective pressure of initially effective immunotherapy, manifesting as disease progression after a period of clinical benefit [14]. Acquired resistance in LUSC arises through diverse mechanisms—genomic, epigenomic, and phenotypic—that collectively enable tumor cells to evade ongoing immune attack.

### 5.1 Clonal Evolution Under Immunotherapy Pressure

The administration of ICIs imposes potent immunologic selective pressure on genetically heterogeneous tumor cell populations, driving a Darwinian process of clonal evolution [7,14]. Tumor subclones harboring mutations that confer immune evasion advantages—through reduced immunogenicity, enhanced immunosuppressive factor secretion, or activation of anti-apoptotic pathways—are positively selected during ICI therapy, eventually emerging as dominant populations responsible for disease progression [14].

Several genomic mechanisms of acquired resistance have been documented in NSCLC, with relevance to LUSC. Loss-of-function mutations in *JAK1* and *JAK2*, which abrogate interferon-γ receptor signaling and thereby render tumor cells insensitive to T cell-derived IFN-γ, have been identified in acquired resistance biopsies [14]. Similarly, acquired *B2M* (β2-microglobulin) mutations or loss of heterozygosity eliminate cell-surface MHC class I expression, enabling tumor cells to evade CD8+ T cell recognition entirely [7,14]. While the frequency of these specific alterations in LUSC remains to be defined through systematic genomic profiling of paired pre-treatment and progression biopsies, the underlying principle—that immunoediting under ICI pressure selects for clones with reduced antigen presentation capacity—is likely to be broadly operative [7].

### 5.2 Histological Transformation: Adenosquamous Transition

A particularly instructive form of acquired resistance relevant to LUSC biology is **adenocarcinoma-to-squamous cell carcinoma transformation (AST)** [36]. Initially documented in the context of EGFR-TKI resistance in LUAD, AST has increasingly been recognized as a mechanism of acquired resistance to ICIs as well. Xu et al. comprehensively reviewed the immune mechanisms underlying adenosquamous transformation, demonstrating that this histological switch is accompanied by profound remodeling of the TIME [36].

During AST, LUAD cells undergo a lineage plasticity program driven by activation of squamous transcription factors and concomitant suppression of the LUAD lineage determinant NKX2-1 (TTF-1) [36]. This transcriptional reprogramming is coupled with extensive changes in the immune microenvironment: the transformed squamous-like tumor cells secrete a distinct repertoire of cytokines and chemokines that alter immune cell recruitment patterns; the ECM is remodeled in a CAF-dependent manner that promotes immune exclusion; and the expression profile of immune checkpoint molecules shifts, potentially affecting responsiveness to different ICI combinations [36].

The clinical significance of AST for LUSC is twofold. First, AST demonstrates that squamous differentiation can emerge as an adaptive resistance mechanism, raising the possibility that some *de novo* LUSC tumors may harbor a constitutively active squamous lineage program that intrinsically limits ICI efficacy. Second, understanding the signaling dependencies of squamous-transformed tumors may identify therapeutic strategies to prevent or reverse this resistance mechanism [36].

### 5.3 Phenotypic Plasticity

Beyond full histological transformation, tumor cells can undergo more subtle phenotypic shifts that confer resistance to ICIs. Phenotypic plasticity—the ability of tumor cells to dynamically transition between alternative differentiation states in response to microenvironmental cues—has been implicated in LUSC metastasis and drug resistance [37].

Wang et al. characterized phenotypic plasticity-related gene expression patterns in LUSC and demonstrated that patients with and without lymph node metastasis exhibit significantly different genomic features of plasticity [37]. A phenotypic plasticity-related prognostic signature successfully stratified LUSC patients into high- and low-plasticity groups with divergent survival outcomes. Importantly, patients with low plasticity scores were predicted to be more sensitive to PD-L1 inhibitors, cisplatin, paclitaxel, and several targeted agents, while high-plasticity tumors were associated with broad therapeutic resistance [37]. Enrichment analysis revealed that phenotypic plasticity is strongly associated with cellular contraction and cytoskeletal remodeling pathways—biological processes that facilitate both metastasis and immune evasion by altering tumor cell mechanics and their interaction with immune effector cells.

Plasticity-driven resistance is particularly challenging because it is dynamic and reversible, meaning that resistance-conferring phenotypic states may not be captured by single time-point biopsies [14,37]. This underscores the potential value of liquid biopsies—including circulating tumor DNA (ctDNA) and circulating tumor cells (CTCs)—for longitudinal monitoring of resistance mechanisms under therapeutic pressure [7].

### 5.4 SCLC Transformation and Other Lineage Switches

An extreme manifestation of phenotypic plasticity is the transformation of NSCLC—including LUSC—into small cell lung cancer (SCLC) under ICI therapy. While originally described in EGFR-mutant adenocarcinomas, SCLC transformation has also been documented in LUSC [38]. This phenomenon, while rare (estimated frequency <5% in ICI-treated NSCLC), is clinically devastating, as transformed SCLC is aggressive and responds poorly to currently available therapies. SCLC transformation is characterized by loss of RB1 and TP53 function, activation of ASCL1 or NEUROD1 neuroendocrine transcriptional programs, and acquisition of characteristic SCLC morphology [38]. Whether specific features of LUSC biology—such as the high prevalence of baseline TP53 mutations—confer an elevated risk of SCLC transformation compared to LUAD remains an open question.

---

Acquired resistance thus represents the culmination of tumor evolution under immunologic pressure, operating through genomic selection, transcriptional reprogramming, and phenotypic adaptation. The multifactorial nature of acquired resistance—in which multiple resistance mechanisms frequently coexist within a single patient—presents a formidable therapeutic challenge and motivates the development of combination strategies designed to preempt or circumvent these escape pathways.

---

## 6. Strategies to Overcome Resistance

The multidimensional nature of immunotherapy resistance in LUSC—spanning tumor-intrinsic alterations, TME-mediated suppression, and treatment-induced adaptation—demands therapeutic strategies that are equally multifaceted. Emerging approaches to overcome resistance can be broadly categorized into rational immunotherapy combinations, targeting of tumor-intrinsic pathways, TME remodeling, and biomarker-guided precision strategies. The key resistance mechanisms and corresponding therapeutic approaches are catalogued in **Table 1** and **Table 2**.

### 6.1 Rational Immunotherapy Combinations

The co-expression of multiple inhibitory immune checkpoints in LUSC—particularly within the EIC—provides a clear biological rationale for dual or triple checkpoint blockade [7,18]. While the Lung-MAP S1400F substudy demonstrated that adding CTLA-4 blockade (tremelimumab) to PD-L1 inhibition (durvalumab) yields only minimal benefit in unselected anti-PD-(L)1-resistant patients, this does not negate the potential of more precisely targeted combinations [15]. Novel bispecific antibodies—including QL1706 (PD-1/CTLA-4) and rilvegostomig (PD-1/TIGIT)—offer the advantage of simultaneous dual-target engagement with potentially improved therapeutic indices by preferentially targeting T cells co-expressing both receptors [39]. The combination of PD-1 blockade with TIGIT inhibition is of particular interest in LUSC, given the high frequency of TIGIT co-expression within the EIC [18].

ICI combined with platinum-based chemotherapy remains the standard first-line approach for LUSC (KEYNOTE-407), and chemotherapy likely contributes to overcoming resistance through multiple mechanisms: induction of immunogenic cell death, depletion of MDSCs, and reduction of Treg frequencies [5]. ICI combined with anti-angiogenic agents—while requiring careful consideration of bleeding risk in centrally located squamous tumors—has shown promise in LUAD and is being explored in LUSC with the VEGF receptor inhibitor ramucirumab and other agents [5,16].

### 6.2 Targeting Tumor-Intrinsic Pathways

The convergence of oncogenic signaling and immune evasion creates opportunities for pathway-targeted immunotherapy combinations [5,26]. In *PIK3CA*-altered LUSC, PI3K/mTOR inhibitors may simultaneously suppress tumor growth and relieve mTOR-driven PD-L1 expression, potentially sensitizing tumors to ICIs. In *KEAP1*-mutant LUSC, strategies to target the NRF2 pathway—including glutaminase inhibitors that exploit the metabolic dependencies created by NRF2 activation, or STING agonists that bypass suppressed innate immune sensing—are being explored [5]. Epigenetic priming with DNMT inhibitors (decitabine, azacitidine) or HDAC inhibitors to restore expression of silenced antigen presentation and interferon-response genes, followed by ICI administration, represents a mechanistically appealing strategy supported by preclinical evidence in LUSC models [26].

### 6.3 TME Remodeling

Overcoming TME-mediated resistance requires strategies that convert an immunosuppressive milieu into one permissive for anti-tumor immunity [16]. CAF-targeted approaches—including FAP inhibitors, hedgehog pathway antagonists, and TGF-β trap agents—aim to reduce ECM deposition, normalize tumor vasculature, and facilitate T cell penetration into tumor nests [16]. TAM reprogramming strategies, such as CSF1R inhibition, CD47 blockade, or CD40 agonism, seek to shift the macrophage polarization balance from M2 to M1, restoring T cell-supportive functions [16,17]. Cytokine-directed therapies, including TGF-β neutralizing antibodies (fresolimumab) and CCR4 inhibitors (mogamulizumab) that deplete Tregs, aim to interrupt immunosuppressive signaling circuits [16]. The STING/cGAS pathway—suppressed under hypoxia in LUSC—represents an attractive target for innate immune activation, with STING agonists capable of triggering type I interferon responses that recruit and activate DCs even in immune-desert tumors [34].

### 6.4 Emerging Strategies and Biomarker-Guided Precision Immunotherapy

Looking forward, several emerging directions hold particular promise for LUSC [5,16]. The development of a TIME-based classification framework—integrating molecular subtype, immune infiltration pattern, and spatial architecture—could guide the selection of mechanism-appropriate combination strategies: ICI + TIGIT blockade for EIC tumors with TIGIT co-expression; CAF-targeted therapies for immune-excluded tumors with high stromal content; and STING agonists or oncolytic viruses for immune-desert tumors devoid of T cell infiltration [16]. Liquid biopsy-based dynamic monitoring of resistance mechanisms—through ctDNA profiling of emerging *JAK1*, *JAK2*, or *B2M* mutations, or tracking of TMB and neoantigen clonality over time—could enable adaptive treatment strategies that preempt clonal escape [7]. Finally, the emerging role of the intratumoral microbiome in modulating ICI responses raises the possibility that microbiome-directed interventions—including selective antibiotics, defined probiotic consortia, or fecal microbiota transplantation—could be leveraged to enhance immunotherapy efficacy in LUSC [33].

---

## 7. Conclusions and Future Perspectives

Immunotherapy has transformed the treatment landscape for patients with lung squamous cell carcinoma, yet the majority of patients either fail to respond initially or eventually develop resistance. This review has synthesized current understanding of the mechanisms underlying immunotherapy resistance in LUSC across three interconnected dimensions—tumor-intrinsic alterations, TME-mediated suppression, and acquired resistance—yielding several overarching principles.

First, resistance in LUSC is rarely attributable to a single mechanism; rather, it arises from the convergence of multiple, mutually reinforcing pathways. The KEAP1/NRF2-mutant tumor cell simultaneously resists oxidative killing, suppresses innate immune sensing, and secretes factors that promote an immunosuppressive TME. The CAF-TAM axis simultaneously excludes T cells physically while suppressing those that manage to infiltrate. The EIC co-expresses nine inhibitory checkpoints, any one of which can sustain immune suppression when another is blocked. This principle of mechanistic redundancy underscores why single-agent PD-1/PD-L1 blockade is insufficient for a substantial proportion of LUSC patients and motivates the development of rationally designed, mechanism-informed combination strategies.

Second, the functional state of the immune infiltrate matters more than its quantity. The EIC—with its abundant TILs, high PD-L1 expression, and paradoxically poor prognosis—illustrates the critical distinction between immune infiltration and immune competence. Biomarker strategies that rely solely on TIL density or PD-L1 immunohistochemistry are inherently limited; future predictive models must incorporate multidimensional assessments of T cell functionality, checkpoint co-expression patterns, and spatial organization.

Third, LUSC is immunobiologically distinct from LUAD and requires histology-specific therapeutic strategies. The higher prevalence of immune-excluded phenotypes, the distinct genomic landscape dominated by tumor suppressor loss rather than oncogenic driver mutations, and the specific CAF and metabolic features of the LUSC TME all argue against the extrapolation of LUAD-derived therapeutic paradigms without LUSC-specific validation.

Looking forward, several priorities emerge. **Prospective biomarker-driven clinical trials** that stratify patients by TIME subtype, *KEAP1* mutation status, or EIC molecular signature will be essential to evaluate mechanism-matched combination therapies. **Multi-omics integration**—combining genomic, transcriptomic, spatial proteomic, and microbiomic data—will provide the resolution necessary to dissect the full complexity of resistance mechanisms operating within an individual patient. **Dynamic monitoring** of resistance through liquid biopsy-based ctDNA profiling and circulating immune cell analysis will enable adaptive therapeutic strategies that respond to emerging resistance in real time. Finally, **novel therapeutic modalities**—including bispecific antibodies, epigenetic priming, STING agonists, and CAF-targeted therapies—are poised to expand the arsenal of strategies available to overcome immunotherapy resistance in LUSC.

Ultimately, overcoming immunotherapy resistance in LUSC will require a shift from a one-size-fits-all approach to a precision medicine paradigm in which the specific resistance mechanisms operating in each patient's tumor are identified and therapeutically addressed. The mechanistic framework presented in this review aims to provide a foundation for that transition.

---

## Search Strategy and Selection Criteria

This narrative review was conducted through a structured literature search of PubMed/MEDLINE (via the Europe PMC API) and Semantic Scholar. Search terms combined Medical Subject Headings (MeSH) and free-text keywords across four dimensions: (1) disease: "non-small cell lung cancer," "NSCLC," "lung squamous cell carcinoma," "LUSC"; (2) intervention: "immunotherapy," "immune checkpoint inhibitor," "anti-PD-1," "anti-PD-L1," "anti-CTLA-4," with specific drug names (pembrolizumab, nivolumab, atezolizumab, durvalumab, ipilimumab, cemiplimab); (3) outcome: "resistance," "refractory," "immune evasion," "non-response"; and (4) mechanism: "tumor microenvironment," "T cell exhaustion," "neoantigen," "antigen presentation," and related signaling pathways. The search was conducted on June 4, 2026, covering literature published between January 2020 and June 2026, restricted to English-language articles and reviews.

After deduplication (n = 4,106 records), a two-stage screening process was applied: (1) title and abstract screening of 432 records with keyword filtering for squamous histology and resistance mechanisms, applying a strategy of "when uncertain, include"; (2) full-text assessment of 62 articles (60 open access via PubMed Central, 96.8%) against predefined inclusion criteria. Studies were excluded if they focused on non-lung squamous cell carcinomas (e.g., laryngeal, head and neck, oral, esophageal, cutaneous), non-squamous NSCLC without squamous subgroup analysis, or lacked substantive mechanistic content. Following full-text review, 37 studies were included in the qualitative synthesis (8 reviews, 26 original research articles, 3 systematic reviews/meta-analyses).

**Limitations**: Searches were limited to PubMed/MEDLINE (via Europe PMC) and Semantic Scholar. Embase and Cochrane CENTRAL were not searched due to institutional access constraints at the time of manuscript preparation. As this review involves pharmacological agents (immune checkpoint inhibitors) and clinical trials, the absence of Embase—the gold-standard database for pharmacology literature—and Cochrane CENTRAL—the primary registry of clinical trials—represents a methodological limitation that may result in incomplete coverage of pharmacology-related and trial-based literature. Additionally, no formal risk-of-bias assessment was performed for individual included studies, and the synthesis is qualitative rather than quantitative. Pre-compiled search strategies for Embase (Ovid) and Cochrane Library are available as supplementary material for future updates. The review was not registered with PROSPERO as it is a narrative rather than systematic review.

---

## Declarations

**Funding**: [To be completed — specify grant numbers and funding bodies if applicable]

**Competing interests**: The authors declare no competing interests.

**Author contributions**: [To be completed — specify each author's contribution]

**Ethics approval**: Not applicable (review article).

**Data availability statement**: No primary data were generated for this review. All analyzed literature is publicly available via PubMed/PubMed Central.

**Supplementary material**: Pre-compiled search strategies for Embase (Ovid) and Cochrane Library (CENTRAL + CDSR) are documented in `docs/search-results/manual-search-checklist.md`.

---

## References

1. Sung H, Ferlay J, Siegel RL, et al. Global Cancer Statistics 2020: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. *CA Cancer J Clin*. 2021;71(3):209–249. doi:10.3322/caac.21660 | PMID: 33538338

2. Travis WD, Brambilla E, Nicholson AG, et al. The 2015 World Health Organization classification of lung tumors: impact of genetic, clinical and radiologic advances since the 2004 classification. *J Thorac Oncol*. 2015;10(9):1243–1260. doi:10.1097/JTO.0000000000000630 | PMID: 26291008

3. Siegel RL, Miller KD, Fuchs HE, Jemal A. Cancer statistics, 2022. *CA Cancer J Clin*. 2022;72(1):7–33. doi:10.3322/caac.21708 | PMID: 35020204

4. Schiller JH, Harrington D, Belani CP, et al. Comparison of four chemotherapy regimens for advanced non-small-cell lung cancer. *N Engl J Med*. 2002;346(2):92–98. doi:10.1056/NEJMoa011954 | PMID: 11784886

5. Niu Z, Jin R, Zhang Y, Li H. Signaling pathways and targeted therapies in lung squamous cell carcinoma: mechanisms and clinical trials. *Signal Transduct Target Ther*. 2022;7:353. doi:10.1038/s41392-022-01200-x | PMID: 36198685

6. Cancer Genome Atlas Research Network. Comprehensive genomic characterization of squamous cell lung cancers. *Nature*. 2012;489(7417):519–525. doi:10.1038/nature11404 | PMID: 22960745

7. Yuan H, Liu J, Zhang J. The current landscape of immune checkpoint blockade in metastatic lung squamous cell carcinoma. *Molecules*. 2021;26(5):1392. doi:10.3390/molecules26051392 | PMID: 33807509

8. Paz-Ares L, Luft A, Vicente D, et al. Pembrolizumab plus chemotherapy for squamous non-small-cell lung cancer. *N Engl J Med*. 2018;379(21):2040–2051. doi:10.1056/NEJMoa1810865 | PMID: 30280635

9. Brahmer J, Reckamp KL, Baas P, et al. Nivolumab versus docetaxel in advanced squamous-cell non-small-cell lung cancer. *N Engl J Med*. 2015;373(2):123–135. doi:10.1056/NEJMoa1504627 | PMID: 26028407

10. Chen W, Liu H, Li Y, et al. First-line immunotherapy efficacy in advanced squamous non-small cell lung cancer with PD-L1 expression ≥50%: a network meta-analysis. *Front Oncol*. 2024;14:1360583. doi:10.3389/fonc.2024.1360583 | PMID: 38725635

11. Jotte R, Cappuzzo F, Vynnychenko I, et al. Atezolizumab in combination with carboplatin and nab-paclitaxel in advanced squamous NSCLC (IMpower131): results from a randomized phase III trial. *J Thorac Oncol*. 2020;15(8):1351–1360. doi:10.1016/j.jtho.2020.03.028 | PMID: 32302702

12. Ikeda S, Araki K, Kitagawa M, et al. Why cemiplimab? Defining a unique therapeutic niche in first-line non-small-cell lung cancer with ultra-high PD-L1 expression and squamous histology. *Cancers*. 2026;18(2):272. doi:10.3390/cancers18020272 | PMID: 41595192

13. Reck M, Rodríguez-Abreu D, Robinson AG, et al. Pembrolizumab versus chemotherapy for PD-L1-positive non-small-cell lung cancer. *N Engl J Med*. 2016;375(19):1823–1833. doi:10.1056/NEJMoa1606774 | PMID: 27718847

14. Sharma P, Hu-Lieskovan S, Wargo JA, Ribas A. Primary, adaptive, and acquired resistance to cancer immunotherapy. *Cell*. 2017;168(4):707–723. doi:10.1016/j.cell.2017.01.017 | PMID: 28187290

15. Leighl NB, Redman MW, Rizvi N, et al. Phase II study of durvalumab plus tremelimumab as therapy for patients with previously treated anti-PD-(L)1 resistant stage IV squamous cell lung cancer (Lung-MAP sub-study S1400F). *J Immunother Cancer*. 2021;9(8):e002973. doi:10.1136/jitc-2021-002973 | PMID: 34429332

16. Tong Y, Wang Y, Chen Y, Fan Y, Li H. Decoding the tumor immune microenvironment in lung squamous cell carcinoma: characteristics, regulatory mechanisms, and future directions in immunotherapy. *Transl Lung Cancer Res*. 2025;14(4):1170–1190. doi:10.21037/tlcr-2025-350 | PMID: 41133013

17. Ji Y, Li X, Shen X, et al. Aldolase A in pan-cancer and lung squamous cell carcinoma: prognostic value and macrophage-driven immune suppression unveiled by multi-omics analysis. *Cancer Cell Int*. 2025;25:184. doi:10.1186/s12935-025-03721-3 | PMID: 41239433

18. Yang M, Lin C, Wang Y, et al. Identification of a cytokine-dominated immunosuppressive class in squamous cell lung carcinoma with implications for immunotherapy resistance. *Genome Med*. 2022;14(1):72. doi:10.1186/s13073-022-01079-x | PMID: 35799269

19. Yin L, et al. Identification of immune subtypes of lung squamous cell carcinoma by integrative genome-scale analysis. *Front Oncol*. 2021;11:778324. doi:10.3389/fonc.2021.778324 | PMID: 35186710

20. Song T, Yang Y, Wang Y, et al. Bulk and single-cell RNA sequencing reveal the contribution of laminin γ2-CD44 to the immune resistance in lymphocyte-infiltrated squamous lung cancer subtype. *Heliyon*. 2024;10(11):e31299. doi:10.1016/j.heliyon.2024.e31299 | PMID: 38803944

21. Zhang A, He J, Lin Q. A risk scoring model for lung squamous cell carcinoma based on epithelial-mesenchymal transition-related genes: an integrative analysis of prognosis and immune infiltration characteristics. *PeerJ*. 2026;14:e21117. doi:10.7717/peerj.21117 | PMID: 42089102

22. Shen Y, Chen JQ, Li XP. Differences between lung adenocarcinoma and lung squamous cell carcinoma: driver genes, therapeutic targets, and clinical efficacy. *Genes Dis*. 2025. doi:10.1016/j.gendis.2024.101374 | PMID: 40083325

23. Yan T, et al. The immune heterogeneity between pulmonary adenocarcinoma and squamous cell carcinoma: a comprehensive analysis based on lncRNA models. *Front Immunol*. 2021;12:703797. doi:10.3389/fimmu.2021.703797 | PMID: 34394068

24. Lin C, Li S, Yi L, et al. TGM2 regulated by transcription factor NR3C1 drives p38 MAPK-mediated tumor progression and immune evasion in lung squamous cell carcinoma. *Front Immunol*. 2025;16:1547241. doi:10.3389/fimmu.2025.1547241 | PMID: 41050683

25. Ju L, et al. Mechanism of intrinsic resistance of lung squamous cell carcinoma to epithelial growth factor receptor-tyrosine kinase inhibitors. *Front Oncol*. 2020;10:568878. doi:10.3389/fonc.2020.568878 | PMID: 33133263

26. Sasa GBK, Xuan C, Chen M, Jiang Z, Ding X. Clinicopathological implications of lncRNAs, immunotherapy and DNA methylation in lung squamous cell carcinoma: a narrative review. *Transl Cancer Res*. 2021;10(12):5324–5341. doi:10.21037/tcr-21-1607 | PMID: 35116387

27. Zhang LX, Gao J, Long X, et al. The circular RNA circHMGB2 drives immunosuppression and anti-PD-1 resistance in lung adenocarcinomas and squamous cell carcinomas via the miR-181a-5p/CARM1 axis. *Mol Cancer*. 2022;21(1):110. doi:10.1186/s12943-022-01586-w | PMID: 35525959

28. Lu H, Huang W, Shen Q, Liu R. Anoikis-related genes signature contributes to predicting prognosis and response to immunotherapy in lung squamous cell carcinoma. *Med Sci Monit*. 2026;31:e951722. doi:10.12659/MSM.951722 | PMID: 41902322

29. Ou D, Wang H, Liu Y, Nie J, Liu D. A novel anoikis resistance-associated gene model for prognostic prediction and immune microenvironment characterization in lung squamous cell carcinoma. *Discover Oncol*. 2026. doi:10.1007/s12672-026-04395-5 | PMID: 41530460

30. Lu HP, Nong K, Pang L, et al. Epigenetic activation of SLC7A11 defines a ferroptosis-immune axis and enables robust DNA methylation-based diagnosis of lung squamous cell carcinoma. *PeerJ*. 2026;14:e20686. doi:10.7717/peerj.20686 | PMID: 41700135

31. Deng X, et al. Prediction of lung squamous cell carcinoma immune microenvironment and immunotherapy efficiency with pyroptosis-derived genes. *J Cancer Res Clin Oncol*. 2022. doi:10.1007/s00432-022-04381-8 | PMID: 36123889

32. Newsom-Davis T, Melosky B, Heist RS, et al. TROPION-Lung10: a phase 3 study of datopotamab deruxtecan and rilvegostomig in patients with treatment-naïve locally advanced or metastatic nonsquamous non-small cell lung cancer with high PD-L1 expression. *Front Oncol*. 2025;15:1721624. doi:10.3389/fonc.2025.1721624 | PMID: 41669261

33. Qiu X, Li D. Multi-omics analysis untangles the crosstalk between intratumor microbiome, lactic acid metabolism and immune status in lung squamous cell carcinoma. *Front Immunol*. 2025. doi:10.3389/fimmu.2025.1603822 | PMID: 40568577

34. Chen F, Wen X, Li S, et al. Targeting hypoxia-mediated chemo-immuno resistance by a hybrid NBDHEX-Pt(IV) prodrug via declining nuclear STING1-promoted AhR-CIN in human lung squamous cell carcinoma. *Transl Oncol*. 2025;52:102350. doi:10.1016/j.tranon.2025.102350 | PMID: 40138855

35. Zhao F, et al. Hypoxia-related lncRNAs to build prognostic classifier and reveal the immune characteristics of EGFR wild type and low expression of PD-L1 in lung squamous cell carcinoma. *Front Oncol*. 2021. doi:10.3389/fonc.2021.694551 | PMID: 34250747

36. Xu H, Yang Y, Wang P, et al. Unraveling the immune mechanisms and therapeutic targets in lung adenosquamous transformation. *Front Immunol*. 2025;16:1502584. doi:10.3389/fimmu.2025.1502584 | PMID: 40568576

37. Wang F, Zhu L. Phenotypic plasticity promotes lymph nodes metastasis and drug resistance in lung squamous cell carcinomas. *Heliyon*. 2023;9(4):e15083. doi:10.1016/j.heliyon.2023.e15083 | PMID: 37025908

38. Marcoux N, Gettinger SN, O'Kane G, et al. EGFR-mutant adenocarcinomas that transform to small-cell lung cancer and other neuroendocrine carcinomas: clinical outcomes. *J Clin Oncol*. 2019;37(4):278–285. doi:10.1200/JCO.18.01585 | PMID: 30550363

39. Huang L, Li H. Case report: PD-1/CTLA-4 dual checkpoint blockade (QL1706) in advanced pulmonary squamous cell carcinoma complicated by multidrug-resistant tuberculosis. *Front Oncol*. 2026. doi:10.3389/fonc.2026.1775568 | PMID: 42078800

40. Gettinger SN, Redman MW, Bazhenova L, et al. Nivolumab plus ipilimumab vs nivolumab for previously treated patients with stage IV squamous cell lung cancer: the Lung-MAP S1400I phase 3 randomized clinical trial. *JAMA Oncol*. 2021;7(9):1368–1377. doi:10.1001/jamaoncol.2021.2201 | PMID: 34264316

41. Lu T, et al. Intrapulmonic cavity or necrosis on baseline CT scan serves as an efficacy predictor of anti-PD-(L)1 inhibitor in advanced lung squamous cell carcinoma. *Front Immunol*. 2021. doi:10.3389/fimmu.2021.715758 | PMID: 34354375

---

*Manuscript prepared for submission to Journal for ImmunoTherapy of Cancer (JITC)*
*Format: Vancouver reference style | BMJ house style*
*Date: 2026-06-04*
