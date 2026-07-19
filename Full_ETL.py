import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(level = logging.INFO,
                    format = "%(asctime)s - %(levelname)s - %(message)s")

def load_file(file_path):
    logging.info("Ingestion has started.....")
    logging.info("Reading the CSV File......")
    try:
        df = pd.read_csv(file_path)
        logging.info("File Successfully loaded......")

        logging.info(f"rows: {df.shape[0]}, columns: {df.shape[1]}")
        logging.info(f"The columns in the file are:{list(df.columns)}")
        print(df.shape)
        print(df.head())
        df.info()
        return df
    except FileNotFoundError:
        logging.error(f"File Not Found..{file_path}")
    except pd.errors.EmptyDataError:
        logging.error("The CSV File is Empty")
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")

def remove_duplicates(df):
    before = len(df)
    df.drop_duplicates(inplace=True)
    after = len(df)
    logging.info(f"Removing'{before-after}' Duplicated from CSV File")
    return df

def trim_spaces(df,columns):
    for col in columns:
        df[col] = df[col].str.strip()
    logging.info(f"The columns trimmed are: {columns}")
    return df

def lower_text(df,columns):
    df[columns] = df[columns].str.lower()
    logging.info(f"Converted '{columns}' to lowercase")
    return df

def title_text(df,columns):
    for col in columns:
        df[col] = df[col].str.title()
        logging.info(f"Converted '{col}' to title text")
    return df

def clean_numbers(df,columns):
    df[columns] = (df[columns].astype(str).str.replace(r'[^0-9]','',regex=True).str[-10:].apply(lambda x: f"+91 {x}" if len(x)==10 else None))
    logging.info(f"Phone numbers are cleaned in '{columns}'")
    return df

def clean_dates(df,columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        invalid_dates = df[col].isna().sum()

        logging.info(f"Converted '{col}' to timedate")
        logging.warning(f"{invalid_dates} invalid/missing dates found")
    return df
    

def convert_cols(df,columns):
    df[columns] = pd.to_numeric(df[columns],errors='coerce')
    logging.info(f"Converted '{columns}' to numeric.")
    return df

def handle_missing_names(df,columns):
    for col in columns:
        before = len(df)
        df.dropna(subset=[col],inplace=True)
        after = len(df)
        logging.info(f"Removed {before - after} rows with missing {col}.")
    return df

def handle_missing_salary(df,columns):
    df[columns] = df[columns].fillna('0')

    negative_count = (df[columns] < 0).sum()

    if negative_count > 0:
        logging.warning(f"{negative_count} records have negative salary")

    logging.info(f"Filled missing salary values in '{columns}'.")
    return df

def handle_missing_dates(df,columns):
    missing = df[columns].isna().sum()
    logging.warning(f"{missing} missing dates found in '{columns}'.")
    return df


def standardize_gender(df):
    df["Gender"] = df["Gender"].replace({
        "Male": "M",
        "Female": "F"
    })

    logging.info("Standardized Gender values.")

    return df

def create_full_name(df):
    df['Full_name'] = df['FirstName'] + '' + df['LastName']
    return df

def create_salary_band(df):
    def salary_band(salary):
        if salary<50000:
            return "Low"
        elif salary > 50000 and salary<80000:
            return "Medium"
        else:
            return "High"
        
    df['SalaryBand'] = df['Salary'].apply(salary_band)
    return df

def create_join_month(df):
    df['JoinMonth'] = df['JoinDate'].dt.month_name()
    logging.info("Created the Join Month")
    return df

def create_age(df):
    current_year = datetime.now().year
    df['Age'] = current_year - df['DateOfBirth'].dt.year
    logging.info("Created Age Column")
    return df

def load_to_csv(df,output_path):
    try:
        df.to_csv(output_path, index=False)
        logging.info(f"Parquet file saved successfully at:")
        logging.info(output_path)
    except Exception as e:
        logging.error(f"Failed to save csv file: {e}")


logging.info("ETL Pipeline started.............")

df = load_file(r"C:\Users\saisa\Desktop\customer_data_raw.csv")

df = trim_spaces(df,['FirstName','LastName','Email','Gender','Department','City','State'])

df = lower_text(df,'Email')

df = title_text(df,['FirstName','LastName'])

df = standardize_gender(df)

df = remove_duplicates(df)

df = handle_missing_names(df,['FirstName','LastName','PhoneNumber','Email'])

df = handle_missing_dates(df,['DateOfBirth'])

df = handle_missing_salary(df,'Salary')

df = clean_dates(df,['DateOfBirth','JoinDate'])

df = convert_cols(df,'Salary')

df = clean_numbers(df,'PhoneNumber')

df = create_full_name(df)

df = create_salary_band(df)

df = create_join_month(df)

df = create_age(df)

load_to_csv(df,r"C:\Users\saisa\Desktop\customer_data_cleaned_2.csv")

logging.info("ETL Pipeline Ended Successfully....................")






                                        
    




    

    