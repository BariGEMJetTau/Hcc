from CRABClient.UserUtilities import config, getUsername
config = config()

config.General.requestName = 'RUN2022F_corrected'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../templateData_2022_F_corrected.py'
config.Data.inputDBS = 'global'
config.Data.inputDataset = '/JetMET/Run2022F-22Sep2023-v2/MINIAOD'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 3
config.JobType.numCores = 2
config.Data.publication = True
config.Data.allowNonValidInputDataset = True
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_eraF_360390_362167_Golden.json'
# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'RUN2022F_corrected'

config.Site.storageSite = 'T2_IT_Bari'
#config.JobType.allowUndistributedCMSSW = True
#config.Site.ignoreGlobalBlacklist  = True