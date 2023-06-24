# Change the APPId, AppSecret, TenantId, SubscriptionName and ResourceGroup Name
$appId="4435e54f-4131-4b0f-be15-141f5af8d984"
$appSecret="FYo8Q~980a5PL9On45NwDYF3Uu~aTXKlHwNNiaje"
$tenantId="91006505-05ea-40ff-97ac-20e0378eb509"
$subscriptionName="Free Trial"
$resourceGroup = "cookbookan"

az login --service-principal --username $appId --password $appSecret --tenant $TenantId

az account set --subscription $subscriptionName

cd "/Users/abhisheknagpurkar/Downloads/Azure-Databricks-Cookbook-main/Chapter05/Code" #Location where the code is saved in local drive

az deployment group create --resource-group $resourceGroup --template-file azuredeploy.json --parameters azuredeploy.parameters.json

