# Change the APPId, AppSecret, TenantId, SubscriptionName and ResourceGroup Name
$appId="aasdadabc-c00a-4e2a-9bfd-34sdadadaa57b2"
$appSecret="_.ytodasdasdasdj-TXuqS6O.4U"
$tenantId="sdasdada4-sdasde0-sadd7c-8514-e5fsdasd375d"
$subscriptionName="Pay As You Go"
$resourceGroup = "CookbookRG"

az login --service-principal --username $appId --password $appSecret --tenant $TenantId

az account set --subscription $subscriptionName

cd "C:\Users\admin\Azure Databricks Book\Chapter05\Code" #Location where the code is saved in local drive

az deployment group create --resource-group $resourceGroup --template-file azuredeploy.json --parameters azuredeploy.parameters.json

