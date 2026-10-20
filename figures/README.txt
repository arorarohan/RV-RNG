Save your plots in this folder with these names (case sensitive), as .pdf
(best for LaTeX) or .png:

  q1-histograms          Section 1: histograms of 1,000 and 100,000 samples
  q2-square              Section 2: y = x^2
  q2-log                 Section 2: y = ln(x) - ln(1 - x)
  q3-exponential         Section 3: inverse CDF samples
  q4-neutral-selection   Section 4: neutral selection runs

For example, in Python:

  plt.savefig("figures/q1-histograms.pdf", bbox_inches="tight")

report.tex picks each plot up automatically; until the file exists it shows
a placeholder box instead. On Overleaf, select this folder before clicking
Upload.
