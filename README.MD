# Short explanation of the results

Each of the benchmarks was performed 5 times, with the suffix indicating the
index of the run. The results contains the standard output and timing results
for every subdirectory next to the README.MD.

 - `result_naive` contains the results for the feature/impossible-futures-naive branch
 - `results_opt` contains the results for the feature/impossible-futures branch
 - `result_stable`, `result_with_antichains`, `result_antichain_{positive, negative}` contain the results for the feature/impossible-futures branch using ONLY the stable, none, antichain positive and negative optimisations respectively.

The optimisations can be disabled with the following changes:
    * stable can be removed by commenting lines 135, 136 and removing the stable check on line 169.
    * antichain positive can be removed by changing line 102 (removing the `!detail::antichain_include(anti_chain_positive, t.to(), spec_prime)`), and commnting lines 117-119.
    * antichain negative can be removed by commenting lines 63-65, and 93.