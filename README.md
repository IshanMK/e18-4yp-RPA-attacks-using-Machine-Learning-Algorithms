___
# RPA Attacks using Machine Learning Algorithms
___

This project aims to investigate the use of machine learning algorithms to enhance remote power analysis attacks (RPAAs) on cryptographic systems. RPAAs are a type of side-channel attack that exploit the power consumption patterns of a target device to extract secret information, such as keys, without physical access. Machine learning algorithms can improve the accuracy and efficiency of RPAAs by reducing the data requirements, adapting to different scenarios, and overcoming noise and countermeasures. This project reviews the state-of-the-art methods for RPAAs using machine learning, including supervised learning techniques such as regression, classification, and ensemble methods. It also discusses the challenges, benefits, and ethical issues of applying machine learning to RPAAs, as well as the potential countermeasures and future research directions. The project is based on the AISY framework, which provides a flexible and adaptive platform for side-channel analysis using information-theoretic metrics.

# Instruction Guide for Setting Up AISY Framework

Follow the steps below to set up and run the AISY Framework properly:

## Step 1: Create a Conda Environment
Create a Conda environment with Python version 3.7:
```bash
conda create --name <conda_env_name> python=3.7
conda activate <conda_env_name>
```

## Step 2: Install Requirements
Navigate to the `AISY_Framework` directory and install the required packages:
```bash
cd AISY_Framework
pip install -r requirements.txt
```

after this don't forget to install protobuf
```bash
conda install protobuf==3.20.*
```

## Step 3: Locate AISY Database Package
Find the `aisy_database` package in your Conda environment:
```
/home/{username}/miniconda3/envs/{conda_env_name}/lib/python3.7/site-packages/aisy_database/
```
Edit the following files:
- `db_save.py`
- `db_select.py`
- `db_update.py`
- `db_delete.py`

Replace the code lines as per the marked region text provided in the right side of the picture.

Replace the `self.metadata = MetaData(self.engine)` with `self.metadata = MetaData(); self.metadata.bind = self.engine`
![db save](https://github.com/user-attachments/assets/9468e590-5558-4b1c-8631-491505d019d0)
![db select](https://github.com/user-attachments/assets/f4fb85ac-e4f0-4701-ac2f-6b4dc555a1ff)
![db update](https://github.com/user-attachments/assets/bc930e1d-7c0c-44c3-8089-12ad2c011e4c)
![db delete](https://github.com/user-attachments/assets/72672aca-6880-4c93-ae77-a298329d39fa)


## Step 4: Edit the `app.py` File
Update the `app.py` file to reflect the correct locations of the following folders:
- `databases`
- `datasets`
- `resources`

Ensure the folder paths are set correctly in the application logic.
![app file](https://github.com/user-attachments/assets/2ac587b0-9274-412e-9662-1492fa8fb738)


## Step 5: Run the Web Application
Start the web application using Flask:
```bash
flask run
```

## Step 6: Execute RPA attack 
Run the program:
```bash
python scripts/script_aes_final_constant_key.py
```
