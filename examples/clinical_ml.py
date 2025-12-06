"""
Oxford Matplotlib Theme - Clinical Machine Learning Examples
=============================================================
Demonstrates visualization of clinical prediction models and ML metrics.

These examples are particularly relevant for healthcare research and
CPRD data analysis at the University of Oxford.

Requirements: scikit-learn, scipy, pandas
"""

import numpy as np
import matplotlib.pyplot as plt
from oxford_matplotlib_theme import apply_oxford_theme, get_palette

# Apply Oxford theme
apply_oxford_theme()

# Check for optional dependencies
try:
    from sklearn.metrics import roc_curve, auc, precision_recall_curve
    from sklearn.calibration import calibration_curve
    SKLEARN_AVAILABLE = True
except ImportError:
    print("Warning: scikit-learn not available. Some examples will use simulated metrics.")
    SKLEARN_AVAILABLE = False


def generate_sample_predictions(n_samples=1000, seed=42):
    """Generate sample prediction data for demonstration."""
    np.random.seed(seed)

    # True labels
    y_true = np.random.binomial(1, 0.3, n_samples)

    # Predictions from different models (with varying performance)
    model1_pred = y_true * np.random.beta(8, 2, n_samples) + (1 - y_true) * np.random.beta(2, 8, n_samples)
    model2_pred = y_true * np.random.beta(7, 3, n_samples) + (1 - y_true) * np.random.beta(3, 7, n_samples)
    model3_pred = y_true * np.random.beta(6, 4, n_samples) + (1 - y_true) * np.random.beta(4, 6, n_samples)

    return y_true, [model1_pred, model2_pred, model3_pred]


def example_1_roc_curve():
    """Example 1: ROC curves for multiple models."""
    print("Creating Example 1: ROC curves...")

    fig, ax = plt.subplots(figsize=(10, 8))

    # Generate sample data
    y_true, predictions = generate_sample_predictions()
    model_names = ['Logistic Regression', 'Random Forest', 'Neural Network']

    # Get colors
    colors = get_palette('primary', n_colors=3)

    if SKLEARN_AVAILABLE:
        # Plot ROC curve for each model
        for pred, name, color in zip(predictions, model_names, colors):
            fpr, tpr, _ = roc_curve(y_true, pred)
            roc_auc = auc(fpr, tpr)

            ax.plot(fpr, tpr, color=color, linewidth=2.5,
                   label=f'{name} (AUC = {roc_auc:.3f})')
    else:
        # Plot simulated ROC curves
        fpr = np.linspace(0, 1, 100)
        for i, (name, color) in enumerate(zip(model_names, colors)):
            tpr = fpr ** (0.3 + i * 0.1)  # Simulated curves
            roc_auc = 0.85 - i * 0.05
            ax.plot(fpr, tpr, color=color, linewidth=2.5,
                   label=f'{name} (AUC = {roc_auc:.3f})')

    # Plot diagonal reference line
    ax.plot([0, 1], [0, 1], 'k--', linewidth=1.5, alpha=0.5, label='Random Classifier')

    # Styling
    ax.set_xlabel('False Positive Rate', fontsize=12)
    ax.set_ylabel('True Positive Rate', fontsize=12)
    ax.set_title('ROC Curves for Clinical Prediction Models', fontsize=14, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([-0.02, 1.02])
    ax.set_ylim([-0.02, 1.02])

    plt.tight_layout()
    return fig


def example_2_precision_recall():
    """Example 2: Precision-Recall curves."""
    print("Creating Example 2: Precision-Recall curves...")

    fig, ax = plt.subplots(figsize=(10, 8))

    # Generate sample data
    y_true, predictions = generate_sample_predictions()
    model_names = ['Model A', 'Model B', 'Model C']

    # Get colors
    colors = get_palette('vibrant', n_colors=3)

    if SKLEARN_AVAILABLE:
        # Calculate baseline (prevalence)
        prevalence = np.mean(y_true)

        # Plot PR curve for each model
        for pred, name, color in zip(predictions, model_names, colors):
            precision, recall, _ = precision_recall_curve(y_true, pred)
            pr_auc = auc(recall, precision)

            ax.plot(recall, precision, color=color, linewidth=2.5,
                   label=f'{name} (AUC = {pr_auc:.3f})')

        # Plot baseline
        ax.axhline(y=prevalence, color='k', linestyle='--', linewidth=1.5,
                   alpha=0.5, label=f'Baseline (prevalence = {prevalence:.3f})')
    else:
        # Simulated PR curves
        recall = np.linspace(0, 1, 100)
        for i, (name, color) in enumerate(zip(model_names, colors)):
            precision = 0.7 - i * 0.05 - recall * 0.2
            pr_auc = 0.65 - i * 0.05
            ax.plot(recall, precision, color=color, linewidth=2.5,
                   label=f'{name} (AUC = {pr_auc:.3f})')

        ax.axhline(y=0.3, color='k', linestyle='--', linewidth=1.5, alpha=0.5,
                   label='Baseline (prevalence = 0.300)')

    # Styling
    ax.set_xlabel('Recall (Sensitivity)', fontsize=12)
    ax.set_ylabel('Precision (PPV)', fontsize=12)
    ax.set_title('Precision-Recall Curves for Rare Event Prediction', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([-0.02, 1.02])
    ax.set_ylim([-0.02, 1.02])

    plt.tight_layout()
    return fig


def example_3_calibration_plot():
    """Example 3: Calibration plot (reliability diagram)."""
    print("Creating Example 3: Calibration plot...")

    fig, ax = plt.subplots(figsize=(10, 8))

    # Generate sample data
    y_true, predictions = generate_sample_predictions()

    # Get color
    colors = get_palette('health')

    if SKLEARN_AVAILABLE:
        # Calculate calibration for first model
        fraction_of_positives, mean_predicted_value = calibration_curve(
            y_true, predictions[0], n_bins=10, strategy='uniform'
        )

        # Plot calibration curve
        ax.plot(mean_predicted_value, fraction_of_positives, 'o-',
               color=colors[0], linewidth=2.5, markersize=8,
               label='Model Calibration', markeredgecolor='white', markeredgewidth=1.5)
    else:
        # Simulated calibration
        x = np.linspace(0, 1, 10)
        y = x + np.random.normal(0, 0.05, 10)
        ax.plot(x, y, 'o-', color=colors[0], linewidth=2.5, markersize=8,
               label='Model Calibration', markeredgecolor='white', markeredgewidth=1.5)

    # Plot perfect calibration line
    ax.plot([0, 1], [0, 1], 'k--', linewidth=2, alpha=0.7, label='Perfect Calibration')

    # Styling
    ax.set_xlabel('Predicted Probability', fontsize=12)
    ax.set_ylabel('Observed Frequency', fontsize=12)
    ax.set_title('Calibration Plot (Reliability Diagram)', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([-0.02, 1.02])
    ax.set_ylim([-0.02, 1.02])

    plt.tight_layout()
    return fig


def example_4_feature_importance():
    """Example 4: Feature importance bar chart."""
    print("Creating Example 4: Feature importance...")

    fig, ax = plt.subplots(figsize=(10, 8))

    # Sample features and importances
    features = [
        'Age', 'BMI', 'Systolic BP', 'HbA1c',
        'Total Cholesterol', 'Smoking Status',
        'Family History', 'Medication Count',
        'Comorbidity Score', 'eGFR'
    ]
    importances = np.array([0.18, 0.15, 0.14, 0.12, 0.10, 0.09, 0.08, 0.07, 0.05, 0.02])

    # Sort by importance
    sorted_idx = np.argsort(importances)
    sorted_features = [features[i] for i in sorted_idx]
    sorted_importances = importances[sorted_idx]

    # Get color
    colors = get_palette('professional')

    # Create horizontal bar chart
    y_pos = np.arange(len(sorted_features))
    ax.barh(y_pos, sorted_importances, color=colors[0], alpha=0.8, edgecolor='white', linewidth=0.5)

    # Styling
    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_features, fontsize=10)
    ax.set_xlabel('Feature Importance', fontsize=12)
    ax.set_title('Clinical Variable Importance in Prediction Model', fontsize=14, fontweight='bold')
    ax.grid(True, axis='x', alpha=0.3)

    # Add value labels
    for i, v in enumerate(sorted_importances):
        ax.text(v + 0.005, i, f'{v:.3f}', va='center', fontsize=9)

    plt.tight_layout()
    return fig


def example_5_confusion_matrix():
    """Example 5: Confusion matrix heatmap."""
    print("Creating Example 5: Confusion matrix...")

    fig, ax = plt.subplots(figsize=(8, 7))

    # Sample confusion matrix
    confusion = np.array([
        [850, 50],
        [100, 200]
    ])

    # Get colors for heatmap
    from oxford_matplotlib_theme.colors import OXFORD_COLORS

    # Create heatmap
    im = ax.imshow(confusion, cmap='Blues', alpha=0.8)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Count', rotation=270, labelpad=20, fontsize=11)

    # Set ticks
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(['Predicted Negative', 'Predicted Positive'], fontsize=11)
    ax.set_yticklabels(['Actual Negative', 'Actual Positive'], fontsize=11)

    # Add text annotations
    for i in range(2):
        for j in range(2):
            text = ax.text(j, i, confusion[i, j],
                         ha="center", va="center", color="black" if confusion[i, j] > 400 else "white",
                         fontsize=20, fontweight='bold')

    # Add metrics as text
    accuracy = (confusion[0,0] + confusion[1,1]) / confusion.sum()
    sensitivity = confusion[1,1] / (confusion[1,0] + confusion[1,1])
    specificity = confusion[0,0] / (confusion[0,0] + confusion[0,1])

    metrics_text = f'Accuracy: {accuracy:.3f} | Sensitivity: {sensitivity:.3f} | Specificity: {specificity:.3f}'
    ax.text(0.5, -0.15, metrics_text, ha='center', transform=ax.transAxes,
           fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    ax.set_title('Confusion Matrix - Clinical Prediction Model', fontsize=14, fontweight='bold', pad=15)

    plt.tight_layout()
    return fig


def example_6_survival_curves():
    """Example 6: Kaplan-Meier style survival curves."""
    print("Creating Example 6: Survival curves...")

    fig, ax = plt.subplots(figsize=(10, 8))

    # Generate sample survival data
    np.random.seed(42)
    time = np.linspace(0, 60, 100)  # 60 months follow-up

    # Simulated survival for different treatment groups
    survival1 = np.exp(-0.02 * time)  # Treatment A
    survival2 = np.exp(-0.03 * time)  # Treatment B
    survival3 = np.exp(-0.04 * time)  # Control

    # Get colors
    colors = get_palette('traditional', n_colors=3)

    # Plot survival curves
    ax.plot(time, survival1, color=colors[0], linewidth=2.5,
           label='Treatment A', drawstyle='steps-post')
    ax.plot(time, survival2, color=colors[1], linewidth=2.5,
           label='Treatment B', drawstyle='steps-post')
    ax.plot(time, survival3, color=colors[2], linewidth=2.5,
           label='Control', drawstyle='steps-post')

    # Add confidence intervals (simulated)
    for survival, color in zip([survival1, survival2, survival3], colors):
        ci_lower = survival - 0.05
        ci_upper = survival + 0.05
        ax.fill_between(time, ci_lower, ci_upper, color=color, alpha=0.2, step='post')

    # Styling
    ax.set_xlabel('Time (months)', fontsize=12)
    ax.set_ylabel('Survival Probability', fontsize=12)
    ax.set_title('Kaplan-Meier Survival Curves by Treatment Group', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 60])
    ax.set_ylim([0, 1.05])

    # Add at-risk table (simulated)
    risk_text = "Numbers at risk:\nTreatment A: 500  450  380  290\nTreatment B: 500  430  350  250\nControl:     500  400  300  200"
    ax.text(0.02, 0.02, risk_text, transform=ax.transAxes,
           fontsize=8, verticalalignment='bottom', fontfamily='monospace',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    return fig


def main():
    """Run all examples and display them."""
    print("=" * 70)
    print("Oxford Matplotlib Theme - Clinical ML Examples")
    print("=" * 70)
    print()

    if not SKLEARN_AVAILABLE:
        print("Note: scikit-learn not found. Using simulated metrics.")
        print()

    # Create all examples
    examples = [
        example_1_roc_curve(),
        example_2_precision_recall(),
        example_3_calibration_plot(),
        example_4_feature_importance(),
        example_5_confusion_matrix(),
        example_6_survival_curves(),
    ]

    print()
    print("=" * 70)
    print(f"Created {len(examples)} example figures")
    print("Close the figure windows to exit")
    print("=" * 70)

    # Show all figures
    plt.show()


if __name__ == '__main__':
    main()
