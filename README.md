# **Pattern-Recognition-EEG**

## Description
This project focuses on classifying mental attention states — **focused, unfocused, and drowsy** — using EEG signals recorded from EMOTIV devices. By applying machine learning techniques, we aim to develop an accurate and reliable model to distinguish these states. The results can support various applications, including cognitive enhancement, neurofeedback, and real-time mental state monitoring.

### **About Data**  
The dataset consists of EEG recordings from **5 subjects**, with each subject performing 7 experiments, except for one who completed 6 experiments. EEG signals were recorded at `128 Hz` across multiple trials from **4 to 17 channels**. Mental states were labeled based on time intervals:  
- **Focused**: 0 - 10 minutes  
- **Unfocused**: 10 - 20 minutes  
- **Drowsy**: 20 minutes onward  

For model training and analysis, EEG data from the last **5 days** of experiments (except for one subject with 4 days) was selected. The dataset is stored in `.mat` format, with files named as `eeg_recordX.mat`, where **X** ranges from **1 to 34**, corresponding to 34 recorded experiments. Each file contains raw EEG signals, which will be preprocessed and analyzed for classification.

To download the data, you can access the `dataset` folder or download it from the following **Kaggle** link: [data_here](https://www.kaggle.com/datasets/inancigdem/eeg-data-for-mental-attention-state-detection/data)

## Project Structure

| **Folder**              | **Description**                                              |
|-------------------------|--------------------------------------------------------------|
| dataset                 | Contains the original dataset used for training and testing. |
| report                  | Documented reports and presentations summarizing the project findings. |
| set_up                  | Contains the environment setup files and dependencies required to run. |

## Contributors
| **Name**| **Major**| **University**|
|-|-|-|
| Kieu Thi Ngoc Vui     | Data Science  | University of Science (VNUHCM) |
| Nguyen Ngoc Thanh Thu | Data Science  | University of Science (VNUHCM) |
| Phan Binh Phuong      | Data Science  | University of Science (VNUHCM) |
| Huynh Thao Quynh      | Data Science  | University of Science (VNUHCM) |


## Git Commit Message Rule
After performing the **`git add .`** command, the **`git commit`** message should follow this structure:

    git commit -m "[folder/file updated] - [task description]"

**Example:**
    
    git commit -m "DataPreprocessing/preprocess.ipynb - handling missing values"

Task description should provide enough information for other members to understand what was updated or changed, e.g., fixing bugs, adding features, refactoring code.

After that, use the **`git push`** command to push into the GitHub repository.








