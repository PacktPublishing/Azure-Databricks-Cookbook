# Change the APPId, AppSecret, TenantId, SubscriptionName and ResourceGroup Name
$appId=""
$appSecret=""
$tenantId=""
$subscriptionName="Pay As You Go"
$resourceGroup = "CookbookRG"

az login --service-principal --username $appId --password $appSecret --tenant $TenantId

az account set --subscription $subscriptionName

cd "C:\Users\admin\Azure Databricks Book\Chapter05\Code" #Location where the code is saved in local drive

az deployment group create --resource-group $resourceGroup --template-file azuredeploy.json --parameters azuredeploy.parameters.json

