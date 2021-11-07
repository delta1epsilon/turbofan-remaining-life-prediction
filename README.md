# Remaining Useful Life (RUL) prediction for Turbofan Engines

The project objective is to estimate Remaining Useful Life (RUL) with Machine Learning. RUL is defined as a remaining time that a component can function with an acceptable performance before it fails. The model should provide prediction uncertainties and be extensively tested with Prognostics metrics.

[Turbofan Engines Degradation Simulation Data Set](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/)
provided by NASA is being used in this project for Remaining Useful Life prediction.


See the notebooks descriptions:

1. `1-EDA.ipynb` - contains Exploratory Data Analysis. The objective is to inspect the data, get general understanding of the datasets, check for patterns, understand what preprocessing should be done before the modeling.
2. `2-target-metrics-baseline.ipynb` - define the target, discuss evaluation metrics, and build a baseline model.
3. `3-features_engineering.ipynb` - features engineering pipelines.
4. `4-predict_rul_with_ML.ipynb` - contains experiments with different algorithms, features sets and evaluation with prognostics metrics.



## Setup

Environment setup:

```
python3.8 -m venv ./venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name=venv
```

Download the dataset:

```
wget -O CMAPSSData.zip  https://ti.arc.nasa.gov/c/6/
unzip -d CMAPSSData/ CMAPSSData.zip
```


## References

1. A. Saxena, K. Goebel, D. Simon, and N. Eklund, "Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation", in the Proceedings of the Ist International Conference on Prognostics and Health Management (PHM08), Denver CO, Oct 2008

2. Saxena, A.; Celaya, J.; Saha, B.; Saha, S.; Goebel, K. Metrics for Offline Evaluation of Prognostic Performance. Int. J. Progn. Health Manag. 2010

3. https://www.researchgate.net/publication/224358896_Recurrent_neural_networks_for_remaining_useful_life_estimation

4. Christ, M., Kempa-Liehr, A.W. and Feindt, M. (2016). Distributed and parallel time series feature extraction for industrial big data applications. ArXiv e-prints: 1610.07717 URL: http://adsabs.harvard.edu/abs/2016arXiv161007717C

5. Dempster A., Petitjean F. and Webb G., "ROCKET: Exceptionally fast and accurate time series classification using random convolutional kernels": https://arxiv.org/pdf/1910.13051.pdf
