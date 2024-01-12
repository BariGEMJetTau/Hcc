from CRABClient.UserUtilities import config, getUsername
config = config()

config.General.requestName = 'Zqq_HT800toInf_2022v4_ntuple'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../templateMC_Zqq_preEE_2022v4.py'
config.Data.inputDBS = 'global'
config.Data.inputDataset = '/Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 3
config.JobType.numCores = 2
config.Data.publication = True
# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'Zqq_HT800toInf_2022v4_ntuple'

config.Site.storageSite = 'T2_IT_Bari'
#config.JobType.allowUndistributedCMSSW = True
#config.Site.ignoreGlobalBlacklist  = True