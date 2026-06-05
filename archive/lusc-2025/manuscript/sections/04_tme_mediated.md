# 4. Tumor Microenvironment-Mediated Resistance

While tumor-intrinsic alterations establish the molecular foundation for immune evasion, the tumor microenvironment—comprising diverse immune cell populations, stromal elements, cytokines, metabolites, and microbial communities—constitutes the battlefield on which immunotherapy succeeds or fails. In LUSC, the TME is characterized by a convergence of immunosuppressive forces that collectively drive resistance to ICIs, even in tumors with abundant T cell infiltration.

## 4.1 T Cell Exhaustion and Dysfunction

T cell exhaustion—a state of progressive loss of effector function arising from chronic antigen stimulation—is a central mechanism of immune evasion in LUSC [1]. The exhausted T cell differentiation trajectory is governed by a hierarchical transcriptional program: progenitor exhausted T cells (Tpex), characterized by TCF-1 expression and maintained by the transcription factor TOX at intermediate levels, retain proliferative capacity and are the primary cellular targets of PD-1 blockade [1,2]. As exhaustion progresses, Tpex differentiate into terminally exhausted T cells (Tex-term) that express high levels of TOX, multiple inhibitory receptors, and exhibit severely impaired cytokine production and cytolytic function [2]. Critically, Tex-term cells are largely refractory to anti-PD-1 therapy, as their dysfunctional state is maintained by epigenetic imprinting rather than ongoing PD-1 signaling [1].

In the LUSC Exhausted Immune Class described by Yang et al., the T cell compartment is skewed toward a Tex-term-dominant state, with diminished TCF-1+ Tpex frequencies, elevated TOX and EOMES expression, and co-expression of numerous inhibitory receptors [2]. This exhaustion state is reinforced by multiple TME-derived factors: persistent antigen exposure from high neoantigen burden; immunosuppressive cytokines including IL-10, TGF-β, and CCL18; metabolic competition from tumor cells that depletes glucose and glutamine essential for T cell effector function; and chronic type I interferon signaling that, while initially immunostimulatory, can paradoxically drive T cell exhaustion when sustained [1,2].

## 4.2 Multi-Receptor Immune Checkpoint Co-Expression

A defining feature of the LUSC EIC is the co-upregulation of up to nine inhibitory immune checkpoints—CTLA-4, PD-1, LAG-3, BTLA, TIGIT, TIM-3, IDO1, SIGLEC7, and VISTA—creating a state of broad, multi-receptor immunosuppression [2]. This co-expression pattern carries critical therapeutic implications: blockade of the PD-1/PD-L1 axis alone leaves multiple alternative inhibitory pathways intact, enabling compensatory signaling through other checkpoints to maintain T cell suppression [2,3]. This concept is supported by the clinical experience in the Lung-MAP S1400F substudy, in which dual PD-L1/CTLA-4 blockade (durvalumab + tremelimumab) produced minimal clinical benefit in patients with acquired resistance to prior anti-PD-(L)1 therapy, suggesting that resistance in these patients is maintained through checkpoint-independent or additional checkpoint-mediated mechanisms [4].

The specific repertoire of co-expressed checkpoints has implications for rational combination design. LAG-3 and TIGIT, both frequently co-expressed with PD-1 in LUSC, engage distinct ligands (MHC class II and CD155/PVR, respectively) and signal through independent intracellular pathways, making them attractive targets for combination with PD-1 blockade [2,3]. The bispecific antibody rilvegostomig, which simultaneously targets PD-1 and TIGIT, is currently being evaluated in phase III trials including TROPION-Lung10 in NSCLC [5]. Similarly, TIM-3, which marks highly dysfunctional CD8+ T cells and is co-expressed with PD-1 on tumor-infiltrating lymphocytes in LUSC, represents a clinically relevant target with anti-TIM-3 antibodies in development [2].

## 4.3 Immunosuppressive Cell Populations

### 4.3.1 Tumor-Associated Macrophages (TAMs)

Tumor-associated macrophages represent the most abundant immune cell population in the LUSC TME and are a dominant driver of immunosuppression [6]. TAMs exhibit remarkable functional plasticity, with their polarization state heavily influenced by local environmental cues. In LUSC, TAMs are predominantly polarized toward an M2-like phenotype, characterized by expression of CD163, CD206, and APOE, driven by TME-derived signals including CSF-1, IL-4, IL-10, lactic acid, and tumor-secreted exosomes [6,7].

Ji et al. demonstrated that aldolase A (ALDOA), a key glycolytic enzyme, is significantly overexpressed in LUSC and strongly correlates with macrophage infiltration. Spatial transcriptomics and immunofluorescence confirmed co-localization of ALDOA-expressing tumor cells with CD68+ macrophages in LUSC tissues [6]. Functional analyses revealed that ALDOA-driven glycolytic flux generates a lactate-rich microenvironment that promotes M2 macrophage polarization, establishing a self-reinforcing metabolic-immune circuit: elevated glycolysis → lactic acid secretion → M2 TAM polarization → immunosuppressive cytokine production → T cell dysfunction [6]. High ALDOA expression was independently associated with poor overall survival, disease-specific survival, and progression-free interval in LUSC.

The interaction between TAMs and other stromal cells amplifies their immunosuppressive function. Spatial transcriptomic analyses have identified a POSTN+ CAF/APOE+ TAM signaling axis in squamous carcinomas, representing a cooperative signaling circuit: POSTN secreted by CAFs binds integrin receptors on TAMs, reinforcing M2 polarization, while APOE+ TAMs reciprocally secrete growth factors that sustain CAF activation [1]. This CAF-TAM co-dependency creates a spatially organized immunosuppressive niche at the tumor-stromal interface that physically excludes CD8+ T cells while simultaneously suppressing those that manage to infiltrate [1].

### 4.3.2 Cancer-Associated Fibroblasts (CAFs)

CAFs are activated fibroblasts that constitute a major component of the LUSC stroma and contribute to immune resistance through multiple mechanisms [7,8]. In LUSC, the CAF compartment is heterogeneous, with functionally distinct subpopulations: inflammatory CAFs (iCAFs) that secrete cytokines and chemokines; myofibroblastic CAFs (myCAFs) that deposit ECM components; and antigen-presenting CAFs (apCAFs) that may modulate T cell responses [7].

The most well-characterized immune-evasion mechanism mediated by CAFs in LUSC is the physical exclusion of T cells. POSTN+ and FAP+ CAFs deposit dense ECM—particularly collagen type I, fibronectin, and laminin—creating a physical barrier that prevents CTL penetration into tumor nests [7,8]. ECM alignment perpendicular to the tumor boundary, mediated by CAF contractile forces, creates tracks that guide T cell migration along the tumor periphery rather than into the tumor interior. Beyond physical exclusion, CAFs secrete chemokines—including CXCL12 and CCL2—that actively repel T cells while recruiting immunosuppressive populations including Tregs and MDSCs. Furthermore, CAF-secreted TGF-β drives EMT in tumor cells and directly inhibits CTL function, creating multiple reinforcing immunosuppressive loops [7].

### 4.3.3 Myeloid-Derived Suppressor Cells (MDSCs) and Regulatory T Cells (Tregs)

MDSCs are a heterogeneous population of pathologically activated immature myeloid cells that expand in the LUSC TME and exert potent immunosuppressive functions through diverse mechanisms: depletion of arginine and cysteine, essential amino acids for T cell activation, via arginase-1 and xCT transporter expression; production of ROS and peroxynitrite that nitrosylate T cell receptor (TCR) components, rendering T cells unresponsive to antigen stimulation; and secretion of IL-10 and TGF-β that promote Treg expansion and inhibit DC maturation [1,8]. In LUSC, MDSC frequencies in peripheral blood and tumor tissue correlate with disease stage and inversely correlate with response to ICIs, suggesting that MDSC burden may serve as a predictive biomarker.

CD4+FOXP3+ Tregs are enriched in the LUSC TME, particularly in the EIC subtype, where their abundance is a defining feature [2]. Tregs suppress anti-tumor immunity through contact-dependent mechanisms—including CTLA-4-mediated transendocytosis of CD80/CD86 from DCs and granzyme B-mediated killing of effector T cells—and through secretion of immunosuppressive cytokines (IL-10, TGF-β, IL-35). The chemokine milieu of the LUSC TME, characterized by CCL22 and CCL17 production by TAMs and tumor cells, actively recruits CCR4+ Tregs, establishing a positive-feedback loop of immunosuppression [2].

## 4.4 Cytokine Networks

The LUSC cytokine milieu is dominated by a network of immunosuppressive mediators that collectively paralyze anti-tumor immunity. **TGF-β** is the central orchestrator, produced by tumor cells, CAFs, TAMs, and Tregs. TGF-β signaling in CD8+ T cells directly represses the expression of cytolytic effector molecules—perforin, granzyme B, and IFN-γ—while simultaneously promoting Treg differentiation and EMT in tumor cells [1,8]. The EIC is characterized by elevated TGF-β and CCL18 expression: CCL18, primarily secreted by M2 TAMs, recruits additional Tregs and immature DCs while promoting further TAM M2 polarization [2].

**Interleukin-6** (IL-6) activates STAT3 signaling in tumor cells and immune cells, driving a feed-forward loop of chronic inflammation that promotes tumor progression and immune evasion. **IL-10**, produced by Tregs, TAMs, and exhausted T cells, broadly suppresses antigen presentation, co-stimulatory molecule expression, and pro-inflammatory cytokine production by DCs and macrophages [2].

## 4.5 Metabolic Immune Modulation

### 4.5.1 Glycolysis and Lactic Acidosis

The LUSC TME is metabolically characterized by the Warburg effect—aerobic glycolysis resulting in high rates of glucose consumption and lactic acid production by tumor cells [6]. This metabolic program has profound consequences for anti-tumor immunity. Lactic acid accumulation acidifies the TME to pH 6.0–6.5, which directly inhibits T cell proliferation, cytokine production, and cytolytic activity while promoting Treg stability and M2 macrophage polarization [6]. The glucose-depleted TME metabolically starves CTLs, which are highly dependent on glycolysis for effector function, while Tregs—which can utilize fatty acid oxidation—maintain a metabolic advantage in low-glucose conditions [6,9].

ALDOA overexpression in LUSC, as discussed above, exemplifies how tumor cell-intrinsic metabolic reprogramming drives immune suppression [6]. Beyond ALDOA, multi-omics analyses have revealed complex interactions between the intratumoral microbiome composition, lactic acid metabolism, and immune status in LUSC, suggesting that microbial metabolites may directly modulate the metabolic-immune axis within the TME [7].

### 4.5.2 Hypoxia-Driven Immune Evasion

Hypoxia is a pervasive feature of the LUSC TME resulting from aberrant tumor vasculature and high metabolic demand [7]. Hypoxia-inducible factor-1α (HIF-1α) is stabilized under low oxygen tension and transcriptionally activates a program that simultaneously promotes tumor survival and immune evasion: PD-L1 upregulation; VEGF secretion that promotes abnormal angiogenesis and further hypoxia; and recruitment of MDSCs and TAMs [7].

A recently elucidated mechanism linking hypoxia to immune resistance involves the STING (stimulator of interferon genes) pathway, a critical node in innate immune sensing of cytosolic DNA [7]. Hypoxia suppresses STING signaling through HIF-1α-mediated mechanisms, resulting in decreased production of type I interferons, impaired dendritic cell maturation, and diminished cross-priming of tumor-specific CD8+ T cells. Restoration of STING signaling—either through hypoxia relief or direct STING agonism—has been shown to enhance ICI efficacy in preclinical LUSC models, identifying the hypoxia-STING axis as a therapeutically tractable immune evasion mechanism [7].

A hypoxia-related lncRNA signature has been developed in LUSC that stratifies patients by immune characteristics and prognosis, with high hypoxia scores associated with reduced immune infiltration and a microenvironment dominated by immunosuppressive cells. This signature was particularly informative in EGFR-wild-type, low-PD-L1 LUSC—a population for whom ICI monotherapy is often of limited benefit [7].

### 4.5.3 Amino Acid and Tryptophan Metabolism

Indoleamine 2,3-dioxygenase 1 (IDO1), one of the nine co-upregulated checkpoints in the LUSC EIC [2], catalyzes the rate-limiting step of tryptophan degradation along the kynurenine pathway. Tryptophan depletion and kynurenine accumulation act synergistically to suppress T cell proliferation—through GCN2 kinase activation and mTOR inhibition—while promoting Treg differentiation through aryl hydrocarbon receptor (AhR) activation [2]. Arginine metabolism by arginase-1-expressing MDSCs and TAMs similarly depletes the TME of arginine, which is essential for TCR ζ-chain expression and T cell activation [1].

## 4.6 Tumor Microbiome-Immune Crosstalk

An emerging dimension of LUSC TME biology is the role of the intratumoral microbiome in modulating immune responses and immunotherapy outcomes [7]. Multi-omics integration has revealed that the composition of the intratumoral microbiota in LUSC is significantly correlated with lactic acid metabolism, immune cell infiltration patterns, and immune checkpoint expression [7]. Specific bacterial taxa have been associated with distinct immune phenotypes: for example, enrichment of *Lactobacillus* species correlates with an immunosuppressive TME characterized by M2 macrophage predominance and attenuated CD8+ T cell responses, potentially through modulation of tryptophan and lactate metabolism [7].

Conversely, certain microbial signatures are associated with immune-inflamed tumors and may predict favorable ICI responses, paralleling observations in LUAD and other cancers where gut and intratumoral microbiome composition influences immunotherapy outcomes [7]. While the mechanistic links between the LUSC microbiome and immune resistance are still being defined, these findings raise the possibility that microbiome-directed interventions—including antibiotics, probiotics, or metabolite supplementation—could be leveraged to modulate immunotherapy responses in LUSC.

---

The TME-mediated resistance mechanisms described above do not arise *de novo* at the time of treatment; rather, they evolve dynamically under the selective pressure of ICI therapy. The following section will examine how therapeutic pressure drives acquired resistance through clonal evolution, histological transformation, and phenotypic plasticity.

---

## References (Section 4)

1. Tong Y, Wang Y, Chen Y, Fan Y, Li H. Decoding the tumor immune microenvironment in lung squamous cell carcinoma: characteristics, regulatory mechanisms, and future directions. *Transl Lung Cancer Res*. 2025;14(4):1170–1190. | **PMID: 41133013**
2. Yang M, Lin C, Wang Y, et al. Identification of a cytokine-dominated immunosuppressive class in squamous cell lung carcinoma with implications for immunotherapy resistance. *Genome Med*. 2022;14(1):72. | **PMID: 35799269**
3. Yuan H, Liu J, Zhang J. The Current Landscape of Immune Checkpoint Blockade in Metastatic Lung Squamous Cell Carcinoma. *Molecules*. 2021;26(5):1392. | **PMID: 33807509**
4. Leighl NB, Redman MW, Rizvi N, et al. Phase II study of durvalumab plus tremelimumab as therapy for patients with previously treated anti-PD-(L)1 resistant stage IV squamous cell lung cancer (Lung-MAP S1400F). *J Immunother Cancer*. 2021;9(8):e002973. | **PMID: 34429332**
5. Newsom-Davis T, et al. TROPION-Lung10: a phase 3 study of datopotamab deruxtecan and rilvegostomig in patients with treatment-naïve locally advanced or metastatic nonsquamous NSCLC. *Front Oncol*. 2025. | **PMID: 41669261**
6. Ji Y, Li X, Shen X, et al. Aldolase A in pan-cancer and lung squamous cell carcinoma: prognostic value and macrophage-driven immune suppression. *Cancer Cell Int*. 2025;25:184. | **PMID: 41239433**
7. Niu Z, Jin R, Zhang Y, Li H. Signaling pathways and targeted therapies in lung squamous cell carcinoma: mechanisms and clinical trials. *Signal Transduct Target Ther*. 2022;7:353. | **PMID: 36198685**
8. (Microbiome-lactic acid). Multi-omics analysis untangles the crosstalk between intratumor microbiome, lactic acid metabolism and immune status in LUSC. 2025. | **PMID: 40568577**
9. (Hypoxia-STING). Targeting hypoxia-mediated chemo-immuno resistance by a hybrid NBDHEX-Pt(IV) prodrug via declining nuclear STING1-promoted AhR-CIN pathway. 2025. | **PMID: 40138855**
10. Zhao F, et al. Hypoxia-related lncRNAs to build prognostic classifier and reveal the immune characteristics of EGFR wild type and low expression of PD-L1 in LUSC. *Front Oncol*. 2021. | **PMID: 34250747**
