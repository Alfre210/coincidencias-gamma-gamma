
x1 = c(2302,
       1828,
       1067,
       482)
x2 = c(2378,
       1743,
       1025,
       368)
y1 = c(-7.70,
       -6.20,
       -3.72,
       -1.83)
y2 = c(-8.07,
       -6.05,
       -3.74,
       -1.62)       



df1 = data.frame(x1,y1)
df2 = data.frame(x2,y2)

model1 = lm(y1 ~ x1, data = df1)
summary(model1)
summary(model1)$adj.r.squared

model2 = lm(y2 ~ x2, data = df2)
summary(model2)


summary(model2)$adj.r.squared

coef(model2)





