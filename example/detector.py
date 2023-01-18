from scipy import stats

#ksTest detector
def detector(trainSet, liveSet, parameters):
    firstFeature = trainSet.axes[1][0]
    pValue = stats.ks_2samp(trainSet[firstFeature].to_list(), liveSet[firstFeature].to_list())[1]
    threshold = float (parameters.get("pValue", 0.05))
    return int(pValue < threshold), pValue