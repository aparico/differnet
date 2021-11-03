# DifferNet

This is forked from the [official repository](https://github.com/marco-rudolph/differnet) to the WACV 2021 paper "[Same Same But DifferNet: Semi-Supervised Defect Detection with Normalizing Flows](https://arxiv.org/abs/2008.12577)" by Marco Rudolph, Bastian Wandt and Bodo Rosenhahn.

Changes:
* config.py
* dataset (MVTec AD, Class = Screw)
* training details are saved to a log file and can be converted to csv

[![PWC](https://user-images.githubusercontent.com/4096485/86174097-b56b9000-bb29-11ea-9240-c17f6bacfc34.png)](https://colab.research.google.com/drive/1rEC1wuIoffuZ9ijXq2-cyakQeGL_pGQD?usp=sharing)


[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/same-same-but-differnet-semi-supervised/anomaly-detection-on-mvtec-ad)](https://paperswithcode.com/sota/anomaly-detection-on-mvtec-ad?p=same-same-but-differnet-semi-supervised)


## Results

I have tested the effect of different number of input images (hyperparameters are same with the original paper) on AUROC. Here are the results:

![auroc_vs_inputimages](https://user-images.githubusercontent.com/47623790/140013160-b1505af0-8a0d-485f-abc0-dccdb15fa1ba.png)


## Dataset Structure

The dataset is the Screw Class from the [MVTec AD dataset](https://www.mvtec.com/company/research/datasets/mvtec-ad).

Set the variables _dataset_path_ and _class_name_ in _config.py_ to run experiments on a dataset of your choice. The structure of the data is as follows:

``` 
train data:

        dataset_path/class_name/train/good/any_filename.png
        dataset_path/class_name/train/good/another_filename.tif
        dataset_path/class_name/train/good/xyz.png
        [...]

test data:

    'normal data' = non-anomalies

        dataset_path/class_name/test/good/name_the_file_as_you_like_as_long_as_there_is_an_image_extension.webp
        dataset_path/class_name/test/good/did_you_know_the_image_extension_webp?.png
        dataset_path/class_name/test/good/did_you_know_that_filenames_may_contain_question_marks????.png
        dataset_path/class_name/test/good/dont_know_how_it_is_with_windows.png
        dataset_path/class_name/test/good/just_dont_use_windows_for_this.png
        [...]

    anomalies - assume there are anomaly classes 'crack' and 'curved'

        dataset_path/class_name/test/crack/dat_crack_damn.png
        dataset_path/class_name/test/crack/let_it_crack.png
        dataset_path/class_name/test/crack/writing_docs_is_fun.png
        [...]

        dataset_path/class_name/test/curved/wont_make_a_difference_if_you_put_all_anomalies_in_one_class.png
        dataset_path/class_name/test/curved/but_this_code_is_practicable_for_the_mvtec_dataset.png
        [...]
``` 

## Getting Started

You will need [Python 3.6](https://www.python.org/downloads) and the packages specified in _requirements.txt_.
We recommend setting up a [virtual environment with pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
and installing the packages there.

Install packages with:

```
$ pip install -r requirements.txt
```

## Configure and Run

All configurations concerning data, model, training, visualization etc. can be made in _config.py_. The default configuration will run a training with paper-given parameters on the screw dataset. 

To start the training, just run _main.py_! But I recommend the command below:

```
$ python main.py | tee $(date +%Y%m%d).log
```

There's a script _log_to_csv.py_ to convert the log file into a csv file with the training loss, test loss, and AUROC per epoch. 

If you have issues when using the code, please report to the main [repo](https://github.com/marco-rudolph/differnet).


## Credits

Most of the code is from the  [official repository](https://github.com/marco-rudolph/differnet) and some of the implementation of Normalizing Flows are from the [FrEIA framework](https://github.com/VLL-HD/FrEIA) . Follow [their tutorial](https://github.com/VLL-HD/FrEIA) if you need more documentation about it.


## Citation
Please cite the original paper in your publications if it helps your research.

    @inproceedings { RudWan2021,
    author = {Marco Rudolph and Bastian Wandt and Bodo Rosenhahn},
    title = {Same Same But DifferNet: Semi-Supervised Defect Detection with Normalizing Flows},
    booktitle = {Winter Conference on Applications of Computer Vision (WACV)},
    year = {2021},
    month = jan
    }
    
Another paper link because you missed the first one:

* [Same Same But DifferNet: Semi-Supervised Defect Detection with Normalizing Flows](
https://arxiv.org/abs/2008.12577)


## License

This project is licensed under the MIT License.

 
