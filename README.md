# Code Repo BT5153 2024 Spring


<br><br>


### Google Colab:

1. Follow this Notebook installation :
https://colab.research.google.com/drive/17SKoFRagHWZisth7iwWPrkNGsXQ78uGz?usp=sharing

2. Open your Google Drive :
https://www.google.com/drive

3. Open in Google Drive Folder 'BT5153_2024' and go to Folder 'BT5153_2024/codes/'
Select the notebook 'notebookname.ipynb' and open it with Google Colab using Control Click + Open With Colaboratory

4. If we need to load datasets from gdrive, we should run the following code at the beginning to specifiy the path

```python
   import sys, os
   if 'google.colab' in sys.modules:
      # mount google drive
      from google.colab import drive
      drive.mount('/content/gdrive')
      # specify the path of the folder containing "file_name" by changing the lecture index:
      lecture_index = '01'
      path_to_file = '/content/gdrive/My Drive/BT5153_2024/codes/lab_lecture{}/'.format(lecture_index) 
      print(path_to_file)
      # change current path to the folder containing "file_name"
      os.chdir(path_to_file)
      !pwd
   ```
   For example, you can check this [notebook](https://github.com/rz0718/BT5153_2024/blob/main/codes/lab_lecture01/Best%20Practices%20to%20use%20Pandas.ipynb)
<br><br>


### Local Installation (Tested on Mac OS X arm64 (Apple silicon))

* Based on your architecture and OS type, download the corresponding **Miniforge3** from this [page](https://github.com/conda-forge/miniforge).

Miniforge is the community driven minimalistic conda installer. (open source version of Miniconda)

```sh
   # Conda installation
   chmod +x Miniforge3-$(osname)-$(archname).sh  # for mac m1 pro, it would be Miniforge3-MacOSX-arm64.sh
   ./Miniforge3-$(osname)-$(archname).sh

   # Clone GitHub repo
   git clone git@github.com:rz0718/BT5153_2024.git
   cd BT5153_2024

   # Install python libraries and environment
   conda env create -f env.yml
   conda activate bt5153env

   # Run the notebooks
   jupyter notebook
   ```
