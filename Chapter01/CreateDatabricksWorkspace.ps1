# Change the APPId, AppSecret, TenantId, SubscriptionName and ResourceGroup Name
$appId="xxx-xxx-xxxx-xxx"
$appSecret="xxx-xxx-xxx-xxxx"
$tenantId="xxx-xx-xxx-x-xxxx"
$subscriptionName="Pay As you Go"
$resourceGroup = "CookbookRG"

az login --service-principal --username $appId --password $appSecret --tenant $TenantId

az account set --subscription $subscriptionName

az group deployment create --resource-group $resourceGroup `
--template-file azuredeploy.json --parameters azuredeploy.parameters.json
