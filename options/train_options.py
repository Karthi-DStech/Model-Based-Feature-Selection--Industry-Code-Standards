from options.base_options import BaseOptions
import os
import sys
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def none_or_int(value):
    """
    This function checks if the value is an integer or None.

    Parameters
    ----------
    value : str
        The value to check.

    Returns
    -------
    int
        The integer value.

    None
        If the value is None.
    """
    if value.lower() == "none":
        return None
    try:
        return int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid value: {value}")


class TrainOptions(BaseOptions):
    """Train options"""

    def __init__(self) -> None:
        super().__init__()

    def initialize(self) -> None:
        """Initialize train options"""
        BaseOptions.initialize(self)

        # Training Parameters

        self.parser.add_argument(
            "-m",
            "--model_name",
            type=str,
            default="GradientBoostingClassifier",
            choices=[
                "LogisticRegression",
                "KNeighborsClassifier",
                "SVC",
                "DecisionTreeClassifier",
                "RandomForestClassifier",
                "AdaBoostClassifier",
                "GradientBoostingClassifier",
                "XGBClassifier",
                "CatBoostClassifier",
                "LGBMClassifier",
            ],
            help="Name of the model to train",
        )

        self.parser.add_argument(
            "--random_state",
            type=int,
            default=101,
            help="Seed for random state",
        )

        self.parser.add_argument(
            "--test_size",
            type=float,
            default=0.3,
            help="Size of the test set",
        )

        self.parser.add_argument(
            "--n_trials",
            type=int,
            default=100,
            choices=[50, 100, 150, 200],
            help="Number of trials for hyperparameter tuning using Optuna",
        )

        self.parser.add_argument(
            "-s",
            "--scale_data",
            type=bool,
            default=True,
            choices=[True, False],
            help="Whether to scale the data",
        )

        self.parser.add_argument(
            "--target_column",
            type=str,
            default="Status",
            help="Name of the target column",
        )

        self.parser.add_argument(
            "--drop_columns",
            type=list,
            default=["Age"],
            help="List of columns to drop",
        )

        self.parser.add_argument(
            "--label_encode_columns",
            type=list,
            default=["Sex", "Edema", "Status"],
            help="List of columns to label encode",
        )

        self.parser.add_argument(
            "--one_hot_encode_columns",
            type=list,
            default=["Drug", "Hepatomegaly", "Spiders", "Ascites"],
            help="List of columns to one hot encode",
        )

        self.parser.add_argument(
            "--dtype_dict",
            type=dict,
            default=None,
            help="Dictionary of column names and their respective data types. \
                eg: {'Date of Admission': 'datetime64', 'Discharge Date': 'datetime64'}.",
        )

        self.parser.add_argument(
            "--missing_values_imputation",
            type=dict,
            default={
                "Drug": ("fillna", "Unknown"),
                "Ascites": ("fillna", "Unknown"),
                "Hepatomegaly": ("fillna", "Unknown"),
                "Spiders": ("fillna", "Unknown"),
                "Cholesterol": ("mean", None),
                "Albumin": ("mean", None),
                "Copper": ("mean", None),
                "Alk_Phos": ("mean", None),
                "SGOT": ("mean", None),
                "Tryglicerides": ("mean", None),
                "Platelets": ("mean", None),
                "Prothrombin": ("mean", None),
                "Stage": ("mode", None),
            },
            help="Missing Value Imputation Dictionary. Key is the column name and \
            value is a tuple of the imputation method and the value to impute. \
            The imputation methods are mean, median and mode. \
            For mean, median and mode, the value to impute should be None. \
            For eg:{'Ever_Married': ('mode', None), Var_1: ('fillna', 'Unknown'),}.",
        )

        self.parser.add_argument(
            "--feature_engg_name",
            type=list,
            default=None,
            help="Name of the feature engineering column. eg: ['calculate_total_days'].",
        )

        # XGBoost specific parameters for handling missing values

        self.parser.add_argument(
            "--missing_value_setup_model",
            type=int,
            default=-1,
            help="What value the models should consider as missing value",
        )

        self.parser.add_argument(
            "--missing_value_model",
            type=bool,
            default=False,
            choices=[True, False],
            help="The model will handle missing values",
        )

        # CatBoost specific parameters for handling missing and categorical values

        self.parser.add_argument(
            "--cat_columns",
            type=bool,
            default=True,
            choices=[True, False],
            help="The model will handle categorical values",
        )

        self.parser.add_argument(
            "--do_one_hot_encode",
            type=bool,
            default=True,
            choices=[True, False],
            help="To perform one hot encoding on the columns",
        )

        self.parser.add_argument(
            "--do_label_encode",
            type=bool,
            default=True,
            choices=[True, False],
            help="To perform label encoding on the columns",
        )

        self.parser.add_argument(
            "--cat_boost_features",
            type=list,
            default=[None],
            help="List of columns to be treated as categorical features",
        )

        # Feature Selection Parameters

        self.parser.add_argument(
            "--top_n",
            type=int,
            default=5,
            help="Number of top features to log",
        )

        self.parser.add_argument(
            "--feature_importance",
            type=bool,
            default=True,
            choices=[True, False],
            help="Whether to calculate feature importance",
        )

        # Sequential Feature Selector Parameters

        self.parser.add_argument(
            "--sequential_feature_selector",
            type=bool,
            default=True,
            choices=[True, False],
            help="Whether to perform sequential feature selection",
        )

        self.parser.add_argument(
            "--sfs_direction",
            type=str,
            default="forward",
            choices=["forward", "backward"],
            help="Direction of sequential feature selection",
        )

        self.parser.add_argument(
            "--sfs_k_features",
            type=str,
            default="best",
            choices=["best", "parsimonious"],
            help="Method to select the number of features",
        )
        self.parser.add_argument(
            "--sfs_verbose",
            type=int,
            default=1,
            help="Verbosity of sequential feature selection",
        )

        self.parser.add_argument(
            "--sfs_scoring",
            type=str,
            default="accuracy",
            choices=["accuracy", "roc_auc"],
            help="Scoring metric for sequential feature selection",
        )

        self.parser.add_argument(
            "--sfs_n_features",
            type=none_or_int,
            default=None,
            help="Number of features to select",
        )

        self.parser.add_argument(
            "--sfs_cv",
            type=int,
            default=5,
            help="Number of cross-validation folds",
        )
