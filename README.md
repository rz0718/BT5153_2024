# Code Repo BT5153 2023 Spring


<br><br>


### Google Colab:

1. Follow this Notebook installation :
https://colab.research.google.com/drive/17SKoFRagHWZisth7iwWPrkNGsXQ78uGz?usp=sharing

2. Open your Google Drive :
https://www.google.com/drive

3. Open in Google Drive Folder 'BT5153_2023' and go to Folder 'BT5153_2023/codes/'
Select the notebook 'notebookname.ipynb' and open it with Google Colab using Control Click + Open With Colaboratory


<br><br>


### Local Installation (Tested on Mac OS X arm64 (Apple Silocon))


* Based on your architecture and OS type, download the corresponding **Miniforge3** from this [page](https://github.com/conda-forge/miniforge). 

Miniforge is the community driven minimalistic conda installer. (open source version of Miniconda)

```sh
   # Conda installation
   chmod +x Miniforge3-$(osname)-$(archname).sh  # for mac m1 pro, it would be Miniforge3-MacOSX-arm64.sh
   ./Miniforge3-$(osname)-$(archname).sh

   # Clone GitHub repo
   git clone git@github.com:rz0718/BT5153_2023.git
   cd BT5153_2023

   # Install python libraries and environment
   conda env create -f env.yml
   conda activate bt5153appliedml

   # Run the notebooks
   jupyter notebook
   ```
