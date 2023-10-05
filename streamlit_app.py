import streamlit as st
import pandas as pd
import numpy as np

def process_data(df_all_original, df_KSA):
    df_all = df_all_original.copy()
    df_all.insert(0, "country", "RSA")
    df_all.insert(1, "c_trans_date", df_all["Date"])
    df_all.insert(2, "tv_program_from_hour", 0)
    df_all.insert(3, "tv_program_from_minute", 0)
    df_all.insert(4, "tv_program_from_second", 0)
    df_all.insert(5, "tv_spot_start_time_hour", df_all["Time"].apply(lambda x: int(x.split(":")[0])))
    df_all.insert(6, "tv_spot_start_time_minute", df_all["Time"].apply(lambda x: int(x.split(":")[1])))
    df_all.insert(7, "tv_spot_start_time_second", df_all["Time"].apply(lambda x: int(x.split(":")[2])))
    df_all.insert(8, "tv_ad_15_minutes_interval", 0)
    df_all.insert(9, "booking_agency", "STARCOM MEDIA VEST GROUP")
    df_all.insert(10, "distributor", "distributor")
    df_all.insert(11, "sector_code", 0)
    df_all.insert(12, "sector", "sector")
    df_all.insert(13, "category_code", 0)
    df_all.insert(14, "category", "category")
    df_all.insert(15, "product_code", 0)
    df_all.insert(16, "product", "product")
    df_all.insert(17, "brand_code", 0)
    df_all.insert(18, "brand", df_all["Brand"])
    df_all.insert(19, "subbrand_code", 0)
    df_all.insert(20, "subbrand", df_all["Brand"])
    df_all.insert(21, "spot", "spot")
    df_all.insert(22, "tv_program_name", df_all["Programme"])
    df_all.insert(23, "break_number", 1)
    df_all.insert(24, "total_breaks_in_program", 1)
    df_all.insert(25, "spot_number", df_all["PIB"])
    df_all.insert(26, "total_spots_in_break", df_all["No Of Breaks"])
    df_all.insert(27, "page_number", np.nan)
    df_all.insert(28, "total_pages_in_publication", np.nan)
    df_all.insert(29, "press_ad_color", np.nan)
    df_all.insert(30, "visual_size", np.nan)
    df_all.insert(31, "press_size", np.nan)
    df_all.insert(32, "ad_language", df_all["Language"])
    df_all.insert(33, "ad_picture_name", "no_picture")
    df_all.insert(34, "media", "television")
    df_all.insert(35, "type_descr", "SATELLITE")
    df_all.insert(36, "medium", df_all["Channel"])
    df_all.insert(37, "sub_medium_code", 0)
    df_all.insert(38, "sub_medium_descr", df_all["Channel"])
    df_all.insert(39, "frequency", 1)
    df_all.insert(40, "space", df_all["Duration"])
    df_all.insert(41, "amount", df_all["Cost"])
    df_all.insert(42, "brand_agency", "publicis")
    df_all.insert(43, "promotion_sponsorship", "promotion_sponsorship")
    df_all.insert(44, "tv_program_to_hour", 0)
    df_all.insert(45, "tv_program_to_minute", 0)
    df_all.insert(46, "tv_program_to_second", 0)
    df_all.insert(47, "tv_program_type", df_all["Feature"])
    df_all.insert(48, "cost_of_30", df_all["30 Sec CPP"])
    df_all.insert(49, "bwa_program", 1)
    df_all.insert(50, "country_code", "RSA")
    df_all.insert(51, "spot_visual_code", 0)
    df_all.insert(52, "media_code", 1)
    df_all.insert(53, "medium_code", 0)
    df_all.insert(54, "final_media_type", "tv")
    df_all.insert(55, "program_domain", "general")
    df_all.insert(56, "program_sub_type", "general")
    df_all.insert(57, "actual_ad_size", np.nan)
    df_all.insert(58, "user_defined_field",  np.nan)
    df_all.insert(59, "producer", "producer")
    df_all.insert(60, "program_duration", 100)
    df_all.insert(61, "dealer_corporate", "corporate")
    df_all.insert(62, "dd", pd.DatetimeIndex(df_all["c_trans_date"]).day)
    df_all.insert(63, "mm", pd.DatetimeIndex(df_all["c_trans_date"]).month)
    df_all.insert(64, "yy", pd.DatetimeIndex(df_all["c_trans_date"]).year)
    df_all["spots_2_numbers"]=df_all["spot_number"].astype(str)+"_"+df_all["total_spots_in_break"].astype(str)
    df_all.insert(65, "spot_position", df_all["spots_2_numbers"].apply(lambda x: "first spot" if int(x.split("_")[0])<3 else "before last spot" if (int(x.split("_")[1])-int(x.split("_")[0]))<2 else "middle spots"))
    df_all.insert(66, "spot_duration", df_all["Duration"])
    df_all.insert(67, "subject", "general")
    df_all.insert(68, "ipsos_estimated_expenditure", 0)
    df_all.insert(69, "internet_website_category", np.nan)
    df_all.insert(70, "internet_device", np.nan)
    df_all.insert(71, "internet_channel", np.nan)
    df_all.insert(72, "internet_visual_digital_type", np.nan)
    df_all.insert(73, "visual_campaign", np.nan)
    df_all.insert(74, "campaign_status", np.nan)
    df_all.insert(75, "campaigns_count", 0)
    df_all.insert(76, "origin_country_by_brand", "RSA")
    df_all.insert(77, "origin_country_by_subbrand", "RSA")
    df_all.insert(78, "target_by_product", "TOTAL POPULATION")
    df_all.insert(79, "program_detail", "general")
    df_all.insert(80, "program_status", "recorded")
    df_all.insert(81, "ADDED_DAY", pd.DatetimeIndex(df_all["c_trans_date"]).day)
    df_all.insert(82, "ADDED_MONTH", pd.DatetimeIndex(df_all["c_trans_date"]).month)
    df_all.insert(83, "ADDED_YEAR", pd.DatetimeIndex(df_all["c_trans_date"]).year)
    df_all.insert(84, "RSAGRP", df_all["TVR"])
    df_all.insert(85, "UAEMAR23/Target: HAleon LA/DOW/TSG/GRP", np.nan)
    df_all=df_all.iloc[:,:86]

    columns_difference = set(df_KSA.columns).difference(set(df_all.columns))

    return df_all, columns_difference

def main():
    st.title("South Africa Data Processing App")

    # Upload files
    uploaded_all_file = st.file_uploader("Upload South Africa Data File (Excel)", type=["xlsx"])
    uploaded_ksa_file = st.file_uploader("Upload KSA Data File (Excel)", type=["xlsx"])

    if uploaded_all_file and uploaded_ksa_file:
        # Read the uploaded files into Pandas DataFrames
        df_all_original = pd.read_excel(uploaded_all_file, sheet_name="Pivotable")
        df_all = df_all_original.copy()

        df_KSA_original = pd.read_excel(uploaded_ksa_file, sheet_name="March PAn Aab")
        df_KSA = df_KSA_original.copy()

        # Process the data
        df_all_processed, columns_difference = process_data(df_all, df_KSA)

        # Display the columns difference
        st.write("Columns in df_KSA but not in df_all:")
        st.write(columns_difference)

        # Provide a download button for the processed data
        st.markdown(f"### Download Processed Data")
        st.download_button('Download file',data=pd.DataFrame.to_csv(df_all_processed,index=False), mime='text/csv')

if __name__ == "__main__":
    main()
