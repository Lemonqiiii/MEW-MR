# Language Naturalness

## Core Insight

"Natural" cannot be defined positively — defining it produces the opposite of nature.
But stiffness can be precisely detected. **Natural = not stiff = high variance.**

The following anti-patterns are concrete sources of stiffness. The review agent checks for them during every review pass.

## Anti-Pattern 1: Nominalization Chain
- **Detection**: ≥3 actions nominalized in a single sentence (-tion, -ment, -ence, -sis, -ance suffixes + "of" structures)
- **Example**: "The administration of ICIs imposes potent immunologic selective pressure on genetically heterogeneous tumor cell populations, driving a Darwinian process of clonal evolution" → 6 nominalized actions stacked, no breathing point
- **Fix**: Break the nominalization chain → split into two sentences, return at least one action to verb form
- **Severity**: Nice to Have (Must Fix if ≥5 in a single sentence)

## Anti-Pattern 2: Transition Monotony
- **Detection**: ≥3 consecutive paragraphs begin with the same transition type ("Furthermore/Moreover/In addition" = additive; "However/In contrast/Conversely" = contrastive; "Consequently/Therefore/Thus" = causal)
- **Fix**: Alternate transition types, or replace transitions with concrete statements
- **Severity**: Must Fix

## Anti-Pattern 3: Sentence-Length Entropy
- **Detection**: All sentences in a paragraph fall within 22-35 words (no short sentence <12 words, no long sentence >35 words)
- **Fix**: At least 1 short sentence (<12 words) per paragraph for rhythm; key arguments can use short standalone sentences for emphasis
- **Example**: "This matters. Because KEAP1 mutation alone can doom an immune response."
- **Severity**: Nice to Have

## Anti-Pattern 4: Passive Voice Stacking
- **Detection**: ≥4 consecutive sentences in passive voice (be + past participle)
- **Fix**: Convert at least 1 of the consecutive passive sentences to active voice. Passive itself is not wrong — consecutive use creates stiffness
- **Severity**: Nice to Have

## Anti-Pattern 5: Template Paragraph
- **Detection**: ≥3 consecutive paragraphs using the identical structure (e.g., topic sentence → evidence A → evidence B → evidence C → summary)
- **Fix**: Vary paragraph structure — some open with questions, some with data, some with controversy
- **Severity**: Nice to Have

## Anti-Pattern 6: Empty Intensifiers
- **Detection**: "Interestingly," "Notably," "Of note," "It is worth noting that," "Importantly," "Of particular importance," "Surprisingly,"
- **Fix**: **Delete directly.** The emphasized content should be convincing on its own, without a prefix telling you it's "interesting"
- **Severity**: Must Fix (delete on sight, leave no trace)

## Review Flow

Agent 4 performs naturalness scanning during every review pass:

1. Scan each paragraph for the 6 anti-patterns
2. Mark hit locations (paragraph number + anti-pattern number)
3. Provide fix suggestions for Must Fix items
4. Calculate "naturalness score": `passing_paragraphs / total_paragraphs` (passing = no anti-pattern 1-5 hits; anti-pattern 6 deletions don't count toward score)

**Naturalness Target**: ≥80% paragraphs passing (Phase 6 baseline; Phase 7+ target ≥90%)
