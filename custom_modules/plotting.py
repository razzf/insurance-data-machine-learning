import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def box_hist_plot(df, feature_name, ylim_min, ylim_max, xticks=None):
    f, (ax_box, ax_hist) = plt.subplots(
        1, 2, sharey=True, gridspec_kw={"width_ratios": (0.50, 0.25)}, figsize=(5, 5)
    )

    sns.boxplot(df[feature_name], ax=ax_box)
    sns.histplot(data=df, y=feature_name, ax=ax_hist, bins=20, kde=True)

    ax_box.set(xticks=[], xlabel="")
    ax_box.set_ylabel(feature_name, labelpad=10)
    ax_box.set_title(f"Box plot of $\\it{{{feature_name}}}$ (incl. histogram)", pad=35)
    plt.ylim(ylim_min, ylim_max)
    plt.ylim(ylim_min, ylim_max)
    if xticks is not None:
        ax_hist.set(xticks=xticks, xlabel="Respondents")
    else:
        ax_hist.set(xlabel="Respondents")
    sns.despine(ax=ax_box)
    sns.despine(ax=ax_hist, right=True, top=True)
    plt.tight_layout()
    plt.show()



def plot_features(df, feature_types, figsize=(8, 6), fixed_feature2=None):
    plotted_pairs = set()  
    
    feature2_list = [fixed_feature2] if fixed_feature2 else df.columns

    for feature1 in df.columns:
        for feature2 in feature2_list:
            if feature1 == feature2:
                continue 

            feature_pair = tuple(sorted([feature1, feature2]))

            if feature_pair in plotted_pairs:
                continue
            
            plotted_pairs.add(feature_pair)
            
            type1 = feature_types[feature1]
            type2 = feature_types[feature2]
            
            fig, ax = plt.subplots(figsize=figsize)

            # Continuous x Continuous (scatter plot)
            if type1 == "continuous" and type2 == "continuous":
                sns.scatterplot(data=df, x=feature1, y=feature2, ax=ax)
                title = f"Scatter plot: {feature1} vs {feature2}"
                
            # Binary x Binary (Stacked Bar plot of Proportions)
            elif type1 == "binary" and type2 == "binary":
                contingency_table = pd.crosstab(df[feature1], df[feature2])
                proportions = contingency_table.div(contingency_table.sum(axis=1), axis=0)
                proportions.plot(kind="bar", stacked=True, color=["#66b3ff", "#ffb3e6"], ax=ax)
                title = f"Stacked Bar Plot of Proportions: {feature1} vs {feature2}"
                ax.legend(loc='center', title=feature2)
                
            # Binary x Continuous or Continuous x Binary (violin plot)
            elif (type1 == "binary" and type2 == "continuous") or (type1 == "continuous" and type2 == "binary"):
                if type1 == "binary":
                    sns.violinplot(data=df, x=feature1, y=feature2, split=True, ax=ax)
                else:
                    sns.violinplot(data=df, x=feature2, y=feature1, split=True, ax=ax)
                title = f"Violin plot: {feature1} vs {feature2}"
                
            # Ordinal x Continuous (box plot)
            elif (type1 == "ordinal" and type2 == "continuous") or (type1 == "continuous" and type2 == "ordinal"):
                if type1 == "ordinal":
                    sns.boxplot(data=df, x=feature1, y=feature2, ax=ax)
                else:
                    sns.boxplot(data=df, x=feature2, y=feature1, ax=ax)
                title = f"Box plot: {feature1} vs {feature2}"
                
            # Ordinal x Binary (Stacked Bar plot of Proportions)
            elif (type1 == "ordinal" and type2 == "binary") or (type1 == "binary" and type2 == "ordinal"):
                contingency_table = pd.crosstab(df[feature1], df[feature2])
                proportions = contingency_table.div(contingency_table.sum(axis=1), axis=0)
                proportions.plot(kind="bar", stacked=True, colormap="viridis", ax=ax)
                title = f"Stacked Bar Plot of Proportions: {feature1} vs {feature2}"
                ax.legend(loc='center', title=feature2)
                

            max_title_length = max(len(feature1), len(feature2))
            title_font_size = min(12 + max_title_length // 10, 6)

            ax.set_title(title, fontsize=title_font_size)
            
            plt.tight_layout()  
            plt.show()
