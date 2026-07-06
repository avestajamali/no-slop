#!/usr/bin/env Rscript
# no-slop factorial analysis.
# Input: factorial.csv with columns probe, arm, run, judge, total, c1..c5
# Design: 6 arms x 4 probes (P6, P7 original; P17r, P18 extension) x 30 runs
# (original P6/P7 wave was cut from 4 planned probes to 2 by server rate-limiting;
# the extension adds P17r + P18). Each subject scored by an Opus judge and a Sonnet
# judge. Subject = (probe,arm,run);
# the two judge rows per subject are nested.
# Model: total ~ arm + probe + judge + arm:judge, random intercept per subject.
# arm:judge tests whether no-slop's advantage is an artifact of same-family (Opus)
# judging — if the effect holds under Sonnet judges, self-preference is not the driver.

suppressWarnings(suppressMessages({ library(lme4); library(car) }))

args <- commandArgs(trailingOnly = TRUE)
csv <- if (length(args)) args[1] else "factorial.csv"
d <- read.csv(csv, stringsAsFactors = FALSE)
d$subject <- paste(d$probe, d$arm, d$run, sep = "_")
d$arm   <- factor(d$arm)
d$probe <- factor(d$probe)
d$judge <- factor(d$judge)
d$arm <- relevel(d$arm, ref = "bare")   # estimate each arm's lift over bare Opus

cat("=== N ===\n"); cat("judge-rows:", nrow(d), " subjects:", length(unique(d$subject)),
    " cells:", nlevels(d$arm) * nlevels(d$probe), "\n\n")
cat("=== per-cell mean total (max 10) ===\n")
cm <- tapply(d$total, list(d$arm, d$probe), mean)
print(round(cm, 2))
cat("\n=== per-arm marginal mean (pooled over probe+judge) ===\n")
am <- sort(tapply(d$total, d$arm, mean), decreasing = TRUE)
print(round(am, 3))

cat("\n=== mixed model: total ~ arm + probe + judge + arm:judge + (1|subject) ===\n")
m <- lmer(total ~ arm + probe + judge + arm:judge + (1|subject), data = d, REML = FALSE)
cat("\n--- Type II Wald ANOVA ---\n"); print(Anova(m, type = 2))

# Fixed-effect table
cat("\n--- fixed effects (ref arm = bare, ref judge = opus) ---\n")
co <- summary(m)$coefficients
print(round(co, 3))

# Pairwise: no-slop (full) vs every other arm, marginal over probe & judge.
cat("\n=== no-slop_full vs each arm (marginal means, Welch t on subject means) ===\n")
subj <- aggregate(total ~ subject + arm, data = d, FUN = mean)  # 1 value per subject
ref <- subj$total[subj$arm == "noslop_full"]
for (a in setdiff(levels(d$arm), "noslop_full")) {
  x <- subj$total[subj$arm == a]
  tt <- t.test(ref, x)
  # Cohen's d (pooled SD)
  sp <- sqrt(((length(ref)-1)*var(ref) + (length(x)-1)*var(x)) / (length(ref)+length(x)-2))
  d_es <- (mean(ref) - mean(x)) / sp
  cat(sprintf("noslop_full - %-14s  diff=%+5.2f  t=%6.2f  p=%.4g  d=%+.2f\n",
              a, mean(ref)-mean(x), tt$statistic, tt$p.value, d_es))
}

# Self-preference / judge-robustness: arm effect under each judge model.
cat("\n=== judge-model check: per-arm mean by judge ===\n")
jm <- tapply(d$total, list(d$arm, d$judge), mean)
print(round(jm, 2))
cat("\nOpus-minus-Sonnet per arm (negative = Sonnet judges score that arm higher):\n")
print(round(jm[,"opus"] - jm[,"sonnet"], 2))
cat("\narm:judge interaction p-value (is no-slop's edge judge-dependent?):\n")
m0 <- lmer(total ~ arm + probe + judge + (1|subject), data = d, REML = FALSE)
print(anova(m0, m))

# Per-criterion descriptive: where does the arm effect live?
cat("\n=== per-criterion arm means (0-2) ===\n")
for (cc in c("c1","c2","c3","c4","c5")) {
  cat(cc, ":\n"); print(round(sort(tapply(d[[cc]], d$arm, function(x) mean(x, na.rm=TRUE)), decreasing=TRUE), 2))
}
cat("\n=== done ===\n")
