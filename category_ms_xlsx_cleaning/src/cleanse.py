"""
This module exposes functionality to clean the data.
"""
import pandas as pd
import re
import numpy as np

class CleanseRules:
    """
    This is the base class which performs operations
    to clean the dataframe.

    Attributes:
    -------------------
    dataframe (DataFrame): DataFrame to be cleaned.
    drug_name_column (str): Drug name column name.
    operations (list): List of cleaning operations to perform.
    """

    # def __init__(self, columns_info):
    #     pass

    def __init__(self):
        pass

    def apply_defaults(self, data):
        pass

    def apply(self, data, operations):
        pass

    def rule_replace_single_char_across(self, data, **kwargs):
        """This function will find the 'to_char' and replace the same with
        'from_char' within all the columns of the dataframe.

        Args:
            data (dataframe): Original data that
            needs cleanup;
            from_char: The char to be replaced;
            to_char: The char to replace with;

        Returns:
            data (dataframe): Cleaned data;
        """
        # check if the dataframe is empty
        if data.empty:
            return data

        from_char = kwargs.pop('from_char')
        to_char = kwargs.pop('to_char')

        data = data.replace(to_replace=from_char, value=to_char, regex=True)
        return data

    def row_replace_string(self, row, column_name, from_str, to_str):
        '''
        Replace an existing old_string within the specified column with
        a new_string value.

        Parameters:
        -----------
        row (series): Dataframe row to iterate over.

        column_name (string): Column for which the string replcement
                                needs to be performed

        from_str (string): Old string that needs to be replaced

        to_str (string): New string that will replace the old one

        Returns:
        --------
        modified_string (string): Returns the modified string value
                                    iteratively for the column

        '''
        if isinstance(row[column_name], str):
            # if the from_str contains spaces
            if ' ' in from_str:
                len_from = len(from_str)
                str_idx = row[column_name].find(from_str)
                if str_idx != -1:
                    modified_string = row[column_name][0:str_idx] + \
                        row[column_name][str_idx+len_from:]
                else:
                    # do nothing
                    modified_string = row[column_name]
            # if from_str is null or blank
            elif pd.isna(from_str) or len(from_str.strip()) == 0:
                modified_string = to_str
            # for all the other cases
            else:
                modified_string = re.sub(r"\b{}\b".format(from_str), to_str,
                                    row[column_name], flags=re.IGNORECASE)
        else:
            # do nothing
            modified_string = row[column_name]

        return modified_string

    def rule_replace_string(self, data, **kwargs):
        """This function will replace the 'from_str' in the
        provided 'column_name' with the 'to_str' value.

        Args:
            data (dataframe): Original data that
            needs cleanup;
            column_name: The column within which the data needs
            to be replaced;
            from_str: The string to be replaced;
            to_str: The string to replace with;

        Returns:
            data (dataframe): Cleaned data;
        """
        if data.empty:
            return data

        column_name = kwargs.pop('column_name')
        from_str = kwargs.pop('from_str')
        to_str = kwargs.pop('to_str')

        data.loc[:, column_name] = data.apply(
            self.row_replace_string,
            column_name=column_name,
            from_str=from_str,
            to_str=to_str,
            axis=1)

        return data

    def rule_stack_columns_vertically(self, data, mappings):
        """This function will vertically stack the 'to_column'
        and 'from_column' together under the 'to_column' and
        drop the 'from_column' from the data.

        Args:
            data (dataframe): Original data that
            needs cleanup;
            to_column: The column to which the other columns
            needs to be appended;
            from_column: The column which needs to be appended
            to the other column;

        Returns:
            data (dataframe): Cleaned data;
        """
        if data.empty:
            return data

        # create a blank dataframe
        merged_data = pd.DataFrame()

        if isinstance(mappings, dict):
            to_col = mappings.pop('to_column')
            from_col = mappings.pop('from_column')

            to_col_list = list(data[to_col])
            to_col_list = [val for val in to_col_list if not pd.isna(val)]            

            from_col_list = list(data[from_col])
            from_col_list = [val for val in from_col_list if not pd.isna(val)]

            to_col_list.extend(from_col_list)
            merged_data[to_col] = to_col_list

            # drop the two columns merged together
            data.drop([to_col, from_col], axis=1, inplace=True)

            # merge the new col dataframe with remaining columns
            merged_data = pd.concat([merged_data,  data], axis=1)
            # breakpoint()
            return merged_data
        elif isinstance(mappings, list):
            for mapping in mappings:
                to_col = mapping.pop('to_column')
                from_col = mapping.pop('from_column')

                to_col_list = list(data[to_col])
                to_col_list = [val for val in to_col_list if not pd.isna(val)]
                from_col_list = list(data[from_col])
                from_col_list = [val for val in from_col_list if not pd.isna(val)]

                to_col_list.extend(from_col_list)
                merged_data[to_col] = to_col_list

                # drop the two columns merged together
                data.drop([to_col, from_col], axis=1, inplace=True)

                # merge the new col dataframe with remaining columns
                merged_data = pd.concat([merged_data,  data], axis=1)

            return merged_data

    def rule_merge_multiple_files(self, data_list):
        """This function will merge all the different extract
        outputs read as dataframes into one single dataframe.

        Args:
            data_list (list of dataframe): List of dataframes
            that should be merged together;

        Returns:
            data (dataframe): Cleaned data;
        """
        data = pd.concat(data_list)
        data.reset_index(inplace=True, drop=True)

        return data

    def rule_remove_blank_rows(self, data):
        """This function will remove all the blank rows
        from the dataset.

        Args:
            data (dataframe): Original data that
            needs cleanup;

        Returns:
            data (dataframe): Cleaned data;
        """
        if data.empty:
            return data

        data.dropna(axis=0, how='all', inplace=True)

        return data

    def rule_create_col_with_constant(self, data, **kwargs):
        """The function will create a new column to the data with
        a provided constant values for each cell/row.

        Args:
            data (dataframe): Original data that
            needs cleanup;
            column_name: Name of the column to be created new
            or overridden;
            constant_value: The constant value to be appended;

        Returns:
            data (dataframe): Cleaned data;
        """
        if data.empty:
            return data

        column_name = kwargs.pop('column_name')
        constant_value = kwargs.pop('constant_value')

        data.loc[:, column_name] = constant_value

        return data

    def rule_split_column_to_another(self, data, **kwargs):
        """The function will split 'from_column' to 'to_column'
        based on 'delimiter' (default: ' '). In case of multiple
        delimiters, only the last value moves to 'to_column'.

        Args:
            data (dataframe): Original data that
            needs cleanup;
            to_column: The column to be split into another;
            from_column: The column which receives the split
            portion; 
            delimiter: The delimiter based on which the split needs to happen;

        Returns:
            data (dataframe): Cleaned data;
        """
        if data.empty:
            return data

        from_column = kwargs.pop('from_column')
        to_column = kwargs.pop('to_column')
        delimiter = kwargs.pop('delimiter')

        data.loc[:, to_column] = [
                val.split(delimiter)[-1]
                if len(val.split(delimiter)) >= 2
                else np.NaN for val in data[from_column]
            ]

        data.loc[:, from_column] = [
                val.split(delimiter)[0]
                if len(val.split(delimiter)) <= 2
                else delimiter.join(val.split(delimiter)[:-1])
                for val in data[from_column]
            ]

        return data

    def rule_convert_multitable_to_one(self, data):
        """The function will convert the multitable data format into
        a single table with records stacked vertically.

        Args:
            data (dataframe): Original data that
            needs cleanup;

        Returns:
            data (dataframe): Cleaned data;
        """
        # find the length of columns
        total_col_len = len(data.columns)
        if total_col_len % 2 == 0:
            actual_col_count = total_col_len // 2
            left_data = data.iloc[:, range(actual_col_count)]
            right_data = data.iloc[:, range(actual_col_count+1, total_col_len)]

            merged_data = pd.concat([left_data, right_data])
            merged_data.reset_index(inplace=True, drop=True)
            return merged_data
        else:
            return data

    def row_merge_multiple_columns(row, dict_mapping):
        """Combine the string contents of the columns as per the mapping
        if the current value is non-null

        Args:
            row (pd.series): a single row of a dataframe
            dict_mapping (dictionary): Mapping that identifies the
                    replacement value as per the existing column name

        Returns:
            new_col_val (string): The newly created value as per merge
        """
        new_col_val = ''
        for key in dict_mapping:
            if not pd.isna(row[key]):
                new_col_val = new_col_val + dict_mapping[key] + ' '

        return new_col_val

    def rule_drop_dataframe_columns(df, columns_to_drop):
        """The function will drop the set of
        columns not needed from the dataframe.
        Args:
            columns_to_drop (string or list): A single colun name (string)
                            Or a list of columns that need to be dropped.
        """
        df.drop(columns=columns_to_drop, axis=1, inplace=True)

    def rule_merge_multiple_columns_to_one(self, data, **kwargs):
        """The function will read the cleaned and processed
        dataframe and merge the columns as per the supplied
        mapping to form the new concatenated column.
        """
        if data.empty:
            return data

        new_column = kwargs.pop('to')
        dict_mapping = kwargs.pop('from')

        # identify the colums to drop
        cols_to_drop = list(dict_mapping.keys())

        # data = split_data_to_next_record(data, cols_to_drop)

        data[new_column] = data.apply(
            row_merge_multiple_columns, dict_mapping=dict_mapping, axis=1)

        # drop unwanted columns
        rule_drop_dataframe_columns(data, cols_to_drop)

        return data



















    # @validate_none_params('to', 'from')
    # def merge_multiple_columns_to_one(self, data, **kwargs):
    #     """The function will read the cleaned and processed
    #     dataframe and merge the columns as per the supplied
    #     mapping to form the new concatenated column.
    #     """
    #     if data.empty:
    #         return data
    
    #     new_column = kwargs.pop('to')
    #     dict_mapping = kwargs.pop('from')

    #     # identify the colums to drop
    #     cols_to_drop = list(dict_mapping.keys())

    #     # data = split_data_to_next_record(data, cols_to_drop)

    #     data[new_column] = data.apply(
    #         merge_multiple_columns, dict_mapping=dict_mapping, axis=1)

    #     # drop unwanted columns
    #     drop_dataframe_columns(data, cols_to_drop)

    #     return data
    # def remove_drugname_null(self, data):
    #     """Removes the rows containing drugname as null or None or empty string

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data with improper drug name
    #     """
    #     if data.empty:
    #         return data

    #     col = self.columns_info.drug_name_column

    #     data.loc[:, col] = data.apply(replace_null_with_nan,
    #                            drug_name_col=col, axis=1)
    #     data.dropna(subset=[col], inplace=True)

    #     return data

    # @validate_none_params('from_col', 'to_col')
    # def split_merged_data(self, data, **kwargs):
    #     """Use this function to clean-up the data in from_col in cases where
    #     values of to_col is merged with values of from_col at the end
    #     in extracted data.
    #     The merged data will be moved to to_col.
    #     The possible values of to_col are identified
    #     as unique values of to_col.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column
    #     from_col (str): Target column to find the merged value and clean
    #     to_col (str): Target column to fill the found value in from_col

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data
    #     """
    #     if data.empty:
    #         return data

    #     to_col = kwargs.pop('to_col')
    #     from_col = kwargs.pop('from_col')

    #     # remove nan values
    #     unique_values = data.loc[:, to_col].dropna().unique()
    #     # remove empty string
    #     unique_values = [i for i in unique_values if len(i) > 0]

    #     for val in unique_values:
    #         regx_val = re.compile(f'{re.escape(val)}$')
    #         mask = data.loc[:, from_col].astype(str).str.contains(regx_val)
    #         subset = data[mask]
    #         # fill the to_col values
    #         subset.loc[:, to_col] = val
    #         # replace the to_col value in from_col with empty string
    #         subset[from_col] = subset[from_col].str.replace(regx_val, '')
    #         data.loc[subset.index, :] = subset

    #     return data

    # def remove_superscript(self, data):
    #     """
    #     Removes everything in tag <s> including the tag in drug name.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data
    #     """
    #     if data.empty:
    #         return data

    #     col = self.columns_info.drug_name_column
    #     data.loc[:, col] = data.loc[:, col].str.replace('<s>(.*)</s>', '')

    #     return data

    # def remove_subheaders(self, data):
    #     """
    #     Removes sub-header, except drug name if all data is null those
    #     rows are considered as sub-header rows and will be removed.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data
    #     """
    #     if data.empty:
    #         return data

    #     drug_name_column = self.columns_info.drug_name_column
    #     columns = data.columns
    #     cols_other_than_drugname = [
    #         i for i in columns if i != drug_name_column]

    #     for column in cols_other_than_drugname:
    #         data.loc[:, column] = data.apply(
    #             replace_null_with_nan_non_dn,
    #             column=column,
    #             axis=1)

    #     data.dropna(
    #         how='all',
    #         subset=cols_other_than_drugname,
    #         inplace=True)

    #     return data

    # def remove_duplicates(self, data):
    #     """
    #     Removes the duplicated rows.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data    
    #     """
    #     data = data.drop_duplicates(keep='first')
    #     return data

    # def remove_leading_trailing_spaces(self, data):
    #     """
    #     Removes leading and trailing spaces in all columns.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data    
    #     """
    #     if data.empty:
    #         return data

    #     def repl(v): return v.strip() if isinstance(v, str) else v
    #     for column in data.columns:
    #         data.loc[:, column] = data.loc[:, column].apply(repl)

    #     return data

    # def remove_extra_spaces(self, data):
    #     """
    #     Removes extra spaces in between the value.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data
    #     """
    #     if data.empty:
    #         return data

    #     exp = re.compile(r'\t|\s{2}')
    #     def repl(v): return re.sub(exp, ' ', v) if isinstance(v, str) else v
    #     for column in data.columns:
    #         data.loc[:, column] = data.loc[:, column].apply(repl)

    #     return data

    # def remove_carriage_return(self, data):
    #     """
    #     PDF text will be wrapped to next line with '\r' char and
    #     it will be removed.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data    
    #     """
    #     col = self.columns_info.drug_name_column
    #     if not data.empty:
    #         data.loc[:, col] = data.loc[:, col].str.replace(
    #             '\r', repl=handle_carriage)

    #     return data

    # def remove_columnnames_in_values(self, data):
    #     """
    #     Column names come into the data. This method cleans the column names
    #     from data.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data        
    #     """
    #     filter_rows_condition = pd.Series()
    #     column_mapping = self.columns_info.column_mapping

    #     for old_col, new_col in column_mapping.items():
    #         if filter_rows_condition.empty:
    #             filter_rows_condition = (data.loc[:, new_col] == old_col)
    #         else:
    #             filter_rows_condition |= (data.loc[:, new_col] == old_col)

    #     data.where(cond=~filter_rows_condition, axis=0, inplace=True)

    #     data.dropna(how='all', inplace=True)

    #     return data

    # def merge_overflown_rows(self, data):
    #     """Merge rows if drug name column overflows to next row.
    #     Overflow is identified as other than drug name column
    #     remaining columns will be null. It doesn't work when sub
    #     headers are present in the data.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data
    #     """
    #     if data.empty:
    #         return data

    #     col = self.columns_info.drug_name_column

    #     _data = {
    #         'data': pd.DataFrame(columns=data.columns)
    #     }
    #     row_count = {'cnt': 0}

    #     def perform(row, drug_name_col, _data, row_count):
    #         _c = [i for i in row.index if i != drug_name_col]
    #         _isnull = True

    #         for c in _c:
    #             if isinstance(row[c], str):
    #                 _isnull = _isnull and len(row[c].strip()) == 0
    #             else:
    #                 _isnull = _isnull and pd.isna(row[c])

    #         if _isnull:
    #             _data['data'].loc[row_count['cnt'] - 1,
    #                               drug_name_col] += row[drug_name_col]
    #         else:
    #             _data['data'] = _data['data'].append([row], ignore_index=True)
    #             row_count['cnt'] += 1

    #     data.apply(perform, axis=1, drug_name_col=col,
    #                _data=_data, row_count=row_count)

    #     data = _data['data']

    #     return data

    # def remove_bracketted_text(self, data):
    #     """
    #     Text within () including the () will be removed.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     ---------
    #     data (DataFrame): Cleaned data
    #     """
    #     col = self.columns_info.drug_name_column
    #     if not data.empty:
    #         data.loc[:, col] = data.loc[:, col].apply(delete_text_in_brackets)

    #     return data

    # def move_drug_category_from_prefix_to_suffix(self, data):
    #     """
    #     Use this rule if you want to move the category enclosed in brackets
    #     from prefix to suffix in the drug name column.
    #     For example: (some text) drug name -> drug name (some text)

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data
    #     """

    #     col = self.columns_info.drug_name_column

    #     if not data.empty:
    #         data.loc[:, col] = data.loc[:, col].apply(
    #             move_text_in_paranthesis_to_end)

    #     return data

    # @validate_none_params('from', 'to', 'column')
    # def replace_string(self, data, **kwargs):
    #     """
    #     The function will read the pair of old and new
    #     strings passed as a UI rule and replace the same
    #     within the drug_name column.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column
    #     from_str (str): String to be replaced
    #     to_str (str): String to replace with

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data
    #     """
    #     column_name = kwargs.pop('column')
    #     from_str = kwargs.pop('from')
    #     to_str = kwargs.pop('to')
    #     if not data.empty:
    #         data.loc[:, column_name] = data.apply(
    #             replace_old_with_new_string,
    #             column_name=column_name,
    #             from_str=from_str,
    #             to_str=to_str,
    #             axis=1)

    #     return data

    # def remove_newline(self, data):
    #     """
    #     Removes newline from all the columns within the dataframe.
    #     """
    #     data = data.replace('\n', ' ', regex=True)
    #     return data

    # @validate_none_params('reference_col')
    # def merge_drug_with_reference(self, data, **kwargs):
    #     """The function will merge the drug name with reference column in
    #     the following fashion:
    #     drug_name_column = reference (original_drug_name)
    #     """
    #     if data.empty:
    #         return data

    #     reference_col = kwargs.pop('reference_col')
    #     col = self.columns_info.drug_name_column

    #     data.loc[:, col] = data.apply(
    #         join_reference_with_drugname,
    #         reference_col=reference_col,
    #         drug_name_col=col,
    #         axis=1)

    #     data.drop(columns=reference_col, axis=1, inplace=True)

    #     return data

    # @validate_none_params('columns_to_drop')
    # def drop_columns(self, data, **kwargs):
    #     """
    #     Drop the provided set/list of columns.
    #     """
    #     columns_to_drop = kwargs.pop('columns_to_drop')
    #     data.drop(columns=columns_to_drop, axis=1, inplace=True)
    #     return data

    # @validate_none_params('restrictions_column')
    # def move_caps_to_front(self, data, **kwargs):
    #     """The function will move CAPS strings to suffix
    #     followed by normal text in the restrictions column
    #     """
    #     if data.empty:
    #         return data

    #     restrictions_column = kwargs.pop('restrictions_column')
    #     data.loc[:, restrictions_column] = data.loc[
    #         :, restrictions_column].apply(move_caps_to_front)

    #     return data

    # @validate_none_params('first_column', 'second_column')
    # def merge_columns(self, data, **kwargs):
    #     """The function will merge the contents of two
    #     columns if they are non-blank in the following fashion:
    #     first_column = first_column + ' ' + second_column
    #     """
    #     if data.empty:
    #         return data

    #     first_column = kwargs.pop('first_column')
    #     second_column = kwargs.pop('second_column')
    #     brackets = kwargs.pop('brackets', False)

    #     if brackets:
    #         brackets = True

    #     data.loc[:, first_column] = data.apply(
    #         merge_columns,
    #         first_col=first_column,
    #         second_col=second_column,
    #         brackets=brackets,
    #         axis=1)

    #     data.drop(columns=second_column, axis=1, inplace=True)

    #     return data

    # @validate_none_params('column_name', 'replacement_value')
    # def override_column(self, data, **kwargs):
    #     """The function will bulk override the value within the
    #     column provided with a specific replacement string
    #     value provided.
    #     """
    #     if data.empty:
    #         return data

    #     column_name = kwargs.pop('column_name')
    #     replacement_value = kwargs.pop('replacement_value')

    #     data.loc[:, column_name] = replacement_value

    #     return data

    # @validate_none_params('column_name')
    # def remove_column_with_null(self, data, **kwargs):
    #     """Removes the rows containing null or None or
    #     empty string in a particular column.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     kwargs: Contains the mapping for column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data with required rows removed
    #     """
    #     if data.empty:
    #         return data

    #     column_name = kwargs.pop('column_name')

    #     data.loc[:, column_name] = data.apply(
    #                                     replace_null_with_nan_non_dn,
    #                                     column=column_name,
    #                                     axis=1)
    #     data.dropna(subset=[column_name], inplace=True)

    #     return data

    # @validate_none_params('column_name', 'constant_value')
    # def create_col_with_constant(self, data, **kwargs):
    #     """The function will create a new column to the data with
    #     a provided constant values for each cell/row.
    #     """
    #     if data.empty:
    #         return data

    #     column_name = kwargs.pop('column_name')
    #     constant_value = kwargs.pop('constant_value')

    #     data.loc[:, column_name] = constant_value

    #     return data

    # @validate_none_params('to', 'from')
    # def merge_multiple_columns_to_one(self, data, **kwargs):
    #     """The function will read the cleaned and processed
    #     dataframe and merge the columns as per the supplied
    #     mapping to form the new concatenated column.
    #     """
    #     if data.empty:
    #         return data
    
    #     new_column = kwargs.pop('to')
    #     dict_mapping = kwargs.pop('from')

    #     # identify the colums to drop
    #     cols_to_drop = list(dict_mapping.keys())

    #     # data = split_data_to_next_record(data, cols_to_drop)

    #     data[new_column] = data.apply(
    #         merge_multiple_columns, dict_mapping=dict_mapping, axis=1)

    #     # drop unwanted columns
    #     drop_dataframe_columns(data, cols_to_drop)

    #     return data

    # @validate_none_params('from_column', 'to_column')
    # def split_column_to_another(self, data, **kwargs):
    #     """The function will split the value in from_column to to_column
    #     appending the split value as a prefix to existing values in
    #     to_column. This will work if the values in from_column are
    #     separated by only one space and both from_column and to_column
    #     values are single strings with no spaces in between.
    #     """
    #     if data.empty:
    #         return data

    #     from_column = kwargs.pop('from_column')
    #     to_column = kwargs.pop('to_column')
    #     value_to_append = kwargs.get('value_to_append', None)

    #     # create a mask of the values that need to be updated
    #     mask = [
    #         True if not pd.isna(val) and len(str(val).split()) > 1
    #         else False for val in data[from_column]
    #     ]

    #     # if no default value_to_append is passed, the value_to_append
    #     # should be the last splitted value from from_column
    #     if not value_to_append:
    #         values_to_append = []
    #         for val in data.loc[mask, from_column]:
    #             values_to_append.append(val.split()[-1])

    #         # append the values in the to_column
    #         data.loc[mask, to_column] = values_to_append + data.loc[mask, to_column]
    #     else:
    #         # append the values in the to_column
    #         data.loc[mask, to_column] = [value_to_append + str(val) for val in data.loc[mask, to_column]]

    #     # either way, from_column always retains everything other than the last split value
    #     data.loc[mask, from_column] = [val.split()[0] for val in data.loc[mask, from_column]]

    #     return data

    # @validate_none_params('column_to_update', 'column_to_consult', 'string_to_check', 'replacement_mapping')
    # def update_column_based_another(self, data, **kwargs):
    #     """Update the value in one column if a specific string
    #     is present in another column.

    #     Args:
    #         column_to_update (str): The column that needs to be updated.
    #         column_to_consult (str): The column that needs to be checked
    #                     for a particular string.
    #         string_to_check (str): The string_to_check in the column_to_consult.
    #         replacement_mapping (str): Dictionary mapping indicating which string
    #                     to replace with what.

    #     Returns:
    #         data (DataFrame): Cleaned data
    #     """
    #     if data.empty:
    #         return data

    #     column_to_update = kwargs.pop('column_to_update')
    #     column_to_consult = kwargs.pop('column_to_consult')
    #     replacement_mapping = kwargs.pop('replacement_mapping')
    #     string_to_check = kwargs.pop('string_to_check')

    #     # create a mask of the values that need to be updated
    #     mask = [
    #         True if not pd.isna(val) and string_to_check in val
    #         else False for val in data[column_to_consult]
    #     ]

    #     data.loc[mask, column_to_update] = [replacement_mapping[val] if not pd.isna(val) else val for val in data.loc[mask, column_to_update]]

    #     return data

    # @validate_none_params('from_chr', 'to_chr', 'column_name')
    # def replace_special_character(self, data, **kwargs):
    #     """
    #     The function will replace one special character
    #     passed as 'from' value with a new 'to' value.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     columns_info (ColumnsInfo): Columns information like column_names,
    #                                 column_mapping and drug_name_column
    #     from (str): Special character to be replaced
    #     to (str): Special character/string to replace with
    #     column (str): name of the column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data
    #     """
    #     if data.empty:
    #         return data

    #     column_name = kwargs.pop('column_name')
    #     from_spchr = kwargs.pop('from_chr')
    #     to_str = kwargs.pop('to_chr')
    #     if not data.empty:
    #         data.loc[:, column_name] = data.apply(
    #             replace_spl_char_with_new,
    #             column_name=column_name,
    #             from_spchr=from_spchr,
    #             to_str=to_str,
    #             axis=1)

    #     return data

    # @validate_none_params('string_to_check', 'column_name')
    # def remove_column_with_string(self, data, **kwargs):
    #     """
    #     The function will remove rows that contain the
    #     provided sub-string within the mentioned column.

    #     Parameters:
    #     -----------
    #     data (DataFrame): Data to be cleaned
    #     string_to_check (str): String to be checked within the column
    #     column_name (str): name of the column

    #     Returns:
    #     --------
    #     data (DataFrame): Cleaned data
    #     """
    #     if data.empty:
    #         return data

    #     column_name = kwargs.pop('column_name')
    #     string_to_check = kwargs.pop('string_to_check')

    #     data.loc[:, column_name] = data.apply(
    #                                     replace_string_with_nan,
    #                                     column_name=column_name,
    #                                     string_to_check=string_to_check,
    #                                     axis=1)
    #     data.dropna(subset=[column_name], inplace=True)

    #     return data
