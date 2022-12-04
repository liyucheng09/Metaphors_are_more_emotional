
# Code and data for our Figlang@EMNLP2022 paper: The Secret of Metaphor on Expressing Stronger Emotion

## Explaining data files

`specificity.tsv` annotates **which is more specific? metaphor or literal.**

- The `specificity` column indicates whether the metaphor is more specific. `1` means metaphor is more specific, `0` means literal is more specific, and `2` means same specific.
- The `common_hyper` column indicates the common hypernym of the metaphoric and literal term. For example, `(Synset('blast.v.07'), 1, 0, Synset('blaze_away.v.02'), Synset('blast.v.07'))`, the first item of the tuple indicates their common hypernym, the `1` and `0` means it takes the metaphoric term `1` step to reach the common hypernym, and it take `0` steps to reach the common hypernym. the last two items indicate the synset of metaphor and literal terms.

`similar_specific_terms.tsv` annotates **which is more emotional? metaphor or more specific literal.**

- The `more_emotional` column indicates whether the chosen more specific literal term is more emotional. `2` means the metaphor is more emotional; `1` means the more specific literal is more emotioanl; and `0` means they share the same level specificity.
- The `substitute` column is the manual chosen more specific literal term.
- The `similar_specific_terms` are all potential terms from worknet sharing the same level specificity with the metaphoric one.

`more_specific_terms.tsv` annotates **which is more emotional? literal or more specific literal.**

- The `substitute` column is the manual chosen more specific literal term.
- The `emotional` column indicates whether the chosen more specific literal term is more emotional than the original literal one. `2` means the original literal is more emotional; `1` means the more specific literal is more emotioanl; and `0` means they share the same level specificity.

## Expalining code files

`wordnet_level.py` locate terms in the wordnet hierarchy.

`specificity_emotion.py` produce terms in the same/lower level specificity in the wordnet hierarchy.