# Imbalanced Data
## Discrete Classification
### Issues with Vanilla Accuracy
- High imbalances in classes may mask poor classification performance in high metrics  
 *e.g. a classifier that always assigns the majority class to a new instance will achieve 99% accuracy where the majority class is 99% prevalent*
- Accuracy assumes errors are equally cost, imbalanced classification: misclassifying instances of minority class are generally much costlier
- Accuracy assumes class proportion is statis




### Cohen's Kappa
$$
Acc_e = \frac{\bold{E}(TP)+\bold{E}(TN)}{N}
$$
where $\bold{E}$ is expectation:

$$
\bold{E}(TP) = \frac{POS\times P(POS)}{N}
$$

$$
\bold{E}(TN) = \frac{NEG\times P(NEG)}{N}
$$

Values less than zero indicate that performance of classifier is lower than random guessing
$$
\kappa = \frac{Acc_0-Acc_e}{1-Acc_e}
$$

### Weighted Loss Function
Since misclassifying the minority class may be significantly costlier than misclassifying the majority, we can apply selective weights to the loss function by weighting each outcome as follows:
$$
L = \frac{w_{+|+}TP + w_{+|-}FP + w_{-|+}FN + w_{-|-}TN}{N}
$$

#### Balanced Class Distribution
Setting misclassification costs to the inverse of class proportions, i.e. $w_{+|-} = N/NEG$ and $w_{-|+} = N/POS$ 

### F-Measure 
$$
F_\beta = (1+\beta^2)\frac{\text{precision}\times\text{recall}}{\beta^2\text{precision} + \text{recall}}
$$

## Continuous Output
By using a set threshold, we cannot differentiate more/less likely predictions in a given class

### ROC Curve
> TPR vs FPR 
For each possible threshold value, a point in the ROC curve is plotted based on the TPR and FPR for that threshold

### PR Graph
> Precision vs Recall
Focuses ONLY on the positive class  
Good classifiers have optimal trade-off in terms of precision and recall, and should be to the top right side