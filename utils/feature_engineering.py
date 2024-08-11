import pandas as pd


class FeatureEngineering:
    """
    This class contains methods for feature engineering on the input data.
    
    Parameters
    ----------
    None
    """

    def __init__(self, data, logger, opt):
        """
        Initialize the FeatureEngineering object with the logger instance.

        Parameters
        ----------
        data : pd.DataFrame
            The input dataframe.
        logger : Logger
            The logger instance for logging information.
        opt : Namespace
            The namespace object containing the experiment options.
        """
        self.data = data
        self.logger = logger
        self._opt = opt

    def calculate_total_days(self):
        """
        Calculate the total days admitted based on the Date of Admission and Discharge Date columns.

        Returns
        -------
        pd.DataFrame
            The dataframe with the Total Days Admitted column added.
        """
        date_admission_col = "Date of Admission"
        discharge_date_col = "Discharge Date"

        if self.data is None:
            raise ValueError("Data not loaded. Please call load_data() first.")

        if (
            date_admission_col in self.data.columns
            and discharge_date_col in self.data.columns
        ):
            self.data["Total Days Admitted"] = (
                pd.to_datetime(self.data[discharge_date_col])
                - pd.to_datetime(self.data[date_admission_col])
            ).dt.days
            print("\nColumn 'Total Days Admitted' has been created.\n")

        if "Total Days Admitted" in self.data.columns:
            self.logger.update_log(
                "data_processing", "feature_engineering", "Total Days Admitted created"
            )
        else:
            self.logger.update_log(
                "data_processing", "feature_engineering", "Date columns missing"
            )

        return self.data

    # Add other feature engineering methods here as needed
