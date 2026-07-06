suppressWarnings(suppressMessages({ library(lme4); library(car) }))
d <- read.csv("factorial.csv", stringsAsFactors = FALSE)
d$subject <- paste(d$probe, d$arm, d$run, sep = "_")
d$arm <- relevel(factor(d$arm), ref = "bare"); d$probe <- factor(d$probe); d$judge <- factor(d$judge)
m1 <- lmer(total ~ arm + probe + judge + (1|subject), data = d, REML = FALSE)
m2 <- lmer(total ~ arm * probe + judge + (1|subject), data = d, REML = FALSE)
cat("arm:probe interaction LRT:\n"); print(anova(m1, m2))
cat("\nnoslop rank per probe (marginal means):\n")
for (p in levels(d$probe)) {
  mm <- sort(tapply(d$total[d$probe==p], droplevels(d$arm[d$probe==p]), mean), decreasing=TRUE)
  cat(p, ": ", paste(names(mm), round(mm,2), collapse=" | "), "\n")
}
