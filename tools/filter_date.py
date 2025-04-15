import pandas as pd
from datetime import datetime 

def filter_annual_reports(data, start_date=None, end_date=None):
        start_date = start_date if start_date is not None else "1900-01-01"
        end_date = end_date if end_date is not None\
            else (datetime.now() + pd.Timedelta(days=365)).strftime('%Y-%m-%d')
        data_df = pd.DataFrame(data["annualReports"])
        data_df["fiscalDateEnding"] = pd.to_datetime(data_df["fiscalDateEnding"])
        data_df = data_df.set_index("fiscalDateEnding").sort_index()
        data_df = data_df.loc[start_date:end_date]
        data["fiscalDateEnding"] = (
            data_df.rename(lambda x: x.strftime('%Y-%m-%d'))
                   .reset_index()
                   .to_dict(orient="records")
        )
        return data