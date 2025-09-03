import numpy as np
import pandas as pd
from scipy.stats import loguniform, spearmanr, pearsonr, chi2_contingency

def custom_correlation_with_pvalues(df, feature_types):
    corr_matrix = pd.DataFrame(np.zeros((df.shape[1], df.shape[1])), columns=df.columns, index=df.columns)
    pval_matrix = pd.DataFrame(np.zeros((df.shape[1], df.shape[1])), columns=df.columns, index=df.columns)

    for col1 in df.columns:
        for col2 in df.columns:
            if col1 == col2:
                corr = np.nan
                p_value = np.nan
            else:
                type1 = feature_types[col1]
                type2 = feature_types[col2]

                # Continuous vs Continuous (Pearson)
                if type1 == "continuous" and type2 == "continuous":
                    corr, p_value = pearsonr(df[col1], df[col2])

                # Binary vs Binary (Phi coefficient and chi-squared test p-value)
                elif type1 == "binary" and type2 == "binary":
                    contingency_table = pd.crosstab(df[col1], df[col2])
                    chi2, p_value, _, _ = chi2_contingency(contingency_table)
                    corr = np.sqrt(chi2 / df.shape[0])

                # Skip if Categorical variable involved
                elif type1 == "categorical" or type2 == "categorical":
                    continue

                # Ordinal/Binary vs Continuous or Ordinal vs Ordinal (Spearman)
                else:
                    corr, p_value = spearmanr(df[col1], df[col2])

            corr_matrix.loc[col1, col2] = corr
            pval_matrix.loc[col1, col2] = p_value

    return corr_matrix, pval_matrix

